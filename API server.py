import time

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import multiprocessing
import time

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


class Display(Resource):
    def __init__(self):
        self.__listeners = []

    def add_listener(self, listener):
        self.__listeners.append(listener)

    def __notify_listeners(self, notification: str):
        if self.__listeners:
            for listener in self.__listeners:
                process = multiprocessing.Process(target=listener, args=(notification,))
                process.start()

    def get(self):
        try:
            content = request.json["queryResult"]["parameters"]
            for option in content:
                if content[option]:
                    self.__notify_listeners(option)
                    return {"option": option}
        except Exception as e:
            print("Protocol Error", e)
            return "Protocol Error: " + str(e)

    def post(self):
        try:
            content = request.json["queryResult"]["parameters"]
            print(content)
            for option in content:
                if content[option]:
                    self.__notify_listeners(option)
                    return {
                        "fulfillmentMessages": [
                            {
                                "text": {
                                    "text": [
                                        option
                                    ]
                                }
                            }
                        ]
                    }
        except Exception as e:
            print("Protocol Error: ", e)
            return "Protocol Error " + str(e)


api.add_resource(HelloWorld, "/")
api.add_resource(Display, "/api")

if __name__ == "__main__":
    app.run(debug=True)
