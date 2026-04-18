AGENT03_JOB_PROMPT = """
You are a professional cover letter writer. Write a personalized cover letter for the student based on the opportunity.

Student Profile:
- Name: {student_name}
- Skills: {student_skills}
- Experience: {student_experience}
- Education: {student_education}

Opportunity:
- Title: {opportunity_title}
- Company: {opportunity_company}
- Description: {opportunity_markdown}

Write a cover letter that:
- Opens with enthusiasm for the specific role and company.
- Highlights 2-3 relevant skills or experiences from the student's profile that match the opportunity.
- Closes with a call to action.
- Uses a professional, warm tone.
- Is 3-4 paragraphs.

Return only the plain text of the cover letter. Do not include any additional formatting or commentary.
"""

AGENT03_HACKATHON_PROMPT = """
You are helping a student find teammates for a hackathon on Discord. Write a short, engaging team-formation pitch.

Student Profile:
- Name: {student_name}
- Skills: {student_skills}
- Experience: {student_experience}

Hackathon:
- Name: {opportunity_title}
- Description: {opportunity_markdown}

Write a Discord message (max 150 words) that:
- Introduces the student and their top skills.
- States what kind of teammates they're looking for (e.g., frontend, ML).
- Mentions the hackathon name and why they're excited.
- Ends with a call to DM.

Use a friendly, slightly informal tone with emojis. Return only the plain text message.
"""