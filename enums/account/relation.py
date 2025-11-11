from enum import IntEnum


class RelationStatus(IntEnum):
    NOT_MARRIED = 1  # Not married
    IN_A_RELATIONSHIP = 2  # In a relationship
    ENGAGED = 3  # Engaged
    MARRIED = 4  # Married
    ITS_COMPLICATED = 5  # It's complicated
    ACTIVELY_LOOKING = 6  # Actively looking
    IN_LOVE = 7  # In love
    CIVIL_UNION = 8  # In a civil union
    NOT_SPECIFIED = 0  # Not specified

