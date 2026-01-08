import pandas as pd

print("=" * 70)
print("UPDATING PNEUMONIA CSV WITH CORRECT RANGES")
print("=" * 70)

# Read the pneumonia CSV
pneumonia_df = pd.read_csv('data/pneumonia_simple.csv')

print("\nBefore update:")
print(f"Total records: {len(pneumonia_df)}")
print(f"Sample records:")
print(pneumonia_df.head(10))

def classify_pneumonia(row):
    """
    Pneumonia Classification based on healthy ranges:
    
    HEALTHY (Normal):
    - Age: 20–40
    - Cough Severity: None (0)
    - WBC: 4k–10k
    - Oxygen Saturation: 95–100%
    - Fever: 36.1–37.2°C
    
    DISEASE (Risky):
    - Age: >40 (older adults at higher risk)
    - Cough Severity: Mild/Severe (1,2)
    - WBC: >10k
    - Oxygen Saturation: <94%
    - Fever: >38°C
    """
    age = row['Age']
    cough = row['Cough']
    severity = row['Severity']
    wbc = row['WBC']
    oxygen = row['OxygenSaturation']
    fever = row['Fever']
    
    # Age: 20–40 healthy, >40 at risk (risky)
    if age > 40:
        return 1
    
    # Cough Severity: 0 (None) healthy, 1,2 (Mild/Severe) risky
    if severity > 0:
        return 1
    
    # Fever: 36.1–37.2 healthy, >38 risky
    if fever > 38:
        return 1
    
    # WBC: 4k–10k healthy, >10k risky
    # Handle both formats: 4-10 (in thousands) or 4000-10000 (actual count)
    wbc_normalized = wbc if wbc > 100 else wbc * 1000
    if wbc_normalized > 10000:
        return 1
    
    # Oxygen Saturation: 95–100 healthy, <94 risky
    if oxygen < 94:
        return 1
    
    # All parameters within healthy range
    return 0

# Apply classification
pneumonia_df['health_status'] = pneumonia_df.apply(classify_pneumonia, axis=1)
pneumonia_df['classification'] = pneumonia_df['health_status']

# Save updated CSV
pneumonia_df.to_csv('data/pneumonia_simple.csv', index=False)

print("\n" + "=" * 70)
print("AFTER UPDATE - CLASSIFICATION RESULTS")
print("=" * 70)
print(f"Total records: {len(pneumonia_df)}")
print(f"Healthy (0): {(pneumonia_df['health_status'] == 0).sum()}")
print(f"Risky (1): {(pneumonia_df['health_status'] == 1).sum()}")

print("\nSample records after classification:")
print(pneumonia_df.head(10))

print("\n" + "=" * 70)
print("PNEUMONIA RANGES APPLIED")
print("=" * 70)
print("""
✓ Age: 20–40 healthy, >40 disease
✓ Cough Severity: None (0) healthy, Mild/Severe (1,2) disease
✓ WBC: 4k–10k healthy, >10k disease
✓ Oxygen Saturation: 95–100% healthy, <94% disease
✓ Fever: 36.1–37.2°C healthy, >38°C disease
""")

print("✓ Pneumonia CSV file updated successfully!")
print("=" * 70)
