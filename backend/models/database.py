from sqlalchemy import (
    Column, String, Integer, Boolean,
    Text, TIMESTAMP, ForeignKey, ARRAY
)
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    supabase_id = Column(String(255), unique=True, nullable=False)
    resume_url = Column(Text)
    experience_level = Column(String(50))
    education = Column(Text)
    location = Column(String(255))
    preferred_roles = Column(ARRAY(Text))
    preferred_types = Column(ARRAY(Text))
    profile_version = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, server_default=func.now())
    last_updated = Column(TIMESTAMP, server_default=func.now())


class Skill(Base):
    __tablename__ = "skills"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    level = Column(String(50))
    since = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(500), nullable=False)
    company = Column(String(255))
    source = Column(String(100))
    type = Column(String(50))
    apply_url = Column(Text, nullable=False)
    raw_markdown = Column(Text)
    required_skills = Column(ARRAY(Text))
    location = Column(String(255))
    deadline = Column(TIMESTAMP)
    scraped_at = Column(TIMESTAMP, server_default=func.now())
    expires_at = Column(TIMESTAMP)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())


class Match(Base):
    __tablename__ = "matches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    opportunity_id = Column(UUID(as_uuid=True), ForeignKey("opportunities.id", ondelete="CASCADE"), nullable=False)
    match_percentage = Column(Integer)
    verdict = Column(String(100))
    matched_skills = Column(ARRAY(Text))
    missing_skills = Column(ARRAY(Text))
    confidence_message = Column(Text)
    apply_now = Column(Boolean, default=False)
    cover_letter = Column(Text)
    team_pitch = Column(Text)
    profile_version_at_match = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())


class SkillUpdate(Base):
    __tablename__ = "skill_updates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id", ondelete="CASCADE"), nullable=False)
    skill_name = Column(String(255), nullable=False)
    update_type = Column(String(100))
    description = Column(Text)
    date = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())


class LearningPath(Base):
    __tablename__ = "learning_paths"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    match_id = Column(UUID(as_uuid=True), ForeignKey("matches.id", ondelete="CASCADE"), nullable=False)
    steps = Column(JSONB, default=list)
    created_at = Column(TIMESTAMP, server_default=func.now())