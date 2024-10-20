import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from nltk.corpus import stopwords
import nltk

# download NLTK stopwords (only required once)
nltk.download('stopwords')

# Load the stopwords from NLTK
stop_words = set(stopwords.words('english'))

# Step 1: Load Dataset
def load_data(file_path):
    """Loads the IMDB dataset from a CSV file."""
    data = pd.read_csv(file_path)
    return data['text'], data['sentiment']

# Step 2: Text Preprocessing
def preprocess_text(texts):
    """Cleans the text data and removes stopwords."""
    processed_texts = []
    for text in texts:
        # Remove non-alphabetic characters
        text = re.sub(r'\W', ' ', text)
        # Convert to lowercase
        text = text.lower()
        # Remove stopwords
        text = ' '.join([word for word in text.split() if word not in stop_words])
        processed_texts.append(text)
    return processed_texts

# Step 3: Train and Save the Model and Vectorizer
def train_and_save_model(reviews_train, reviews_test, sentiments_train, sentiments_test):
    """Vectorizes the text data, trains a model, and saves both the model and vectorizer."""
    # Step 3.1: Vectorization (TF-IDF)
    vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2), stop_words='english')

    X_train = vectorizer.fit_transform(reviews_train) 
    X_test = vectorizer.transform(reviews_test) 
    # Vectorize the cleaned text data

    # Define the target sentiment labels
    y_train = sentiments_train
    y_test = sentiments_test

    # Step 3.2: Train a simple logistic regression model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Step 3.3: Evaluate the model (Optional: Check accuracy on test data)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    # Step 3.4: Save the trained model and vectorizer using joblib
    joblib.dump(model, 'model/sentiment_model.pkl')  # Save the trained model
    joblib.dump(vectorizer, 'model/vectorizer.pkl')  # Save the vectorizer

    print("Model and vectorizer have been saved to 'model/' folder.")

if __name__ == "__main__":
    # Load the dataset from "IMDB Dataset.csv"
    reviews_train, sentiments_train = load_data('train.csv')
    
    reviews_test, sentiments_test = load_data('test.csv')

    # Preprocess the text data
    print("Preprocessing the text data...")
    processed_reviews_train = preprocess_text(reviews_train)

    processed_reviews_test = preprocess_text(reviews_test)

    # Train the model and save the vectorizer and model
    print("Training the model and saving vectorizer and model...")
    train_and_save_model(processed_reviews_train, processed_reviews_test, sentiments_train, sentiments_test)
