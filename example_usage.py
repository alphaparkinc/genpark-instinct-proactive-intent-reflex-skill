from client import InstinctProactiveIntentReflex
import json

def test_instinct():
    engine = InstinctProactiveIntentReflex()
    print("=== Testing Instinct Proactive Intent Reflex Skill ===")
    
    res = engine.run_benchmark_proactive_reflex()
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    test_instinct()
