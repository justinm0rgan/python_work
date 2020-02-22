# Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland.
# Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city_name, country = 'usa'):
	"""Prints message with city and its country"""
	if country == 'usa':
		print(f"{city_name.title()} is located in the {country.upper()}.")
	else:
		print(f"{city_name.title()} is located in {country.title()}.")

describe_city('new york')
describe_city('los angeles')
describe_city(country = 'russia', city_name = 'moscow')