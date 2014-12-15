import sys,os
import pprint
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn import tree
from sklearn.externals.six import StringIO
import subprocess
from sklearn.cross_validation import cross_val_score

def read_file(path):
    f = open(path, 'r')
    cnt = 0
    table = []
    for line in f:
        items = line.split()
        if cnt == 0:
            header = items
        else:
            table.append(items)

        cnt += 1
    f.close()

    d = {'header': header,
         'table' : table}
    return d

def head(df):
    print ' '.join(df['header'])
    cnt = 0
    for row in df['table']:
        if cnt > 10:
            break
        print ' '.join(row)
        cnt += 1

    return

def del_col(df, colname):
    k = df['header'].index(colname)
    del df['header'][k]
    for i,row in enumerate(df['table']):
        del df['table'][i][k]

def get_cols(df, colnames):
    positions = [df['header'].index(name) for name in colnames]
    table = []
    for row in df['table']:
        newrow = [row[i] for i in positions]
        table.append(newrow)

    df = {'header':colnames,
          'table' :table}
    return df

def df_to_dicdf(df):
    hdr = df['header']
    dicdf = []
    for row in df['table']:
        dic = dict(zip(hdr, row))
        dicdf.append(dic)

    return dicdf

def categorize_class(dicdf):
    if 'dspan' in dicdf[0].keys():
        for rowdic in dicdf:
            dspan = float(rowdic['dspan'])
            if dspan > 10*(2**30):
                rowdic['dspan'] = 1 #tail
            else:
                rowdic['dspan'] = 0 #nontail
    return

def convert_type(dicdf):
    # more numeric
    #typemap = {'sync':'num', 
               #'num.chunks':'num', 
               #'chunk.order':'num', 
               #'file.size':'num',
               #'fullness':'num', 
               #'num.cores':'num', 
               #'fsync':'num', 
               #'num.files':'num',
               #'layoutnumber':'num',
               #'disk.size':'num', 
               #'disk.used':'num',
               #'file.system':'factor',
               #'dspan':'factor'}

    # more factors
    typemap = {'sync':'factor', 
               'num.chunks':'num', 
               'chunk.order':'factor', 
               'file.size':'num',
               'fullness':'num', 
               'num.cores':'num', 
               'fsync':'factor', 
               'num.files':'num',
               'layoutnumber':'num',
               'disk.size':'num', 
               'disk.used':'num',
               'file.system':'factor',
               'dir.span':'num',
               'dspan':'factor'}

    for rowdic in dicdf:
        for k,v in rowdic.items():
            if typemap[k] == 'num':
                rowdic[k] = float(v)
            elif typemap[k] == 'factor':
                rowdic[k] = str(v)
            else:
                print 'bad type name'
                exit(1)

def split_bitmap(name, value):
    """
    it returns a dic with the splitted keys and values
    value has to be a string
    """
    newvalues = list(value)
    newvalues = [int(x) for x in newvalues]
    n = len(newvalues)
    newnames = [name+str(i) for i in range(n)]
    dic = dict(zip(newnames, newvalues))
    return dic

def get_top_features(featurearray, myclass, featurenames, n):
    clf_sel = ExtraTreesClassifier()
    clf_sel.fit(featurearray, myclass)
    feature_imp = zip(featurenames, clf_sel.feature_importances_)
    feature_imp.sort(key=lambda k: k[1], reverse=True)
    
    print 'Feature importance'
    for x, y in feature_imp:
        print x, y
    
    l = [x for x,y in feature_imp]
    return l[0:n]


def transform_sync_fsync(dicdf_features):
    # tranform sync, fsync to multiple features
    for i, rowdic in enumerate(dicdf_features):
        newsync = split_bitmap('sync', rowdic['sync'])
        del rowdic['sync']
        newfsync = split_bitmap('fsync', rowdic['fsync'])
        del rowdic['fsync']
        dicdf_features[i] = dict(rowdic.items() +
                                 newsync.items() +
                                 newfsync.items())
    return dicdf_features
 
def main():
    #df = read_file('./agga.fixedimg-3.12.5.txt-nosetaffinity')
    df = read_file('./agga.fixedimg-3.12.5.txt-nosetaffinity1cpu')
    
    featurecols = ['sync', 'num.chunks', 'chunk.order', 'file.size',
              'fullness', 'num.cores', 'fsync', 'num.files', 'layoutnumber',
              'disk.size', 'disk.used', 'dir.span']
    #featurecols = ['file.system', 'file.size']

    df_features = get_cols(df, featurecols)
    dicdf_features = df_to_dicdf(df_features)
    convert_type(dicdf_features)

    dicdf_features = transform_sync_fsync(dicdf_features)

    #cnt = 0
    #for rowdic in dicdf_features:
        #print rowdic
        #cnt += 1
        #if cnt > 10:
            #break

    vec_features = DictVectorizer()
    featurearray = vec_features.fit_transform(dicdf_features).toarray()
    #print vec_features.get_feature_names()

    df_class = get_cols(df, ['dspan'])
    dicdf_class = df_to_dicdf(df_class)
    convert_type(dicdf_class)
    categorize_class(dicdf_class)
    
    myclass = []
    for rowdic in dicdf_class:
        myclass.append(rowdic['dspan']) 

    # feature selection
    feature_selected = get_top_features(featurearray, myclass, vec_features.get_feature_names(), 3)

    clf = tree.DecisionTreeClassifier(max_depth=8, criterion='entropy')
    clf = clf.fit(featurearray, myclass)
    onerow = featurearray[1]
    print vec_features.get_feature_names()
    print onerow
    print clf.predict([onerow])
    print clf.predict_proba([onerow])
    print myclass[1]
    print 'score:', clf.score(featurearray, myclass)

    #for mydepth in range(1, 20):
        ##print 'current depth:', mydepth
        #clf2 = tree.DecisionTreeClassifier(max_depth=mydepth, criterion='entropy')
        #scores = cross_val_score(clf2, featurearray, myclass, cv=10)
        #ave = sum(scores)/len(scores)
        #print mydepth, ave


    #X = [[0, 0], [0, 0], [1, 0]]
    #Y = [0,0,1]
    #clf = tree.DecisionTreeClassifier()
    #clf = clf.fit(X, Y)
    #print clf.predict([[1,1]])
    #print clf.predict_proba([[1,1]])

    with open('allocator.dot', 'w') as f:
        f = tree.export_graphviz(clf, 
                                 feature_names=vec_features.get_feature_names(),
                                 #feature_names=['a','b'],
                                 out_file=f)

    # generate plot
    map = [{'old':'X['+str(i)+']', 'new':col} for i,col in enumerate(featurecols)]

    #f = open('allocator.dot', 'r')
    #for line in f:
        #for dic in map:
            #line = line.replace(dic['old'], dic['new'])
    #f.close()

    cmd = 'dot -Tpdf allocator.dot -o allocator.pdf'
    subprocess.call(cmd.split())

if __name__ == '__main__':
    main()



