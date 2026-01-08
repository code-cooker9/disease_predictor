import pandas as pd
from app import pneumonia_rule

# Read the updated CSV
df = pd.read_csv('data/pneumonia_simple.csv')

print("Testing pneumonia predictions with combined CoughSeverity field...\n")
print(f"CSV columns: {list(df.columns)}")
print(f"CSV shape: {df.shape}\n")

# Test cases
test_cases = [
    # (Age, CoughSeverity, WBC, OxygenSaturation, Fever, Expected)
    (35, 0, 7000, 98, 37, "Normal"),       # All healthy
    (45, 1, 7000, 98, 37, "Risky"),        # Mild cough
    (45, 2, 7000, 98, 37, "Risky"),        # Severe cough
    (60, 0, 7000, 98, 37, "Risky"),        # Age >50
    (35, 0, 11000, 98, 37, "Risky"),       # WBC >10k
    (35, 0, 7000, 92, 37, "Risky"),        # O2 <94
    (35, 0, 7000, 98, 39, "Risky"),        # Fever >38
]

print("Test Results:")
print("-" * 80)
for age, cough_severity, wbc, o2, fever, expected in test_cases:
    inputs = {
        'Age': str(age),
        'CoughSeverity': str(cough_severity),
        'WBC': str(wbc),
        'OxygenSaturation': str(o2),
        'Fever': str(fever)
    }
    result = pneumonia_rule(inputs)
    status = "✓" if result == expected else "✗"
    print(f"{status} Age={age}, CoughSeverity={cough_severity}, WBC={wbc}, O2={o2}, Fever={fever}")
    print(f"   Expected: {expected}, Got: {result}")

print("\n" + "-" * 80)
print("CSV Record Distribution:")
print(f"Total records: {len(df)}")
print(f"CoughSeverity value counts:")
print(df['CoughSeverity'].value_counts().sort_index())
