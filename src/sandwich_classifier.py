from fastai.vision import load_learner
import os
from io import BytesIO
import requests

class SandwichClassifier:
  def __init__(self, model_dir):
    self.model = load_learner(model_dir)
  
  def predict(self, img):
    pred_class = str(self.model.predict(img)[0])
    if pred_class not in ['hot_dogs', 'tacos']:
      raise ValueError('Unexpected class ' + pred_class)
    return pred_class

model_dir = os.path.join(os.path.dirname(__file__), "..", "model")
classifier = SandwichClassifier(model_dir)