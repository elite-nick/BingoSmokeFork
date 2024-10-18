from flask import Flask
from flask import request
from threading import Thread
import requests
from datetime import datetime


app = Flask('')

@app.route('/')
def home():
  return "I'm alive"

def run():
  app.run(host='0.0.0.0', port=80)

def keep_alive():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print('Работает. Проверено: ', current_time)
  t = Thread(target=run)
  t.start()