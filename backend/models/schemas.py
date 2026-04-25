from pydantic import BaseModel, EmailStr
from typing import List, Literal, Optional


# ─── Skill ────────────────────────────────────────────
class Skill(BaseModel):
    name: str
    level: Literal["strong", "learning", "beginner"]
    since: Optional[str] = None


# ─── Preference ───────────────────────────────────────
class Preference(BaseModel):
    types: List[Literal["job", "hackathon", "internship"]]
    location: Optional[str] = None
    role: Optional[str] = None


# ─── Student ──────────────────────────────────────────
class StudentProfile(BaseModel):
    id: str
    supabase_id: str
    name: str
    email: str
    skills: List[Skill] = []
    experience: Optional[str] = None
    experience_level: Optional[str] = None
    education: Optional[str] = None
    location: Optional[str] = None
    projects: List[str] = []
    certificates: List[str] = []
    preferred_roles: List[str] = []
    preferences: Optional[Preference] = None
    profile_version: int = 1
    last_updated: Optional[str] = None


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    supabase_id: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    experience: Optional[str] = None
    experience_level: Optional[str] = None
    education: Optional[str] = None
    location: Optional[str] = None


# ─── Auth ─────────────────────────────────────────────
class SignupRequest(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    student: StudentProfile


# ─── Opportunity ──────────────────────────────────────
class Opportunity(BaseModel):
    id: str
    title: str
    company: Optional[str] = None
    source: Optional[str] = None
    type: Optional[str] = None
    apply_url: str
    raw_markdown: Optional[str] = None
    required_skills: List[str] = []
    location: Optional[str] = None
    deadline: Optional[str] = None
    scraped_at: Optional[str] = None
    expires_at: Optional[str] = None
    is_active: bool = True


# ─── Match ────────────────────────────────────────────
class MatchResult(BaseModel):
    match_percentage: int
    verdict: str
    matched_skills: List[str] = []
    missing_skills: List[str] = []
    confidence_message: str
    apply_now: bool


class MatchResponse(BaseModel):
    id: str
    student_id: str
    opportunity_id: str
    match_percentage: int
    verdict: str
    matched_skills: List[str] = []
    missing_skills: List[str] = []
    confidence_message: str
    apply_now: bool
    cover_letter: Optional[str] = None
    team_pitch: Optional[str] = None
    profile_version_at_match: Optional[int] = None


# ─── Skill Update ─────────────────────────────────────
class SkillUpdate(BaseModel):
    skill_name: str
    update_type: str
    description: Optional[str] = None
    date: Optional[str] = None


class SkillUpdateResponse(BaseModel):
    updated_profile: StudentProfile
    newly_unlocked: List[MatchResponse] = []


# ─── Learning Path ────────────────────────────────────
class LearningStep(BaseModel):
    title: str
    platform: str
    url: str
    duration: Optional[str] = None
    free: bool = True


class LearningPath(BaseModel):
    steps: List[LearningStep] = []


# ─── Analyze ──────────────────────────────────────────
class AnalyzeRequest(BaseModel):
    url: str
    resume_text: str
    track: Literal["job", "hackathon"]


class AnalyzeResponse(BaseModel):
    opportunity: Opportunity
    match: MatchResult
    draft: str
    learning_path: LearningPath


# ─── Profile Build ────────────────────────────────────
class ProfileBuildResponse(BaseModel):
    student: StudentProfile
    message: str = "Profile built successfully"