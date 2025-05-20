from langchain_google_genai import ChatGoogleGenerativeAI
import os
import getpass
from dotenv import load_dotenv

# Load variables from .env file (if it exists)
load_dotenv()

def _set_env(var_name: str) -> None:
    """
    Set an environment variable if not already set.
    Priority order:
    1. Environment variable already set
    2. Variable found in .env file
    3. Prompt user for the value
    """
    if var_name not in os.environ or not os.environ[var_name]:
        value = os.getenv(var_name)
        if not value:
            value = getpass.getpass(f"Enter your {var_name}: ")
        os.environ[var_name] = value




def load_model() -> ChatGoogleGenerativeAI:
    '''
    load gemini llm
    '''
    _set_env("GOOGLE_API_KEY")
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    return llm