aprioriFD = open('apriori.out', 'r')
apriori_data = aprioriFD.read().split('\n')[1:]
aprioriFD.close()
bfFD = open('bruteforce.out', 'r')
bf_data = bfFD.read().split('\n')[1:]
bfFD.close()

# print(apriori_data)
# print(bf_data)

for item_a in apriori_data:
    if item_a not in bf_data:
        print(item_a)
print("-------------")
for item_b in bf_data:
    if item_b not in apriori_data:
        print(item_b)