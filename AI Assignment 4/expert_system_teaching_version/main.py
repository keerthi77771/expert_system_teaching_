from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    print("=== Laptop Recommendation Expert System ===\n")
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")

    # Budget - three different budget ranges (high, medium, low)
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    elif input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
    else:
        facts.append("budget_low")

    if input("Do you play games frequently? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you do creative work (photo/video/design)? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Do you use it mainly for office work? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    if input("Do you prefer a large screen (15\"+)? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")

    # OS preference (mac, linux, windows)
    if input("Prefer macOS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    elif input("Prefer Linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    else:
        facts.append("pref_os_windows")

    if input("Do you need AI acceleration (GPU for AI models)? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")

    return facts

def main():
    rules = load_rules(KB_PATH)
    facts = collect_initial_facts()

    engine = ForwardChainingEngine(rules)
    engine.assert_facts(facts)

    results = engine.run()

    print("\nFinal Results")
    if results["recommendations"]:
        print()
    for rec in results["recommendations"]:
        # to find out which rule produced the specific recommendation
        matching = [t for t in engine.trace if t["added"] == f"recommend:{rec}"]
        rule_name = matching[0]["rule"] if matching else "Unknown Rule"
        print(f"> Recommendation: {rec}")
        print(f"> Explanation: derived from rule '{rule_name}'")
    if results["specs"]:
        print()
        for spec in results["specs"]:
            matching = [t for t in engine.trace if t["added"] == f"spec:{spec}"]
            rule_name = matching[0]["rule"] if matching else "Unknown Rule"
            print(f"> Specification: {spec}")
            print(f"> Explanation: derived from rule '{rule_name}'")


if __name__ == "__main__":
    main()
