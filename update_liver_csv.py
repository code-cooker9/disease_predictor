import pandas as pd

# Update Liver Disease CSV with correct health status
print("Updating liver_simple.csv with corrected ranges...")
liver_df = pd.read_csv('data/liver_simple.csv')

def classify_liver(row):
    """
    Correct classification based on healthy ranges:
    - Age: 20-40 healthy, >50 disease
    - Total Bilirubin: 0.1-1.2 healthy, >1.2 disease
    - Direct Bilirubin: 0-0.3 healthy, >0.3 disease
    - Alkaline Phosphatase: 44-147 healthy, >147 disease
    - ALT: 7-56 healthy, >56 disease
    - AST: 10-40 healthy, >40 disease
    """
    age = row['Age']
    tb = row['Total_Bilirubin']
    db = row['Direct_Bilirubin']
    alkphos = row['Alkaline_Phosphotase']
    alt = row['Alamine_Aminotransferase']
    ast = row['Aspartate_Aminotransferase']
    
    # Age: 20-40 healthy, >50 indicates disease
    if age > 50:
        return 1
    # Total Bilirubin: 0.1-1.2 healthy
    if tb < 0.1 or tb > 1.2:
        return 1
    # Direct Bilirubin: 0-0.3 healthy
    if db < 0 or db > 0.3:
        return 1
    # Alkaline Phosphatase: 44-147 healthy
    if alkphos < 44 or alkphos > 147:
        return 1
    # ALT: 7-56 healthy
    if alt < 7 or alt > 56:
        return 1
    # AST: 10-40 healthy
    if ast < 10 or ast > 40:
        return 1
    
    return 0

liver_df['health_status'] = liver_df.apply(classify_liver, axis=1)
liver_df['Dataset'] = liver_df['health_status']
liver_df.to_csv('data/liver_simple.csv', index=False)
print("✓ liver_simple.csv updated with correct health status classifications!")
print(f"✓ Total records: {len(liver_df)}")
print(f"✓ Healthy records (0): {(liver_df['health_status'] == 0).sum()}")
print(f"✓ Risky records (1): {(liver_df['health_status'] == 1).sum()}")
