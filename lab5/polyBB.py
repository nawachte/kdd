import sys, requests
from webbrowser import get
from bs4 import BeautifulSoup

url = "http://frank.ored.calpoly.edu/BB/www.gopoly.com/sports/mbkb/2018-19/schedule"
myRequest = requests.get(url)
soup = BeautifulSoup(myRequest.text,"html.parser")


print("Welcome to polyBB by Nicholas Wachter")
print("Developed Spring 2022 for CSC 466")

def play(opp):
    opps = {}
    for eventRow in soup.find_all('div', attrs={'class':'event-row'}):
        opponentHTML = eventRow.find('div', attrs={'class':'opponent'})
        opponent = opponentHTML.span.string.strip()

        dateHTML = eventRow.find('div', attrs={'class':'date'})
        date = dateHTML['title']

        opps[opponent] = date

    if opp in opps.keys():
        print("Yes, Cal Poly played", opp, "on", opps[opp])
    else:
        print("No, Cal Poly did no play",opp)


def winlose(opp):
    scores = [] 
    for eventRow in soup.find_all('div', attrs={'class':'event-row'}):
        opponentHTML = eventRow.find('div', attrs={'class':'opponent'})
        opponent = opponentHTML.span.string.strip()

        if opp == opponent:
            scoreHTML = eventRow.find('div',attrs={'class':'result'})
            score = scoreHTML.string.strip()
            scores.append(score)
    if len(scores) == 1:
        print("Lost:" if scores[0][0] == "L" else "Won:",scores[0][3:])
    else:
        score1 = ("lost " if scores[0][0] == "L" else "won ") + scores[0][3:]
        score2 = ("lost " if scores[1][0] == "L" else "won ") + scores[1][3:]
        print("There were two games, in the first they",score1,"and in the second they",score2,".")


def bestworst_opp(bw, opp):
    scores = []
    for eventRow in soup.find_all('div', attrs={'class':'event-row'}):
        opponentHTML = eventRow.find('div', attrs={'class':'opponent'})
        opponent = opponentHTML.span.string.strip()
        if opp == opponent:
            scoreHTML = eventRow.find('div',attrs={'class':'result'})
            score = scoreHTML.string.strip()
            score = score[3:].split("-")[0 if score[0] == "W" else 1]
            scores.append(int(score))
    print("Against",opp,"Cal Poly's", "worst" if bw == 'w' else "best", "score was",min(scores) if bw == 'w' else max(scores))

def bestworst_oa(bw):
    scores = []
    for eventRow in soup.find_all('div', attrs={'class':'event-row'}):
        scoreHTML = eventRow.find('div',attrs={'class':'result'})
        score = scoreHTML.string.strip()
        score = score[3:].split("-")[0 if score[0] == "W" else 1]
        scores.append(int(score))
    print("Cal Poly's","worst" if bw == 'w' else "best","overall score was",min(scores) if bw == 'w' else max(scores))

def lev_dist(str1, str2):
    if "play" in str1 and "play" in str2:
        return 0
    if ("win" in str1 and "win" in str2) or ("lose" in str1 and "lose" in str2):
        return 0
    if ("best" in str1 and "best" in str2) or ("worst" in str1 and "worst" in str2):
        return 0

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

def get_opp(words, word_before):
    if len(words) < 3:
        return " ".join(words)
    opp = words[-1]
    dist1 = [
        lev_dist(words[-2], word_before),
        lev_dist(words[-2],'UC'),
        lev_dist(words[-2],'Santa'),
        lev_dist(words[-2],'Beach'),
        lev_dist(words[-2],'State'),
        lev_dist(words[-2],'Texax'),
        lev_dist(words[-2],'Washington'),
        lev_dist(words[-2],'USC')
    ]
    if dist1.index(min(dist1)) == 0:
        return opp
    
    opp = words[-2] + " " + opp
    dist2 = [
        lev_dist(words[-3], word_before),
        lev_dist(words[-3],'UC'),
        lev_dist(words[-3],'Santa'),
        lev_dist(words[-3],'Beach'),
        lev_dist(words[-3],'State'),
        lev_dist(words[-3],'Texax'),
        lev_dist(words[-3],'Washington'),
        lev_dist(words[-3],'USC')
    ]

    if dist2.index(min(dist2)) == 0:
        return opp
    else:
        return words[-3] + " " + opp


usr_in = ''
while usr_in != 'exit':
    print()
    print("What would you like to know?")
    usr_in = input()
    if usr_in == 'exit':
        sys.exit(0)
    words = "".join(char for char in usr_in if char.isalnum() or char in [" ","\'","-"])
    words = [word for word in words.split(" ") if word != ""]

    q_strs = ["Did Cal Poly play","Did Cal Poly win or lose against","What was the best/worst score for Cal Poly?"]
    score1 = lev_dist(q_strs[0], usr_in[:14 if len(usr_in) > 14 else len(usr_in)])
    score2 = lev_dist(q_strs[1], usr_in[:26 if len(usr_in) > 26 else len(usr_in)])
    score3 = lev_dist(q_strs[2], usr_in[:30 if len(usr_in) > 30 else len(usr_in)])
    scores = [score1, score2, score3]
    selection  = scores.index(min(scores))
    if selection == 0:
        opp = get_opp(words, 'play')
        play(opp)
    elif selection == 1:
        opp = get_opp(words, 'against')
        winlose(opp)
    else:
        wb = 'w' if 'worst' in words else 'b'
        if 'overall' in words[-2:]:
            bestworst_oa(wb)
        else:
            opp = get_opp(words, 'against')
            bestworst_opp(wb, opp)

