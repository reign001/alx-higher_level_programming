#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Parameters:
    - text (str): The input text.

    Returns:
    None
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing whitespaces
    text = text.strip()

    # Iterate through each character in the text
    for char in text:
        # Print the character without a newline if it is not '.', '?', or ':'
        if char not in ['.', '?', ':']:
            print(char, end="")
        else:
            # Print the character with two new lines after it
            print(char + "\n\n", end="")
