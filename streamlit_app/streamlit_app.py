import os

import requests
import streamlit as st

CLASSES = ['Negative', 'Positive']


def predict(text: str, model_api_url:str) -> str:
    """
    Sentiment classification of the text
    :param text: Text for classification
    :param model_api_url: url of a model predict endpoint
    :return: sentiment class
    """
    response = requests.post(model_api_url, json={'text': text})
    return response.json()['prediction']


if __name__ == '__main__':
    model_api_url = os.getenv('MODEL_API_URL')

    st.title('Sentiment Analysis')
    st.write('Final Project(Butuzov Evgenii)')
    text_input = st.text_input('Enter a sentence to classify:')
    if st.button('Classify'):
        if text_input:
            prediction = predict(text_input, model_api_url)
            st.write(f'Sentiment: {CLASSES[prediction]}')
        else:
            st.write('Please enter a sentence for classification.')
