import pymysql.cursors
import re

# create tables
connection = pymysql.connect(host='localhost',
                             user='nawachte466',
                             password='nawachte466985',
                             database='nawachte466',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        fd = open('makeChat80Tables.sql', 'r')
        sql = fd.read()
        fd.close()
        cursor.execute(sql)

    connection.commit()

# populate tables
# world1.pl
with connection:
    with connection.cursor() as cursor:
        fd = open('world1.pl', 'r')
        data = fd.read()
        fd.close()

        # circle_of_latitude
        lat_match = re.findall(r'circle_of_latitude\((\w+),(\S+)\).', data)
        for match in lat_match:
            sql = "INSERT INTO circle_of_latitude (`name`,`latitude`) VALUES (%s, %s);"
            cursor.execute(sql, list(match))

        # in_continent
        in_cont_match = re.findall(r'in_continent\((\w+),(\w+)\)', data)
        for match in in_cont_match:
            sql = "INSERT INTO in_continent (`region`, `continent`) VALUES (%s, %s);"
            cursor.execute(sql, list(match))

        # continents
        cont_match = re.findall(r'continent\((\w+)\)', data)
        for match in cont_match:
            sql = "INSERT INTO continents (`name`) VALUES (%s);"
            cursor.execute(sql, match)

        # ocean
        ocean_match = re.findall(r'ocean\((\w+)\)', data)
        for match in ocean_match:
            sql = "INSERT INTO ocean (`name`) VALUES (%s);"
            cursor.execute(sql, match)

        # sea
        sea_match = re.findall(r'sea\((\w+)\)', data)
        for match in sea_match:
            sql = "INSERT INTO sea (`name`) VALUES (%s);"
            cursor.execute(sql, match)
    connection.commit()

# borders
with connection:
    with connection.cursor() as cursor:
        fd = open('borders.pl', 'r')
        data = fd.read()
        fd.close()

        border_match = re.findall(r'borders\((\w+),(\w+)\)', data)
        for match in border_match:
            sql = "INSERT INTO borders (`entity1`, `entity2`) VALUES (%s, %s);"
            cursor.execute(sql, list(match))
    connection.commit()

# cities
with connection:
    with connection.cursor() as cursor:
        fd = open('cities.pl', 'r')
        data = fd.read()
        fd.close()

        city_match = re.findall(r'city\((\w+),(\w+),(\w+)\)', data)
        for match in city_match:
            sql = "INSERT INTO cities (`name`, `country`, `population`) VALUES (%s, %s, %s);"
            cursor.execute(sql, list(match))
    connection.commit()

# contain
with connection:
    with connection.cursor() as cursor:
        fd = open('contain.pl', 'r')
        data = fd.read()
        fd.close()

        contain_match = re.findall(r'contains0\((\w+),(\w+)\)', data)
        for match in contain_match:
            sql = "INSERT INTO contain (`outer`, `inner`) VALUES (%s, %s);"
            cursor.execute(sql, list(match))
    connection.commit()

# countries
with connection:
    with connection.cursor() as cursor:
        fd = open('countries.pl', 'r')
        data = fd.read()
        fd.close()

        country_match = re.findall(r'country\((\w+),(\w+),(\S+),(\S+),(\w+),(\w+),(\w+),(\S+)\)', data)
        for match in country_match:
            sql = "INSERT INTO countries (`country`, `region`, `latitude`, `longitude`, `area`, `population`, `capital`, `currency`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(sql, list(match))
    connection.commit()

# rivers
with connection:
    with connection.cursor() as cursor:
        fd = open('rivers.pl', 'r')
        data = fd.read()
        fd.close()

        river_match = re.findall(r'river\((\w+),\[(\w+),(\S+)\]', data)
        for match in river_match:
            sql = "INSERT INTO rivers (`name`, `drains`, `passes_through`) VALUES (%s, %s, %s);"
            cursor.execute(sql, list(match))
    connection.commit()

# get table information
tables = []
with connection:
    with connection.cursor() as cursor:
        sql = "show tables;"
        cursor.execute(sql)
        result = cursor.fetchall()
        tables = [x['Tables_in_nawachte466'] for x in result]
tables.remove('us_cities')

fields = {}
with connection:
    with connection.cursor() as cursor:
        for table in tables:
            sql = "desc "+table+";"
            cursor.execute(sql)
            result = cursor.fetchall()
            fields[table] = [x['Field'] for x in result]

counts = {}
with connection:
    with connection.cursor() as cursor:
        for table in tables:
            sql = "select count(*) from "+table+";"
            cursor.execute(sql)
            result = cursor.fetchall()
            counts[table] = result[0]['count(*)']

for table in tables:
    cols = ", ".join(fields[table])
    print("Table "+table+": "+cols+", "+str(counts[table])+" rows")