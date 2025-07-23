import re
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class RuleBasedChatbot:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! 👋 How can I help you today?",
                "Hi there! 👋 What can I do for you?",
                "Hey! 👋 Nice to meet you!"
            ],
            'how_are_you': [
                "I'm just a bot, but I'm doing great! 🤖",
                "I'm functioning perfectly, thanks for asking! ⚡",
                "Doing awesome! How about you? 😊"
            ],
            'name_identity': [
                "I'm a simple Flask chatbot 🤖",
                "You can call me ChatBot! I'm here to help 🤖",
                "I'm your friendly neighborhood Flask bot! 🕷️🤖"
            ],
            'joke': [
                "Why don't scientists trust atoms? Because they make up everything! 😂",
                "Why did the scarecrow win an award? He was outstanding in his field! 🌾😂",
                "What do you call a fake noodle? An impasta! 🍝😂",
                "Why don't eggs tell jokes? They'd crack each other up! 🥚😂"
            ],
            'creator': [
                "I was created using Python and Flask 💻",
                "My creator built me with Python and Flask! Pretty cool, right? 🐍⚡",
                "I'm powered by Python and Flask magic! ✨💻"
            ],
            'help': [
                "You can ask things like 'hello', 'your name', 'how are you', 'tell me a joke', or 'who made you' 💬",
                "Try asking me: hello, how are you, your name, tell me a joke, who made you, or just chat! 🗣️",
                "I can respond to greetings, questions about myself, jokes, and more! Just talk to me 😊"
            ],
            'goodbye': [
                "Goodbye! 👋 Have a great day!",
                "See you later! 👋 Take care!",
                "Bye! 👋 Come back anytime!"
            ],
            'thanks': [
                "You're welcome! 😊",
                "No problem! Happy to help! 😄",
                "Anytime! That's what I'm here for! 🤖"
            ],
            'default': [
                "I didn't understand that. Try asking about my name, a joke, or just say hello! 🤔",
                "Hmm, I'm not sure about that. Try one of my suggestions below! 💭",
                "I don't quite get that. Ask me something else! 🤷‍♂️"
            ]
        }
        
        self.patterns = {
            'greeting': [
                r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b',
                r'^(yo|sup|wassup)$'
            ],
            'how_are_you': [
                r'\b(how are you|how\'re you|how do you do|how are things)\b',
                r'\b(what\'s up|whats up|how\'s it going|hows it going)\b'
            ],
            'name_identity': [
                r'\b(what\'s your name|whats your name|your name|who are you)\b',
                r'\b(what are you|tell me about yourself|introduce yourself)\b'
            ],
            'joke': [
                r'\b(tell me a joke|joke|make me laugh|something funny|be funny)\b',
                r'\b(do you know any jokes|got any jokes)\b'
            ],
            'creator': [
                r'\b(who made you|who created you|your creator|your maker)\b',
                r'\b(who built you|who developed you|your developer)\b'
            ],
            'help': [
                r'\b(help|what can you do|commands|options)\b',
                r'\b(how to use|instructions|guide)\b'
            ],
            'goodbye': [
                r'\b(bye|goodbye|see you|farewell|exit|quit)\b',
                r'\b(see ya|catch you later|talk to you later|ttyl)\b'
            ],
            'thanks': [
                r'\b(thank you|thanks|thx|appreciate it)\b',
                r'\b(thank u|thankyou|much appreciated)\b'
            ]
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check patterns and return appropriate response
        for intent, patterns in self.patterns.items():
            for pattern in patterns:
                if re.search(pattern, user_input):
                    return random.choice(self.responses[intent])
        
        # Default response if no pattern matches
        return random.choice(self.responses['default'])

# Initialize chatbot
chatbot = RuleBasedChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_text = request.args.get('msg')
    if user_text:
        bot_response = chatbot.get_response(user_text)
        return jsonify({'response': bot_response})
    return jsonify({'response': 'Please say something!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)