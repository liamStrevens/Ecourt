# Main router for flask application
# Handles routing, parsing and retrieval of data

from functools import wraps
import time
import zmq
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_restful import Api


def run():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.bind("tcp://*:5556")

    while True:
        #  Wait for next request from client
        message = socket.recv()
        print("Received request: %s" % message)

        #  Do some 'work'
        time.sleep(1)

        #  Send reply back to client
    socket.send(b"World")



if __name__ == "__main__":
    run()
