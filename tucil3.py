import time
import copy
''' Tucil 3 Strategi Algoritma
    Nama    : Muchammad Ibnu Sidqi
    Nim     : 13518072
    Kelas   : K-3 
'''
''' Fungsi untuk menghitung fungsi g(x) dari suatu input Puzzle(Ubin), 
    untuk f(x) didapatkan dari level simpul diluar fungsi 
'''
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
''' Fungsi untuk menghitung apakah suatu 15-Puzzle Solved atau Unsolved 
    dengan menghitung nilai kurang pada masing masing indeks serta faktor X. 
    Fungsi akan mengembalikkan true jika persoalan dapat diselesaikan 
'''
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
''' Prosedur untuk menampilkan ke layar 15-Puzzle 
''' 
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
''' Fungsi untuk mengambil simpul dari Queue yang memiliki cost terkecil. 
    Mengembalikkan simpul dari antrian Queue yang memiliki nilai terkecil. 
'''
def popQueue(Queue,CostQueue,levelQueue):
    costMin = 10000000000000000000000000000000000000000000
    idx=0
    for i in range(len(CostQueue)):
        if(costMin>CostQueue[i]):
            costMin=CostQueue[i]
            idx=i
    return idx
''' MAIN PROGRAM
'''
if(__name__== "__main__"):
    # Inisiasi Puzzle Awal berupa matriks
    Puzzle=[[0 for i in range(4)] for i in range(4)]
    # inisiasi nama file masukkan 
    namefile=input("Masukkan nama file: ")
    # parsing masukkan file lalu masukkan kedalam Puzzle 
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
    # Print masukkan 15-Puzzle
    print("PUZZLE AWAL:")
    printPuzzle(Puzzle)
    # Inisiasi level dari simpul untuk menghitung nilai f(x) pada cost(c(x))
    level=1
    # Temporary Puzzle (digunakan sebagai pengganti solusi yang dipilih untuk setiap langkah)
    tempPuzzle=copy.deepcopy(Puzzle)
    # Jumlah simpul yang dibangkitkan
    countSimpul=0
    # Cek apakah Puzzle Solved 
    if(kurangPuzzle(Puzzle)):
        print("\nPATH MENUJU SOLUSI:")
        # Inisiasi variabel untuk menghitung waktu yang diperlukan
        mulai = 0
        # Variabel penampung Simpul-Simpul yang telah dibangkitkan
        history=[copy.deepcopy(Puzzle)]
        # Variabel antrian Queue untuk simpul yang akan dibangkitkan
        queue=[copy.deepcopy(Puzzle)]
        # Variabel penampung nilai Cost dari antrian Queue
        costQueue=[]
        # Variabel penampung nilai kedalaman simpul/level
        levelQueue=[]
        # Variabel penampung index dari antrian Queue yang diambil
        idx=0
        mulai= mulai + time.time_ns()
        # Jika g(x) bernilai nol hentikan pencarian solusi (urutan Puzzle sudah tepat)
        while(costPuzzle(tempPuzzle)!=0):
            # Hapus elemen simpul yang akan dibangkitkan
            del queue[0]
            # Puzzle yang dibangkitkan sesuai state yang mungkin
            upPuzzle=copy.deepcopy(tempPuzzle)
            downPuzzle=copy.deepcopy(tempPuzzle)
            leftPuzzle=copy.deepcopy(tempPuzzle)
            rightPuzzle=copy.deepcopy(tempPuzzle)
            for i in range(0,4):
                for j in range(0,4):
                    if(tempPuzzle[i][j]==16):
                        # Pengecekan state down
                        if(i-1>=0):
                            downPuzzle[i][j]=int(downPuzzle[i-1][j])
                            downPuzzle[i-1][j]=16
                            # Pengecekkan apakah simpul yang dibangkitkan sudah pernah dibangkitkan sebelumnya
                            if(downPuzzle not in history):
                                countSimpul = countSimpul + 1
                                history.insert(0,(downPuzzle))
                                queue.insert(0,(downPuzzle))
                                cost=costPuzzle(downPuzzle)+level
                                costQueue.insert(0,cost)
                                levelQueue.insert(0,level)
                        # Pengecekan state up
                        if(i+1<4):
                            upPuzzle[i][j]=int(upPuzzle[i+1][j])
                            upPuzzle[i+1][j]=16
                            # Pengecekkan apakah simpul yang dibangkitkan sudah pernah dibangkitkan sebelumnya
                            if(upPuzzle not in history):
                                countSimpul = countSimpul + 1
                                history.insert(0,(upPuzzle))
                                queue.insert(0,(upPuzzle))
                                cost=costPuzzle(upPuzzle)+level
                                costQueue.insert(0,cost)
                                levelQueue.insert(0,level)
                        # Pengecekan state left
                        if(j+1<4):
                            leftPuzzle[i][j]=int(leftPuzzle[i][j+1])
                            leftPuzzle[i][j+1]=16
                            # Pengecekkan apakah simpul yang dibangkitkan sudah pernah dibangkitkan sebelumnya
                            if(leftPuzzle not in history):
                                countSimpul = countSimpul + 1
                                history.insert(0,(leftPuzzle))
                                queue.insert(0,(leftPuzzle))
                                cost=costPuzzle(leftPuzzle)+level
                                costQueue.insert(0,cost)
                                levelQueue.insert(0,level)
                        # Pengecekan state righta
                        if(j-1>=0):
                            rightPuzzle[i][j]=int(rightPuzzle[i][j-1])
                            rightPuzzle[i][j-1]=16
                            # Pengecekkan apakah simpul yang dibangkitkan sudah pernah dibangkitkan sebelumnya
                            if(rightPuzzle not in history):
                                countSimpul = countSimpul + 1
                                history.insert(0,(rightPuzzle))
                                queue.insert(0,(rightPuzzle))
                                cost=costPuzzle(rightPuzzle)+level
                                costQueue.insert(0,cost)
                                levelQueue.insert(0,level)
                        break;
            idx = popQueue(queue,costQueue,levelQueue)
            level = levelQueue[idx] + 1
            tempPuzzle=copy.deepcopy(queue[idx])
            del costQueue[idx]
            del queue[idx]
            del levelQueue[idx]
            # Jika Antrian kosong hentikan pencarian solusi
            if(len(queue)==0):
                print("Program dihentikan akibat antrian sudah kosong")
                break;
            queue.insert(0,tempPuzzle)
            printPuzzle(tempPuzzle)
        mulai= time.time_ns() - mulai
        print("Jumlah simpul yang dibangkitkan adalah ", countSimpul)
        print("Waktu program untuk menjalankan proses: ", mulai ," nanoseconds")