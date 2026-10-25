import time

class ExpertSystem:
    def __init__(self):
        # 1. Facts Base (Initial Symptoms)
        self.facts = set()
        
        # 2. Knowledge Base (Rules)
        self.rules = [
            {"id": "R01", "conditions": ["fever", "cough"], "produces": "flu_suspected", "explanation": "Fever + Cough -> Influenza Suspected"},
            {"id": "R02", "conditions": ["fever", "rash"], "produces": "dengue_suspected", "explanation": "Fever + Skin Rash -> Dengue Suspected"},
            {"id": "R03", "conditions": ["flu_suspected", "sore_throat"], "produces": "influenza", "explanation": "Flu Suspected + Sore Throat -> Influenza Confirmed"},
            {"id": "R04", "conditions": ["dengue_suspected", "joint_pain"], "produces": "dengue_fever", "explanation": "Dengue Suspected + Joint Pain -> Dengue Fever Confirmed"},
            {"id": "R05", "conditions": ["influenza", "fatigue"], "produces": "bed_rest_critical", "explanation": "Influenza + Fatigue -> Extended Bed Rest Critical"}
        ]
        
        self.log = []

    def forward_chaining(self, initial_symptoms):
        self.facts = set(initial_symptoms)
        fired_rules = set()
        changed = True
        
        print(f"\n[STARTING INFERENCE] Initial Facts: {self.facts}")
        
        while changed:
            changed = False
            for rule in self.rules:
                if rule["id"] in fired_rules:
                    continue
                
                # Check if all conditions are met
                if all(condition in self.facts for condition in rule["conditions"]):
                    # Produce new fact
                    new_fact = rule["produces"]
                    if new_fact not in self.facts:
                        self.facts.add(new_fact)
                        self.log.append(rule["explanation"])
                        fired_rules.add(rule["id"])
                        print(f"  > Rule {rule['id']} Fired: Derived '{new_fact}'")
                        changed = True
        
        return self.facts

    def display_results(self):
        print("\n" + "="*30)
        print("FINAL INFERENCE REPORT")
        print("="*30)
        
        if not self.log:
            print("No conclusions could be reached.")
        else:
            print("\nReasoning Path (Inference Log):")
            for i, step in enumerate(self.log, 1):
                print(f"{i}. {step}")
            
            print("\nFinal Conclusions:")
            # Filter out original symptoms to show only what was inferred
            conclusions = [f for f in self.facts if "_" in f or f == "influenza"] 
            for c in conclusions:
                print(f" - {c.upper().replace('_', ' ')}")

# --- Execution ---
if __name__ == "__main__":
    system = ExpertSystem()
    
    print("Available Symptoms: fever, cough, rash, joint_pain, sore_throat, fatigue")
    user_input = input("Enter symptoms (comma separated): ").lower().replace(" ", "").split(",")
    
    system.forward_chaining(user_input)
    system.display_results()