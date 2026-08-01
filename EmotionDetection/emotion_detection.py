"""
Emotion Detection module using Watson NLP.
"""

import json

import requests


def emotion_detector(text_to_analyse):
    """
    Analyze the emotion of the given text using Watson NLP.

    Args:
        text_to_analyse (str): Input text to analyze.

    Returns:
        dict: Dictionary containing emotion scores and the dominant emotion.
    """

    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id":
        "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(
        url,
        json=input_json,
        headers=headers,
        timeout=10
    )

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": max(emotions, key=emotions.get)
    }
