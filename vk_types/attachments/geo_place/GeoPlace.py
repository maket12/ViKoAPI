from vk_types.attachments.geo_place.geoplace_subclasses.Place import Place


class GeoPlace:
    def __init__(self, place_type: str, coordinates: str, place: Place | None):
        self.place_type = place_type
        self.coordinates = coordinates
        self.place = place

    def to_dict(self) -> dict:
        """Returns the geo place object as a dictionary."""
        return {
            "place_type": self.place_type,
            "coordinates": self.coordinates,
            "place": self.place.to_dict() if self.place else None
        }

