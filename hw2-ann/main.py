import os,sys
scriptdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(scriptdir)
import arff
import math
import pprint
import random

classdic = {'Rock':0,
            'Mine':1}

classdic2 = {'Rock':'neg',
            'Mine':'pos'}

def pretty_print(example_table):
    width = 15
    header = [x.ljust(width) for x in get_fieldnames(example_table)]
    print ' '.join(header)
    for row in example_table:
        itms = [str(x).ljust(width) for x in row]
        line = ' '.join(itms)
        print line

def nrows(example_table):
    return len(example_table)

def get_fieldnames(example_table):
    if nrows(example_table) > 0 :
        return example_table[0].get_fieldnames()
    else:
        return []

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


def get_column_uniques(example_table, colname):
    col = get_column(example_table, colname)
    colset = set(col)
    return colset


def row2xlist(row):
    nx = len(row)-1
    xlist = [row[i] for i in range(nx)]
    xlist.insert(0, 1)
    return xlist

def get_output(row, wlist):
    "wlist=[w0,w1,...wn]. w0 is the bia paramter."
    xlist = row2xlist(row)
    assert len(xlist)==len(wlist)

    items = [x*w for x,w in zip(xlist, wlist)]
    total = sum(items)
    return 1/(1+math.exp(-total))


def ann_train(datatable, lrate, nepochs):
    colnames = get_fieldnames(datatable)
    ncols = len(colnames)
    n_nodes = ncols

    # let's use index 0 for the bias parameter
    wlist = [0.1 for i in range(n_nodes)]

    for epoch in range(nepochs):
        for row in datatable:
            out = get_output(row, wlist)
            y = classdic[row['Class']]
            #print out, y
            coeff = -(y-out)*out*(1 - out)
            xlist = row2xlist(row)
            Ew = [coeff*x for x in xlist]
            delta_w = [-lrate*ew for ew in Ew] 
            wlist = [wi+d for wi,d in zip(wlist, delta_w)]
    return wlist

def num2class(x):
    if x >= 0.5:
        return 'Mine'
    else:
        return 'Rock'

def ann_test(datatable, wlist):
    outvec = []
    for row in datatable:
        outvec.append( get_output(row, wlist) )

    yvec = get_column(datatable, 'Class')
    outvecclass = [num2class(y) for y in outvec]
    comp = [x1==x2 for x1,x2 in zip(yvec, outvecclass)]
    
    accuracy = float(sum(comp))/len(comp)
    #print accuracy
    d = {'accuracy':accuracy,
         'numout'  :outvec,
         'classout':outvecclass,
         'correctclass':yvec}
    return d

def roc_points(instances):
    "instances are in the form of [(c,y),...]"
    # sort
    instances = sorted(instances, key=lambda x: x[0]) # sort by c 

    TP = 0
    FP = 0
    last_TP = 0

    c = [x[0] for x in instances]
    y = [x[1] for x in instances]

    num_neg = len( [x for x in y if x=='neg'] )
    num_pos = len( [x for x in y if x=='pos'] )
    
    m = len(instances)

    coords_list = [(0,0)]
    for i in range(1, m):
        if c[i] != c[i-1] and y[i] == 'neg' and TP > last_TP:
            FPR = float(FP)/num_neg
            TPR = float(TP)/num_pos
            coords_list.append((FPR, TPR))
            last_TP = TP

        if y[i] == 'pos':
            TP += 1
        else:
            FP += 1

    FPR = float(FP)/num_neg
    TPR = float(TP)/num_pos
    coords_list.append((FPR, TPR))

    print 'x','y'
    for x,y in coords_list:
        print x,y


       

if __name__ == '__main__':
    argv = sys.argv

    if len(argv) != 5 :
        print 'Usage: python', argv[0], \
                '<datafile> n l e ' 
        exit(1)

    datafile = argv[1]
    nfold = int(argv[2])
    lrate = float(argv[3])
    epochs = int(argv[4])

    fulltable = list(arff.load(datafile))
    random.shuffle(fulltable)
    n = nrows(fulltable)
    setsize = (n+nfold-1)/nfold
    setlist = []
    assert setsize > 0
    for i in range(n):
        setindex = i/setsize
        if setindex > len(setlist)-1:
            # not in the list
            setlist.append([i])
        else:
            setlist[setindex].append(i)

    #ann_train(fulltable, lrate, epochs)
    # cross validation

    assert nfold == len(setlist), 'hello{nf}!={nset}'.format(nf=nfold,nset=len(setlist))
    accuracylist = []
    for testid in range(nfold):
        train_sets = [id for id in range(nfold) if id != testid] 
        trainids = [id for i in train_sets for id in setlist[i]] 

        traintable = [fulltable[i] for i in trainids]
        testtable = [fulltable[i] for i in setlist[testid]]
       
        # train
        wlist = ann_train(traintable, lrate, epochs)
        
        # test
        testresult = ann_test(testtable, wlist)
        accuracylist.append(testresult['accuracy'])
        
        c = testresult['numout']
        y = [classdic2[x] for x in testresult['correctclass']]
        roc_points(zip(c,y))

    ave_accuracy = float(sum(accuracylist))/len(accuracylist)
    print ave_accuracy


