# AI Based Fake News Detection Tool

## Overview

A Machine Learning and Natural Language Processing (NLP) project that classifies news articles as **REAL** or **FAKE** using **TF-IDF Vectorization** and **Logistic Regression**.

## Features

* Fake/Real News Classification
* Text Preprocessing
* Tokenization & Stopword Removal
* TF-IDF Vectorization
* Confidence Score Prediction
* Model Saving & Loading
* Menu-Driven Interface

## Technologies Used

* Python
* Pandas
* Scikit-learn
* NLTK
* Pickle

## Project Structure

```text
Project-3-Fake-News-Detection/
│
├── dataset.csv
├── generate_dataset.py
├── main.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## Sample Output

```text
-------Fake News Detection-------
1. View Dataset
2. Train Model
3. Detect News
4. Exit

Enter your choice: 3

Enter News Text:
Dragon found in Lucknow

Prediction: FAKE
Confidence Score: 89.43%
```

## Learning Outcomes

* Natural Language Processing (NLP)
* Text Classification
* TF-IDF Feature Extraction
* Machine Learning Workflow
* Model Persistence using Pickle
* Git & GitHub Version Control
