def chess():
    print("Now start to playing chess")
    print("s means soilder, h meas horse, kg means king")
    print("Please don't try to get over to the map. There are still some bugs")
    print("And please don't walk to the cell where your other characters are. There are still some bugs,too.")
    a = ['rs1','rh1','rkg','rh2','rs2'],["   ","   ","   ","   ","   "],["   ","   ","   ","   ","   "],["   ","   ","   ","   ","   "],["bs1","bh1","bkg","bh2","bs2"]
    demonstrate(a)
    black=True
    while True:
        if black:
            print("Now it's Black's turn.")
        else:
            print("Now it's Red's turn.")
        b=input("What characters? You can type s1,s2,h1,h2,kg")
        if b!='s1' and b!='s2' and b!='h1' and b!='h2' and b!='kg':
            print("Sorry, the input is not valid.")
            continue
        if black:
            b="b"+b
        else:
            b="r"+b
        direct=input("Which ways you want to move ?,you can type up,down,left,right")
        if direct!='up'and direct!='down'and direct!='left'and direct!='right':
            print("Sorry, the input is not valid.")
            continue
        move(a,b,direct,black)
        demonstrate(a)
        result=check(a)
        black = not black
        if result:
            break
def move(field,character,direction,black):
    k=False
    for i in range(0,5):
        for j in range(0,5):
            if field[i][j]==character:
                c=i
                d=j
                k=True
    if not k:
        print("Your chrarcter is dead.Please pick another one.")
    if direction=='up':
        if field[c-1][d]=="   ":
            temp=field[c][d]
            field[c][d]=field[c-1][d]
            field[c-1][d]=temp
        else:
            print("%s was eliminated" % (field[c-1][d]))
            field[c-1][d]=field[c][d]
            field[c][d]="   "
    elif direction=='down':
        if field[c+1][d]=="   ":
            temp=field[c][d]
            field[c][d]=field[c+1][d]
            field[c+1][d]=temp
        else:
            print("%s was eliminated" % (field[c+1][d]))
            field[c+1][d]=field[c][d]
            field[c][d]="   "
    elif direction=='left':
        if field[c][d-1]=="   "
            temp=field[c][d]
            field[c][d]=field[c][d-1]
            field[c][d-1]=temp
        else:
            print("%s was eliminated" % (field[c][d-1]))
            field[c][d-1]=field[c][d]
            field[c][d]="   "
    elif direction=='right':
        if field[c][d+1]=="   ":
            temp=field[c][d]
            field[c][d]=field[c][d+1]
            field[c][d+1]=temp
        else:
            print("%s was eliminated" % (field[c][d+1]))
            field[c][d+1]=field[c][d]
            field[c][d]="   "
    return field
def check(field):       #check whether the kings are alive or not
    bkgIsAlive=False
    rkgIsAlive=False
    for i in range(0,5):
        for j in range(0,5):
            if field[i][j]=="rkg":
                rkgIsAlive=True
            if field[i][j]=="bkg":
                bkgIsAlive=True
    if not bkgIsAlive:
        print("Game over.")
        print("Red is the winner.")
        return True
    elif not rkgIsAlive:
        print("Game over.")
        print("Black is the winner.")
        return True
    else:
        print("Both of the kings are still alive.")
        print("Game will continue")
        return False
def demonstrate(field):
    print("--------------------")
    for i in range(0, 5):
        print("|",end="")
        for j in range(0, 5):
            print(field[i][j], end="|")
        print("\n--------------------")
chess()