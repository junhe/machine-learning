import os,sys
scriptdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(scriptdir)
import arff

# Let me begin by describing the program.
# It first read an arff file into a list. Each element of the list
# is a row. each row has equal number of attributes. 
# The 'class' attribute has the target concept.
# 
# Craete a function that takes as input the 
#   Examples
#   TargetAttributes
#   Attributes
# In this function, first, create a Root node for the tree. 
# If all examples are positive, return the single node tree Root, with lable +
# If all examples are negaive, return the single node tree Root, with label -
# If attributes is empty, return the single -node tree Root, with
# lable=most common value of Target Attributes in example
# if all the above 'if's are false, do the following:
# A = the attribute that best best classifies examples. Use information gain
# to choose. So now we know we need to several more function:
#   1. BestAttribute(Examples, Attributes, TargetAttributes): this function
#      finds all the InformationGain of all the attributes in Attributes.
#      And pick the one with the largest informationgain.
#      
#      InformationGain(Examples, OneAttribute): Get the InformationGain of 
#        an attribute OneAttribute.
#
#      Entropy(Examples): Get the Entropy of some examples.
#
# Root = A
# For each possible value vi of A (so we need a function to find all possible 
# values of a Attribute in some examples):
#   Add a new tree branch to below Root, corresponding to A=vi
#   Let Examples_vi = Examples where A=vi
#
#   if Examples_vi is empty:
#       add leaf node to this branch with label=most common value of 
#       most common value of Targetattributes in *Examples*
#   else:
#       add subtree ID3(Examples_vi, targetattributes, Attributes-A)
#
#


def nrows(example_table):
    return len(example_table)

def get_fieldnames(example_table):
    if nrows(example_table) > 0 :
        return example_table[0].get_fieldnames()
    else:
        return None

def get_column(example_table, colname):
    return [row[colname] for row in example_table]

def entropy(example_table):
    "example_table is a list, each element of which is a row"

if __name__ == '__main__':
    fulltable = list(arff.load('./heart_test.arff'))
    print get_fieldnames(fulltable)
    print get_column(fulltable, "class")



