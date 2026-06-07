import requests
import json

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the provided text using the Watson NLP API.
    """
    # Define the URL for the Emotion detection function
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Define the required headers
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the JSON with the text variable
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Make a POST request to the API
    response = requests.post(URL, headers = headers, json = input_json)

    # Convert the response text into a dictionary
    data = json.loads(response.text)

    # Extract the emotion scores
    emotions = data['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the required output format
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
