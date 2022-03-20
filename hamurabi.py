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
        print(f'You have {acres} acres now. And {bushels} in storage')

        if acre_bought == 0:
            acres_sold = ask_how_many_acres_to_sell(acres)
            acres -= acres_sold
            bushels += acres_sold * price
            print(f'You currently have {bushels} bushels and {acres} acres after you sold land')

        print(f'It takes {floor(population * 20)} bushels and {acres} after you sold land.')
        bushels_fed_to_people = how_much_grain_to_feed_people(bushels)
        bushels -= bushels_fed_to_people
        print(f'After you fed your people you have {bushels} bushels remaining.')

        print(f'You need 2 bushels per acre, currently you have {bushels}'
              f' and you need 1 person per 10 acres, current population is {population}')
        acres_planted = ask_how_many_acres_to_plant(acres, population, bushels)
        bushels -= acres_planted * 2

        number_of_plague = plague_deaths(population)
        population -= number_of_plague
        if number_of_plague > 0:
            plague(number_of_plague)

        death = starvation_deaths(population, bushels_fed_to_people)
        population -= deaths
        total_deaths = deaths + number_of_plague

        if uprising(population, deaths):
            break

        if deaths == 0:
            immigrants = immigrants(population, acres, bushels)
        population += immigrants

        bushels_used_as_seed = acres_planted * 2
        harvest = harvest(acres_planted, bushels_used_as_seed)
        bushels += harvest

        grain_eaten = grain_eaten_by_rats(bushels)
        if grain_eaten > 0:
            rat_plague(grain_eaten)
        bushels -= grain_eaten

        price = new_cost_of_land()
        total_immigration += immigrants
        total_grain_eaten_by_rats += grain_eaten
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

def plague(number_of_plague):
    print(f'*********************************************************************************'
          f'*********************************************************************************'
          f'***********COVID HAS SWEPT THROUGH THE KINGDOM! {number_of_plague} people have died...***********'
          f'*********************************************************************************'
          f'*********************************************************************************')

def rat_plague(grain_eaten):
    print(f'*********************************************************************************'
          f'*********************************************************************************'
          f'*****A SWARM OF RELENTLESS RATS HAVE APPEARED! {grain_eaten} bushels has been eaten...*****'
          f'*********************************************************************************'
          f'*********************************************************************************')


play_game()
