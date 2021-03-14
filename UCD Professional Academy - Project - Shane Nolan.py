# UCD Professional Academy - Project Submission

# 1) Real World Scenario
    # Data imported from Kaggle as CSV file

# 2) Importing Data

import pandas as pd

country_vaccinations = pd.read_csv("country_vaccinations.csv")
print(country_vaccinations.head(), country_vaccinations.shape, country_vaccinations.info())

country_population = pd.read_csv("Country_populations.csv")
print(country_population.head(), country_population.shape, country_population.info())


# 3) Analyzing data

#Subsetting Country Vaccination data to focus on number of people vaccinated with single dose on latest date
pop_vaccinated = country_vaccinations[["Country Name", "Country Code", "date", "people_vaccinated", "vaccines"]]
print(pop_vaccinated.head())

# Groupby - sum of people vaccinated per country
vaccinated_per_country = pop_vaccinated.groupby("Country Name")["people_vaccinated"].max()
print(vaccinated_per_country.head())

# Replace Missing or Drop Duplicates

# Slicing of Country Population Data to exclude incomplete 2020 population data
pop_country = country_population.loc[:, "Country Name": "2019"]

# Subsetting Country Population data to focus on 2019 population
pop_2019 = pop_country[["Country Name", "Country Code", "2019"]]
print(pop_2019.head())

# Merging of Vaccination (total people vaccinated per country) data with Population data (2019 population data)
vaccinated_per_pop = pop_2019.merge(vaccinated_per_country, on='Country Name')
print(vaccinated_per_pop.head())

#Create a list of EU countries
EU_Countries = {"Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark",
                "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy",
                "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal",
                "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"}
print(EU_Countries)

#Subsetting merged Vaccination and population data by EU Countries
EU_Vaccinated_per_pop = vaccinated_per_pop[vaccinated_per_pop['Country Name'].isin(EU_Countries)]
print(EU_Vaccinated_per_pop.head())