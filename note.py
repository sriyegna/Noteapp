import ast

# add: (void) -> (void)
# Purpose: Add a note to the database
def add():
    with open("noteapp.txt", "r") as f:
        full_list = ast.literal_eval(f.read())
    print full_list
    inlist = checkfn(full_list)
    curnote = raw_input("Enter the note: ")
    if inlist[0] == True:
        full_list[inlist[2]].extend([curnote])
    else:
        full_list.append([inlist[1], curnote])
    strlist = str(full_list)
    with open("noteapp.txt", "w") as f:
        f.write(strlist)
    print full_list

# read: (void) -> (listof str)
# Purpose: Reads the notes of the person	
def read():
    with open("noteapp.txt", "r") as f:
        full_list = ast.literal_eval(f.read())
    inlist = checkfn(full_list)
    if inlist[0] == True:
        print full_list[inlist[2]][1:]
    else:
        callfn = raw_input("The name doesn't exist. Do you want to add it? (y,n)")
        if callfn == "y":
            add()
            
# checkfn: (listof str) -> (listof any)
# Purpose: Checks if a person is already in the database.            
def checkfn(full_list): 
    n = 0
    curname = raw_input("Enter a name: ")
    lenflist = len(full_list)
    checked = False
    while checked == False:
        if full_list[n][0] == curname:
            checked = True
            inlist = [True, curname, n]
        elif n == lenflist - 1:
            checked = True
            inlist = [False, curname, n]
        n = n + 1
    return inlist
    