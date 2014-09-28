import os,sys
scriptdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(scriptdir)
import arff
from collections import Counter
import math
import pprint

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

def pretty_print(example_table):
    for row in example_table:
        itms = [str(x).ljust(15) for x in row]
        line = ' '.join(itms)
        print line

def nrows(example_table):
    return len(example_table)

def get_fieldnames(example_table):
    if nrows(example_table) > 0 :
        return example_table[0].get_fieldnames()
    else:
        return None

def get_fieldtype(example_table, attrname):
    if nrows(example_table) > 0 :
        return example_table[0].fieldnumornom[attrname]
    else:
        return None

def get_column(example_table, colname):
    return [row[colname] for row in example_table]

def entropy(example_table):
    "example_table is a list, each element of which is a row"
    classes = get_column(example_table, 'class')
    cnter = Counter(classes)
    total = sum(cnter.values())
    assert total > 0
    probs = [float(freq)/total for freq in cnter.values()]
    items = [p*math.log(p,2) for p in probs]
    return -sum(items)

def subset_equal(example_table, attr, value):
    "return a subset of rows in example_table"
    return [row for row in example_table if row[attr]==value]

def information_gain_nominal(example_table, attr):
    counttotal = nrows(example_table)
    Entropy_S = entropy(example_table)

    attrcolumn = get_column(example_table, attr)
    freqs = Counter(attrcolumn)
    Sum_right = 0
    for v in freqs.keys():
        subtable = subset_equal(example_table, attr, v)
        count_v = nrows(subtable)
        Entropy_v = entropy(subtable)
        Sum_right += (float(count_v)/float(counttotal)) + Entropy_v
        print 'count_v',count_v, \
              'Entropy_v', Entropy_v, \
              'Sum_right', Sum_right
    
    gain = Entropy_S - Entropy_v
    print gain
    print 'totalcount', counttotal, \
          'freqs', freqs
    return gain

def information_gain_numeric(example_table, attr):
    # sort table
    # find split candidates
    # calculate the information gain of each candidates 
    # (transform it to nominal to calculate)
    # find the best one

    # sort table
    tablesorted = sorted(example_table, key=lambda k: k[attr]) 

    # find split candidates
    split_candidates = []
    #value of this attribute and its set of corresponding classes
    attrclasses = [] 
    for i, row in enumerate(tablesorted):
        curvalue = row[attr]
        curclass = row['class']
        if len(attrclasses) == 0 or attrclasses[-1]['value'] != curvalue:
            attrclasses.append( {'value':curvalue,
                                 'class':set([curclass])} )
        else :
            attrclasses[-1]['class'].add(curclass)
    print attrclasses


if __name__ == '__main__':
    fulltable = list(arff.load('./heart_test.arff'))
    print get_fieldnames(fulltable)
    #print get_column(fulltable, "class")
    #print entropy(fulltable)
    #pretty_print( subset_equal(fulltable, 'class', 'positive') )
    #information_gain_nominal(fulltable, 'sex')
    #print get_fieldtype(fulltable, 'class')
    #print get_fieldtype(fulltable, 'age')
    information_gain_numeric(fulltable, 'age')


