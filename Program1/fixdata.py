fd = open('grocery.csv','r')
data = fd.read()
fd.close()

newfd = open('grocery_filtered.csv', 'w')

for line in data.split('\n'):
    splitdata = line.split(',')
    if len(splitdata) >= 10:
        # print(line)
        newfd.write(line+"\n")
newfd.close()