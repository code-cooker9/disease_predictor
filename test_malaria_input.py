import sys
sys.path.insert(0, '.')
from app import malaria_rule

# Test your input parameters
test_input = {
    'Temperature': 37,
    'Headache': 0,
    'Vomiting': 0,
    'JointPain': 0,
    'RBC': 4.5
}

print("=" * 70)
print("TESTING MALARIA RULE WITH YOUR PARAMETERS")
print("=" * 70)
print(f"\nInput Parameters: {test_input}")
print(f"Temperature: 37 (Healthy range: 36.1–37.2) ✓")
print(f"Headache: 0 (Healthy range: 0 = None) ✓")
print(f"Vomiting: 0 (Healthy range: 0 = None) ✓")
print(f"JointPain: 0 (Healthy range: 0 = None) ✓")
print(f"RBC: 4.5 (Healthy range: 4.2–6.1) ✓")

result = malaria_rule(test_input)
print(f"\nPREDICTION RESULT: {result}")

if result == "Normal":
    print("✅ CORRECT - All parameters are within healthy ranges!")
else:
    print("❌ ISSUE DETECTED - Result should be 'Normal' but got 'Risky'")
    print("\nDebugging info:")
    print(f"  Temperature check (>38): {37 > 38} → Risky? {37 > 38}")
    print(f"  Headache check (==1): {0 == 1} → Risky? {0 == 1}")
    print(f"  Vomiting check (==1): {0 == 1} → Risky? {0 == 1}")
    print(f"  JointPain check (==1): {0 == 1} → Risky? {0 == 1}")
    print(f"  RBC check (<4.2): {4.5 < 4.2} → Risky? {4.5 < 4.2}")

print("\n" + "=" * 70)
