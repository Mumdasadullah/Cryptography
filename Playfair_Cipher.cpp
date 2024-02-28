def table(key):
    lst = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P',
            'Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(key)):
        if key[i] in lst:
            for j in range (len(lst)):
                if lst[j] == key[i]:
                    break
            lst.pop(j)
    tab = []
    val = []
    for i in range (len(key)):
        if i==5:
            tab.append(val)
            val = []
        val.append(key[i])
    # k = len(val)
    if len(val) > 0 and len(val) < 5:
        for i in lst:
            val.append(i)
            if (len(val) == 5):
                tab.append(val)
                val = []
    # tab.append(val)
    print(tab)

if __name__ == '__main__':
    key = str(input("Enter Key : "))
    table(key)
