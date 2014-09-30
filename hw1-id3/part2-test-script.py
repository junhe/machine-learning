import subprocess
import sys


treatments = [
          {'ratio' : 0.05,
           'repeat': 10,
           'm'     : 4},
          {'ratio' : 0.10,
           'repeat': 10,
           'm'     : 4},
          {'ratio' : 0.20,
           'repeat': 10,
           'm'     : 4},
          {'ratio' : 0.50,
           'repeat': 10,
           'm'     : 4},
          {'ratio' : 1,
           'repeat': 1,
           'm'     : 4}
          ]

#for treatment in treatments:
    #treatment['trainfile'] = 'heart_train.arff'
    #treatment['testfile'] = 'heart_test.arff'

for treatment in treatments:
    treatment['trainfile'] = './diabetes_train.arff'
    treatment['testfile'] = './diabetes_test.arff'

headerprinted = False
for treatment in treatments:
    for i in range(treatment['repeat']):
        cmd = ['python', 'main.py',
               treatment['trainfile'], treatment['testfile'],
               treatment['m'], treatment['ratio'],
               0,0,0,1]

        cmd = [str(x) for x in cmd]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        proc.wait()

        for line in proc.stdout:
            if 'DATALINEMARK' in line:
                print line,
            if 'HEADERLINEMARK' in line and headerprinted == False:
                print line,
                headerprinted = True
            sys.stdout.flush()



