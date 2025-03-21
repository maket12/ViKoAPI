from datetime import datetime


class GeoPlace:
    def __init__(self, place_id: int, title: str, latitude: int,
                 longitude: int, created_unix: int, icon: str,
                 checkins: int, updated_unix: int, place_type: int,
                 city: int, address: str):
        self.place_id = place_id
        self.title = title
        self.latitude = latitude
        self.longitude = longitude
        self.created_datetime = datetime.fromtimestamp(created_unix)
        self.icon = icon
        self.checkins = checkins
        self.updated_datetime = datetime.fromtimestamp(updated_unix)
        self.place_type = place_type
        self.city = city
        self.address = address
