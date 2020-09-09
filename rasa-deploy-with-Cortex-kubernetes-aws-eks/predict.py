import json
from rasa.nlu.model import Interpreter
import subprocess

class PythonPredictor:
    def __init__(self, config):
        subprocess.call("python -m spacy download es_core_news_sm".split(" "))
        self.model = Interpreter.load('models/20200821-014743/nlu') ## this should be an extracted model

    def predict(self, payload):
        prediction = json.dumps(self.model.parse(payload["text"],only_output_properties=True))
        return prediction
