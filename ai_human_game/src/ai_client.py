import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from typing import Dict, Any, Type
from pydantic import BaseModel, ValidationError

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
debug = os.getenv('DEBUG', 'false').lower() == 'true'

def initialize_client():
    """Initialize and return an AsyncOpenAI client"""
    return AsyncOpenAI(api_key=openai_api_key)


async def get_response(
    client: AsyncOpenAI, 
    messages: list[Dict[str, str]], 
    response_format: Type[BaseModel] | None = None,
    model: str = "gpt-4o-2024-08-06"
) -> Dict[str, Any] | BaseModel:
    """
    Get a response from the OpenAI API with optional structured output format.
    
    What are Structured Outputs?
    ---------------------------
    Structured Outputs is a feature that forces the AI to return data in a specific JSON format.
    Instead of returning free-form text, the AI must follow our schema exactly.
    This is useful when you need consistent, parseable data instead of natural language.
    
    How it Works:
    ------------
    1. You define a Pydantic model (in models.py) that describes your desired JSON structure
    2. You pass this model to the API call using response_format
    3. The API guarantees that the response will match your schema
    4. The response is automatically parsed into a Python object
    
    Benefits:
    --------
    - No more JSON parsing errors
    - No unexpected fields or missing data
    - Type safety and validation built-in
    - Easier to work with in code
    
    Args:
        client: AsyncOpenAI client instance
        messages: List of message dictionaries (your prompts to the AI)
        response_format: Optional Pydantic model class for structured output
        dashboard: Optional dashboard for tracking API usage
        model: Optional string specifying the OpenAI model to use (default: "gpt-4o-2024-08-06")
    
    Returns:
        If response_format is provided: A parsed Pydantic model instance
        Otherwise: Raw text content from the AI
    
    Example Usage:
    -------------
    response = await get_response(
        client=client,
        messages=[
            {"role": "system", "content": "Analyze this text"},
            {"role": "user", "content": "Some text to analyze"}
        ],
        response_format=ChapterAnalysis  # Your Pydantic model
    )
    # Now response.chapter_summary and response.key_themes are available
    """
    try:
        if response_format:
            # When using structured outputs, we need to:
            # 1. Tell the AI about our requirements in the prompt
            # 2. Pass our schema to the API
            # 3. Validate the response meets our specific needs

            # Make the API call with structured output
            response = await client.beta.chat.completions.parse(
                model=model,
                messages=messages,
                temperature=0.85,
                response_format=response_format
            )

            # Extract the parsed response
            parsed_response = response.choices[0].message.parsed

            # Extract total tokens used
            total_tokens = response.usage.total_tokens if response.usage else 0

            return parsed_response

        else:
            # Regular non-structured API call
            response = await client.chat.completions.create(
                model=model,
                messages=messages,
                stream=False,
            )

            # Extract total tokens used
            total_tokens = response.usage.total_tokens if response.usage else 0

            return response.choices[0].message.content
        
    except Exception as e:
        # Handle any other API errors
        if debug:
            print(f"OpenAI API Error: {str(e)}")
        raise