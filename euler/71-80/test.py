Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: C:\Users\Jaxn8\MyStuff\euler\71-80\72.py ==============
primed
10000
20000
30000
40000
50000
60000
70000
80000
90000
100000
110000
120000
130000
140000
150000
160000
170000
180000
190000
200000
210000
220000
230000
240000
250000
260000
270000
280000
290000
300000
310000
320000
330000
340000
350000
360000
370000
380000
390000
400000
410000
420000
430000
440000
450000
460000
470000
480000
490000
500000
510000
520000
530000
540000
550000
560000
570000
580000
590000
600000
610000
620000
630000
640000
650000
660000
670000
680000
690000
700000
710000
720000
730000
740000
750000
760000
770000
780000
790000
800000
810000
820000
830000
840000
850000
860000
870000
880000
890000
900000
910000
920000
930000
940000
950000
960000
970000
980000
990000
1000000
Traceback (most recent call last):
  File "C:\Users\Jaxn8\MyStuff\euler\71-80\72.py", line 9, in <module>
    file.write(factors)
TypeError: write() argument must be str, not list
>>> factors[0:100]
[1, [2], [3], [2, 2], [5], [2, 3], [7], [2, 2, 2], [3, 3], [2, 5], [11], [2, 2, 3], [13], [2, 7], [3, 5], [2, 2, 2, 2], [17], [2, 3, 3], [19], [2, 2, 5], [3, 7], [2, 11], [23], [2, 2, 2, 3], [5, 5], [2, 13], [3, 3, 3], [2, 2, 7], [29], [2, 3, 5], [31], [2, 2, 2, 2, 2], [3, 11], [2, 17], [5, 7], [2, 2, 3, 3], [37], [2, 19], [3, 13], [2, 2, 2, 5], [41], [2, 3, 7], [43], [2, 2, 11], [3, 3, 5], [2, 23], [47], [2, 2, 2, 2, 3], [7, 7], [2, 5, 5], [3, 17], [2, 2, 13], [53], [2, 3, 3, 3], [5, 11], [2, 2, 2, 7], [3, 19], [2, 29], [59], [2, 2, 3, 5], [61], [2, 31], [3, 3, 7], [2, 2, 2, 2, 2, 2], [5, 13], [2, 3, 11], [67], [2, 2, 17], [3, 23], [2, 5, 7], [71], [2, 2, 2, 3, 3], [73], [2, 37], [3, 5, 5], [2, 2, 19], [7, 11], [2, 3, 13], [79], [2, 2, 2, 2, 5], [3, 3, 3, 3], [2, 41], [83], [2, 2, 3, 7], [5, 17], [2, 43], [3, 29], [2, 2, 2, 11], [89], [2, 3, 3, 5], [7, 13], [2, 2, 23], [3, 31], [2, 47], [5, 19], [2, 2, 2, 2, 2, 3], [97], [2, 7, 7], [3, 3, 11], [2, 2, 5, 5]]
>>> str(factors[0:100])
'[1, [2], [3], [2, 2], [5], [2, 3], [7], [2, 2, 2], [3, 3], [2, 5], [11], [2, 2, 3], [13], [2, 7], [3, 5], [2, 2, 2, 2], [17], [2, 3, 3], [19], [2, 2, 5], [3, 7], [2, 11], [23], [2, 2, 2, 3], [5, 5], [2, 13], [3, 3, 3], [2, 2, 7], [29], [2, 3, 5], [31], [2, 2, 2, 2, 2], [3, 11], [2, 17], [5, 7], [2, 2, 3, 3], [37], [2, 19], [3, 13], [2, 2, 2, 5], [41], [2, 3, 7], [43], [2, 2, 11], [3, 3, 5], [2, 23], [47], [2, 2, 2, 2, 3], [7, 7], [2, 5, 5], [3, 17], [2, 2, 13], [53], [2, 3, 3, 3], [5, 11], [2, 2, 2, 7], [3, 19], [2, 29], [59], [2, 2, 3, 5], [61], [2, 31], [3, 3, 7], [2, 2, 2, 2, 2, 2], [5, 13], [2, 3, 11], [67], [2, 2, 17], [3, 23], [2, 5, 7], [71], [2, 2, 2, 3, 3], [73], [2, 37], [3, 5, 5], [2, 2, 19], [7, 11], [2, 3, 13], [79], [2, 2, 2, 2, 5], [3, 3, 3, 3], [2, 41], [83], [2, 2, 3, 7], [5, 17], [2, 43], [3, 29], [2, 2, 2, 11], [89], [2, 3, 3, 5], [7, 13], [2, 2, 23], [3, 31], [2, 47], [5, 19], [2, 2, 2, 2, 2, 3], [97], [2, 7, 7], [3, 3, 11], [2, 2, 5, 5]]'
>>> file.write(str(factors))
16822472
>>> file.close
<built-in method close of _io.TextIOWrapper object at 0x0334C370>
>>> file.close()
>>> 2 in [1,2,4]
True
>>> total = 0
>>> i = 0
>>> for i in range(0,len(factors)):
	for possible in factors[0:i]:
		good = True
		for fact in factors[i]:
			if fact in possible:
				good = False
				break
		if good:
			total +=1
	if i % 10000 == 0:
		print(i)
		print(total)