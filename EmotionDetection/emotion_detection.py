import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes emotions in a given text.
    Args:
        text_to_analyze (str): The input text string to be analyzed for emotions.
    Returns:
        dict: A dictionary containing emotion scores and dominant emotion.
    """
    #Define url for emotion detection
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # create the payload for the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }
    # Set header with the model-id
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        # Send a POST request to the API with the specified URL, headers, and JSON payload
        response = requests.post(url, headers=header, json=input_json, timeout = 10)
        print(f"API Response Status Code: {response.status_code}")
        response.raise_for_status()
        # Parse the JSON response text into a Python dictionary
        response_dict = response.json()
        print(f"Raw API Response Dictionary: {response_dict}")
        if response.status_code == 500:
            print("Internal server error")
        # Extract the emotion scores from the nested dictionary structure of the API response.
        emotions = response_dict.get("emotionPredictions", [])[0].get('emotion', {})
        dominant_emotion = max(emotions, key = emotions.get)
        # Create a dictionary of the relevant emotion scores for easier processing
        relevant_emotions = {
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0),
        'dominant_emotion': dominant_emotion
        }
        # Return the final dictionary containing all emotion scores and the dominant emotion.
        return relevant_emotions

    except requests.exceptions.RequestException as e:
        print("Error", str(e))