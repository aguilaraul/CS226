'''
DEVELOPER: Raul Aguilar
COLLABORATORS: <other names>
COURSE:	CS226 Discrete Structures
PROJECT:	Project01
LAST MODIFIED: 09 23 2021
'''
##########################################
#	<TITLE OF PROGRAM>
########################################## PROGRAM DESCRIPTION:
# Write a project that takes as input two sets, A and B, and outputs the following:
# AuB, AnB, AxB, AxorB, 
# The program should take file input and output to both the console and a file
##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
#<imports here>

##########################################
# FUNCTIONS:
##########################################
def union(setA, setB):
    return unionHelper(setA, setB, "")

def unionHelper(setA, setB, unionSet):
    for i in range(len(setA)):
        if setA[i] == "1" or setB[i] == "1":
            unionSet += "1"
            return unionHelper(setA[1:], setB[1:], unionSet)
        else:
            unionSet += "0"
            return unionHelper(setA[1:], setB[1:], unionSet)
    return unionSet

def intersection(setA, setB):
    return intersectionHelper(setA, setB, "")

def intersectionHelper(setA, setB, interSet):
    for i in range(len(setA)):
        if setA[i] == "1" and setB[i] == "1":
            interSet += "1"
            return intersectionHelper(setA[1:], setB[1:], interSet)
        else:
            interSet += "0"
            return intersectionHelper(setA[1:], setB[1:], interSet)
    return interSet

def cartesianProduct(setA, setB):
    for i in range(len(setA)):
        for j in range(len(setB)):
            print('{', setA[i], ', ', setB[j], '}')

def exclusiveOr(setA, setB):
    return exclusiveOrHelper(setA, setB, "")

def exclusiveOrHelper(setA, setB, exclusiveSet):
    for i in range(len(setA)):
        if setA[i] != setB[i]:
            exclusiveSet += "1"
            return exclusiveOrHelper(setA[1:], setB[1:], exclusiveSet)
        else:
            exclusiveSet += "0"
            return exclusiveOrHelper(setA[1:], setB[1:], exclusiveSet)
    return exclusiveSet

##########################################
# MAIN PROGRAM:
##########################################
def main():
    setA = '12'
    setB = 'abc'

    print("Set A: ", setA)
    print("Set B: ", setB)
    print('-------------------')
    # print('Union:             ', union(setA, setB))
    # print('Intersection:      ', intersection(setA, setB))
    # print('Cartesian Product: ')
    # print('Exclusive Or:      ', exclusiveOr(setA, setB))
    # print('Phi of A:          ')
    cartesianProduct(setA, setB)


main()