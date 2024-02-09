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
    char arr[2][input.length()];
    int num[3][input.length()];
    int j = 0;
    string cipher_text;
    
    
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
    
    for(int i=0; i<input.length(); i++)
    {
        arr[0][i] = input[i];
        arr[1][i] = key[j];
        j++;
        if(j == 6)
        {
            j = 0;
        }
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
    string output = encryption(text,shift_key);
    cout << endl;\
    cout << "Cipher Text is : " << output << endl;
    
    return 0;
}
