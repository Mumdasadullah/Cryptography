// Online C++ compiler to run C++ program online
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string user_plain_text_input()
{
    string plain_text;
    cout << "Enter Plain Text : ";
    getline(cin,plain_text);
    int l = plain_text.length();
    int c = count(plain_text.begin(), plain_text.end(), ' ');
    remove(plain_text.begin(), plain_text.end(), ' ');
    plain_text.resize(l-c);
    return plain_text;
}

string user_keyword_input()
{
    string keyword;
    cout << "Enter Keyword : ";
    cin >> keyword;
    return keyword;
}

string encryption(string input, string key, char tab[][26])
{
    char arr[2][input.length()];
    int j = 0;
    int row, col;
    string cipher_text;
    
    for(int i=0; i<input.length(); i++)
    {
        arr[0][i] = input[i];
        arr[1][i] = key[j];
        j++;
        if(j == key.length())
        {
            j = 0;
        }
        row = int(arr[0][i]) - 65;
        col = int(arr[1][i]) - 65;
        cipher_text += tab[col][row];
    }
    return cipher_text;
}

string decryption(string input, string key, char tab[][26])
{
    char arr[2][input.length()];
    int j = 0;
    int row, col;
    string cipher_text;
    
    for(int i=0; i<input.length(); i++)
    {
        arr[0][i] = input[i];
        arr[1][i] = key[j];
        j++;
        if(j == key.length())
        {
            j = 0;
        }
        row = int(arr[1][i]) - 65;
        for(int j=0; j<26; j++)
        {
            if(tab[row][j] == arr[0][i])
            {
                col = j;
                cipher_text += tab[0][col];
                break;
            }
        }
    }
    return cipher_text;
}

int main() {
    // Write C++ code here
    cout << "Hello world!" << endl;
    int n;
    string output;
    char table[26][26];
    for(int i=0; i<26; i++)
    {
        for(int j=0; j<26; j++)
        {
            table[i][j] = char(65 + j + i);
            if((65 + j + i) >= 91 )
            {
                table[i][j] = char(65 + j + i - 26);
            }
        }
    }
    
    string text = user_plain_text_input();
    string shift_key = user_keyword_input();
    
    cout << "Encryption(1) or Decryption(2) : ";
    cin >> n;
    if(n == 1)
    {
        output = encryption(text,shift_key,table);
    }
    else
    {
        output = decryption(text,shift_key,table);
    }
    cout << endl;
    cout << "Output is : " << output << endl;
    cout << endl;
    cout << "Table is : " << endl;
    for(int i=0; i<26; i++)
    {
        for(int j=0; j<26; j++)
        {
            cout << table[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
