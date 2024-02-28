def user_input():
    text = str(input("Enter Plain Text : "))
    keys = str(input("Enter Key : "))
    text = text.replace(" ","")
    return text,keys

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
    # for i in range (len(key)):
    #     if i==5:
    #         tab.append(val)
    #         val = []
    #     val.append(key[i])
    if len(val) > 0 and len(val) < 5:
        for i in lst:
            val.append(i)
            if (len(val) == 5):
                tab.append(val)
                val = []
    return tab

if __name__ == '__main__':
    plain_text,key = user_input()
    # key = str(input("Enter Key : "))
    mat = table(key)
    print(mat)
