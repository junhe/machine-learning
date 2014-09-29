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
    #print cnter
    total = sum(cnter.values())
    assert total > 0
    probs = [float(freq)/total for freq in cnter.values()]
    items = [p*math.log(p,2) for p in probs]
    return -sum(items)

def subset_equal(example_table, attr, value):
    "return a subset of rows in example_table"
    return [row for row in example_table if row[attr]==value]

def information_gain_general(example_table, attr):
    fieldtype = get_fieldtype(example_table, attr)
    if fieldtype == 'numeric':
        infogain = information_gain_numeric(example_table, attr)
        infogain['attrname'] = attr
        return infogain
    else :
        infogain = information_gain_nominal(example_table, attr)
        d = {'type':'nominal',
             'infogain':infogain,
             'attrname':attr}
        return d


def information_gain_nominal(example_table, attr):
    #print '-------------------', attr
    counttotal = nrows(example_table)
    Entropy_S = entropy(example_table)
    #print 'Entropy_S', Entropy_S

    attrcolumn = get_column(example_table, attr)
    freqs = Counter(attrcolumn)
    Sum_right = 0
    #print freqs.keys()
    for v in freqs.keys():
        #print v
        subtable = subset_equal(example_table, attr, v)
        count_v = nrows(subtable)
        Entropy_v = entropy(subtable)
        Sum_right += (float(count_v)/float(counttotal)) * Entropy_v
        #print 'count_v',count_v, \
              #'counttotal', counttotal, \
              #'Entropy_v', Entropy_v, \
              #'Sum_right', Sum_right
    
    gain = Entropy_S - Sum_right
    #print 'gain', gain
    #print 'totalcount', counttotal, \
          #'freqs', freqs
    return gain

def information_gain_numeric(example_table, attr):
    split_dic = infogain_of_numeric_splits(example_table, attr)
    
    maxinfogain = -float('inf')
    maxsplit = None
    for split,infogain in split_dic.items():
        if maxinfogain < infogain:
            maxinfogain = infogain
            maxsplit = split

    return {'type': 'numeric',
            'split': maxsplit,
            'infogain': maxinfogain}


def infogain_of_numeric_splits(example_table, attr):
    "it return {split:infogain, ..}"
    split_candidates = get_split_candidates(example_table, attr)

    split_dic = {}
    for split in split_candidates:
        infogain = information_gain_on_numeric_split(example_table, 
                                                      attr,
                                                      split)
        split_dic[split] = infogain

    return split_dic

def get_split_candidates(example_table, attr):
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
    #pprint.pprint( attrclasses )
    for i, item in enumerate(attrclasses):
        if i == 0 :
            continue
        # cases needs split
        # v_i-1 and v_i have a pair of different 'class'
        # if a set has more than one item, it must has a item
        # that is different to an item in another set
        if attrclasses[i]['class'] != attrclasses[i-1]['class'] or \
            len(attrclasses[i-1]['class']) > 1 or \
            len(attrclasses[i]['class']) > 1 :
            # this is a candidate
            #print 'this is a candidate----'
            #print attrclasses[i-1]
            #print attrclasses[i]
            candi = (attrclasses[i]['value'] + attrclasses[i-1]['value'])/2
            split_candidates.append(candi)
        #else :
            #print 'this is not a candidate----'
            #print attrclasses[i-1]
            #print attrclasses[i]
    
    return split_candidates

def information_gain_on_numeric_split(example_table, attr, split):
    # add a new nominal attribute according to the split
    # use the implemented information_gain for actual calculation
    attrname = '<= ' + str(split) 
    for row in example_table:
        if row[attr] <= split:
            row.add_attr(attrname, 'true')
        else :
            row.add_attr(attrname, 'false')
    infogain = information_gain_nominal(example_table, attrname)

    for row in example_table:
        row.del_attr(attrname)

    return infogain

def get_column_uniques(example_table, colname):
    col = get_column(example_table, colname)
    colset = set(col)
    return colset

def get_empty_node():
    nd = {'example_table': None,
          'decision_attr': None,
          'class_count'  : None, #[positive, negative]
          'label'        : None,
          'children'     : {}} #{'branch1': node, ..}
    return nd

def get_most_freq_item(dic):
    mymax = {'key': None,
             'value': -float('inf')}
    for k,v in dic.items():
        if v > mymax['value']:
            mymax['key'] = k
            mymax['value'] = v

    return mymax

def id3(example_table, attributes, target_attr):
    print '--------attributes', attributes, '----target_attr',target_attr
    root = get_empty_node()
   
    classes = get_column(example_table, 'class')
    classcnt = Counter(classes)
    #print classcnt
    if len(classcnt) == 1 :
        root['label'] = classcnt.keys()[0]
        return root 
    if len(attributes) == 0 :
        root['label'] = get_most_freq_item(classcnt)['key']
        return root
        
    # find the best attribute that classifies this example_table
    infogains = []
    for attr in attributes:
        infogains.append( information_gain_general(example_table, attr) )
    best_attr = max(infogains, key=lambda x: x['infogain'])
    print 'best:', best_attr
    #print information_gain_general(example_table, 'thal')
    #print information_gain_general(example_table, 'ca')
    #print information_gain_general(example_table, 'exang')

    root['decision_attr'] = best_attr
    root['class_count'] = classcnt
    #root['example_table'] = example_table
    valueset = get_column_uniques(example_table, 
                                  root['decision_attr']['attrname'])
    
    print root
    assert root['decision_attr']['type'] in ['numeric', 'nominal']
    
    # get subsets
    sublist = []
    if root['decision_attr']['type'] == 'nominal':
        for v in valueset:
            subexample = subset_equal(example_table, 
                                      root['decision_attr']['attrname'],   
                                      v)
            sublist.append( {v: subexample} )
    else :
        # get subset
        split = root['decision_attr']['split']
        attr = root['decision_attr']['attrname']
        smallerset = [row for row in example_table if row[attr] <= split]
        branchname = '<= '+str(split)
        sublist.append({branchname: smallerset})

        largerset = [row for row in example_table if row[attr] > split]
        branchname = '> '+str(split)
        sublist.append({branchname: largerset})

    for sub in sublist:
        branchname = sub.keys()[0]
        subexample = sub[branchname]
        if len(subexample) == 0 :
            subcounter = Counter(get_column(subexample, 'class'))
            commontarget = max(subcounter, key=lambda x:subcounter[x[0]])
            leaf = get_empty_node()
            leaf['class_coun'] = subcounter
            leaf['label']      = commontarget
            root['children'][branchname] = leaf
        else :
            subattributes = [attr for attr in attributes \
                    if attr != root['decision_attr']['attrname']]
            #print 'attrname',root['decision_attr']['attrname']
            #print 'attrs', attributes
            #print 'subattributes',subattributes
            node = id3(subexample, subattributes, 'class')
            root['children'][branchname] = node
    return root




        
            
if __name__ == '__main__':
    fulltable = list(arff.load('./heart_train.arff'))
    #fulltable = list(arff.load('./diabetes_train.arff'))
    attributes = get_fieldnames(fulltable)
    if 'class' in attributes:
        attributes.remove('class')
    #print get_column(fulltable, "class")
    #print entropy(fulltable)
    #pretty_print( subset_equal(fulltable, 'class', 'positive') )
    #information_gain_nominal(fulltable, 'sex')
    #print get_fieldtype(fulltable, 'class')
    #print get_fieldtype(fulltable, 'age')
    #information_gain_numeric(fulltable, 'age')
    #information_gain_on_numeric_split(fulltable, 'age', 55.5)
    #information_gain_on_numeric_split(fulltable, 'age', 60.5)
    #information_gain_on_numeric_split(fulltable, 'age', 40.5)
    #information_gain_numeric(fulltable, 'age')
    #print information_gain_numeric(fulltable, 'age')
    tree = id3(fulltable, attributes, 'class')
    #tree = id3(fulltable, ['ca', 'thal', 'thalach'], 'class')
    pprint.pprint(tree)


