# def lev_dist(dist1, dist2, str1, str2):
#     if dist1 == len(str1) or dist2 == len(str2):
#         return len(str1) - dist1 + len(str2) - dist2

#     if str1[dist1] == str2[dist2]:
#         return lev_dist(dist1 + 1, dist2 + 1, str1, str2)

#     return 1 + min(
#             lev_dist(dist1, dist2 + 1, str1, str2),
#             lev_dist(dist1 + 1, dist2, str1, str2),
#             lev_dist(dist1 + 1, dist2 + 1, str1, str2))

def lev_dist(str1, str2):
    if len(str1) < len(str2):
        return lev_dist(str2, str1)
    if len(str2) == 0:
        return len(str1)
    prev_row = range(len(str2) + 1)
    for i, chr1 in enumerate(str1):
        curr_row = [i + 1]
        for j, chr2 in enumerate(str2):
            curr_row.append(min(
            prev_row[j + 1] + 1,
            curr_row[j] + 1,
            prev_row[j] + (1 if chr1 != chr2 else 0)))
        prev_row = curr_row
    
    return prev_row[-1]

print(lev_dist("against", "agint"))
print(lev_dist("against", "UC"))
print(lev_dist("play", "ply"))
print(lev_dist("play", "UC"))


s1 = "Did Cal Poly play?"
s2 = "Did Cal Poly win or lose against?"
s3 = "What was the worst score for Cal Poly?"
s4 = "What was the best score for Cal Poly?"

t1 = "dd Poly play Cal against another team is length a problem?"
t2 = "Did CAL POLY win  or did they lose agains Cal?"
t3 = "what was the worst score for cal poly overall"
t4 = "what was the best score for cal poly overall"

s = [s1,s2,s3,s4]
t = [t1,t2,t3,t4]

# for i in range(4):
#     print(s[i])
#     for j in range(4):
#         print(t[j],": ",lev_dist(s[i],t[j]))
#     print()
# print("---")
# for i in range(4):
#     print(lev_dist(s[i], 'this shit dont make sense'))