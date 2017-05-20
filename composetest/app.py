from flask import Flask
from redis import Redis
import os
import socket

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
host = socket.gethostname()

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello from Docker! I have been seen {} times.\n My host name is {}.'.format(count, host)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)