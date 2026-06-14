import pickle
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess and tokenize the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    return dict(FreqDist(words))

# Load the trained model from the pickle file
with open('naive_bayes_model.pkl', 'rb') as model_file:
    trained_classifier = pickle.load(model_file)

# Example usage: predict action for a user command
user_command = "open file explorer"
predicted_action = trained_classifier.classify(preprocess_text(user_command))
print(f"Predicted Action: {predicted_action}")
