# Smart Recommendation System (AI/ML)

## Project Overview

Smart Recommendation System is an AI/ML based application that provides personalized movie recommendations based on user preferences.

This project uses Content-Based Filtering techniques with TF-IDF Vectorization and Cosine Similarity to analyze movie data and recommend similar movies to users.

---

## Objective

The objective of this project is to build an intelligent recommendation engine that understands user preferences and generates relevant movie recommendations using machine learning techniques.

---

## Features

- View Movie Dataset
- Analyze Dataset Information
- User Preference Based Recommendation
- Content-Based Filtering
- TF-IDF Text Vectorization
- Cosine Similarity Algorithm
- Similarity Score Calculation
- Top-N Movie Recommendations
- Export Recommendations into CSV File

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

---

## Project Structure

Project-5-Smart-Recommendation-System

│
├── dataset.csv
├── main.py
├── recommendations.csv
├── requirements.txt
├── README.md
│
└── screenshots
    ├── dataset_view.png
    ├── analysis.png
    └── recommendation_output.png

---

## Working Process

1. User enters a preferred genre or keyword.

2. Movie information such as genre and description is processed.

3. TF-IDF Vectorization converts text data into numerical vectors.

4. Cosine Similarity compares user preference with available movies.

5. Movies are ranked according to similarity score.

6. Top matching movies are displayed as personalized recommendations.

---

## Installation

Install the required libraries:

pip install -r requirements.txt


---

## How to Run

Run the application using:

python main.py


---

## Example Output

Input:

Enter preferred Genre or Keyword: Sci-Fi


Output:

Recommended Movies:

Interstellar
The Martian
Gravity
Arrival
Passengers


---

## Learning Outcomes

- Implemented AI based recommendation system
- Learned content-based filtering techniques
- Applied NLP concepts for text processing
- Used TF-IDF for feature extraction
- Implemented cosine similarity for recommendations
- Improved understanding of ML based ranking systems

---

## Future Improvements

- Add user login and profile system
- Implement user history based recommendations
- Add collaborative filtering
- Improve recommendation accuracy
- Deploy application using Flask