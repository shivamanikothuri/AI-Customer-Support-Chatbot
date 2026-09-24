from flask import Flask, render_template, request, jsonify

from chatbot import get_response
from database import create_database, save_chat, get_chat_logs


app = Flask(__name__)

# Create database when application starts
create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({
            "response": "Please enter a message."
        })

    bot_response = get_response(user_message)

    # Save conversation
    save_chat(user_message, bot_response)

    return jsonify({
        "response": bot_response
    })


@app.route("/logs")
def logs():
    chat_logs = get_chat_logs()

    return jsonify(chat_logs)


if __name__ == "__main__":
    app.run(debug=True)