from enum import Enum


class RelativeType(Enum):
    CHILD = "child"
    SIBLING = "sibling"
    PARENT = "parent"
    GRANDPARENT = "grandparent"
    GRANDCHILD = "grandchild"
    PARTNER = "partner"
