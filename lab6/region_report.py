from os import name
import pymysql.cursors
import sys

if len(sys.argv) != 2:
    print("Usage: region_report <region>")
    sys.exit(0)

region = sys.argv[1]

connection = pymysql.connect(host='localhost',
                             user='nawachte466',
                             password='nawachte466985',
                             database='nawachte466',
                             cursorclass=pymysql.cursors.DictCursor)

def name_convert(name):
    words = name.split('_')
    new = []
    for word in words:
        new.append(word[0].upper()+word[1:])
    return " ".join(new)

continent = ''
num_countries = 0
country_list = []
num_rivers = 0
river_drains = [] # [(r1, d1), (r2, d2), ...]
top_cities = [] 
with connection:
    with connection.cursor() as cursor:
        # continent
        sql = "select `continent` from in_continent where region = \'"+region+"\';"
        cursor.execute(sql)
        result = cursor.fetchall()
        # print(result)
        continent = result[0]['continent']

        # num_countries
        sql = "select count(distinct `country`) from countries where region = \'"+region+"\';"
        cursor.execute(sql)
        result = cursor.fetchall()
        num_countries = result[0]['count(distinct `country`)']

        # country_list
        sql = "select distinct country from countries where region = \'"+region+"\';"
        cursor.execute(sql)
        result = cursor.fetchall()
        for res in result:
            country_list.append(res['country'])

        # num_rivers
        for country in country_list:
            sql = "select count(distinct `name`) from rivers where passes_through like \'%"+country+"%\';"
            cursor.execute(sql)
            result = cursor.fetchall()
            num_rivers += result[0]['count(distinct `name`)']

        # river_drains
        for country in country_list:
            sql = "select name, drains from rivers where passes_through like \'%"+country+"%\';"
            cursor.execute(sql)
            result = cursor.fetchall()
            for res in result:
                river_drains.append((res['name'],res['drains']))

        # top cities
        sql = "select name, country from cities where country = \'" + country_list[0] + "\'"
        for country in country_list[1:]:
            sql += " or country = \'"+country+"\'"
        sql += " order by population desc limit 5;"
        cursor.execute(sql)
        result = cursor.fetchall()
        top_cities = [(x['name'],x['country']) for x in result]

# [REGION] is a region in the continent of [CONTINENT].
print(name_convert(region),"is a region in the continent of",name_convert(continent)+".")
print()
# It contains [NUM_COUNTRIES] countries. They are: [COUNTRY1], [COUNTRY2], … .
if num_countries == 1:
    print("It contains 1 country. It is",country_list[0])
else:
    country_str = ''
    for country in country_list:
        country_str += (name_convert(country)+", ")
    country_str = country_str[:-2]+"."
    print("It contains",num_countries,"countries. They are:",country_str)
print()
# It contains [NUM_RIVERS] rivers: [RIVER1] (drains to [DRAINAGE1]), [RIVER2] (drains to [DRAINAGE2], … .
if num_rivers == 0:
    print("It contains 0 rivers.")
elif num_rivers == 1:
    print("It contains 1 river:",name_convert(river_drains[0][0])," (drains to",name_convert(river_drains[0][1])+")")
else:
    river_str = ''
    for river in river_drains:
        river_str += (name_convert(river[0])+" (drains to "+name_convert(river[1])+"), ")
    river_str = river_str[:-2]+"."
    print("It contains",str(num_rivers),"rivers:",river_str)
print()
# [REGION]’s most populous cities are: [CITY1] in [COUNTRY1], [CITY2] in [COUNTRY2], [CITY3] in [COUNTRY3], [CITY4] in [COUNTRY4], [CITY5] in [COUNTRY5].
if len(top_cities) == 0:
    print(name_convert(region),"has no cities.")
elif len(top_cities) == 1:
    print(name_convert(region)+"\'s most populous city is: "+name_convert(top_cities[0][0])+" in "+name_convert(top_cities[0][1])+".")
else:
    city_str = name_convert(top_cities[0][0])+" in "+name_convert(top_cities[0][1])+", "
    for city in top_cities[1:]:
        city_str += (name_convert(city[0])+" in "+name_convert(city[1])+", ")
    city_str = city_str[:-2]+"."
    print(name_convert(region)+"\'s most populous cities are: "+city_str)