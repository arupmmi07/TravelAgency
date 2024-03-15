from langchain_openai import ChatOpenAI
import os

def llm_models(modelname='gpt-4'):
    if modelname == 'gpt-4':
        return ChatOpenAI(model_name="gpt-4", temperature=0.7)
    elif modelname == 'gpt-3.5':
        return ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    elif modelname == 'llama2' or modelname == 'autoagent-llama2':
        return ChatOpenAI(model_name="autoagent-llama2", base_url=os.environ['OPENAI_API_BASE'] , temperature=0.7)  
    elif modelname == 'mistral' or modelname == 'autoagent-mistral':
        return ChatOpenAI(model_name="autoagent-llama2", base_url=os.environ['OPENAI_API_BASE'] , temperature=0.7)
    else:
        return ChatOpenAI(model_name="gpt-4", temperature=0.7)