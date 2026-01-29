# Predicting Student Test Scores

This is the repo for my Kaggle's 2026 playground series - Season 6 Episode 1

## Overview
* Goal: Predict a student's exam score
 
### Initial Exploration
* Look for missing values
    - no missing values

* Understand dtypes
    - categorical variables: age, gender, course, internet_access, study_method, facility_rating, exam_difficulty
    - numerical variables: study_hours, class_attendance, sleep_hours
    - target variable: exam_score (numerical)

* See which features need to be encoded
    
* Ideas for features
* See distribution of variables
    - NOTE: very few people do not have internet access
    - NOTE: Many distributions (exam_score, study_hours, sleep_hours, class_attendance) have high frequencies at either extreme
        - Ex. exam_score has a high frequency of 100's and 20's 
* See variable relationships with score and each oteher

