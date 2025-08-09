def caesar_cipher(text: str, shift: int) -> str:
    """
    Encodes a string using the Caesar cipher.
    
    Args:
        text (str): The input string to be encoded.
        shift (int): The number of positions to shift each letter.

    Returns:
        str: The encoded message.
    """
    result = []

    for char in text:
        if char.isalpha():
            # Preserve case
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)

    return ''.join(result)


