# # import re

# # fd = open('test.txt', 'r')
# # data = fd.read()
# # fd.close()

# # # print(data)

# # namematch = re.findall(r'continent\((\w+)\)', data)

# # print(namematch)

# # for name in namematch:
# #     print(name)
# import pymysql.cursors

# connection = pymysql.connect(host='localhost',
#                              user='nawachte466',
#                              password='nawachte466985',
#                              database='nawachte466',
#                              cursorclass=pymysql.cursors.DictCursor)

# tables = []
# with connection:
#     with connection.cursor() as cursor:
#         sql = "show tables;"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#         tables = [x['Tables_in_nawachte466'] for x in result]
# tables.remove('us_cities')

# fields = {}
# with connection:
#     with connection.cursor() as cursor:
#         for table in tables:
#             sql = "desc "+table+";"
#             cursor.execute(sql)
#             result = cursor.fetchall()
#             fields[table] = [x['Field'] for x in result]

# counts = {}
# with connection:
#     with connection.cursor() as cursor:
#         for table in tables:
#             sql = "select count(*) from "+table+";"
#             cursor.execute(sql)
#             result = cursor.fetchall()
#             counts[table] = result[0]['count(*)']

# for table in tables:
#     cols = ", ".join(fields[table])
#     print("Table "+table+": "+cols+", "+str(counts[table])+" rows")

def name_convert(name):
    words = name.split('_')
    new = []
    for word in words:
        new.append(word[0].upper()+word[1:])
    return " ".join(new)

num_countries = 2
country_list = ['canada', 'united_states']
country_str = ''
for country in country_list:
    country_str += (name_convert(country)+", ")
print(country_str)
country_str = country_str[:-2]+"."
print(country_str)
print("It contains",num_countries,"countries. They are:",country_str)