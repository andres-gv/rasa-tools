# 1 Rasa model-API deploy with Cortex in AWS (EKS - Kubernetes)

## 1.1 Description
This is a deployment example of an intent-entity extractor built with [Rasa](https://rasa.com/docs/).

The deployment is done by using [Cortex](https://docs.cortex.dev/), a very powerful open source software that allows to deploy AI-APIs in AWS though  customizable infrastructures, including Kubernetes with CPUs and GPUs.

In [Cortex](https://docs.cortex.dev/) both, Realtime-APIs and Batch-APs can be deployed, in this repository a Realtime-API is deployed.

## 1.2 Requirements
- A model built with [Rasa](https://rasa.com/docs/) for intent entity extraction. The model must be extracted, not in tar.gz.
- [Cortex](https://docs.cortex.dev/) install and documentation review

## 1.3 Deployment
To deploy an intent-entity extractor with [Cortex](https://docs.cortex.dev/), the source files are included in this repository or
you can use a customized version.

The unique important consideration is in the file  predictor.py, which should have a structure similar as shown below,  the other files can be used as described in  [Cortex](https://docs.cortex.dev/) documentation.

```python
import json
from rasa.nlu.model import Interpreter
import subprocess

class PythonPredictor:
    def __init__(self, config):
        subprocess.call("python -m spacy download en_core_news_sm".split(" "))
        self.model = Interpreter.load('models/20200821-014743/nlu') ## this should be an extracted model. Set your model path

    def predict(self, payload):
        prediction = json.dumps(self.model.parse(payload["text"],only_output_properties=True))
        return prediction
```

By following the [Cortex](https://docs.cortex.dev/)  documentation,  the local deploy is:

```bash
cortex deploy
cortex get <name in cortex.yaml> --env aws
```

and the deploy in AWS is:
```bash
cortex cluster up
```

## 1.4 Quick use
1 model creation:
```bash
rasa init
```
extract tar.gz file,  then in the predictor.py file set the model path

2a Model local deploy

```bash
cortex deploy
```

2b Model AWS deploy

```bash
cortex cluster up
```

3 API Request: 
```bash
curl http://localhost:8888 -X POST -H "Content-Type: application/json" -d '{"text": "hello, I want to test the API"}'
```

A similar strategy could be followed to deploy another types of Rasa-APIs.


# 2 Cortex Architecture diagram
[Architecture](https://docs.cortex.dev/miscellaneous/architecture)

![architecture diagram](https://user-images.githubusercontent.com/808475/83995909-92c1cf00-a90f-11ea-983f-c96117e42aa3.png)



