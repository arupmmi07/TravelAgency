import os
from llm.models.constants import *

from llm.models.model import Model

class GPT4(Model):
    def name(self):
        return DEFAULT_GPT4

    def base_url(self):
        return os.environ['OPENAI_API_BASE']

    def temperature(self):
        return DEFAULT_TEMPERATURE

class GPT35(Model):
    def name(self):
        return DEFAULT_GPT35

    def base_url(self):
        return os.environ['OPENAI_API_BASE']

    def temperature(self):
        return DEFAULT_TEMPERATURE

class Llama2(Model):
    def name(self):
        return DEFAULT_LLAMA2

    def base_url(self):
        return os.environ['OLLAMA_API_BASE']

    def temperature(self):
        return DEFAULT_TEMPERATURE

class Mistral(Model):
    def name(self):
        return DEFAULT_MISTRAL

    def base_url(self):
        return os.environ['OLLAMA_API_BASE']

    def temperature(self):
        return DEFAULT_TEMPERATURE

class LLMModels:
    def __init__(self):
        self.models = {
            DEFAULT_GPT4: GPT4(),
            DEFAULT_GPT35: GPT35(),
            DEFAULT_LLAMA2: Llama2(),
            DEFAULT_MISTRAL: Mistral()
        }