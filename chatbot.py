import random
import re

responses = {
    "hello": [
        "Hello! 👋 How can I help you today?",
        "Hi there! How can I assist you?"
    ],

    "hi": [
        "Hi! 👋 Welcome to our support chatbot.",
        "Hello! What can I help you with?"
    ],

    "help": [
        "Sure! I can help with services, pricing, support, working hours, and contact information."
    ],

    "services": [
        "We provide software development, web development, and technical support services."
    ],

    "price": [
        "Our pricing depends on the service you choose. Please contact our support team for a detailed quotation."
    ],

    "support": [
        "Our support team can help you with technical issues and product-related questions."
    ],

    "hours": [
        "Our support hours are Monday to Friday, 9:00 AM to 6:00 PM."
    ],

    "contact": [
        "You can contact our support team through email or phone during business hours."
    ],

    "thanks": [
        "You're welcome! 😊",
        "Happy to help! 👍"
    ],
    "thank":[
        "You're welcome! 😊",
        "Happy to help! 👍"
    ],

    "bye": [
        "Goodbye! Have a great day! 👋",
        "Thanks for chatting with me. Bye!"
    ]
}


def get_response(user_message):

    message = user_message.lower().strip()

    words = re.findall(r"\b\w+\b", message)

    for word in words:
        if word in responses:
            return random.choice(responses[word])

    if "how are you" in message:
        return "I'm doing great! 😊 Thanks for asking."

    if "your name" in message:
        return "I'm an AI-powered customer support chatbot."

    if "what can you do" in message:
        return "I can answer frequently asked questions and provide basic customer support."

    return (
        "I'm sorry, I don't understand that question yet. "
        "Try asking about our services, pricing, support, hours, or contact information."
    )