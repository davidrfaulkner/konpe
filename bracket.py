import itertools
import random
from itertools import izip

"""
Notes on the bracket
Try to not have same Region
If not possible, not same Dojo
Prerounds to get to Base2 draw, to avoid ABC rule (3 competitors in final, vs 4)
2 contenders
3 contendors random abc rule
4 normal
5 1 preround
6 2 prefights
7 3 prefights
8 normal
9 is 1
10 2?
11 3?
12 4 pre rounds
13 5
14 6
15 7
16 normal
32 normal
"""
def test_bracket_region(division):
    bracket = pairwise(division)
    for i in bracket:
        if i[0]['Region'] == i[1]['Region']:
            return False
    return True

def test_bracket_dojo(division):
    bracket = pairwise(division)
    for i in bracket:
        if i[0]['Dojo'] == i[1]['Dojo']:
            return False
    return True

def pairwise(t):
    it = iter(t)
    return izip(it,it)

def bracket_layout(division):
    noParticipants = len(division)
    base2 = 2
    while base2 < noParticipants:
        newbase2 = base2 * 2
        if newbase2 < noParticipants:
            base2 = newbase2
        else:
            break
    round0size = base2*2 #Round 0 size
    prefights = noParticipants - base2 #Amount of pre fights

    round0 = []
    round1 = []
    for i in range(round0size - prefights*2):
        round0.append(None)
    for i in range(prefights*2):
        round0.append(division.pop(0))
    for i in division:
        round1.append(i)
    for i in range(base2 - len(round1)):
        round1.append(None)

    print round0

    print round1



def bracket(division):
    random.shuffle(division)
    good_division = False
    if len(division) < 7:
        for i in itertools.permutations(division):
            if test_bracket_region(i):
                division = i
                good_division = True
                break
    else:
        for i in range(1024): #Base2 number as a joke
            random.shuffle(division)
            if test_bracket_region(division):
                good_division = True
                break
    if not good_division:
        if len(division) < 7:
            for i in itertools.permutations(division):
                if test_bracket_dojo(i):
                    division = i
                    break
        else:
            for i in range(512): #Base2 number as a joke
                random.shuffle(division)
                if test_bracket_dojo(division):
                    break

    print good_division, division
    return list(division)



if __name__ == '__main__':
    #create testing list
    regions = ["ERP", "GFR", "HSD", "LKJ"]
    dojos =['B','F','M', 'G', 'By', 'A', 'N', 'L']

    division = []

    for i in range(5):
        division.append({"ParticipantID":i, "Region":random.choice(regions), "Dojo":random.choice(dojos)})
    division = bracket(division)
    bracket_layout(division)
