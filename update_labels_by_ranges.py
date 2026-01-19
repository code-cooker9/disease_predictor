import pandas as pd

# Update Kidney Disease CSV
print("Updating kidney_simple.csv...")
kidney_df = pd.read_csv('data/kidney_simple.csv')

def classify_kidney(row):
    sg = row['sg']
    al = row['al']
    rbc = row['rbc']
    pc = row['pc']
    hemo = row['hemo']
    wc = row['wc']
    bp = row['bp']
    
    # Specific Gravity: 1.005–1.030 healthy
    if sg < 1.005 or sg > 1.030:
        return 1
    # Albumin: 3.4–5.4 healthy
    if al < 3.4 or al > 5.4:
        return 1
    # RBC: 4.2–6.1 healthy
    if rbc < 4.2 or rbc > 6.1:
        return 1
    # PC (Platelet Count): 150k–450k healthy
    if pc < 150000 or pc > 450000:
        return 1
    # Hemoglobin: 12–18 healthy (combined range for men/women)
    if hemo < 12 or hemo > 18:
        return 1
    # WBC: 4k–10k healthy
    if wc < 4000 or wc > 10000:
        return 1
    # BP: 90-120 / 60-80 healthy
    if bp >= 140 or bp < 90:
        return 1
    
    return 0

kidney_df['health_status'] = kidney_df.apply(classify_kidney, axis=1)
kidney_df['classification'] = kidney_df['health_status']
kidney_df.to_csv('data/kidney_simple.csv', index=False)
print("✓ kidney_simple.csv updated")


# Update Liver Disease CSV
print("Updating liver_simple.csv...")
liver_df = pd.read_csv('data/liver_simple.csv')

def classify_liver(row):
    age = row['Age']
    bilirubin = row['Total_Bilirubin']
    direct_bilirubin = row['Direct_Bilirubin']
    alkaline = row['Alkaline_Phosphotase']
    alt = row['Alamine_Aminotransferase']
    ast = row['Aspartate_Aminotransferase']
    
    # Age: 20-40 healthy, >50 indicates disease
    if age > 50:
        return 1
    # Total Bilirubin: 0.1-1.2 healthy, >1.2 indicates disease
    if bilirubin > 1.2:
        return 1
    # Direct Bilirubin: 0-0.3 healthy, >0.3 indicates disease
    if direct_bilirubin > 0.3:
        return 1
    # Alkaline Phosphatase: 44-147 healthy, >147 indicates disease
    if alkaline > 147:
        return 1
    # ALT: 7-56 healthy, >56 indicates disease
    if alt > 56:
        return 1
    # AST: 10-40 healthy, >40 indicates disease
    if ast > 40:
        return 1
    
    return 0

liver_df['health_status'] = liver_df.apply(classify_liver, axis=1)
liver_df['Dataset'] = liver_df['health_status']
liver_df.to_csv('data/liver_simple.csv', index=False)
print("✓ liver_simple.csv updated")

# Update Malaria CSV
print("Updating malaria_simple.csv...")
malaria_df = pd.read_csv('data/malaria_simple.csv')

def classify_malaria(row):
    temp = row['Temperature']
    headache = row['Headache']
    vomiting = row['Vomiting']
    joint_pain = row['JointPain']
    rbc = row['RBC']
    
    # Temperature: 36.1-37.2 healthy, >38 indicates disease
    if temp > 38:
        return 1
    # Headache: None (0) healthy, Present (1) indicates disease
    if headache == 1:
        return 1
    # Vomiting: None (0) healthy, Present (1) indicates disease
    if vomiting == 1:
        return 1
    # Joint Pain: None (0) healthy, Present (1) indicates disease
    if joint_pain == 1:
        return 1
    # RBC: 4.2-6.1 healthy, Low indicates disease
    if rbc < 4.2:
        return 1
    
    return 0

malaria_df['health_status'] = malaria_df.apply(classify_malaria, axis=1)
malaria_df['classification'] = malaria_df['health_status']
malaria_df.to_csv('data/malaria_simple.csv', index=False)
print("✓ malaria_simple.csv updated")

# Update Thyroid CSV
print("Updating thyroid_simple.csv...")
thyroid_df = pd.read_csv('data/thyroid_simple.csv')

def classify_thyroid(row):
    tsh = row['TSH']
    t3 = row['T3']
    t4 = row['T4']
    thyroxine = row['Thyroxine']
    
    # TSH: 0.4-4.0 healthy, <0.4 (hyper) or >4.0 (hypo) indicates disease
    if tsh < 0.4 or tsh > 4.0:
        return 1
    # T3: 80-200 healthy, <80 or >200 indicates disease
    if t3 < 80 or t3 > 200:
        return 1
    # T4: 4.5-12 healthy, <4.5 or >12 indicates disease
    if t4 < 4.5 or t4 > 12:
        return 1
    # Thyroxine: Normal (0) healthy, High/Low (1) indicates disease
    if thyroxine == 1:
        return 1
    
    return 0

thyroid_df['health_status'] = thyroid_df.apply(classify_thyroid, axis=1)
thyroid_df.to_csv('data/thyroid_simple.csv', index=False)
print("✓ thyroid_simple.csv updated")

# Update Pneumonia CSV
print("Updating pneumonia_simple.csv...")
pneumonia_df = pd.read_csv('data/pneumonia_simple.csv')

def classify_pneumonia(row):
    age = row['Age']
    cough = row['Cough']
    severity = row['Severity']
    wbc = row['WBC']
    oxygen_sat = row['OxygenSaturation']
    fever = row['Fever']
    
    # Age: 20-40 healthy, Older adults (>50) at higher risk
    if age > 50:
        return 1
    # Cough: None (0) healthy, Present (1) indicates disease
    if cough == 1:
        return 1
    # Severity: None (0) healthy, Mild/Severe (1,2) indicates disease
    if severity > 0:
        return 1
    # WBC: 4k-10k healthy, >10k indicates disease
    if wbc > 10000:
        return 1
    # Oxygen Saturation: 95-100 healthy, <94 indicates disease
    if oxygen_sat < 94:
        return 1
    # Fever: 36.1-37.2 healthy, >38 indicates disease
    if fever > 38:
        return 1
    
    return 0

pneumonia_df['health_status'] = pneumonia_df.apply(classify_pneumonia, axis=1)
pneumonia_df['classification'] = pneumonia_df['health_status']
pneumonia_df.to_csv('data/pneumonia_simple.csv', index=False)
print("✓ pneumonia_simple.csv updated")

print("\n✓ All CSV files updated successfully with health status classifications!")
