class PostsGeo:
    def __init__(self, place_type: str, coordinates: str, place: object | None):
        self.place_type = place_type
        self.coordinates = coordinates
        self.place = place
