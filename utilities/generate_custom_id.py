import uuid


def generate_custom_user_id() -> str:
    """Generate a prefixed unique ID like USR-20250823-abc12345."""
    return f"USER-{uuid.uuid4().hex[:2]}-{uuid.uuid4().hex[:5]}"
