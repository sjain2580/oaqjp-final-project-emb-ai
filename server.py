from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    This function receives the text input from the HTML interface and
    performs emotion detection using the emotion_detector() function.
    The result is returned with the emotion scores
    and the dominant emotion in specified format.
    """
    # Retrieve the text to analyze
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    # Check if the response contains an error message from the emotion_detector
    if "error_message" in response: 
        return jsonify({"error": response["error_message"]}),

    # Format the output as per the requested structure
    result_string = (
        f"For the given text, the emotion results are: "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )
    
    # Return the formatted string as a plain text response
    return result_string

# This function initiates the rendering of the main application page
@app.route("/")
def render_index_page():
    """
    Renders the main HTML page for the application.
    """
    return render_template('index.html')

if __name__ == "__main__": # Corrected: __main__
    # Run the Flask application
    # host='0.0.0.0' makes the server accessible from any IP address
    # on your network, crucial for Docker/VM environments.
    app.run(host="0.0.0.0", port=8888)
