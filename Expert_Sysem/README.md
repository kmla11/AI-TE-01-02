# Syntecxhub_Rule-Based-Expert-System
A Python-based expert system using forward chaining for medical diagnosis
# Project Overview
I have developed a rule-based Expert System designed to mimic a doctor's diagnostic reasoning. Instead of just giving a final answer, this system "thinks" through the symptoms provided by the user and reaches a logical conclusion using an AI technique called Forward Chaining.

# How the System "Thinks"
The project is built on three core AI concepts:

# Fact Base: 
This is where the system stores the symptoms you enter (like fever, cough, or joint pain).

Knowledge Base: A collection of "If-Then" rules. For example: If a patient has a fever and a rash, then it might be Dengue.

# Inference Engine:
This is the brain of the system. It looks at the facts, matches them with the rules, and keeps digging until it finds a solid diagnosis.

# Key Features
Multi-Step Reasoning: The system doesn't just jump to conclusions. It might first suspect a common cold, but as it finds more symptoms (like a sore throat), it upgrades the diagnosis to Influenza. This is what we call "Rule Chaining."

Full Transparency (Reasoning Path): I believe AI shouldn't be a "black box." My system provides a step-by-step log, so you can see exactly which rules were triggered and why it reached a specific diagnosis.

Built with Python: Since I am focusing on the AI track, I chose Python to keep the logic clean, modular, and easy to scale with more complex rules in the future.

# How to Run & Test
Run the expert_system.py script.

Input a few symptoms when prompted (e.g., fever, cough, fatigue).

The system will process the data and display the Inference Log, showing you the step-by-step path from symptoms to the final medical advice.