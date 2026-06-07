"""
Main server file.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask app
app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main app webpage.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Retrieves the text to analyze from the request, passes it to the 
    emotion_detector function, and formats the output string.
    """
    # Retrieve the text to analyze from the GET request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function from your package
    response = emotion_detector(text_to_analyze)

    # Error Handling: Check if dominant_emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response exactly as requested by the customer
    formatted_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

    return formatted_string

if __name__ == "__main__":
    # Run the application on localhost
    app.run(host="0.0.0.0", port=5000)
