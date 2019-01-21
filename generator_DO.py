import random
import os

nrDO = []
while len(nrDO) < 3:
    nrDO.append(chr(random.randint(65, 90)))
while len(nrDO) < 9:
    nrDO.append(random.randint(0, 9))

chcksum = (ord(nrDO[0])-55) * 7 + (ord(nrDO[1])-55) * 3 + (ord(nrDO[2])-55) + nrDO[4] * 7 + nrDO[5] * 3 + nrDO[6] + \
          nrDO[7] * 7 + nrDO[8] * 3

nrDO[3] = chcksum % 10

chcksum = (ord(nrDO[0])-55) * 7 + (ord(nrDO[1])-55) * 3 + (ord(nrDO[2])-55) + nrDO[3] * 9 + nrDO[4] * 7 + nrDO[5] * 3 \
          + nrDO[6] + nrDO[7] * 7 + nrDO[8] * 3

nrDO = ''.join(map(str, nrDO))
print("Wygenerowany numer Dowodu Osobistego to (numer został skopiowany do schowka): \n{}".format(nrDO))
os.system("echo '%s' | clip" % nrDO)
