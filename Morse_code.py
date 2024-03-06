def userInput():
    plain_text = str(input("Enter Plain Text : "))
    plain_text = plain_text.split(" ")
    plain_text = "".join(plain_text)
    return plain_text
    
def morseCodeTable():
    table = {'A': '.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'
    }
    return table
    
def encryption(text, table):
    res = ""
    for i in text:
        for j in table:
            if i == j:
                res += table[j] + " "
    
    return res
    
def decryption(text, table):
    res = ""
    for i in text:
        for j in table:
            if i == table[j]:
                res += j
    
    return res
if __name__ == '__main__':
    tab = morseCodeTable()
    n = int(input("Encryption(1) or Decryption(2) : "))
    if n == 1:
        text = userInput()
        output = encryption(text.upper(),tab)
    else:
        text = str(input("Enter Morse Code with gap : "))
        # print(text)
        output = decryption(text.split(" "),tab)
    print(output)
