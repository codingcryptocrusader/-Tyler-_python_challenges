import string

def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome, ignoring case, spaces, and punctuation."""
    # Normalize: lowercase + filter out non-alphanumeric characters
    normalized = ''.join(char.lower() for char in text if char.isalnum())
    
    # Compare with reversed version
    return normalized == normalized[::-1]
