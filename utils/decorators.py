# utils/decorators.py

import time
import random
import re
from functools import wraps
from google.api_core.exceptions import ResourceExhausted

def intelligent_retry(max_retries=3, initial_delay=20, backoff_factor=2):
    """
    A decorator to retry a function with exponential backoff, but intelligently
    respects the API's suggested 'retry_delay' if available in the error message.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except ResourceExhausted as e:
                    error_message = str(e)
                    # Use regex to find "retry_delay { seconds: XX }" in the error
                    match = re.search(r"retry_delay {\s*seconds:\s*(\d+)\s*}", error_message)
                    
                    wait_time = 0
                    if match:
                        # If the API suggests a delay, use it
                        suggested_delay = int(match.group(1))
                        wait_time = suggested_delay + random.uniform(0, 1) # Add jitter
                        print(f"API suggested a retry delay. Waiting for {wait_time:.2f} seconds...")
                    else:
                        # Fallback to exponential backoff if no specific delay is found
                        wait_time = delay + random.uniform(0, 1) # Add jitter
                        print(f"API rate limit exceeded. Retrying in {wait_time:.2f} seconds... (Attempt {attempt + 1}/{max_retries})")
                        delay *= backoff_factor
                    
                    time.sleep(wait_time)
                    
            print(f"Failed to execute {func.__name__} after {max_retries} attempts.")
            raise ResourceExhausted(f"API call failed after {max_retries} retries.") from e
        return wrapper
    return decorator