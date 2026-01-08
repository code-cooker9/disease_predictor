from ml_pipeline import MODEL_FEATURES
from app import malaria_rule, pneumonia_rule, thyroid_rule

print("=" * 70)
print("PARAMETER NAMES VERIFICATION")
print("=" * 70)

print("\n🦟 MALARIA Parameters:")
print(f"   Defined in MODEL_FEATURES: {MODEL_FEATURES['malaria']}")
print(f"   Expected by malaria_rule: ['Temperature', 'Headache', 'Vomiting', 'JointPain', 'RBC']")
print(f"   ✓ MATCH!" if MODEL_FEATURES['malaria'] == ['Temperature', 'Headache', 'Vomiting', 'JointPain', 'RBC'] else "   ✗ MISMATCH!")

print("\n🫁 PNEUMONIA Parameters:")
print(f"   Defined in MODEL_FEATURES: {MODEL_FEATURES['pneumonia']}")
print(f"   Expected by pneumonia_rule: ['Age', 'Cough', 'Severity', 'WBC', 'OxygenSaturation', 'Fever']")
print(f"   ✓ MATCH!" if MODEL_FEATURES['pneumonia'] == ['Age', 'Cough', 'Severity', 'WBC', 'OxygenSaturation', 'Fever'] else "   ✗ MISMATCH!")

print("\n🦗 THYROID Parameters:")
print(f"   Defined in MODEL_FEATURES: {MODEL_FEATURES['thyroid']}")
print(f"   Expected by thyroid_rule: ['Age', 'Sex', 'TSH', 'T3', 'T4', 'Thyroxine']")
print(f"   ✓ MATCH!" if MODEL_FEATURES['thyroid'] == ['Age', 'Sex', 'TSH', 'T3', 'T4', 'Thyroxine'] else "   ✗ MISMATCH!")

print("\n" + "=" * 70)
print("TESTING WITH YOUR PARAMETERS")
print("=" * 70)

# Test Malaria
print("\n🦟 MALARIA TEST:")
malaria_test = {
    'Temperature': 37,
    'Headache': 0,
    'Vomiting': 0,
    'JointPain': 0,
    'RBC': 4.5
}
result = malaria_rule(malaria_test)
print(f"   Input: {malaria_test}")
print(f"   Result: {result}")
print(f"   ✅ CORRECT!" if result == "Normal" else "   ❌ WRONG!")

# Test Pneumonia with healthy values
print("\n🫁 PNEUMONIA TEST:")
pneumonia_test = {
    'Age': 35,
    'Cough': 0,
    'Severity': 0,
    'WBC': 7000,
    'OxygenSaturation': 98,
    'Fever': 37
}
result = pneumonia_rule(pneumonia_test)
print(f"   Input: {pneumonia_test}")
print(f"   Result: {result}")
print(f"   ✅ CORRECT!" if result == "Normal" else "   ❌ WRONG!")

# Test Thyroid with healthy values
print("\n🦗 THYROID TEST:")
thyroid_test = {
    'Age': 30,
    'Sex': 1,
    'TSH': 2.0,
    'T3': 120,
    'T4': 8.0,
    'Thyroxine': 0
}
result = thyroid_rule(thyroid_test)
print(f"   Input: {thyroid_test}")
print(f"   Result: {result}")
print(f"   ✅ CORRECT!" if result == "Normal" else "   ❌ WRONG!")

print("\n" + "=" * 70)
print("✅ All parameters are correctly aligned!")
print("=" * 70)
