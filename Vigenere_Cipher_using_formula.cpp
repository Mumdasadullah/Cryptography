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

string encryption(string input, string key)
{
    char alpha[2][26];
    
    
    for(int i=0; i<2; i++)
    {
        for(int j=0; j<26; j++)
        {
            if(i == 0)
                alpha[i][j] = char(j+97);
            else
                alpha[i][j] = char(j+65);
        }
    }
    
    char arr[2][input.length()];
    int j = 0;
    string cipher_text;
    for(int i=0; i<input.length(); i++)
    {
        arr[0][i] = input[i];
        if(key[j] == key[key.length()-1])
        {
            arr[1][i] = key[j];
            j = 0;
            continue;
        }
        arr[1][i] = key[j];
        // cipher_text += char((((int(arr[0][i])%26) + (int(arr[1][i])%26))%26) + 65);
        j++;
    }
    
    int num[3][input.length()];
    for(int i=0; i<input.length(); i++)
    {
        for(int j=0;j<26; j++)
        {
            if(arr[0][i] == alpha[1][j])
            {
                if(arr[0][i] == arr[1][i])
                    num[1][i] = j;
                num[0][i] = j;
            }
            else if(arr[1][i] == alpha[1][j])
            {
                num[1][i] = j;
            }
        }
        num[2][i] = (num[0][i] + num[1][i]) % 26;
        cipher_text += alpha[1][num[2][i]];
    }
    return cipher_text;
}

int main() {
    // Write C++ code here
    string text = user_plain_text_input();
    string shift_key = user_keyword_input();
    // encryption(text,shift_key);
    string output = encryption(text,shift_key);
    cout << endl;\
    cout << "Cipher Text is : " << output << endl;
    
    return 0;
}
