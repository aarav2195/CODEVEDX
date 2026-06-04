# AI Helpdesk Chatbot

## Overview

AI Helpdesk Chatbot is a Python-based conversational AI application designed to answer frequently asked employee queries. The chatbot uses Natural Language Processing (NLP) techniques such as tokenization, stopword removal, and intent-based matching to provide relevant responses from a predefined FAQ dataset.

## Features

* View FAQ Dataset
* Question-Answer Chatbot
* NLP-Based Intent Detection
* Tokenization & Stopword Removal
* Admin FAQ Update Capability
* Dataset Analysis
* Flask Web Application
* Menu-Driven Interface

## Technologies Used

* Python
* Pandas
* NLTK
* Flask
* Git & GitHub

## Project Structure

```text
Project-4-AI-Helpdesk-Chatbot/
│
├── faq_dataset.csv
├── generate_dataset.py
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

Generate Dataset:

```bash
python generate_dataset.py
```

Run Chatbot:

```bash
python main.py
```

Run Flask Application:

```bash
python app.py
```

Open in Browser:

```text
http://127.0.0.1:5000
```

## Sample Output

```text
------AI Helpdesk Chatbot------
1. View FAQ Dataset
2. Chat with Bot
3. Add FAQ
4. Analyze Dataset
5. Exit

Ask a Question:
reset my password

Bot: Use the password reset portal.
```

## Learning Outcomes

* Natural Language Processing (NLP)
* Intent Recognition
* Dataset Management
* Text Preprocessing
* Flask Backend Development
* Git Branching & Collaboration
