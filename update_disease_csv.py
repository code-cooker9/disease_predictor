import pandas as pd

print("=" * 60)
print("Updating CSV files with corrected health ranges")
print("=" * 60)

# ============================================================
# Update Malaria CSV
# ============================================================
print("\n1. Updating malaria_simple.csv...")
malaria_df = pd.read_csv('data/malaria_simple.csv')

def classify_malaria(row):
    """
    Malaria Classification:
    - Temperature: 36.1-37.2 healthy, >38 disease
    - Headache: 0 healthy, 1 disease
    - Vomiting: 0 healthy, 1 disease
    - JointPain: 0 healthy, 1 disease
    - RBC: 4.2-6.1 healthy, <4.2 disease
    """
    temp = row['Temperature']
    headache = row['Headache']
    vomiting = row['Vomiting']
    joint_pain = row['JointPain']
    rbc = row['RBC']
    
    # Temperature: >38 disease
    if temp > 38:
        return 1
    # Headache: 1 disease
    if headache == 1:
        return 1
    # Vomiting: 1 disease
    if vomiting == 1:
        return 1
    # Joint Pain: 1 disease
    if joint_pain == 1:
        return 1
    # RBC: <4.2 disease
    if rbc < 4.2:
        return 1
    
    return 0

malaria_df['health_status'] = malaria_df.apply(classify_malaria, axis=1)
malaria_df['classification'] = malaria_df['health_status']
malaria_df.to_csv('data/malaria_simple.csv', index=False)
print(f"   ✓ Total records: {len(malaria_df)}")
print(f"   ✓ Healthy (0): {(malaria_df['health_status'] == 0).sum()}")
print(f"   ✓ Risky (1): {(malaria_df['health_status'] == 1).sum()}")

# ============================================================
# Update Thyroid CSV
# ============================================================
print("\n2. Updating thyroid_simple.csv...")
thyroid_df = pd.read_csv('data/thyroid_simple.csv')

def classify_thyroid(row):
    """
    Thyroid Classification:
    - TSH: 0.4-4.0 healthy, <0.4 or >4.0 disease
    - T3: 80-200 healthy, <80 or >200 disease
    - T4: 4.5-12 healthy, <4.5 or >12 disease
    - Thyroxine: 0 (normal) healthy, 1 disease
    """
    tsh = row['TSH']
    t3 = row['T3']
    t4 = row['T4']
    thyroxine = row['Thyroxine']
    
    # TSH: <0.4 or >4.0 disease
    if tsh < 0.4 or tsh > 4.0:
        return 1
    # T3: <80 or >200 disease
    if t3 < 80 or t3 > 200:
        return 1
    # T4: <4.5 or >12 disease
    if t4 < 4.5 or t4 > 12:
        return 1
    # Thyroxine: 1 disease
    if thyroxine == 1:
        return 1
    
    return 0

thyroid_df['health_status'] = thyroid_df.apply(classify_thyroid, axis=1)
thyroid_df.to_csv('data/thyroid_simple.csv', index=False)
print(f"   ✓ Total records: {len(thyroid_df)}")
print(f"   ✓ Healthy (0): {(thyroid_df['health_status'] == 0).sum()}")
print(f"   ✓ Risky (1): {(thyroid_df['health_status'] == 1).sum()}")

# ============================================================
# Update Pneumonia CSV
# ============================================================
print("\n3. Updating pneumonia_simple.csv...")
pneumonia_df = pd.read_csv('data/pneumonia_simple.csv')

def classify_pneumonia(row):
    """
    Pneumonia Classification:
    - Age: >50 disease
    - Cough: 1 disease
    - Severity: >0 disease
    - WBC: >10000 disease
    - OxygenSaturation: <94 disease
    - Fever: >38 disease
    """
    age = row['Age']
    cough = row['Cough']
    severity = row['Severity']
    wbc = row['WBC']
    oxygen = row['OxygenSaturation']
    fever = row['Fever']
    
    # Age: >50 disease
    if age > 50:
        return 1
    # Cough: 1 disease
    if cough == 1:
        return 1
    # Severity: >0 disease
    if severity > 0:
        return 1
    # Fever: >38 disease
    if fever > 38:
        return 1
    # WBC: >10000 disease
    wbc_normalized = wbc if wbc > 100 else wbc * 1000
    if wbc_normalized > 10000:
        return 1
    # Oxygen Saturation: <94 disease
    if oxygen < 94:
        return 1
    
    return 0

pneumonia_df['health_status'] = pneumonia_df.apply(classify_pneumonia, axis=1)
pneumonia_df['classification'] = pneumonia_df['health_status']
pneumonia_df.to_csv('data/pneumonia_simple.csv', index=False)
print(f"   ✓ Total records: {len(pneumonia_df)}")
print(f"   ✓ Healthy (0): {(pneumonia_df['health_status'] == 0).sum()}")
print(f"   ✓ Risky (1): {(pneumonia_df['health_status'] == 1).sum()}")

print("\n" + "=" * 60)
print("✓ All CSV files updated successfully!")
print("=" * 60)
