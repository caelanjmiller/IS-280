class InvalidCommandError(Exception):
    """
    Raised when a player enters an invalid command.
    """
    def __init__(self, message: str ="Invalid command entered. Please try again.") -> None:
        super().__init__(message)

class InvalidActionError(Exception):
    """
    Raised during combat or item usage for invalid actions.
    """
    def __init__(self, message: str ="Invalid ") -> None:
        super().__init__(message)

class QuestAvailableError(Exception):
    """
    Raised when a player attempts to start a quest that is unavailable.
    """
    def __init__(self, quest_name: str) -> None:
        message: str = f"The quest '{quest_name}' is not available."
        super().__init__(message)