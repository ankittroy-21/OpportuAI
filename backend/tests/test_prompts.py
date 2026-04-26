import sys
import os
import json

# Add parent directory to path so we can import from utils and prompts
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm_client import llm_client
from prompts.agent02_prompt import AGENT02_PROMPT

# --- Sample Data ---
student_skills = "Python (strong), JavaScript (learning), SQL (beginner)"
student_experience = "Built a personal portfolio website and contributed to open source."
student_education = "B.Tech Computer Science, 3rd year"
student_preferences = "Internship, Remote, Backend Developer"

opportunity_md = """
# Backend Developer Intern
## Requirements:
- Proficiency in Python and Flask/Django
- Experience with SQL databases
- Knowledge of REST APIs
"""

# --- Build Prompt ---
prompt = AGENT02_PROMPT.format(
    student_skills=student_skills,
    student_experience=student_experience,
    student_education=student_education,
    student_preferences=student_preferences,
    opportunity_markdown=opportunity_md
)

# --- Hardcoded Fallback (no import needed) ---
fallback_json = {
    "match_percentage": 65,
    "verdict": "Good Match 🟡",
    "matched_skills": ["python", "sql"],
    "missing_skills": ["docker"],
    "confidence_message": "Fallback response due to LLM error.",
    "apply_now": True
}

# --- Call LLM ---
print("🔄 Calling LLM (Gemini → Groq → Fallback)...")
result = llm_client.generate_json(prompt, fallback_json)

print("\n✅ Match Result:")
print(json.dumps(result, indent=2))