import pandas as pd

# Read the CSV
df = pd.read_csv('data/pneumonia_simple.csv')

# Combine Cough and Severity into Cough_Severity
# Logic: 0 = No Cough (Cough=0, Severity=0)
#        1 = Mild Cough (Cough=1, Severity=0 or 1)
#        2 = Severe Cough (Cough=1, Severity=2)
def combine_cough_severity(row):
    cough = row['Cough']
    severity = row['Severity']
    
    if cough == 0:
        return 0  # No cough
    elif severity == 2:
        return 2  # Severe cough
    else:
        return 1  # Mild cough

df['CoughSeverity'] = df.apply(combine_cough_severity, axis=1)

# Drop old columns
df = df.drop(columns=['Cough', 'Severity'])

# Reorder columns to put CoughSeverity after Age
cols = list(df.columns)
cols.remove('CoughSeverity')
cols.insert(1, 'CoughSeverity')
df = df[cols]

# Save
df.to_csv('data/pneumonia_simple.csv', index=False)

print(f"✓ Combined Cough and Severity into CoughSeverity")
print(f"Total records: {len(df)}")
print(f"\nNew CSV Structure:")
print(df.head(10))
print(f"\nCoughSeverity value counts:")
print(df['CoughSeverity'].value_counts().sort_index())
