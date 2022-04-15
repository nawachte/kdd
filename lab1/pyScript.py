COUNTY = 1
STATE = 2
POP = 7
TYPE = 8

f = open("uscities.csv", 'r')
lines = f.readlines()
f.close()

itemlist = [line.split(",") for line in lines]
print([itemlist[i] for i in range(10)])

county_list = []
for item in itemlist:
    if (item[COUNTY] not in county_list) and item[STATE] == "Alabama" and int(item[POP]) >= 1500 and item[TYPE] == 'City':
        county_list.append(item[COUNTY])

print(county_list)
print(len(county_list))

# print(lines)