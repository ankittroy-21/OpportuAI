export type SkillLevel = "strong" | "learning" | "beginner";
export type OpportunityType = "job" | "hackathon" | "internship";
export type Verdict = "Strong Match 🟢" | "Good Match 🟡" | "Not Ready 🔴";

export interface Skill {
  name: string;
  level: SkillLevel;
  since: string;
}

export interface Preference {
  types: OpportunityType[];
  location: string;
  role: string;
}

export interface StudentProfile {
  id: string;
  name: string;
  email: string;
  skills: Skill[];
  experience: string;
  education: string;
  projects: string[];
  certificates: string[];
  preferences: Preference;
  profile_version: number;
  last_updated: string;
}

export interface Opportunity {
  id: string;
  title: string;
  company: string;
  source: string;
  type: string;
  apply_url: string;
  raw_markdown: string;
  scraped_at: string;
  expires_at: string;
  is_active: boolean;
}

export interface MatchResult {
  match_percentage: number;
  verdict: Verdict;
  matched_skills: string[];
  missing_skills: string[];
  confidence_message: string;
  apply_now: boolean;
}

export interface SkillUpdate {
  skill_name: string;
  update_type: string;
  description: string;
  date: string;
}

export interface LearningStep {
  title: string;
  platform: string;
  url: string;
  duration: string;
  free: boolean;
}

export interface LearningPath {
  steps: LearningStep[];
}

export interface AnalyzeRequest {
  url: string;
  resume_text: string;
  track: string;
}

export interface AnalyzeResponse {
  opportunity: Opportunity;
  match: MatchResult;
  draft: string;
  learning_path: LearningPath;
}