import sys
import time

if len(sys.argv) != 4:
    print("Usage: apriori <CSV> <minsup> <minconf>")
    sys.exit(0)

csv_fd = open(sys.argv[1], 'r')
csv_data = csv_fd.read()
csv_fd.close()

data_lines = csv_data.split('\n')
num_transactions = len(data_lines)


def get_sup_table(c, D):
    sup = {}
    for prefix in c:
        sup[prefix] = 0
    for entry in D:
        for prefix in c:
            occurs = True
            for item in prefix.split(','):
                if item not in entry:
                    occurs = False
                    break
            if occurs:
                sup[prefix] += 1
    return sup

def remove_duplicates(l):
    new_l = []
    for item in l:
        if item not in new_l:
            new_l.append(item)
    return new_l

def extend_prefix_tree(ck):
    next_list = []
    for i, item1 in enumerate(ck):
        for item2 in ck[i+1:]:
            combined = item1 + "," + item2
            filtered = sorted(remove_duplicates(combined.split(",")))
            if len(filtered) == len(item1.split(','))+1:
                next_list.append(",".join(filtered))
    return remove_duplicates(next_list)

def Apriori(D, I, minsup):
    F = {} # hash map of itemsets and their freqencies ex {'a':10, 'a,b':6, 'a,b,c':2}
    c = [] # list of strings with comma separated values ex ['a,b','a,b','b,c']
    for i in I:
        c.append(i)
    while c != []:
        sup = get_sup_table(c, D)
        new_c = []
        for X in c:
            if sup[X] >= minsup:
                F[X] = sup[X]
                new_c.append(X)
        c = extend_prefix_tree(new_c)
    return F

def get_sup(items, F):
    item_list = items.split(',')
    item_list = sorted(item_list)
    try:
        sup = F[','.join(item_list)]
        return sup
    except:
        raise Exception("Unable to find sup.")

# returns a list of tuples, each element containing a list of operands 
# [('a,b','c'), ('a,c',[b]), ('b,c','a'), ('a','b,c'), ('b','a,c'), ('c','a,b')]
def rule_combos(Z):
    Z = Z.split(',')

    all_patterns = []
    for i in range(len(Z)):
        all_patterns.append(Z)
        Z = Z[1:]+[Z[0]]

    rules = []
    for split_idx in range(1, len(all_patterns[0])):
        for combo in range(len(all_patterns)):
            split1 = all_patterns[combo][:split_idx]
            split2 = all_patterns[combo][split_idx:]
            rules.append((",".join(split1), ",".join(split2)))
    return rules


def AssociationRules(F, minconf):
    valid_rules = []
    F_viable = [x for x in F.keys() if len(x.split(",")) >= 2]
    for Z in F_viable:
        A = rule_combos(Z)
        for X in A:
            conf = F[Z]/get_sup(X[0], F)
            if conf >= minconf:
                valid_rules.append(X[0]+" --> "+X[1]) #"x,y --> a,b,c"
    return valid_rules

# D = [x.split(',') for x in data_lines][:-1] # [[item1, item2, ...],[item4, item6, ...],...]
D = [  ['a','b','c','d','r'],
        ['o','c','d','e','s'],
        ['p','d','e','c','r'],
        ['a','q','e','d','s'],
        ['f','k','h','e','t'],
        ['a','l','m','d','u'],
        ['e','f','g','h','w']
      ]
I = []
for line in D:
    for item in line:
        I.append(item)
I = set(I)
minsup = float(sys.argv[2])*len(D)
minconf = float(sys.argv[3])
t1 = time.time()
F = Apriori(D,I,minsup)
t2 = time.time()
print(t2-t1)
rules = AssociationRules(F,minconf)
for rule in rules:
    print(rule)
