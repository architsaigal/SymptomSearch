import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
import numpy as np

def vect_cos(vect, test_list):
    """ Vectorise text and compute the cosine similarity """
    query_0 = vect.transform(test_list)
    query_1 = vect.transform(test_list)
    cos_sim = cosine_similarity(query_0, query_1)  # displays the resulting matrix
    return query_1, np.round(cos_sim.squeeze(), 3)

# Load data
data = pd.read_csv('diseasedataset.csv')
print(data.head())

# Prepare data
y = data.Disease
x = data.drop('Disease', axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Define symptoms for various diseases
symptom_dict = {
    'Dengue': ['rashes', 'chills', 'vomiting', 'fatigue', 'headache', 'fever', 'nausea'],
    'Typhoid': ['chills', 'vomiting', 'fatigue', 'headache', 'nausea', 'constipation', 'diarrhoea'],
    'Common Cold': ['sneezing', 'chills', 'fatigue', 'cough', 'headache', 'malaise', 'phlegm', 'sinus', 'congestion'],
    'Pneumonia': ['chills', 'fatigue', 'cough', 'fever', 'breathlessness', 'sweating', 'malaise', 'phlegm'],
    'Malaria': ['chills', 'vomiting', 'fever', 'sweating', 'headache', 'nausea', 'diarrhoea']
}

# Initialize PorterStemmer
ps = PorterStemmer()

# Get user input and preprocess it
text = input("Enter your text: ").lower()
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text)
filtered_sentence = [w for w in tokens if w.isalnum() and w.lower() not in stop_words]
filtered_sentence = list(dict.fromkeys(filtered_sentence))  # Remove duplicates
print(filtered_sentence)

# Process and analyze symptoms for each disease
for disease, symptoms in symptom_dict.items():
    vectorizer = CountVectorizer(vocabulary=symptoms)
    vectorizer.fit(symptoms)  # Fit on the symptoms list
    filtered_sentence_vect, filtered_sentence_cos = vect_cos(vectorizer, [' '.join(filtered_sentence)])
    print(f'\nThe cosine similarity for {disease} is {filtered_sentence_cos}.')
    print(f'The % match is {filtered_sentence_cos * 100}')
