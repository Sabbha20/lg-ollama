"""
Centralized Tools Module
=========================

This module contains all reusable tools for LangGraph agents.
Import and use: import my_tools
"""

from langchain_core.tools import tool
from dotenv import load_dotenv
import os
import requests

load_dotenv()
# =============================================================================
# Weather Tools
# =============================================================================

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@tool
def get_weather(location:str) -> str:
    """Get current weather for a location.
    
    Use for queries about weather, temperature, or conditions in any city.
    Examples: "weather in Paris", "temperature in Tokyo", "is it raining in London"
    
    Args:
        location: City name (e.g., "New York", "London", "Tokyo")
        
    Returns:
        Current weather information including temperature and conditions.
    """
    try:
        url = f"https://api.weatherapi.com/v1/current.json?q={location}&key={WEATHER_API_KEY}"
        response = requests.get(url, timeout=30)

        response.raise_for_status()
        data = response.json()
        print(f"[TOOL] get_weather ('location') -> '{location}'")

    except Exception as e:
        print(f"Exception has occured with error: {e}")
        return f"Exception has occured with error: {e}"

    return data

# =============================================================================
# Math Tools
# =============================================================================
@tool
def calculate(expression: str) -> str:
    """Calculate a mathematical expression.
    
    USE THIS TOOL FOR:
    - Any mathematical calculations or arithmetic operations
    - Queries involving numbers and operators (+, -, *, /, **, %)
    - Questions asking to compute, calculate, or solve math problems
    - Evaluating mathematical expressions
    
    EXAMPLE QUERIES:
    - "What is 2 + 2?"
    - "Calculate 15 times 7"
    - "Solve 100 / 4"
    - "What's 5 to the power of 3?"
    - "Compute 45 * 12 + 30"
    
    DO NOT USE FOR:
    - Word problems without explicit expressions (extract the math first)
    - Questions about mathematical concepts or theory

    Args:
        expression: Math expression like "2 + 2" or "15 * 7" (use standard Python operators)
    """

    try:
        result = eval(expression)
        print(f"[TOOL] calculate ('{expression}') -> '{result}'")
    except Exception as e:
        print(f"Exception has occured with error: {e}")
        return f"Exception has occured with error: {e}"

    return result