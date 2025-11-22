from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
import time
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Accessibility Text Simplifier API")

# Disable CORS. Do not remove this for full-stack development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))

MODEL = os.getenv("MODEL", "gpt-4o-mini")  # Default to faster model
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "200"))  # Reduced for faster responses

class SimplifyRequest(BaseModel):
    text: str
    level: str = "intermediate"  # basic, intermediate, advanced

class SimplifyResponse(BaseModel):
    original_text: str
    simplified_text: str
    level: str
    word_count_original: int
    word_count_simplified: int
    reading_level: str

class ExplainWordRequest(BaseModel):
    word: str
    context: str = ""

class ExplainWordResponse(BaseModel):
    word: str
    simple_definition: str
    example: str

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.post("/api/simplify", response_model=SimplifyResponse)
async def simplify_text(request: SimplifyRequest):
    """
    Simplify complex text to make it more accessible.
    Levels:
    - basic: Elementary school level (ages 8-10)
    - intermediate: Middle school level (ages 11-14)
    - advanced: High school level (ages 15-18)
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    if request.level not in ["basic", "intermediate", "advanced"]:
        raise HTTPException(status_code=400, detail="Level must be basic, intermediate, or advanced")
    
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    level_prompts = {
        "basic": """Rewrite this text for an 8-10 year old child. Use:
- Very simple words (no more than 2 syllables when possible)
- Short sentences (5-10 words)
- Active voice
- Concrete examples
- No jargon or technical terms
- Keep output under 150 words and 3-5 short sentences

Original text: {text}

Simplified version:""",
        "intermediate": """Rewrite this text for an 11-14 year old student. Use:
- Simple, everyday words
- Clear, medium-length sentences (10-15 words)
- Active voice mostly
- Explain any necessary technical terms
- Break down complex ideas
- Keep output under 150 words and 3-5 sentences

Original text: {text}

Simplified version:""",
        "advanced": """Rewrite this text for a 15-18 year old high school student. Use:
- Clear, straightforward language
- Well-structured sentences
- Explain technical terms when used
- Maintain accuracy while improving clarity
- Remove unnecessary complexity
- Keep output under 150 words and 3-5 sentences

Original text: {text}

Simplified version:"""
    }
    
    reading_levels = {
        "basic": "Elementary (Ages 8-10)",
        "intermediate": "Middle School (Ages 11-14)",
        "advanced": "High School (Ages 15-18)"
    }
    
    try:
        prompt = level_prompts[request.level].format(text=request.text)
        
        start_time = time.time()
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an expert at simplifying complex text to make it accessible to different reading levels. Preserve the core meaning while making it easier to understand. Be concise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=MAX_TOKENS
        )
        latency_ms = int((time.time() - start_time) * 1000)
        
        simplified_text = response.choices[0].message.content.strip()
        
        print(f"Simplification completed in {latency_ms}ms using model {MODEL}")
        
        return SimplifyResponse(
            original_text=request.text,
            simplified_text=simplified_text,
            level=request.level,
            word_count_original=len(request.text.split()),
            word_count_simplified=len(simplified_text.split()),
            reading_level=reading_levels[request.level]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error simplifying text: {str(e)}")

@app.post("/api/explain-word", response_model=ExplainWordResponse)
async def explain_word(request: ExplainWordRequest):
    """
    Explain a difficult word in simple terms with an example.
    """
    if not request.word.strip():
        raise HTTPException(status_code=400, detail="Word cannot be empty")
    
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        context_info = f"\n\nContext where the word appears: {request.context}" if request.context else ""
        
        prompt = f"""Explain the word "{request.word}" in very simple terms that a 10-year-old can understand.{context_info}

Provide:
1. A simple definition (one sentence, using everyday words)
2. An example sentence showing how to use it

Format your response as:
Definition: [simple definition]
Example: [example sentence]"""
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert at explaining difficult words in simple, accessible language for children and non-native speakers."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )
        
        content = response.choices[0].message.content.strip()
        
        lines = content.split('\n')
        definition = ""
        example = ""
        
        for line in lines:
            if line.startswith("Definition:"):
                definition = line.replace("Definition:", "").strip()
            elif line.startswith("Example:"):
                example = line.replace("Example:", "").strip()
        
        if not definition:
            definition = content.split('\n')[0]
        if not example and len(lines) > 1:
            example = lines[-1]
        
        return ExplainWordResponse(
            word=request.word,
            simple_definition=definition,
            example=example
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error explaining word: {str(e)}")

@app.get("/api/stats")
async def get_stats():
    """
    Get API statistics and information.
    """
    return {
        "service": "Accessibility Text Simplifier",
        "version": "1.0.0",
        "description": "AI-powered text simplification for accessibility",
        "levels": ["basic", "intermediate", "advanced"],
        "features": [
            "Multi-level text simplification",
            "Word explanations",
            "Reading level indicators",
            "Word count comparison"
        ]
    }
