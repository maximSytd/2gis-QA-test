import factory
import factory.fuzzy

COLOR_CHOICES = ["BLUE", "GREEN", "RED", "YELLOW"]

class FavoritePlaceFactory(factory.DictFactory):
    """Dict factory for test favorite place instances."""

    title = factory.Faker("street_name")
    lat = factory.Faker("latitude")
    lon = factory.Faker("longitude")
    color = factory.fuzzy.FuzzyChoice(COLOR_CHOICES)
