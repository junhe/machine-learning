dt-learn uses /bin/bash, so please make sure BASH is there.
I use tab to separate when printing tree. 
I use Python 2.7.5. The program has produced identical outputs 
(except for the tabs) for all samples on the homework webpage. 

Here is one of my output:

$./dt-learn diabetes_train.arff diabetes_test.arff 20
plas <= 127.500000 [342 78]
|	age <= 28.500000 [220 20]
|	|	mass <= 31.400000 [130 2]
|	|	|	preg <= 7.000000 [130 1]
|	|	|	|	pedi <= 0.672000 [111 0]: tested_negative
|	|	|	|	pedi > 0.672000 [19 1]
|	|	|	|	|	pedi <= 0.686500 [0 1]: tested_positive
|	|	|	|	|	pedi > 0.686500 [19 0]: tested_negative
|	|	|	preg > 7.000000 [0 1]: tested_positive
|	|	mass > 31.400000 [90 18]
|	|	|	pres <= 37.000000 [0 2]: tested_positive
|	|	|	pres > 37.000000 [90 16]
|	|	|	|	pedi <= 0.509500 [62 6]
|	|	|	|	|	mass <= 45.400000 [62 4]
|	|	|	|	|	|	insu <= 38.000000 [17 4]
|	|	|	|	|	|	|	plas <= 94.000000 [8 0]: tested_negative
|	|	|	|	|	|	|	plas > 94.000000 [9 4]: tested_negative
|	|	|	|	|	|	insu > 38.000000 [45 0]: tested_negative
|	|	|	|	|	mass > 45.400000 [0 2]: tested_positive
|	|	|	|	pedi > 0.509500 [28 10]
|	|	|	|	|	pres <= 64.500000 [9 7]: tested_negative
|	|	|	|	|	pres > 64.500000 [19 3]
|	|	|	|	|	|	pres <= 79.000000 [13 0]: tested_negative
|	|	|	|	|	|	pres > 79.000000 [6 3]: tested_negative
|	age > 28.500000 [122 58]
|	|	mass <= 26.350000 [34 1]
|	|	|	mass <= 9.650000 [0 1]: tested_positive
|	|	|	mass > 9.650000 [34 0]: tested_negative
|	|	mass > 26.350000 [88 57]
|	|	|	pedi <= 0.625000 [75 32]
|	|	|	|	plas <= 93.500000 [26 2]
|	|	|	|	|	plas <= 28.500000 [0 1]: tested_positive
|	|	|	|	|	plas > 28.500000 [26 1]
|	|	|	|	|	|	preg <= 11.500000 [24 0]: tested_negative
|	|	|	|	|	|	preg > 11.500000 [2 1]: tested_negative
|	|	|	|	plas > 93.500000 [49 30]
|	|	|	|	|	skin <= 27.500000 [23 24]
|	|	|	|	|	|	pres <= 84.000000 [15 23]
|	|	|	|	|	|	|	pedi <= 0.468000 [12 23]
|	|	|	|	|	|	|	|	age <= 56.000000 [10 23]
|	|	|	|	|	|	|	|	|	mass <= 27.950000 [0 5]: tested_positive
|	|	|	|	|	|	|	|	|	mass > 27.950000 [10 18]
|	|	|	|	|	|	|	|	|	|	mass <= 29.650000 [4 1]: tested_negative
|	|	|	|	|	|	|	|	|	|	mass > 29.650000 [6 17]
|	|	|	|	|	|	|	|	|	|	|	preg <= 7.000000 [2 13]: tested_positive
|	|	|	|	|	|	|	|	|	|	|	preg > 7.000000 [4 4]: tested_negative
|	|	|	|	|	|	|	|	age > 56.000000 [2 0]: tested_negative
|	|	|	|	|	|	|	pedi > 0.468000 [3 0]: tested_negative
|	|	|	|	|	|	pres > 84.000000 [8 1]: tested_negative
|	|	|	|	|	skin > 27.500000 [26 6]
|	|	|	|	|	|	plas <= 104.000000 [12 0]: tested_negative
|	|	|	|	|	|	plas > 104.000000 [14 6]
|	|	|	|	|	|	|	pres <= 89.000000 [14 4]: tested_negative
|	|	|	|	|	|	|	pres > 89.000000 [0 2]: tested_positive
|	|	|	pedi > 0.625000 [13 25]
|	|	|	|	preg <= 8.500000 [13 18]
|	|	|	|	|	pedi <= 0.698500 [0 5]: tested_positive
|	|	|	|	|	pedi > 0.698500 [13 13]
|	|	|	|	|	|	mass <= 33.100000 [3 8]: tested_positive
|	|	|	|	|	|	mass > 33.100000 [10 5]: tested_negative
|	|	|	|	preg > 8.500000 [0 7]: tested_positive
plas > 127.500000 [93 155]
|	mass <= 29.950000 [43 22]
|	|	plas <= 145.000000 [30 6]
|	|	|	preg <= 1.500000 [12 0]: tested_negative
|	|	|	preg > 1.500000 [18 6]
|	|	|	|	insu <= 132.500000 [13 6]: tested_negative
|	|	|	|	insu > 132.500000 [5 0]: tested_negative
|	|	plas > 145.000000 [13 16]
|	|	|	age <= 61.000000 [9 16]
|	|	|	|	age <= 25.500000 [3 0]: tested_negative
|	|	|	|	age > 25.500000 [6 16]
|	|	|	|	|	pres <= 72.000000 [0 8]: tested_positive
|	|	|	|	|	pres > 72.000000 [6 8]: tested_positive
|	|	|	age > 61.000000 [4 0]: tested_negative
|	mass > 29.950000 [50 133]
|	|	plas <= 157.500000 [39 62]
|	|	|	pedi <= 0.400500 [26 20]
|	|	|	|	mass <= 45.550000 [26 14]
|	|	|	|	|	pres <= 69.000000 [4 7]: tested_positive
|	|	|	|	|	pres > 69.000000 [22 7]
|	|	|	|	|	|	pres <= 79.000000 [12 1]: tested_negative
|	|	|	|	|	|	pres > 79.000000 [10 6]: tested_negative
|	|	|	|	mass > 45.550000 [0 6]: tested_positive
|	|	|	pedi > 0.400500 [13 42]
|	|	|	|	age <= 30.000000 [11 11]
|	|	|	|	|	pres <= 73.000000 [3 10]: tested_positive
|	|	|	|	|	pres > 73.000000 [8 1]: tested_negative
|	|	|	|	age > 30.000000 [2 31]
|	|	|	|	|	plas <= 152.500000 [0 27]: tested_positive
|	|	|	|	|	plas > 152.500000 [2 4]: tested_positive
|	|	plas > 157.500000 [11 71]
|	|	|	insu <= 629.500000 [9 71]
|	|	|	|	age <= 44.500000 [4 56]
|	|	|	|	|	pedi <= 0.306500 [4 13]: tested_positive
|	|	|	|	|	pedi > 0.306500 [0 43]: tested_positive
|	|	|	|	age > 44.500000 [5 15]
|	|	|	|	|	preg <= 7.500000 [5 9]: tested_positive
|	|	|	|	|	preg > 7.500000 [0 6]: tested_positive
|	|	|	insu > 629.500000 [2 0]: tested_negative
preg            plas            pres            skin            insu            mass            pedi            age             class           predicted_class
6.0             148.0           72.0            35.0            0.0             33.6            0.627           50.0            tested_positive tested_positive
8.0             183.0           64.0            0.0             0.0             23.3            0.672           32.0            tested_positive tested_positive
0.0             137.0           40.0            35.0            168.0           43.1            2.288           33.0            tested_positive tested_positive
3.0             78.0            50.0            32.0            88.0            31.0            0.248           26.0            tested_positive tested_negative
2.0             197.0           70.0            45.0            543.0           30.5            0.158           53.0            tested_positive tested_positive
8.0             125.0           96.0            0.0             0.0             0.0             0.232           54.0            tested_positive tested_positive
10.0            168.0           74.0            0.0             0.0             38.0            0.537           34.0            tested_positive tested_positive
1.0             189.0           60.0            23.0            846.0           30.1            0.398           59.0            tested_positive tested_negative
5.0             166.0           72.0            19.0            175.0           25.8            0.587           51.0            tested_positive tested_positive
7.0             100.0           0.0             0.0             0.0             30.0            0.484           32.0            tested_positive tested_negative
0.0             118.0           84.0            47.0            230.0           45.8            0.551           31.0            tested_positive tested_negative
7.0             107.0           74.0            0.0             0.0             29.6            0.254           31.0            tested_positive tested_negative
1.0             115.0           70.0            30.0            96.0            34.6            0.529           32.0            tested_positive tested_negative
7.0             196.0           90.0            0.0             0.0             39.8            0.451           41.0            tested_positive tested_positive
9.0             119.0           80.0            35.0            0.0             29.0            0.263           29.0            tested_positive tested_negative
11.0            143.0           94.0            33.0            146.0           36.6            0.254           51.0            tested_positive tested_negative
10.0            125.0           70.0            26.0            115.0           31.1            0.205           41.0            tested_positive tested_negative
7.0             147.0           76.0            0.0             0.0             39.4            0.257           43.0            tested_positive tested_negative
3.0             158.0           76.0            36.0            245.0           31.6            0.851           28.0            tested_positive tested_positive
9.0             102.0           76.0            37.0            0.0             32.9            0.665           46.0            tested_positive tested_positive
2.0             90.0            68.0            42.0            0.0             38.2            0.503           27.0            tested_positive tested_negative
4.0             111.0           72.0            47.0            207.0           37.1            1.39            56.0            tested_positive tested_negative
9.0             171.0           110.0           24.0            240.0           45.4            0.721           54.0            tested_positive tested_positive
0.0             180.0           66.0            39.0            0.0             42.0            1.893           25.0            tested_positive tested_positive
7.0             103.0           66.0            32.0            0.0             39.1            0.344           31.0            tested_positive tested_negative
8.0             176.0           90.0            34.0            300.0           33.7            0.467           58.0            tested_positive tested_positive
7.0             187.0           68.0            39.0            304.0           37.7            0.254           41.0            tested_positive tested_positive
8.0             133.0           72.0            0.0             0.0             32.9            0.27            39.0            tested_positive tested_negative
7.0             114.0           66.0            0.0             0.0             32.8            0.258           42.0            tested_positive tested_positive
0.0             109.0           88.0            30.0            0.0             32.5            0.855           38.0            tested_positive tested_positive
2.0             100.0           66.0            20.0            90.0            32.9            0.867           28.0            tested_positive tested_negative
13.0            126.0           90.0            0.0             0.0             43.4            0.583           42.0            tested_positive tested_negative
0.0             131.0           0.0             0.0             0.0             43.2            0.27            26.0            tested_positive tested_positive
5.0             137.0           108.0           0.0             0.0             48.8            0.227           37.0            tested_positive tested_positive
15.0            136.0           70.0            32.0            110.0           37.1            0.153           43.0            tested_positive tested_negative
1.0             85.0            66.0            29.0            0.0             26.6            0.351           31.0            tested_negative tested_negative
1.0             89.0            66.0            23.0            94.0            28.1            0.167           21.0            tested_negative tested_negative
5.0             116.0           74.0            0.0             0.0             25.6            0.201           30.0            tested_negative tested_negative
10.0            115.0           0.0             0.0             0.0             35.3            0.134           29.0            tested_negative tested_negative
4.0             110.0           92.0            0.0             0.0             37.6            0.191           30.0            tested_negative tested_negative
10.0            139.0           80.0            0.0             0.0             27.1            1.441           57.0            tested_negative tested_negative
1.0             103.0           30.0            38.0            83.0            43.3            0.183           33.0            tested_negative tested_negative
3.0             126.0           88.0            41.0            235.0           39.3            0.704           27.0            tested_negative tested_negative
8.0             99.0            84.0            0.0             0.0             35.4            0.388           50.0            tested_negative tested_negative
1.0             97.0            66.0            15.0            140.0           23.2            0.487           22.0            tested_negative tested_negative
13.0            145.0           82.0            19.0            110.0           22.2            0.245           57.0            tested_negative tested_negative
5.0             117.0           92.0            0.0             0.0             34.1            0.337           38.0            tested_negative tested_negative
5.0             109.0           75.0            26.0            0.0             36.0            0.546           60.0            tested_negative tested_negative
3.0             88.0            58.0            11.0            54.0            24.8            0.267           22.0            tested_negative tested_negative
6.0             92.0            92.0            0.0             0.0             19.9            0.188           28.0            tested_negative tested_negative
10.0            122.0           78.0            31.0            0.0             27.6            0.512           45.0            tested_negative tested_negative
4.0             103.0           60.0            33.0            192.0           24.0            0.966           33.0            tested_negative tested_negative
11.0            138.0           76.0            0.0             0.0             33.2            0.42            35.0            tested_negative tested_positive
3.0             180.0           64.0            25.0            70.0            34.0            0.271           26.0            tested_negative tested_positive
7.0             133.0           84.0            0.0             0.0             40.2            0.696           37.0            tested_negative tested_positive
7.0             106.0           92.0            18.0            0.0             22.7            0.235           48.0            tested_negative tested_negative
7.0             159.0           64.0            0.0             0.0             27.4            0.294           40.0            tested_negative tested_positive
1.0             146.0           56.0            0.0             0.0             29.7            0.564           29.0            tested_negative tested_positive
2.0             71.0            70.0            27.0            0.0             28.0            0.586           22.0            tested_negative tested_negative
7.0             105.0           0.0             0.0             0.0             0.0             0.305           24.0            tested_negative tested_negative
1.0             103.0           80.0            11.0            82.0            19.4            0.491           22.0            tested_negative tested_negative
1.0             101.0           50.0            15.0            36.0            24.2            0.526           26.0            tested_negative tested_negative
5.0             88.0            66.0            21.0            23.0            24.4            0.342           30.0            tested_negative tested_negative
7.0             150.0           66.0            42.0            342.0           34.7            0.718           42.0            tested_negative tested_positive
1.0             73.0            50.0            10.0            0.0             23.0            0.248           21.0            tested_negative tested_negative
0.0             100.0           88.0            60.0            110.0           46.8            0.962           31.0            tested_negative tested_negative
0.0             146.0           82.0            0.0             0.0             40.5            1.781           44.0            tested_negative tested_positive
0.0             105.0           64.0            41.0            142.0           41.5            0.173           22.0            tested_negative tested_negative
2.0             84.0            0.0             0.0             0.0             0.0             0.304           21.0            tested_negative tested_negative
5.0             44.0            62.0            0.0             0.0             25.0            0.587           36.0            tested_negative tested_negative
2.0             141.0           58.0            34.0            128.0           25.4            0.699           24.0            tested_negative tested_negative
5.0             99.0            74.0            27.0            0.0             29.0            0.203           32.0            tested_negative tested_negative
2.0             109.0           92.0            0.0             0.0             42.7            0.845           54.0            tested_negative tested_negative
1.0             95.0            66.0            13.0            38.0            19.6            0.334           25.0            tested_negative tested_negative
4.0             146.0           85.0            27.0            100.0           28.9            0.189           27.0            tested_negative tested_positive
5.0             139.0           64.0            35.0            140.0           28.6            0.411           26.0            tested_negative tested_negative
4.0             129.0           86.0            20.0            270.0           35.1            0.231           23.0            tested_negative tested_negative
1.0             79.0            75.0            30.0            0.0             32.0            0.396           22.0            tested_negative tested_negative
1.0             0.0             48.0            20.0            0.0             24.7            0.14            22.0            tested_negative tested_negative
7.0             62.0            78.0            0.0             0.0             32.6            0.391           41.0            tested_negative tested_negative
5.0             95.0            72.0            33.0            0.0             37.7            0.37            27.0            tested_negative tested_negative
2.0             112.0           66.0            22.0            0.0             25.0            0.307           24.0            tested_negative tested_negative
3.0             113.0           44.0            13.0            0.0             22.4            0.14            22.0            tested_negative tested_negative
2.0             74.0            0.0             0.0             0.0             0.0             0.102           22.0            tested_negative tested_negative
7.0             83.0            78.0            26.0            71.0            29.3            0.767           36.0            tested_negative tested_positive
0.0             101.0           65.0            28.0            0.0             24.6            0.237           22.0            tested_negative tested_negative
2.0             110.0           74.0            29.0            125.0           32.4            0.698           27.0            tested_negative tested_negative
13.0            106.0           72.0            54.0            0.0             36.6            0.178           45.0            tested_negative tested_negative
2.0             100.0           68.0            25.0            71.0            38.5            0.324           26.0            tested_negative tested_negative
1.0             107.0           68.0            19.0            0.0             26.5            0.165           24.0            tested_negative tested_negative
1.0             80.0            55.0            0.0             0.0             19.1            0.258           21.0            tested_negative tested_negative
4.0             123.0           80.0            15.0            176.0           32.0            0.443           34.0            tested_negative tested_positive
7.0             81.0            78.0            40.0            48.0            46.7            0.261           42.0            tested_negative tested_negative
2.0             142.0           82.0            18.0            64.0            24.7            0.761           21.0            tested_negative tested_negative
6.0             144.0           72.0            27.0            228.0           33.9            0.255           40.0            tested_negative tested_negative
2.0             92.0            62.0            28.0            0.0             31.6            0.13            24.0            tested_negative tested_negative
1.0             71.0            48.0            18.0            76.0            20.4            0.323           22.0            tested_negative tested_negative
6.0             93.0            50.0            30.0            64.0            28.7            0.356           23.0            tested_negative tested_negative
1.0             151.0           60.0            0.0             0.0             26.1            0.179           22.0            tested_negative tested_negative
0.0             125.0           96.0            0.0             0.0             22.5            0.262           21.0            tested_negative tested_negative
correctly_classified: 73, total_instances: 100

