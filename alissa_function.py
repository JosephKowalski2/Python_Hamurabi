import random


def get_starvation_deaths(population, grain_fed_to_people):
    number_of_starved = population - grain_fed_to_people / 20
    if number_of_starved > 0:
        print("****** Unfortunately this year we "  
        "have", number_of_starved, "People Starved****") + "\n"
        return number_of_starved
    else:
        print("****** You are brilliant Hammurabi! This year no one has starved*****")
        return 0

def uprising_bool(population, num_people_starved):
    if num_people_starved > 0.45 * population:
        return 0

def get_immigrants(population, acres, bushels, number_of_starved):
    if number_of_starved:
        print("*** Oh great Hamurabi, due to starvation, No immigrants this year." " come to our kingdom***")
        return 0
    else:
        num_of_immigrants = (20 * acres + bushels) / (100 * population) + 1
        return num_of_immigrants


def get_unit_havst():
    return random.randint(1, 7)  # get random # between 1-6


def get_havst_bushels(acres, unit_havst):
    bushels_havst = acres * unit_havst
    return bushels_havst



def do_rat_infestation(havst):
    if random.randint(0, 99) < 40:
        bushels_destroyed = random.randint(10, 30) * havst / 100
        return bushels_destroyed
    else:
        return 0

def new_cost_of_land():
    land_price = random.randint(17, 23)
    return land_price


