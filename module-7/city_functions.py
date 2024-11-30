# city_functions.py

############################

import unittest
import sys

city_name = "a"
country_name = "b"

def city_country(city_name, country_name):
	print("Enter 'q' at any time to quit program.")
	#########################################
	city_name = input("Enter a city name. >")
	if city_name == "q":
		return
	#########################################
	country_name = input("Enter a country name. >")
	if country_name == "q":
		return
	#########################################
	population_question = input("Would you like to enter population? Press Y for yes, or any other key to continue. >")
	if population_question == "q":
		return
	if population_question == "Y":
		population_number = input("Enter population. >")
		if population_number == "q":
			return
	#########################################
	language_question = input("Would you like to enter language spoken? Press Y for yes, or any other key to continue. >")
	if language_question == "q":
		return
	if language_question == "Y":
		language_spoken = input("Enter what language is spoken. >")
		if language_spoken == "q":
			return
	#########################################
	if population_question == "Y" and language_question == "Y":
		complete_name = str(city_name) + ", " + str(country_name) + " - Population: " + str(population_number) + " || " + str(language_spoken)
	elif population_question == "Y" and language_question != "Y":
		complete_name = str(city_name) + ", " + str(country_name) + " - Population: " + str(population_number)
	elif population_question != "Y" and language_question == "Y":
		complete_name = str(city_name) + ", " + str(country_name) + " || " + str(language_spoken)
	else:
		complete_name = str(city_name) + ", " + str(country_name)
	return complete_name

#complete_name = str(city_name) + ", " + str(country_name) + " - Population: " + str(population_number)

while True:
	returned_name = city_country("a", "b")
	if returned_name == None:
		break
	else:
		print(returned_name)
	print("")
	while_control = input("Operation complete. Press any button to repeat or 'q' to exit. >")
	if while_control == "q":
		break
	print("")

print("Operation terminated.")
print("")



