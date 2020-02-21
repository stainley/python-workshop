#f = open('pg37431.txt')
#text = f.read()
#print(text)

#with open('pg37431.txt') as f:
#    print(f.readline())

from datetime import datetime
import time

f = open('log.txt', 'w+')

for i in range(0, 10):
    print(datetime.now().strftime('%Y%m%d_%H:%M:%S - '), i)
    f.write(datetime.now().strftime('%Y%m%d_%H:%M:%S - '));
    time.sleep(1)
    f.write(str(i))
    f.write("\n")
f.close()
