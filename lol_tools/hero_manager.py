class HeroManager:
    def __init__(self, api):
        self.api = api

    def get_heroes(self):
        return self.api.get_heroes()
