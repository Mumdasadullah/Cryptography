def userInput():
    plain_text = str(input("Enter Plain Text : "))
    plain_text = plain_text.split(" ")
    plain_text = "".join(plain_text)
    return plain_text
    
def morseCodeTable():
    table = {'A': '.-',
             'B':'-...',
             'C':'-.-.',
             'D':'-..',
             'E':'.',
             'F':'..-.',
             'G':'--.',
             'H':'....',
             'I':'..',
             'J':'.---',
             'K':'-.-',
             'L':'.-..',
             'M':'--',
             'N':'-.',
             'O':'---',
             'P':'.--.',
             'Q':'--.-',
             'R':'.-.',
             'S':'...',
             'T':'-',
             'U':'..-',
             'V':'...-',
             'W':'.--',
             'X':'-..-',
             'Y':'-.--',
             'Z':'--.',
             '0':'-----',
             '1':'.----',
             '2':'..---',
             '3':'...--',
             '4':'....-',
             '5':'.....',
             '6':'-....',
             '7':'--...',
             '8':'---..',
             '9':'----.'
    }
    return table
    
def result(text, table):
    res = ""
    for i in text:
        for j in table:
            if i == j:
                res += table[j]
    
    return res
if __name__ == '__main__':
    text = userInput()
    tab = morseCodeTable()
    output = result(text.upper(),tab)
    print(output)
