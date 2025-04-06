from enum import IntEnum


class ReportReason(IntEnum):
    SPAM = 0
    CHILD_PORN = 1
    EXTREMISM = 2
    VIOLENCE = 3
    DRUGS = 4
    PORN = 5
    INSULT = 6
    SUICIDE = 8
