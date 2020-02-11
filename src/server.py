#!/usr/bin/env python
import json
import logging

from flask import Flask, request

from cipher import Cipher
from pubsub import Topic


app = Flask(__name__)


logging.basicConfig(
    format=f"%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG
)
logger = logging.getLogger(__file__)


topics_list = []
topics_dict = {}  # id : topic


@app.route("/api/pubsub", methods=["GET"])
def api_pubsub():
    help = """pubsub - A simple pub/sub service over HTTP
  GET  /api/pubsub                 Get help. Returns: this help message.
  GET  /api/pubsub/ping            Check status. Returns: `Pong`
  GET  /api/pubsub/topic/new       Create new topic. Returns: `{"id": <id>, "pub_key": <pub_key>, "sub_key": <sub_key>}`
  POST /api/pubsub/topic/pub/<id>  Post message to topic. Requires header: `{"pub_key": <pub_key>}`
  GET  /api/pubsub/topic/sub/<id>  Get (and remove) oldest message from topic. Requires header: `{"sub_key": <sub_key>}`."""
    return help, 200


@app.route("/api/pubsub/ping", methods=["GET"])
def api_pubsub_ping():
    return f"Pong", 200


@app.route("/api/pubsub/topic/new", methods=["GET"])
def api_pubsub_topic_new():
    try:
        global topics_list
        global topics_dict
        topic = Topic()
        topics_list.append(topic)
        topics_dict[topic.id] = topic
        return f"{topic}", 200
    except Exception as e:
        return f"{e}", 500


@app.route("/api/pubsub/topic/pub/<id>", methods=["POST"])
def api_pubsub_topic_pub(id):
    try:
        global topics_dict
        topic = topics_dict[id]
        topic.pub(message=request.data, pub_key=request.headers["pub_key"])
        return "OK", 200
    except KeyError as e:
        return "Not found", 404
    except RuntimeError as e:
        return "Unauthorized", 401


@app.route("/api/pubsub/topic/sub/<id>", methods=["GET"])
def api_pubsub_topic_sub(id):
    try:
        global topics_dict
        topic = topics_dict[id]
        message = topic.sub(sub_key=request.headers["sub_key"])
        return f"{message}", 200
    except KeyError as e:
        return "Not found", 404
    except RuntimeError as e:
        return "Unauthorized", 401


def run(host="0.0.0.0", port=5000, debug=True):
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    run()
