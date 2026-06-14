import pickle
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split

nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess and tokenize the text
def preprocess_text(text):
    if pd.isnull(text):
        return dict()  # or any appropriate value for null entries
    elif isinstance(text, str):
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)
        words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
        return dict(FreqDist(words))
    else:
        return dict()  # or any appropriate value for non-string entries

# Load data from CSV
data = pd.read_csv('dataset.csv')  # Replace 'your_data.csv' with the actual file path

# Prepare the dataset
data['features'] = data['userCMD'].apply(preprocess_text)
dataset = list(zip(data['features'], data['action']))

# Split the dataset into training and testing sets
train_set, test_set = train_test_split(dataset, test_size=0.2, random_state=42)

# Train the Naive Bayes Classifier
classifier = NaiveBayesClassifier.train(train_set)

# Test the classifier
accuracy = nltk.classify.accuracy(classifier, test_set)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Example usage
user_command = "thank you"
predicted_action = classifier.classify(preprocess_text(user_command))
print(f"Predicted Action: {predicted_action}")

# Save the trained model
with open('naive_bayes_model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)
