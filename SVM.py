import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import joblib

try:
    from imblearn.over_sampling import SMOTE
    has_smote = True
except ImportError:
    has_smote = False

CSV_PATH = "check.csv"
TARGET_COLUMN = "label_tactic"
FEATURE_COLUMNS = None
MODEL_DIR = "saved_models"
TEST_SIZE = 0.2
RANDOM_STATE = 42
APPLY_SMOTE = True

os.makedirs(MODEL_DIR, exist_ok=True)

df = pd.read_csv(CSV_PATH)

if FEATURE_COLUMNS is None:
    FEATURE_COLUMNS = [col for col in df.columns if col != TARGET_COLUMN]

X = df[FEATURE_COLUMNS].values.astype('float32')
y = df[TARGET_COLUMN].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

if APPLY_SMOTE and has_smote:
    sm = SMOTE(random_state=RANDOM_STATE)
    X_train_scaled, y_train = sm.fit_resample(X_train_scaled, y_train)

svm = SVC(kernel='rbf', probability=True, class_weight='balanced', random_state=RANDOM_STATE)
svm.fit(X_train_scaled, y_train)

y_pred = svm.predict(X_test_scaled)
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
import matplotlib.pyplot as plt
plt.show()

scaler_path = os.path.join(MODEL_DIR, 'scaler.joblib')
model_path = os.path.join(MODEL_DIR, 'svm_model.joblib')
joblib.dump(scaler, scaler_path)
joblib.dump(svm, model_path)
print(f"Scaler saved to: {scaler_path}")
print(f"Model saved to: {model_path}")
