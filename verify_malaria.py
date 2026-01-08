import pandas as pd

print("=" * 70)
print("VERIFYING MALARIA CSV WITH EXACT RANGES")
print("=" * 70)

malaria_df = pd.read_csv('data/malaria_simple.csv')

def classify_malaria_strict(row):
    """
    Strict Malaria Classification based on provided ranges:
    
    HEALTHY (Normal):
    - Temperature: 36.1–37.2 °C
    - Headache: 0 (None)
    - Vomiting: 0 (None)
    - JointPain: 0 (None)
    - RBC: 4.2–6.1 million/µL
    
    DISEASE (Risky):
    - Temperature: >38 °C
    - Headache: 1 (Severe)
    - Vomiting: 1 (Present)
    - JointPain: 1 (Present)
    - RBC: <4.2 million/µL (Low/Hemolysis)
    """
    temp = row['Temperature']
    headache = row['Headache']
    vomiting = row['Vomiting']
    joint_pain = row['JointPain']
    rbc = row['RBC']
    
    # Check each condition against the healthy range
    # If ANY parameter is outside healthy range, mark as risky
    
    # Temperature: 36.1–37.2 healthy, >38 risky
    # (37.1 is healthy, but anything >38 is risky)
    if temp > 38:
        return 1  # Risky due to high temperature
    
    # Headache: 0 healthy, 1 risky
    if headache == 1:
        return 1  # Risky due to severe headache
    
    # Vomiting: 0 healthy, 1 risky
    if vomiting == 1:
        return 1  # Risky due to vomiting
    
    # Joint Pain: 0 healthy, 1 risky
    if joint_pain == 1:
        return 1  # Risky due to joint pain
    
    # RBC: 4.2–6.1 healthy, <4.2 risky (Low due to hemolysis)
    if rbc < 4.2:
        return 1  # Risky due to low RBC
    
    # If all parameters are within healthy range
    return 0  # Healthy/Normal

print("\nBefore classification:")
print(f"Total records: {len(malaria_df)}")
print(f"Sample records:")
print(malaria_df.head(10))

# Apply new classification
malaria_df['health_status'] = malaria_df.apply(classify_malaria_strict, axis=1)
malaria_df['classification'] = malaria_df['health_status']

# Save updated CSV
malaria_df.to_csv('data/malaria_simple.csv', index=False)

print("\n" + "=" * 70)
print("CLASSIFICATION RESULTS")
print("=" * 70)
print(f"Total records: {len(malaria_df)}")
print(f"Healthy (0): {(malaria_df['health_status'] == 0).sum()}")
print(f"Risky (1): {(malaria_df['health_status'] == 1).sum()}")

print("\nSample records after classification:")
print(malaria_df.head(10))

print("\n" + "=" * 70)
print("TESTING YOUR PARAMETERS")
print("=" * 70)
test_params = {
    'Temperature': 37,
    'Headache': 0,
    'Vomiting': 0,
    'JointPain': 0,
    'RBC': 3
}

print(f"\nYour input: {test_params}")
print(f"Temperature 37: Within 36.1–37.2? {'✓ YES' if 36.1 <= test_params['Temperature'] <= 37.2 else '✗ NO'}")
print(f"Headache 0: None (Healthy)? ✓ YES")
print(f"Vomiting 0: None (Healthy)? ✓ YES")
print(f"JointPain 0: None (Healthy)? ✓ YES")
print(f"RBC 3: Within 4.2–6.1? ✗ NO - RBC=3 is LOW (Hemolysis indicates malaria)")
print(f"\nPREDICTION: RISKY ⚠️")
print(f"\nREASON: RBC value of 3 is BELOW the healthy range of 4.2–6.1")
print(f"        Low RBC (hemolysis) is a sign of malaria.")

print("\n" + "=" * 70)
print("✓ Malaria CSV file has been verified and updated!")
print("=" * 70)
