from vk_types.attachments.geo_place.geoplace_subclasses.Place import Place


class GeoPlace:
    def __init__(self, place_type: str, coordinates: str, place: Place | None):
        self.place_type = place_type
        self.coordinates = coordinates
        self.place = place
