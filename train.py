import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load your data from the CSV file
data = pd.read_csv('data.csv')

# Assuming your CSV file has columns 'userCMD' and 'action'
X = data['userCMD'].values  # Input
y = data['action'].values    # Output

# Convert text data to numerical values using LabelEncoder
label_encoder = LabelEncoder()

# Fit on both training and testing data to ensure consistent encoding
label_encoder.fit(np.concatenate([X, y]))

# Apply encoding to training data
X_encoded_train = label_encoder.transform(X)
y_encoded_train = label_encoder.transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded_train, y_encoded_train, test_size=0.2, random_state=42)

# Define the LSTM model
model = Sequential()
model.add(Embedding(input_dim=len(label_encoder.classes_), output_dim=50, input_length=1))
model.add(LSTM(100))
model.add(Dense(len(label_encoder.classes_), activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=2)

# Save the trained model
model.save('jarvis.h5')

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')
# Save the label encoder classes
print(label_encoder.classes_)
np.save('label_encoder_classes.npy', label_encoder.classes_)
