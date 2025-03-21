from vk_types.post.post_attributes.Place import GeoPlace


class PostsGeo:
    def __init__(self, place_type: str, coordinates: str, place: GeoPlace | None):
        self.place_type = place_type
        self.coordinates = coordinates
        self.place = place
