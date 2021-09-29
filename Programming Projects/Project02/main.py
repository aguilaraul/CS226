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

##########################################
# MAIN PROGRAM:
##########################################
def main():
    setA = '1111100000'
    setB = '1010101010'

    print(union(setA, setB))


main()