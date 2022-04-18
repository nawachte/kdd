fd = open('Groceries_dataset.csv','r')
data = fd.read()
fd.close()

db = {}
for line in data.split("\n"):
    items = line.split(',')
    if items != ['']:
        if items[0] in db.keys():
            db[items[0]] += [items[2]]
        else:
            db[items[0]] = [items[2]]
del db['Member_number']

newfd = open('grocery.csv', 'w')
for item_list in db.keys():
    if len(db[item_list]) >= 10:
        newfd.write(",".join(db[item_list])+"\n")
newfd.close()