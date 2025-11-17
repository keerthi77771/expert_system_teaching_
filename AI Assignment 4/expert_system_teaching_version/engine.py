from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """Return True if all antecedents are true and consequent not yet derived."""
        if rule.consequent in self.facts:
            return False
        return all(cond in self.facts for cond in rule.antecedents)

    def run(self) -> None:
        """Implement forward chaining until no new rules can fire."""
        fired_something = True
        while fired_something:
            fired_something = False

            # Sort rules by priority
            for rule in sorted(self.rules, key=lambda r: r.priority, reverse=True):
                if self.can_fire(rule):
                    self.facts.add(rule.consequent)
                    self.trace.append({
                        "rule": rule.name,
                        "added": rule.consequent,
                        "antecedents": rule.antecedents
                    })
                    print(f"Rule fired: {rule.name} → {rule.consequent}")
                    fired_something = True
        return self.conclusions()

    def conclusions(self) -> Dict[str, List[str]]:
        """Separate facts into recommendations, specs, and others."""
        recommendations = [f.split(":", 1)[1] for f in self.facts if f.startswith("recommend:")]
        specs = [f.split(":", 1)[1] for f in self.facts if f.startswith("spec:")]
        others = [f for f in self.facts if not (f.startswith("recommend:") or f.startswith("spec:"))]
        return {
            "recommendations": recommendations,
            "specs": specs,
            "facts": others
        }
