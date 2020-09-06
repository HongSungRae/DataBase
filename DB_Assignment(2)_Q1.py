import random

file_output = open("output.txt","w")
file_F1 = open("F1.txt","w")
file_F2 = open("F2.txt","w")

F1 = []
F2 = []
Buffer = []
Disk_output = []
count = 0

def bufferFunc():
    minimum = min(Buffer[0][0],Buffer[0][1],Buffer[1][0],Buffer[1][1])
    Buffer[2][0] = minimum
    if minimum in Buffer[0]:
        Buffer[0][Buffer[0].index(minimum)] = None
    elif minimum in Buffer[1]:
        Buffer[1][Buffer[1].index(minimum)] = None
    minimum = min(Buffer[j][k] for j in range(2) for k in range(2) if Buffer[j][k] != None)
    Buffer[2][1] = minimum
    if minimum in Buffer[0]:
        Buffer[0][Buffer[0].index(minimum)] = None
    elif minimum in Buffer[1]:
        Buffer[1][Buffer[1].index(minimum)] = None
    Disk_output.append(Buffer[2])


'''                                '''
###############STEP_1#################
## n = How many elements in F1 + F2?##
######################################
'''                                '''
n = 12  # !!! Caution !!! : Only even numbers are recommanded


'''                                '''
###############STEP_2#################
######## CREAT F1 and F1 list ########
######################################
'''                                '''
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

'''                                '''
###############STEP_3#################
## Sort F1 and F2 USING buffer logic##
######################################
'''                                '''
for i in range(3): # Creat 3 buffer pages
    Buffer.append([0,0])

while True:
    if count == 0:
        Buffer[0][0] = F1[0]
        Buffer[0][1] = F1[1]
        Buffer[1][0] = F2[0]
        Buffer[1][1] = F2[1]
        F1.remove(F1[0]); F1.remove(F1[0])
        F2.remove(F2[0]); F2.remove(F2[0])
        bufferFunc()
    else:
        temp = []
        for i in range(2):
            for j in range(2):
                if Buffer[i][j] != None:
                    temp.append(Buffer[i][j])
        temp.sort()
        Buffer[0][0] = None; Buffer[0][1] = None
        Buffer[1][0] = temp[0]; Buffer[1][1] = temp[1]
        
        if len(F1) == 0 and len(F2) == 0:
            Disk_output.append(Buffer[1])
        elif len(F1) == 0 and len(F2) != 0:
            Buffer[0][0] = F2[0]
            Buffer[0][1] = F2[1]
            F2.remove(F2[0]); F2.remove(F2[0])
            bufferFunc()
        elif len(F1) != 0 and len(F2) == 0:
            Buffer[0][0] = F1[0]
            Buffer[0][1] = F1[1]
            F1.remove(F1[0]); F1.remove(F1[0])
            bufferFunc()
        elif F1[0] < F2[0]:
            Buffer[0][0] = F1[0]
            Buffer[0][1] = F1[1]
            F1.remove(F1[0]); F1.remove(F1[0])
            bufferFunc()
        elif F2[0] < F1[0]:
            Buffer[0][0] = F2[0]
            Buffer[0][1] = F2[1]
            F2.remove(F2[0]); F2.remove(F2[0])
            bufferFunc()
            
       
    
    
    if count == 5:
        break
    else:
        Buffer.pop()
        Buffer.append([0,0])
        count += 1
        continue

for i in range(6):
    for j in range(2):
        file_output.write(str(Disk_output[i][j]))
        file_output.write("\n")

file_F1.close()
file_F2.close()
file_output.close()