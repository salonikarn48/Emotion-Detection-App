"""
Flask server for the Emotion Detection application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")


@app.route("/")
def render_index_page():
    """
    Render the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detection():
    """
    Analyze the user's text and return the detected emotions.
    """
    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)