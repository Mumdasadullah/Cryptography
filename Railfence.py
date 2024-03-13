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
    table = [['-']*text_len]*key
    return table
    
def display_table(tabl):
    for i in range(20):
        for j in range(3):
            print(tabl[i][j], end=" ")
        print()

def encryption(table, text, length, key):
    i = 0
    j = 0
    while(i < length):
        while(j < key):
            print(f"j < key loop running and i is {i} nad j is {j}")
            table[j][i] = text[i]
            j+=1
            i+=1
        # print(j)
        j-=2
        while(j > -1):
            print(f"j > 0 loop running and i is {i} nad j is {j}")
            table[j][i] = text[i]
            j-=1
            i+=1
        j+=2
        # print(f"j is {j}")
        # i+=1
    # display_table(table)
    print(table)
    
if __name__ == '__main__':
    text,length,shift_key = user_input()
    # print(f"The text is {text} and it's length is {length} and shift key is {shift_key}")
    t = tab(length,shift_key)
    # print(t)
    encryption(t, text, length, shift_key)
