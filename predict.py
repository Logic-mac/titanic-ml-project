import pandas as pd
import joblib

# Load model
model = joblib.load("titanic_model.pkl")

# Load test dataset
test_data = pd.read_csv("test.csv")

# Fill missing values
test_data['Age'].fillna(test_data['Age'].median(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].median(), inplace=True)
test_data['Embarked'].fillna(test_data['Embarked'].mode()[0], inplace=True)

# Drop unnecessary columns
passenger_ids = test_data['PassengerId']

test_data.drop(['Cabin', 'Name', 'Ticket', 'PassengerId'], axis=1, inplace=True)

# Encode categorical values
test_data['Sex'] = test_data['Sex'].map({'male': 1, 'female': 0})
test_data['Embarked'] = test_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Prediction
predictions = model.predict(test_data)

# Save submission file
submission = pd.DataFrame({
    'PassengerId': passenger_ids,
    'Survived': predictions
})

submission.to_csv("submission.csv", index=False)

print("Prediction completed")
print(submission.head())