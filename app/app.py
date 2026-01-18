from flask import Flask, request

# Initialize Flask app
app = Flask(__name__)

# Simple keyword-based AI function
def classify_message(message):
    message = message.lower()
    if "refund" in message or "complaint" in message:
        return "Complaint"
    elif "price" in message or "help" in message or "question" in message:
        return "Inquiry"
    else:
        return "Feedback"

# Home page with a form to submit messages
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_message = request.form["message"]
        result = classify_message(user_message)
    return f"""
    <h2>AI Customer Support Demo</h2>
    <form method="post">
        <textarea name="message" rows="4" cols="50" placeholder="Type your message here..."></textarea><br><br>
        <input type="submit" value="Classify Message">
    </form>
    <h3>Classification Result: {result}</h3>
    """

# Start the Flask app on port 5000 (non-privileged)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

