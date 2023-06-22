# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def damages_to_number (damages):
  updated_damages = []
  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    else:
      num = float(damage[:-1])
      string = damage[-1]
      if string == "M":
        updated_damages.append(int(num*1000000))
      else:
        updated_damages.append(int(num*1000000000))
  return updated_damages

#print (damages_to_number(damages))

updated_damages = damages_to_number(damages)

# 2 
# Create a Table
def dictionary_hurricanes ():
  hurricanes_dictionary = {}
  index = 0
  for hurricane in names:
    hurricanes_dictionary_temp = {hurricane:
    {"Name": names[index],
    "Month": months[index],
    "Year": years[index],
    "Max Sustained Wind": max_sustained_winds[index],
    "Areas Affected": areas_affected[index],
    "Damage": updated_damages[index],
    "Deaths": deaths[index]}
    }
    hurricanes_dictionary.update(hurricanes_dictionary_temp)
    index += 1
  return hurricanes_dictionary

# Create and view the hurricanes dictionary

hurricanes_dictionary = dictionary_hurricanes()
#print (dictionary_hurricanes())

# 3
# Organizing by Year
hurricanes_dictionary_by_year = {}
def dictionary_hurricanes_by_year ():
  for hurricane in hurricanes_dictionary:
    current_cane = hurricanes_dictionary[hurricane]
    current_year = current_cane['Year']
    list_temp = [current_cane]
    if hurricanes_dictionary_by_year.get(current_year) == None:
      hurricanes_dictionary_by_year.update({current_year:list_temp})
    else:
      list_temp2 = hurricanes_dictionary_by_year.get(current_year)
      list_temp2.append(list_temp)
      hurricanes_dictionary_by_year.update({current_year:list_temp2})
  return hurricanes_dictionary_by_year

# create a new dictionary of hurricanes with year and key
hurricanes_dictionary_by_year = (dictionary_hurricanes_by_year ())

#print(hurricanes_dictionary_by_year[1932])
  
# 4
# Counting Damaged Areas
damaged_areas_dictionary = {}
def dictionary_damaged_areas (hurricanes_dictionary):
  for hurricane in hurricanes_dictionary:
    current_cane = hurricanes_dictionary[hurricane]
    current_areas = current_cane['Areas Affected']
    for area in current_areas:
      if damaged_areas_dictionary.get(area) == None:
        damaged_areas_dictionary.update({area:1})
      else:
        count_damaged_areas_temp = damaged_areas_dictionary.get(area) + 1
        damaged_areas_dictionary.update({area:count_damaged_areas_temp})
  return damaged_areas_dictionary

# create dictionary of areas to store the number of hurricanes involved in
damaged_areas_dictionary = dictionary_damaged_areas (hurricanes_dictionary)

#print(damaged_areas_dictionary)

# 5 
# Calculating Maximum Hurricane Count

def area_most_affected (damaged_areas_dictionary):
  most_affected = max(damaged_areas_dictionary.values())
  area_most_affected = ""
  for area in damaged_areas_dictionary:
    if damaged_areas_dictionary[area] == most_affected:
      area_most_affected = area
  return area_most_affected, most_affected

# find most frequently affected area and the number of hurricanes involved in

#print(area_most_affected(damaged_areas_dictionary))


# 6
# Calculating the Deadliest Hurricane

hurricanes_dictionary_deaths = {}
def dictionary_hurricanes_deaths (hurricanes_dictionary):
  for hurricane in hurricanes_dictionary:
    current_cane = hurricanes_dictionary[hurricane]
    current_death = current_cane['Deaths']
    current_name = current_cane['Name']
    hurricanes_dictionary_deaths.update({current_name:current_death})
  deadliest = max(hurricanes_dictionary_deaths.values())
  for name in hurricanes_dictionary_deaths:
    if hurricanes_dictionary_deaths[name] == deadliest:
      name_deadliest = name
  return name_deadliest,deadliest

# find highest mortality hurricane and the number of deaths

#print(dictionary_hurricanes_deaths (hurricanes_dictionary))

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

hurricanes_dictionary_by_mortality_scale = {0:[],1:[],2:[],3:[],4:[],5:[]}
def dictionary_hurricanes_by_mortality_scale (hurricanes_dictionary):
  for hurricane in hurricanes_dictionary:
    current_cane = hurricanes_dictionary[hurricane]
    current_death = current_cane['Deaths']
    list_temp = current_cane
    if (current_death > 0) and (current_death <=100):
      rate = 1
    elif (current_death > 100) and (current_death <=500):
      rate = 2
    elif (current_death > 500) and (current_death <=1000):
      rate = 3
    elif (current_death > 1000) and (current_death <=10000):
      rate = 4
    elif (current_death > 10000):
      rate = 5
    list_temp2 = hurricanes_dictionary_by_mortality_scale.get(rate)
    list_temp2.append(list_temp)
    hurricanes_dictionary_by_mortality_scale.update({rate:list_temp2})
  return hurricanes_dictionary_by_mortality_scale

# categorize hurricanes in new dictionary with mortality severity as key

#print(dictionary_hurricanes_by_mortality_scale (hurricanes_dictionary))

# 8 Calculating Hurricane Maximum Damage

hurricanes_dictionary_damage = {}
def dictionary_hurricanes_damage (hurricanes_dictionary):
  for hurricane in hurricanes_dictionary:
    current_cane = hurricanes_dictionary[hurricane]
    current_damage = current_cane['Damage']
    current_name = current_cane['Name']
    if current_damage != "Damages not recorded":
      hurricanes_dictionary_damage.update({current_name:current_damage})
  maximum_damage = max(hurricanes_dictionary_damage.values())
  for name in hurricanes_dictionary_damage:
    if hurricanes_dictionary_damage[name] == maximum_damage:
      name_maximum_damage = name
  return name_maximum_damage,maximum_damage

# find highest damage inducing hurricane and its total cost
#print(dictionary_hurricanes_damage(hurricanes_dictionary))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

hurricanes_dictionary_by_damage_scale = {0:[],1:[],2:[],3:[],4:[],5:[]}
def dictionary_hurricanes_by_damage_scale (hurricanes_dictionary):
  for hurricane in hurricanes_dictionary:
    current_cane = hurricanes_dictionary[hurricane]
    current_damage = current_cane['Damage']
    list_temp = current_cane
    if current_damage == "Damages not recorded":
      continue
    if (current_damage > 0) and (current_damage <=100000000):
      rate = 1
    elif (current_damage > 100000000) and (current_damage <=1000000000):
      rate = 2
    elif (current_damage > 1000000000) and (current_damage <=10000000000):
      rate = 3
    elif (current_damage > 10000000000) and (current_damage <=50000000000):
      rate = 4
    elif (current_damage > 50000000000):
      rate = 5
    list_temp2 = hurricanes_dictionary_by_damage_scale.get(rate)
    list_temp2.append(list_temp)
    hurricanes_dictionary_by_damage_scale.update({rate:list_temp2})
  return hurricanes_dictionary_by_damage_scale
  
# categorize hurricanes in new dictionary with damage severity as key

print(dictionary_hurricanes_by_damage_scale(hurricanes_dictionary))
