def user_input():
    text = str(input("Enter Plain Text : "))
    keys = str(input("Enter Key : "))
    text = text.replace(" ","")
    return text,keys

def pair_text(text):
    pair = []
    p = []
    for i in range (0, len(text) , 2):
        p.append(text[i])
        if i < len(text)-1:
            if text[i] == text[i+1]:
                p.append('x')
            else:
                p.append(text[i+1])
        else:
            p.append('Z')
        pair.append(p)
        p = []
    
    return pair

def table(key):
    tab = []
    val = []
    lst = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(key)):
        if key[i] in lst:
            for j in range (len(lst)):
                if lst[j] == key[i]:
                    break
            lst.pop(j)
        if i==5:
            tab.append(val)
            val = []
        val.append(key[i])
    if len(val) > 0 and len(val) < 5:
        for i in lst:
            val.append(i)
            if (len(val) == 5):
                tab.append(val)
                val = []
    return tab

def display_table(tabl):
    for i in range(5):
        for j in range(5):
            print(tabl[i][j], end=" ")
        print()

def rule(pr, matrix):
    res = []
    v = []
    # display_table(matrix)
    for i, row in enumerate(matrix):
        if pr[0] in row:
            v.append(i)
            v.append(row.index(pr[0]))
            break
    res.append(v)
    v = []
    for i, row in enumerate(matrix):
        if pr[1] in row:
            v.append(i)
            v.append(row.index(pr[1]))
            break
    res.append(v)
    return res
    
def encryption(pr, matrix):
    tt = []
    ttt = []
    for i in pr:
        l = rule(i, matrix)
        ttt.append(rule(i, matrix))
        l1,l2 = l[0], l[1]
        if l1[0] == l2[0]:
            if l1[1] != 4 and l2[1] != 4:
                tt.append(matrix[l1[0]][l1[1]+1])
                tt.append(matrix[l2[0]][l2[1]+1])
            elif l1[1] == 4 and l2[1] != 4:
                tt.append(matrix[l1[0]][0])
                tt.append(matrix[l2[0]][l2[1]+1])
            elif l2[1] == 4 and l1[1] != 4:
                tt.append(matrix[l1[0]][l1[1]+1])
                tt.append(matrix[l2[0]][0])
            else:
                tt.append(matrix[l1[0]][0])
                tt.append(matrix[l2[0]][0])
        elif l1[1] == l2[1]:
            if l1[0] != 4 and l2[0] != 4:
                tt.append(matrix[l1[0]+1][l1[1]])
                tt.append(matrix[l2[0]+1][l2[1]])
            elif l1[0] == 4 and l2[0] != 4:
                tt.append(matrix[0][l1[1]])
                tt.append(matrix[l2[0]+1][l2[1]])
            elif l1[0] != 4 and l2[0] == 4:
                tt.append(matrix[l1[0]+1][l1[1]])
                tt.append(matrix[0][l2[1]])
            else:
                tt.append(matrix[0][l1[1]])
                tt.append(matrix[0][l2[1]])
        else:
            tt.append(matrix[l1[0]][l2[1]])
            tt.append(matrix[l2[0]][l1[1]])
    
    return tt

def decryption(pr, matrix):
    tt = []
    ttt = []
    for i in pr:
        l = rule(i, matrix)
        ttt.append(rule(i, matrix))
        l1,l2 = l[0], l[1]
        if l1[0] == l2[0]:
            if l1[1] != 4 and l2[1] != 4:
                tt.append(matrix[l1[0]][l1[1]-1])
                tt.append(matrix[l2[0]][l2[1]-1])
            elif l1[1] == 4 and l2[1] != 4:
                tt.append(matrix[l1[0]][l1[1]-1])
                tt.append(matrix[l2[0]][l2[1]-1])
            elif l2[1] == 4 and l1[1] != 4:
                tt.append(matrix[l1[0]][l1[1]-1])
                tt.append(matrix[l2[0]][0])
            else:
                tt.append(matrix[l1[0]][0])
                tt.append(matrix[l2[0]][0])
        elif l1[1] == l2[1]:
            if l1[0] != 4 and l2[0] != 4:
                tt.append(matrix[l1[0]-1][l1[1]])
                tt.append(matrix[l2[0]-1][l2[1]])
            elif l1[0] == 4 and l2[0] != 4:
                tt.append(matrix[0][l1[1]])
                tt.append(matrix[l2[0]-1][l2[1]])
            elif l1[0] != 4 and l2[0] == 4:
                tt.append(matrix[l1[0]-1][l1[1]])
                tt.append(matrix[0][l2[1]])
            else:
                tt.append(matrix[0][l1[1]])
                tt.append(matrix[0][l2[1]])
        else:
            tt.append(matrix[l1[0]][l2[1]])
            tt.append(matrix[l2[0]][l1[1]])
    
    return tt
    
def result(tt):
    for i in range (len(tt)):
        print(tt[i], end="")
    print()

if __name__ == '__main__':
    plain_text,key = user_input()
    # key = str(input("Enter Key : "))
    mat = table(key)
    plain_pair = pair_text(plain_text)
    display_table(mat)
    # output = encryption(plain_pair, mat)
    n = int(input("Encryption (1) or Decryption (2) : "))
    if n == 1:
        output = encryption(plain_pair, mat)
    else:
        output = decryption(plain_pair, mat)
    print("The Output Text is : ", end=" ")
    result(output)
    # print(mat)
