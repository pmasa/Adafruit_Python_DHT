#!/usr/bin/python
from flask import Flask, render_template, request
import requests

import redis

import sys

import Adafruit_DHT

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

app = Flask(__name__)

#try:
#    r = redis.Redis(host="localhost",port=6379)
#    r.ping()
#except redis.ConnectionError:
#    exit('Failed to connect to Redis, terminating.')                       

@app.route('/')
def index():
    print("index !!!!")
    return render_template('index.html')


@app.route('/suggestions')
def suggestions():
    print("suggestions !!!!")
    text = request.args.get('jsdata')
    print(text)

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is None or temperature is None:
        print("humidity or temperature is None")
        text = int(text)
    text = int(humidity)
    return render_template('suggestions.html', suggestions=text)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
    #app.run(debug=True)
