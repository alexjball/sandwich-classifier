from fastai.vision import open_image
from flask import Flask, request, abort
from io import BytesIO
import requests
import sys

from sandwich_classifier import classifier

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
  try:
    img = open_image(BytesIO(requests.get(request.form['url']).content))
  except:
    app.logger.error("Error fetching and opening image {0}".format(sys.exc_info()[0]))
    abort(400)

  return { 'class': classifier.predict(img) }
