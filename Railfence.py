# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def user_input():
    try:
        # plain_text = str(input("Enter Plain Text : "))
        plain_text = "defend the east wall"
        # key = int(input("Enter the Shift Key : "))
        key = 3
        input_length = len(plain_text)
        return plain_text,input_length,key
    except:
        print("Something went Wrong")

def tab(text_len, key):
    table = [['-' for i in range(text_len)] for j in range(key)]
    return table
    
def display_table(tabl):
    for i in range(3):
        for j in range(20):
            print(tabl[i][j], end=" ")
        print()

def encryption(table, text, length, key):
    i = 0
    j = 0
    while(i < length):
        if j == 3:
            j = 1
            table[j][i] = text[i]
            j = 0
            if i != length - 1:
                i+=1
            else:
                break
        table[j][i] = text[i]
        j+=1
        i+=1
    
    for i in range(3):
        for j in range(20):
            if table[i][j] == '-':
                continue
            print(table[i][j], end="")
    
if __name__ == '__main__':
    text,length,shift_key = user_input()
    # print(f"The text is {text} and it's length is {length} and shift key is {shift_key}")
    t = tab(length,shift_key)
    # print(t)
    encryption(t, text, length, shift_key)
