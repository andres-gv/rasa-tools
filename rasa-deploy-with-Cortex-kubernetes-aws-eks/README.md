# Rasa deploy with Cortex in AWS (EKS-Kubernetes)

## Description
This is a deployment example of an intent-entity extractor built with [Rasa](https://rasa.com/docs/).

The deployment is done by using [Cortex](https://docs.cortex.dev/), a very interesting open source software that allows to deploy AI APIs in AWS using flexible infrastructure, including Kubernetes.


## Requirements
- A model built with [Rasa](https://rasa.com/docs/) for intent entity extraction.
- [Cortex](https://docs.cortex.dev/) install and documentation read

## Deployment
By deploying the intent-entity extractor with [Cortex](https://docs.cortex.dev/), the files needed are included below.
The needed change is in the file predictor.py, the other files can be uses as described in  [Cortex](https://docs.cortex.dev/) documentation.

```python
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
```


By following the [Cortex](https://docs.cortex.dev/)  documentation,  he local deploy is:

```bash
cortex deploy
```

and the deploy in AWS is:
```bash
cortex cluster up
```





