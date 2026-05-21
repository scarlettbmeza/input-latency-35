import re

# Utility function to validate player usernames

def validate_username(username: str) -> bool:
    """
    Validates a player's username according to specific criteria:
    - Must be 3 to 16 characters long
    - Can include letters, numbers, underscores
    - Cannot start with a number
    """
    if not (3 <= len(username) <= 16):
        return False
    if not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', username):
        return False
    return True

# Function to validate game scores

def validate_score(score: int) -> bool:
    """
    Validates that the score is a non-negative integer.
    """
    return isinstance(score, int) and score >= 0

# Function to validate player ID

def validate_player_id(player_id: str) -> bool:
    """
    Validates a player's ID:
    - Must be a 24-character alphanumeric string
    """
    return bool(re.match(r'^[a-fA-F0-9]{24}$', player_id))
