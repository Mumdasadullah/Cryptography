# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def user_input():
    # plain_text = str(input("Enter Plain Text : "))
    plain_text = "Geeks for Geeks"
    # key = str(input("Enter Key : "))
    key = "HACK"
    return plain_text,key
    
def display(table, key):
    print(len(table))
    for i in range(len(table)):
        for j in range(len(key)):
            print(table[i][j], end=" ")
        print()
    
def create_table(text, key):
    table = []
    res = []
    order = []
    o = 1
    for i in range(len(key)):
        res.append(key[i])
    table.append(res)
    res = []
    for i in table[0]:
        for j in range(65,90):
            if i == chr(j):
                res.append(j)
    for i in range(len(table[0])):
        ind = res.index(min(res))
        order.append(ind)
        res[ind] = 1000
    table.append(res)
    res = []
    for i in range(len(table[0])):
        table[1][order[i]] = o
        o+=1
    for i in range(len(text)):
        if i != 0:
            if i % len(key) == 0:
                table.append(res)
                res = []
        if text[i] == ' ':
            res.append('-')
        else:
            res.append(text[i])
    if len(res) != len(key):
        for i in range (len(res),len(key)):
            res.append('-')
    table.append(res)
    # print(table)
    # display(table, key)
    return table
    
def encryption(table):
    cipher_text = ""
    for i in range(1,5):
        ind = table[1].index(i)
        for j in range(2,len(table)):
            if table[j][ind] == '-':
                cipher_text += " "
                continue
            cipher_text += table[j][ind]
            
    print(cipher_text)
    
if __name__ == "__main__":
    text,shift_key = user_input()
    print(f'the text is {text} and shift key is {shift_key}')
    tab = create_table(text, shift_key)
    encryption(tab)
