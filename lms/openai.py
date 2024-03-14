from langchain_openai import ChatOpenAI


def openai_model(modelname='gpt-4'):
    if modelname == 'gpt-4':
        return ChatOpenAI(model_name="gpt-4", temperature=0.7)
    elif modelname == 'gpt-3.5':
        return ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    else:
        return ChatOpenAI(model_name="gpt-4", temperature=0.7)