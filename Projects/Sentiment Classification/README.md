# GenAI-Training - Chapter 2: Review of ML Concepts 

A project on **sentiment analysis** was implemented on text data using Python and machine learning.  
It demonstrates:
- Text cleaning and preprocessing
- Feature extraction with TF-IDF
- Handling numeric and categorical features
- Training multiple classification models

---

## Data Preprocessing
- **Text cleaning**: lowercasing, removing URLs, punctuation, numbers, and extra spaces.
- **Sentiment encoding**: `LabelEncoder` converts sentiment labels to numeric.
- **Age feature**: converted age ranges to midpoints.
- **Numeric features**: scaled using `StandardScaler`.
- **Text features**: vectorized using `TfidfVectorizer` (max 5000 features, n-grams 1-2).

---

## Models Used
- Logistic Regression  
- Support Vector Machine (SVM)  
- Random Forest  
- XGBoost  

**Evaluation metrics**: Accuracy and classification report.  
Also visualized **confusion matrix** for Logistic Regression.



