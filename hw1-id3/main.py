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

global g_levelinfo 
global g_attributes

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
    if len(freqs) == 1 :
        # no candidate split
        return None

    if g_levelinfo.has_key(attr):
        levels = g_levelinfo[attr]
        #print levels,'--------------'
    else :
        levels = freqs.keys()

    Sum_right = 0
    #print freqs.keys()
    for v in levels:
        #print v
        subtable = subset_equal(example_table, attr, v)
        count_v = nrows(subtable)

        if count_v == 0 :
            Sum_right += 0
        else :
            Entropy_v = entropy(subtable)
            Sum_right += (float(count_v)/float(counttotal)) * Entropy_v
        #print 'count_v',count_v, \
              #'counttotal', counttotal, \
              #'Entropy_v', Entropy_v, \
              #'Sum_right', Sum_right
    
    gain = Entropy_S - Sum_right
    return gain

def information_gain_numeric(example_table, attr):
    split_dic = infogain_of_numeric_splits(example_table, attr)
    
    if len(split_dic) == 0 :
        return {'type': 'numeric',
                'split': None,
                'infogain': None}

    #print split_dic
    splitlist = split_dic.keys()
    splitlist.sort()

    maxvalue = max(split_dic.values())
    maxs = {}
    for k,v in split_dic.items():
        if v == maxvalue:
            maxs[k] = v

    for split in splitlist:
        if maxs.has_key(split):
            return {'type':'numeric',
                    'split':split,
                    'infogain':maxs[split]}
    print 'error in information_gain_numeric'
    exit(1)

    #maxinfogain = -float('inf')
    #maxsplit = None
    #for split,infogain in split_dic.items():
        #if maxinfogain < infogain:
            #maxinfogain = infogain
            #maxsplit = split

    #return {'type': 'numeric',
            #'split': maxsplit,
            #'infogain': maxinfogain}


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

def get_most_freq_item(dic, classlevels):
    lst = []
    for k,v in dic.items():
        lst.append({'key':k, 'value':v})
    maxitem = max(lst, key=lambda k:k['value'])
    maxs = {}
    for item in lst:
        if item['value'] == maxitem['value']:
            maxs[item['key']] = item

    for level in classlevels:
        if maxs.has_key(level):
            return maxs[level]
    print 'error in get_most_freq_item'
    exit(1)

    #mymax = {'key': None,
             #'value': -float('inf')}
    #for k,v in dic.items():
        #if v > mymax['value']:
            #mymax['key'] = k
            #mymax['value'] = v

    #return mymax

def id3(example_table, attributes, target_attr, m, attr_order, levelinfo):
    #print '--------attributes', attributes, '----target_attr',target_attr
    root = get_empty_node()
   
    classes = get_column(example_table, 'class')
    classcnt = Counter(classes)
    #print classcnt

    # STOP criteria (i) all the training instances reaching
    # the node belong to the same class
    if len(classcnt) == 1 :
        root['class_count'] = classcnt
        root['label'] = classcnt.keys()[0]
        return root 
    # STOP criteria (ii) there are fewer than m training instances
    # reaching the node
    if len(attributes) == 0 or nrows(example_table) < m :
        root['class_count'] = classcnt
        root['label'] = get_most_freq_item(classcnt, levelinfo['class'])['key']
        return root
        
    # find the best attribute that classifies this example_table
    infogains = []
    for attr in attributes:
        infogains.append( information_gain_general(example_table, attr) )
    #if max(get_column(example_table,'chol')) <= 233 :
        #print infogains
    maxgainval = max(infogains, key=lambda x: x['infogain'])['infogain']
    maxgains = {}
    for gain in infogains:
        if gain['infogain'] == maxgainval:
            maxgains[gain['attrname']]=gain
    #pprint.pprint(maxgains)
    for attr in attr_order:
        if maxgains.has_key(attr):
            best_attr = maxgains[attr]
            break
    #print 'best:', best_attr
    
    # STOP criteria (iii) no feature has positive information gain
    if best_attr['infogain'] <= 0 :
        root['class_count'] = classcnt
        root['label'] = get_most_freq_item(classcnt, levelinfo['class'])['key']
        return root

    # STOP criteria (iv) there are no more remaining candidate splits
    # at the node. i.e., all attribute has only one value
    has_over_one = False
    for gain in infogains:
        if (gain['type'] == 'nominal' and gain['infogain'] != None) or \
           (gain['type'] == 'numeric' and gain['split'] != None):
            has_over_one = True
    if has_over_one == False:
        root['class_count'] = classcnt
        root['label'] = get_most_freq_item(classcnt, levelinfo['class'])['key']
        return 

    root['decision_attr'] = best_attr
    root['class_count'] = classcnt
    
    assert root['decision_attr']['type'] in ['numeric', 'nominal']
    
    # get subsets
    sublist = []
    if root['decision_attr']['type'] == 'nominal':
        valueset = g_levelinfo[root['decision_attr']['attrname']]
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
        branchname = '<= '+"{0:.6f}".format(split)
        sublist.append({branchname: smallerset})

        largerset = [row for row in example_table if row[attr] > split]
        branchname = '> '+"{0:.6f}".format(split)
        sublist.append({branchname: largerset})

    for sub in sublist:
        branchname = sub.keys()[0]
        subexample = sub[branchname]
        #if branchname == 'typ_angina':
            #subcounter = Counter(get_column(example_table, 'class'))
            #pretty_print( example_table )
            #print 'mysubcounter', subcounter
            #exit(1)
        if len(subexample) == 0 :
            #if branchname == 'typ_angina':
                #print 'here'
                #exit(1)
            subcounter = Counter(get_column(example_table, 'class'))
            commontarget = get_most_freq_item(subcounter, g_levelinfo['class'])['key']
            #commontarget = max(subcounter, key=lambda x:subcounter[x[0]])
            leaf = get_empty_node()
            leaf['class_count'] = {} # empty
            leaf['label']      = commontarget
            root['children'][branchname] = leaf
        else :
            subattributes = [attr for attr in attributes \
                    if not (root['decision_attr']['type'] == 'nominal' and  
                    attr == root['decision_attr']['attrname'])]
            #print 'attrname',root['decision_attr']['attrname']
            #print 'attrs', attributes
            #print 'subattributes',subattributes
            node = id3(subexample, subattributes, 'class', m, 
                       attr_order, levelinfo)
            root['children'][branchname] = node
    return root



def print_tree(node, level, levelinfo):
    if node['decision_attr']['type'] == 'nominal':
        levels = levelinfo[node['decision_attr']['attrname']]
    else :
        levels = node['children'].keys()
        levels.sort()

    for branchname in levels:
        subnode = node['children'][branchname]
        sys.stdout.write( ''.join(['|\t']*level) )
        if node['decision_attr']['type'] == 'nominal':
            sep = ' = '
        else :
            sep = ' '
        sys.stdout.write( node['decision_attr']['attrname'] + sep +
                branchname + ' ' +
                get_count_str(subnode['class_count'], levelinfo['class']))

        if len(subnode['children']) == 0 :
            # the subnode is a leaf, we print the label rigth here
            print ': '+subnode['label']
        else :
            print  #start a new line and print the subtree there
            print_tree(subnode, level+1, levelinfo)
    return
        
def get_count_str(classcnt, levels):
    counts = []
    # [negative count, positive count]
    for level in levels:
        if classcnt.has_key(level):
            counts.append(classcnt[level])
        else :
            counts.append(0)
    
    counts = [str(x) for x in counts]
    retstr = '['+' '.join(counts)+']'
    return retstr
            
if __name__ == '__main__':
    global g_levelinfo, g_attributes

    fulltable = list(arff.load('./heart_train.arff'))
    #fulltable = list(arff.load('./diabetes_train.arff'))
    fieldnames = get_fieldnames(fulltable)
    attributes = [x for x in fieldnames if x != 'class']
    levelinfo = fulltable[0].levelinfo
    g_levelinfo = levelinfo
    g_attributes = [x for x in fieldnames if x != 'class'] 

    # for debug
    #fulltable = [row for row in fulltable \
                    #if row['thal'] == 'reversable_defect' and \
                       #row['cp']   == 'non_anginal' and \
                       #row['oldpeak'] < 1.9 and \
                       #row['trestbps'] > 122.5 and \
                       #row['chol'] <= 232.5]
    #pretty_print(fulltable)
    
    tree = id3(fulltable, attributes, 'class', 4, attr_order=attributes,
                  levelinfo=levelinfo)
    #pprint.pprint(tree)
    #print attributes
    print_tree(tree, 0, levelinfo)
    #print levelinfo


