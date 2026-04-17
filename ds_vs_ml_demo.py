import numpy as np

def data_science_approach(ages, fares, survived):
    """
    Focus: Statistical Analysis & EDA (Exploratory Data Analysis)
    Goal: Find insights and correlations to explain 'Why' people survived.
    """
    avg_age_survivors = np.mean(ages[survived == 1])
    correlation = np.corrcoef(fares, survived)[0, 1]
    
    print(f"[Data Science] Avg Age of Survivors: {avg_age_survivors:.2f}")
    print(f"[Data Science] Correlation between Fare and Survival: {correlation:.2f}")
    
    if correlation > 0.5:
        print("Insight: Wealth (Fare) was a strong predictor of survival.")
    else:
        print("Insight: Fare had less impact than expected; likely other factors (Age/Sex) mattered more.")

def machine_learning_approach(ages, survived):
    """
    Focus: Engineering & Deployment
    Goal: Build a robust system that can handle new data in production.
    """
    # A very simple 'learned' threshold (in reality, an algorithm would find this)
    threshold = 18 
    
    # Predict survival for a new person
    new_passenger_age = 15
    prediction = 1 if new_passenger_age < threshold else 0
    
    status = "Survive" if prediction == 1 else "Not Survive"
    print(f"[ML Engineering] API Response for new passenger (age {new_passenger_age}): {status}")

if __name__ == "__main__":
    # Sample data derived from your Titanic context
    passenger_ages = np.array([22, 38, 26, 35, 2, 54, 27, 14])
    passenger_fares = np.array([7.25, 71.28, 7.92, 53.10, 8.05, 8.45, 51.86, 21.07])
    survivals = np.array([0, 1, 1, 1, 0, 0, 1, 1])

    print("--- Distinction: Data Science vs. ML Engineering ---")
    data_science_approach(passenger_ages, passenger_fares, survivals)
    print("-" * 50)
    machine_learning_approach(passenger_ages, survivals)
    
    # Summary:
    # DS: Uses math/stats to find the 'Why'.
    # MLE: Uses engineering to scale the 'How'.




"""
MIT ML with Python              - Theory                5
IBM AI Engineer Certificate     - Practical             3
CS50 AI                         -                       4
Deep Learning Specialization    - deeplearning.ai       2
Standford Machine Learning Specilization                1

    Google
    Meta
    Microsoft


    
AI dev tools zoomcamp

machine-learning zoomcamp

llm-zoomcamp

mlops zoomcamp

data engineering zoomcamp

career-paths




"""