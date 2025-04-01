from datetime import datetime


class Place:
    def __init__(self, place_id: int, title: str, latitude: int,
                 longitude: int, created_unix: int | None, icon: str,
                 checkins: int | None, updated_unix: int | None, place_type: str,
                 city: int, address: str):
        self.id = place_id
        self.title = title
        self.latitude = latitude
        self.longitude = longitude
        self.created_datetime = datetime.fromtimestamp(created_unix)
        self.icon = icon
        self.checkins = checkins
        self.updated_datetime = datetime.fromtimestamp(updated_unix)
        self.type = place_type
        self.city = city
        self.address = address

    def to_dict(self) -> dict:
        """Returns the place object as a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created": self.created_datetime.isoformat() if self.created_datetime else None,
            "updated": self.updated_datetime.isoformat() if self.updated_datetime else None,
            "icon": self.icon,
            "checkins": self.checkins,
            "type": self.type,
            "city": self.city,
            "address": self.address
        }
