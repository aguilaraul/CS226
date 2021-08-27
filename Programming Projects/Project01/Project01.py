'''
DEVELOPER: Raul Aguilar
COLLABORATORS: <other names>
COURSE:	CS226 Discrete Structures
PROJECT:	Project01
LAST MODIFIED: 25 August 2021
'''
##########################################
#	<TITLE OF PROGRAM>
########################################## 
# PROGRAM DESCRIPTION:
# Given the truth values of the propositions p and q, find the truth
# values of the conjuction, disjunction, exclusive or, conditional
# statement, and biconditional of these propositions
##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
#<imports here>

##########################################
# FUNCTIONS:
##########################################
#DESCRIPTION:<description of what function does>
#<define functions here>

##########################################
# MAIN PROGRAM:
##########################################

def isConjunction(pvalue, qvalue):
    return pvalue[0].lower() == 't' and qvalue[0].lower() == 't'

def isDisjunction(pvalue, qvalue):
    return pvalue[0].lower() == 't' or qvalue[0].lower() == 't'

def isExclusiveOr(pvalue, qvalue):
    return isDisjunction(pvalue, qvalue) and not isConjunction(pvalue, qvalue)

def isConditionalStatement(pvalue, qvalue):
    return not (pvalue[0].lower() == 't' and qvalue[0].lower() == 'f')

def isBiconditionalStatement(pvalue, qvalue):
    return pvalue[0].lower() == qvalue[0].lower()

def main():
    p = 't'
    q = 't'

    p = input("Enter the truth value for p: ")
    q = input("Enter the truth value for q: ")

    print("p truth value: ", p)
    print("q truth value: ", q)

    print("Conjunction: ", isConjunction(p, q))
    print("Disjunction: ", isDisjunction(p, q))
    print("Exclusive Or: ", isExclusiveOr(p, q))
    print("Conditional Statement: ", isConditionalStatement(p, q))
    print("Biconditional Statement: ", isBiconditionalStatement(p, q))

main()