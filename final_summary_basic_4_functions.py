# print final summary
import math
from random import randrange
# population=0
# deaths=0
# years=0
# total_deaths=0
# total_immigration =0
# total_grain_eating_by_rats=0
# bushels=0
# acres=0
# def final_summary():
#     if uprising(population, deaths):
#         print(f'The people threw you out because  {deaths} people died from starvation... ')
#         print(f"Maybe being king doesn't suite you... try Zip Code instead...You have lasted { years} year(s)! A total of {total_deaths}  people died.")
#         print(f"{total_immigration } people have chosen to come to your lousy kingdom and the final population was {population }.")
#         print(f"Somehow mutant rats ate a total of {total_grain_eating_by_rats} bushels... gross... Leaving  {bushels} in storage.")
#         print(f"Finally you monopolized {acres} acres of land")
#
#     elif (deaths<10 and (acres/population) * 100 ) > 10 and years ==10 :
#         print(f"All has come to an end! KING OF THE NORTH!!! YOU WILL BE REMEMBERED!!! You have lasted {years} years(s)")
#         print(f"A total of  {total_deaths}  people died. { total_immigration} people have chosen to come to your amazing kingdom and the final population was {population}.")
#         print(f" Somehow mutant rats ate a total of {total_grain_eating_by_rats} bushels... gross...")
#         print(f"Leaving { bushels}  in storage. Finally you monopolized {acres }acres of land.")
#
#     elif (deaths <15 and  (acres/population)* 100) >5 and years == 10 :
#         print(f"All has come to an end! You were an average king...You have lasted {years} year(s)! A total of {total_deaths} people died.")
#         print(f"{ total_immigration } people have chosen to come to your amazing kingdom and the final population was {population}.")
#         print(f"Somehow mutant rats ate a total of {total_grain_eating_by_rats} bushels... gross..Leaving {bushels} in storage.")
#         print(f"Finally you monopolized {acres } acres of land.")
#
#     elif (deaths <20 and ((acres/population)*100)) >0 && years ==10 :
#         print(f"All has come to an end! Your people weren't happy but I guess you did it... king...You have lasted { years} year(s)!")
#         print(f"A total of {total_deaths} people died. {total_immigration} people have chosen to come to your amazing kingdom and the final population was {population}.")
#         print(f"Somehow mutant rats ate a total of {total_grain_eating_by_rats} bushels... gross...")
#         print(f"Leaving  {bushels}in storage. Finally you monopolized {acres }acres of land.")
#
#     else:
#         print(f"All has come to an end! You call yourself a king? Psh... You have lasted {years} years(s)!")
#         print(f" A total of  {total_deaths }people died.{total_immigration} people have chosen to come to your amazing kingdom and the final population was {population }.")
#         print(f"Somehow mutant rats ate a total of {total_grain_eating_by_rats} bushels... gross...")
#         print(f"Leaving {bushels}in storage.Finally you monopolized { acres} acres of land.")

#input prompt
def get_number(message):
    while True :
         # print({message})
         try :
             return input(message)
         except  ValueError :
             print(f"{message} isn't a number!")

#acres to buy
def ask_how_many_acres_to_buy( price:int, bushels:int ) ->int:
    acres_bought = int(get_number("How many acres do you want to buy?\n"))
    while ((price *acres_bought) >bushels or (acres_bought <0)) :
        acres_bought =int(get_number("You can't do that, how many acres CAN you buy???\n"))
    return acres_bought
#acres to sell
def ask_how_many_acres_to_sell(acres_owned:int) -> int :
    acres_sold=int(get_number("How many acres do you want to sell?\n"))
    while ((acres_sold >acres_owned) or (acres_sold <0 )) :
        acres_sold =int(get_number("That makes no sense...try again...\n"))
    return acres_sold

#grains to feed
def how_many_grains_to_feed_people(bushes:int)->int:
    bushels_fed_to_people = int(get_number("How much grain do you want to feed your people?\n"))
    while((bushels_fed_to_people >bushes) or bushels_fed_to_people <0) :
        bushels_fed_to_people=int(get_number("Are you serious?, how much are you actually going to feed them?\n"))
    return bushels_fed_to_people

#acres to plant
def ask_how_many_acres_to_plant(acres_owned:int,population:int,bushles:int)->int:
    acres_to_plant=int(get_number("How many acres do you want to plant?\n"))
    while (acres_to_plant >acres_owned or acres_to_plant > (bushles /2) or (population *10) <acres_to_plant or (acres_to_plant <0)) :
        acres_to_plant=int(get_number("Nope, try again....\n"))
    return acres_to_plant


#chance for covid
def plague_deaths(population :int) ->int :
    number_of_plague = 0
    if randrange(1,101) >85 :
        number_of_plague = math.floor(population,2)
    return number_of_plague









