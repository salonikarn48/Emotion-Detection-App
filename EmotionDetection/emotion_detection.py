import requests
import json


def emotion_detector(text_to_analyse):
    """
    Analyze the emotion of the given text using Watson NLP.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions