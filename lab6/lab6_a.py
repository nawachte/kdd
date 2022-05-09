import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='nawachte466',
                             password='nawachte466985',
                             database='nawachte466',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        fd = open('uscities.csv', 'r')
        data = fd.read()
        fd.close()

        for line in data.split('\n')[1:]:
            items = line.split(",")
            print(items)
            sql = "INSERT INTO us_cities (`name`,`county`,`state`,`state_code`,`zip`,`latitude`,`longitude`,`population`,`type`,`id`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, items)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()



    # '`name`','`county`','`state`','`state_code`','`zip`','`latitude`','`longitude`','`population`','`id`'