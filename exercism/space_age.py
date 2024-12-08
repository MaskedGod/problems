class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year_in_sec = 31_557_600

    def on_mercury(self):
        self.age = round(self.seconds / (self.earth_year_in_sec * 0.2408467), 2)
        return self.age

    def on_venus(self):
        self.age = round(self.seconds / (self.earth_year_in_sec * 0.61519726), 2)
        return self.age

    def on_earth(self):
        self.age = round(self.seconds / self.earth_year_in_sec, 2)
        return self.age

    def on_mars(self):
        self.age = round(self.seconds / (self.earth_year_in_sec * 1.8808158), 2)
        return self.age

    def on_jupiter(self):
        self.age = round(self.seconds / (self.earth_year_in_sec * 11.862615), 2)
        return self.age

    def on_saturn(self):
        self.age = round(self.seconds / (self.earth_year_in_sec * 29.447498), 2)
        return self.age

    def on_uranus(self):
        self.age = round(self.seconds / (self.earth_year_in_sec * 84.016846), 2)
        return self.age

    def on_neptune(self):
        self.age = round(self.seconds / (self.earth_year_in_sec * 164.79132), 2)
        return self.age


print(SpaceAge(1000000000).on_earth())  # 31.68
print(SpaceAge(2134835688).on_mercury())  # 280.88


class SpaceAge(object):
    PLANET_RATIOS = [
        (k, v * 31557600)
        for k, v in (
            ("earth", 1.0),
            ("mercury", 0.2408467),
            ("venus", 0.61519726),
            ("mars", 1.8808158),
            ("jupiter", 11.862615),
            ("saturn", 29.447498),
            ("uranus", 84.016846),
            ("neptune", 164.79132),
        )
    ]

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, ratio in self.PLANET_RATIOS:
            setattr(self, "on_" + planet, self._planet_years(ratio))

    def _planet_years(self, ratio):
        return lambda ratio=ratio: round(self.seconds / ratio, 2)


ratios = {
    "mercury": 0.2408467,
    "venus": 0.6151972,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132,
}
EARTH_YEAR_IN_SECONDS = 31557600.0


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def __getattr__(self, name):
        return lambda: round(
            self.seconds / (EARTH_YEAR_IN_SECONDS * ratios[name[3:]]), 2
        )
