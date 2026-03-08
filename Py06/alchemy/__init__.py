__version__ = "1.0.0"
__author__ = "Master Pythonicus"

from .elements import create_air, create_earth, create_fire, create_water
from .potions import healing_potion


def main():
    create_water()
    create_fire()
    create_earth()
    create_air()


def heal():
    return healing_potion()
