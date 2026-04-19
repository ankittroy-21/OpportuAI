import os
import json
import logging
from typing import Optional, Dict, Any

import google.generativeai as genai
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LLMClient:
    def __init__(self):
        # Configure Gemini
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if gemini_api_key:
            genai.configure(api_key=gemini_api_key)
            self.gemini_model = genai.GenerativeModel("gemini-2.0-flash")
        else:
            logger.warning("GEMINI_API_KEY not found. Gemini will be unavailable.")
            self.gemini_model = None

        # Configure Groq
        groq_api_key = os.getenv("GROQ_API_KEY")
        if groq_api_key:
            self.groq_client = Groq(api_key=groq_api_key)
            self.groq_model = "llama-3.3-70b-versatile"
        else:
            logger.warning("GROQ_API_KEY not found. Groq will be unavailable.")
            self.groq_client = None

    def generate_with_fallback(
        self, 
        prompt: str, 
        use_groq_first: bool = False
    ) -> Optional[str]:
        """
        Try Gemini first, fall back to Groq, then return None if all fail.
        Returns raw text response or None.
        """
        # Attempt 1: Gemini
        if not use_groq_first and self.gemini_model:
            try:
                logger.info("Calling Gemini...")
                response = self.gemini_model.generate_content(prompt)
                return response.text
            except Exception as e:
                logger.warning(f"Gemini failed: {e}. Falling back to Groq.")

        # Attempt 2: Groq
        if self.groq_client:
            try:
                logger.info("Calling Groq...")
                completion = self.groq_client.chat.completions.create(
                    model=self.groq_model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                )
                return completion.choices[0].message.content
            except Exception as e:
                logger.error(f"Groq also failed: {e}.")

        logger.error("All LLM providers failed.")
        return None

    def generate_json(
        self, 
        prompt: str, 
        fallback_json: Dict[str, Any],
        use_groq_first: bool = False
    ) -> Dict[str, Any]:
        """
        Call LLM, parse JSON response, return dict. If all fails, return fallback_json.
        """
        response_text = self.generate_with_fallback(prompt, use_groq_first=use_groq_first)

        if response_text:
            try:
                # Remove markdown code block markers if present
                cleaned = response_text.strip()
                if cleaned.startswith("```json"):
                    cleaned = cleaned[7:]
                if cleaned.startswith("```"):
                    cleaned = cleaned[3:]
                if cleaned.endswith("```"):
                    cleaned = cleaned[:-3]
                result = json.loads(cleaned.strip())

                # ✅ FIX: Ensure verdict includes emoji
                if "verdict" in result:
                    verdict_text = result["verdict"]
                    if "Strong Match" in verdict_text and "🟢" not in verdict_text:
                        result["verdict"] = "Strong Match 🟢"
                    elif "Good Match" in verdict_text and "🟡" not in verdict_text:
                        result["verdict"] = "Good Match 🟡"
                    elif "Not Ready" in verdict_text and "🔴" not in verdict_text:
                        result["verdict"] = "Not Ready 🔴"

                return result
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON: {e}")

        logger.warning("Returning fallback JSON.")
        return fallback_json


# Singleton instance for easy import
llm_client = LLMClient()