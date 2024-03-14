#!/bin/bash

# Variables
model_name="mistral"
custom_model_name="autoagent-mistral"

# Get the base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f ./llm/opensource/mistral.txt