from pydantic import BaseModel
from typing import List, Literal, Optional

class Skill(BaseModel):
    name: str
    level: Literal["strong", "learning", "beginner"]
    since: str

class Preference(BaseModel):
    types: List[Literal["job", "hackathon", "internship"]]
    location: str
    role: str

class StudentProfile(BaseModel):
    id: str
    name: str
    email: str
    skills: List[Skill]
    experience: str
    education: str
    projects: List[str]
    certificates: List[str]
    preferences: Preference
    profile_version: int
    last_updated: str

class Opportunity(BaseModel):
    id: str
    title: str
    company: str
    source: str
    type: str
    apply_url: str
    raw_markdown: str
    scraped_at: str
    expires_at: str
    is_active: bool

class MatchResult(BaseModel):
    match_percentage: int
    verdict: str
    matched_skills: List[str]
    missing_skills: List[str]
    confidence_message: str
    apply_now: bool

class SkillUpdate(BaseModel):
    skill_name: str
    update_type: str
    description: str
    date: str

class LearningStep(BaseModel):
    title: str
    platform: str
    url: str
    duration: str
    free: bool

class LearningPath(BaseModel):
    steps: List[LearningStep]

class AnalyzeRequest(BaseModel):
    url: str
    resume_text: str
    track: str

class AnalyzeResponse(BaseModel):
    opportunity: Opportunity
    match: MatchResult
    draft: str
    learning_path: LearningPath