import time
def costPuzzle(Puzzle):
    cost=0
    for i in range(0,4):
        for j in range(0,4):
            if(Puzzle[i][j]!=16):
                if(i*4+j!=15):
                    if(Puzzle[i][j]!=i*4+j+1):
                        cost= cost + 1
                else:
                    if(Puzzle[i][j]!=16):
                        cost= cost + 1
    return cost
def kurangPuzzle(Puzzle):
    kurang=0
    x=0
    print("\nPERHITUNGAN NILAI KURANG: ")
    for idx in range(16):
        for i in range(0,4):
            for j in range(0,4):
                if(Puzzle[i][j]==idx+1):            
                    kurangi=0
                    print("-----------------")
                    print("Indeks ke-",idx+1)
                    for k in range(i,4):
                        for l in range(4):
                            if(k*4+l+1>i*4+j+1 and Puzzle[k][l]<idx+1):
                                kurangi= kurangi + 1
                    print("kurang(",idx+1, ") = ",kurangi)
                    kurang= kurang + kurangi
                    print("-----------------")
                    break;
    print("Nilai kurang total = ",kurang)
    print("Nilai X = ", end='')
    for i in range(0,4):
        for j in range(0,4):
            if(Puzzle[i][j]==16):
                if(i%2==0):
                    if(j%2==1):
                        x=1
                elif(i%2==1):
                    if(j%2==0):
                        x=1
                break;
    print(x)
    print("Nilai Total = ",kurang+x)
    if((kurang+x) % 2 ==1):
        print("Persoalan TIDAK DAPAT diselesaikan")
        return False
    else:
        print("Persoalan DAPAT diselesaikan")
        return True
def printPuzzle(Puzzle):
    print("----------------------------------------")
    for i in range(0,4):
        for j in range(0,4):
            if(Puzzle[i][j]!=16):
                if(Puzzle[i][j]<10):
                    print("  ",Puzzle[i][j],end='')
                else:
                    print(" ",Puzzle[i][j],end='')
            else:
                print("    ",end='')
        print()
    print("----------------------------------------")
def assignPuzzle(Puzzle,newPuzzle):
    for i in range(4):
        for j in range(4):
            newPuzzle[i][j]=Puzzle[i][j]
def checkHistory(History,Puzzle):
    if Puzzle in History:
        False
    else:
        True
def popQueue(Queue,CostQueue,TempPuzzle):
    costMin = 10000000000000000000000000000000000000000000
    idx=0
    for i in range(len(CostQueue)):
        if(costMin>CostQueue[i]):
            costMin=CostQueue[i]
            idx=i
    assignPuzzle(Queue[idx],TempPuzzle)
    del CostQueue[idx]
    del Queue[idx]
if(__name__== "__main__"):
    Puzzle=[[0 for i in range(4)] for i in range(4)]
    namefile=input("Masukkan nama file: ")
    with open(namefile) as f:
        lines = f.read().split("\n")
        content=[]
        for line in lines:
            content.append(line.split(" "))
        for i in range(4):
            for j in range(4):
                if(content[i][j]==''):
                    Puzzle[i][j]=16
                else:
                    Puzzle[i][j] = int(content[i][j])
    print("PUZZLE AWAL:")
    printPuzzle(Puzzle)
    level=1
    tempPuzzle=[[0 for i in range(4)] for i in range(4)]
    assignPuzzle(Puzzle,tempPuzzle)
    countSimpul=0
    if(kurangPuzzle(Puzzle)):
        print("\nPATH MENUJU SOLUSI:")
        upPuzzle=[[0 for i in range(4)] for i in range(4)]
        downPuzzle=[[0 for i in range(4)] for i in range(4)]
        leftPuzzle=[[0 for i in range(4)] for i in range(4)]
        rightPuzzle=[[0 for i in range(4)] for i in range(4)]
        mulai = 0
        history=[]
        history.append(Puzzle)
        queue=[]
        queue.append(Puzzle)
        costQueue=[]
        mulai= mulai + time.time_ns()
        while(costPuzzle(tempPuzzle)!=0 and len(queue)!=0):
            del queue[0]
            assignPuzzle(tempPuzzle,upPuzzle)
            assignPuzzle(tempPuzzle,downPuzzle)
            assignPuzzle(tempPuzzle,leftPuzzle)
            assignPuzzle(tempPuzzle,rightPuzzle)
            for i in range(0,4):
                for j in range(0,4):
                    if(tempPuzzle[i][j]==16):
                        #cek down
                        if(i-1>=0):
                            downPuzzle[i][j]=downPuzzle[i-1][j]
                            downPuzzle[i-1][j]=16
                            if(checkHistory(history,downPuzzle)):
                                countSimpul = countSimpul + 1
                                history.append(downPuzzle)
                                queue.insert(0,downPuzzle)
                                cost=costPuzzle(downPuzzle)+level
                                costQueue.insert(0,cost)
                        #cek up
                        if(i+1<4):
                            upPuzzle[i][j]=upPuzzle[i+1][j]
                            upPuzzle[i+1][j]=16
                            if(checkHistory(history,upPuzzle)):
                                countSimpul = countSimpul + 1
                                history.append(upPuzzle)
                                queue.insert(0,upPuzzle)
                                cost=costPuzzle(upPuzzle)+level
                                costQueue.insert(0,cost)
                        #cek left
                        if(j+1<4):
                            leftPuzzle[i][j]=leftPuzzle[i][j+1]
                            leftPuzzle[i][j+1]=16
                            if(checkHistory(history,leftPuzzle)):
                                countSimpul = countSimpul + 1
                                history.append(leftPuzzle)
                                queue.insert(0,leftPuzzle)
                                cost=costPuzzle(leftPuzzle)+level
                                costQueue.insert(0,cost)
                        #cek right
                        if(j-1>=0):
                            rightPuzzle[i][j]=rightPuzzle[i][j-1]
                            rightPuzzle[i][j-1]=16
                            if(checkHistory(history,rightPuzzle)):
                                countSimpul = countSimpul + 1
                                history.append(rightPuzzle)
                                queue.insert(0,rightPuzzle)
                                cost=costPuzzle(rightPuzzle)+level
                                costQueue.insert(0,cost)
                        break;
            level= level + 1
            popQueue(queue,costQueue,tempPuzzle)
            queue.insert(0,tempPuzzle)
            printPuzzle(tempPuzzle)
        mulai= time.time_ns() - mulai
        print("Jumlah simpul yang dibangkitkan adalah ", countSimpul)
        print("Waktu program untuk menjalankan proses: ", mulai ," nanoseconds")