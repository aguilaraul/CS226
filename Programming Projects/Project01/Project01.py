'''
DEVELOPER: Raul Aguilar
COLLABORATORS: <other names>
COURSE:	CS226 Discrete Structures
PROJECT:	Project01
LAST MODIFIED: 28 August 2021
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
def isConjunction(pvalue, qvalue):
    # Checks if both truth values are True
    # If so, returns True and is a conjunction
    # Otherwise return False, not a conjunction
    return pvalue[0].lower() == 't' and qvalue[0].lower() == 't'

def isDisjunction(pvalue, qvalue):
    # Checks if either truth value is True
    # If so, returns True and is a disjunction
    # Otherwise return False, not a disjunction
    return pvalue[0].lower() == 't' or qvalue[0].lower() == 't'

def isExclusiveOr(pvalue, qvalue):
    # Checks if both truth values are different from each other
    # If so, returns True
    # Otherwise, returns False
    return isDisjunction(pvalue, qvalue) and not isConjunction(pvalue, qvalue)

def isConditionalStatement(pvalue, qvalue):
    # Checks if p is True and q is False
    # If so, returns False and is not a conditional statement
    # Otherwise, returns True ans is a conditional statement
    return not (pvalue[0].lower() == 't' and qvalue[0].lower() == 'f')

def isBiconditionalStatement(pvalue, qvalue):
    # Check if both truth values are the same
    # If so, returns True and is a biconditional statement
    # Otherwise, return False and is not a biconditional statement
    return pvalue[0].lower() == qvalue[0].lower()


##########################################
# MAIN PROGRAM:
##########################################
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