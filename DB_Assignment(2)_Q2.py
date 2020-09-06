import random

file_output = open("output(Q2).txt","w")
file_F1 = open("F1(Q2).txt","w")
file_F2 = open("F2(Q2).txt","w")

F1 = []
F2 = []
Buffer = []
Disk_output = []
count = 0

temp = []
while True:
    k = random.randrange(1,int(n*10))
    
    if k not in temp:
        count += 1
        temp.append(k)
    else:
        continue
        
    if count == n:
        F1 = temp[0:int(n/2)]
        F2 = temp[int(n/2):n]
        F1.sort()
        F2.sort()
        
        for j in range(int(n/2)):
            file_F1.write(str(F1[j]))
            file_F1.write("\n")
            file_F2.write(str(F2[j]))
            file_F2.write("\n")
        count = 0
        break
    else:
        continue




file_F1.close()
file_F2.close()
file_output.close()