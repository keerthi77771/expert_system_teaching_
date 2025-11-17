import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "kb", "laptop_rules.json")

def run_test(name, input_facts, expected_recommendations=None, expected_specs=None):
    """Runs a single forward-chaining test case and checks expected outputs."""
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    engine.assert_facts(input_facts)
    result = engine.run()

    recs = set(result["recommendations"])
    specs = set(result["specs"])
    expected_recs = set(expected_recommendations or [])
    expected_specs = set(expected_specs or [])

    passed = recs == expected_recs and specs == expected_specs

    print(f"\nTest: {name}")
    print(f"  Input Facts: {input_facts}")
    if expected_recs:
        print(f"  Expected Recommendation(s): {expected_recs}")
    if expected_specs:
        print(f"  Expected Specification(s): {expected_specs}")
    print(f"  Got Recommendations: {recs}")
    print(f"  Got Specifications: {specs}")
    print(f"  RESULT: {'PASS ✅' if passed else 'FAIL ❌'}")

if __name__ == "__main__":
    # 1. Premium Ultrabook
    run_test(
        "Premium Ultrabook",
        ["budget_high", "portable", "long_battery"],
        expected_recommendations=["premium_ultrabook"]
    )

    # 2. Student Ultrabook
    run_test(
        "Student Ultrabook",
        ["budget_low", "office_only", "portable"],
        expected_recommendations=["budget_ultrabook"]
    )

    # 3. Midrange Gaming Laptop
    run_test(
        "Midrange Gaming Laptop",
        ["gaming", "budget_medium"],
        expected_recommendations=["midrange_gaming_laptop"]
    )

    # 4. High-End Gaming Laptop
    run_test(
        "High-End Gaming Laptop",
        ["gaming", "budget_high"],
        expected_recommendations=["high_end_gaming_laptop"]
    )

    # 5. Creative Work (Portable)
    run_test(
        "Creative Work (Portable)",
        ["creative_work", "portable"],
        expected_specs=["ram_16_plus"]
    )

    # 6. Creative Work (Large Screen)
    run_test(
        "Creative Work (Large Screen)",
        ["creative_work", "large_screen"],
        expected_specs=["display_15_plus_color_accurate"]
    )

    # 7. Frequent Traveler (Battery Life)
    run_test(
        "Frequent Traveler (Battery Life)",
        ["travel_often", "long_battery"],
        expected_specs=["battery_60wh_plus"]
    )

    # 8. macOS Preference
    run_test(
        "macOS Preference",
        ["pref_os_macos"],
        expected_specs=["macos_required"]
    )

    # 9. Linux Office User
    run_test(
        "Linux Office User",
        ["pref_os_linux", "office_only"],
        expected_specs=["linux_friendly_hw"]
    )

    # 10. AI Acceleration Need
    run_test(
        "AI Acceleration Need",
        ["needs_ai_accel"],
        expected_specs=["gpu_with_tensor_cores"]
    )
