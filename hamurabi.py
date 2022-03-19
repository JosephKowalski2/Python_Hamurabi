from math import floor

def play_game():
    years = 1
    population = 100
    bushels = 2800
    acres = 1000
    price = 19
    acres_bought = 0
    acres_sold = 0
    number_of_plague = 0
    bushels_fed_to_people = 0
    harvest = 0
    deaths = 0
    immigrants = 0
    grain_eaten = 0
    acres_planted = 0
    bushels_used_as_seed = 0
    total_deaths = 0
    total_immigration = 0
    total_grain_eaten_by_rats = 0

    while years <= 10:
        summary(years, deaths, immigrants, population, harvest, grain_eaten, bushels, acres, price)
        print(f'You can buy {floor(bushels / price)} acres of land')
        acre_bought = ask_how_many_acres_to_buy(price, bushels)
        acres += acre_bought
        bushels -= acre_bought * price
        years += 1


def summary(years, deaths, immigrants, population, harvest, grain_eaten, bushels, acres, price):
    print_summary = """
            O great Hammurabi!
            You are in year {years} of your 10 year rule.
            In the previous year, {deaths} people starved to death.
            In the previous year, {immigrants} people entered the kingdom.
            The population is now {population}.
            We harvested {harvest} bushels.
            Rats destroyed {grain_eaten} bushels, leaving {bushels} bushels in storage.
            The city owns {acres} acres of land.
            Land is currently worth {price} bushels per acre.
            """.format(years=years, deaths=deaths, immigrants=immigrants, population=population, harvest=harvest,
                       grain_eaten=grain_eaten, bushels=bushels, acres=acres, price=price)
    return print(print_summary)

play_game()
