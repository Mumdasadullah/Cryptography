# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def user_input():
    # plain_text = str(input("Enter Plain Text : "))
    plain_text = "e--kefGsGsrekoe"
    # key = str(input("Enter Key : "))
    key = "HACK"
    return plain_text,key
    
def display(table, key):
    print(len(table))
    for i in range(len(table)):
        for j in range(len(key)):
            print(table[i][j], end=" ")
        print()
    
def create_table_enc(text, key):
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
    
def create_table_dec(text, key):
    order = []
    o = 1
    c = 2
    row = int(round(len(text)/len(key)))
    table = [['_' for i in range(row)] for j in range(len(key)+2)]
    # print(table)
    for i in range(len(key)):
        table[0][i] = key[i]
        for j in range(65, 90):
            if key[i] == chr(j):
                table[1][i] = j
    for i in range(len(key)):
        ind = table[1].index(min(table[1]))
        order.append(ind)
        table[1][ind] = 1000
    for i in range(len(key)):
        table[1][order[i]] = o
        o+=1
    i = 0
    for k in range(1,5):
        ind = table[1].index(k)
        for j in range(2,len(table)):
            if i == len(text) or text[i] == ' ':
                table[j][ind] = '-'
                continue
            table[j][ind] = text[i]
            i+=1
    return table
    # print(table)
    # res = []
    # order = []
    # o = 1
    # for i in range(len(key)):
    #     res.append(key[i])
    # table.append(res)
    # res = []
    # for i in table[0]:
    #     for j in range(65,90):
    #         if i == chr(j):
    #             res.append(j)
    # for i in range(len(table[0])):
    #     ind = res.index(min(res))
    #     order.append(ind)
    #     res[ind] = 1000
    # table.append(res)
    # res = []
    # for i in range(len(table[0])):
    #     table[1][order[i]] = o
    #     o+=1
    
    # # for i in range(len(text)):
    # #     if i != 0:
    # #         if i % len(key) == 0:
    # #             table.append(res)
    # #             res = []
    # #     if text[i] == ' ':
    # #         res.append('-')
    # #     else:
    # #         res.append(text[i])
    # # if len(res) != len(key):
    # #     for i in range (len(res),len(key)):
    # #         res.append('-')
    # table.append(res)
    # # print(table)
    # # display(table, key)
    # return table
    
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
    
def decryption(table):
    plain_text = ""
    for i in range(2,len(table)):
        for j in range(len(table[0])):
            if table[i][j] == '-':
                plain_text += " "
                continue
            plain_text += table[i][j]
    print(plain_text)
    
    
if __name__ == "__main__":
    text,shift_key = user_input()
    print(f'the text is {text} and shift key is {shift_key}')
    tab = create_table_dec(text, shift_key)
    # encryption(tab)
    decryption(tab)
