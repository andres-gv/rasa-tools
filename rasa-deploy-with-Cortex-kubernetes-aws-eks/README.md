# Description
This is a deployment example of an intent-entity extractor based in [Rasa](https://rasa.com/docs/).

The deployment is done by using [Cortex](https://docs.cortex.dev/), a very interesting open source software that allows to deploy AI APIs in AWS using flexible infrastructure, including Kubernetes.


## Requirements
- A model built with [Rasa](https://rasa.com/docs/) for intent entity extraction.
- [Cortex](https://docs.cortex.dev/) install and documentation read

## Deployment
By deploying the intent-entity extractor with [Cortex](https://docs.cortex.dev/), these are the files needed, an
the local deploy is:
cortex deploy

the deploy in AWS is:

cortex cluster up






