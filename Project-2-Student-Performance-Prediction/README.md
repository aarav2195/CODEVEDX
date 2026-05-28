# Project 2 – Student Performance Prediction System

## Overview

The Student Performance Prediction System predicts a student’s final performance based on attendance, marks, and study hours. It also includes dataset analysis, missing value handling, and data visualization.

---

## Objective

The goal of this project is to:

- Perform data cleaning and preprocessing
- Analyze student performance data
- Build a machine learning prediction model
- Visualize important trends using charts
- Evaluate model accuracy

---

## Features

### 1. View Dataset
Displays the complete student dataset from CSV.

### 2. Analyze Dataset (EDA)
Provides:
- Total rows and columns
- Mean values
- Minimum values
- Maximum values
- Standard deviation
- Dataset summary

### 3. Handle Missing Values
Detects and fills missing values in the dataset.

### 4. Data Visualization
Creates charts to understand:
- Attendance trends
- Marks distribution
- Study hours comparison
- Final performance patterns

### 5. Predict Student Performance
Predicts final performance using:
- Attendance
- Marks
- Study hours

### 6. Model Accuracy Evaluation
Evaluates machine learning model performance.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## Project Structure

```bash
Project-2-Student-Performance-Prediction/
│
├── dataset.csv
├── generate_dataset.py
├── main.py
├── requirements.txt
└── README.md

## How to Run

Install dependencies:

pip install pandas numpy scikit-learn

Run:

py main.py