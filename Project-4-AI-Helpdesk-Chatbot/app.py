from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI Helpdesk Chatbot</h1>
    <p>Project 4 Flask Aplication Running</p>
    <p>NLP Based Internal Helpdesk Chatbot</p>
    """
if __name__ == "__main__":
    app.run(debug = True)
