import sys
import random
from tabulate import tabulate

arr = [[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0]
]

#print the Array
def printArr():
    for rows in arr:
        print(rows)

# Randomize Bomb Placement
def randomBomb():
    i = 0
    while i < 10:
        bcol = random.randint(0,8)
        brow = random.randint(0,8)
        arr[bcol][brow] = 'X'
        i += 1

#check location for bomb
def checkArr():
    i=0
    while i<9:
        j=0
        while j <9:
            if arr[i][j] == 0:
                count = 0
                num_rows, num_cols = len(arr), len(arr[0])
                for x in range( (0 if i-1 < 0 else i-1), (num_rows if i+2 > num_rows else i+2), 1  ):
                    for y in range( (0 if j-1 < 0 else j-1), (num_cols if j+2 > num_cols else j+2), 1 ):
                        if arr[x][y] == "X":
                            count += 1
                arr[i][j] = count
            j += 1
        i += 1

def main():
    print(tabulate(arr)) 
    randomBomb()
    print("\n")
    print(tabulate(arr)) 
    checkArr()
    print("\n")
    print(tabulate(arr)) 
    
if __name__ == "__main__":
    main()
