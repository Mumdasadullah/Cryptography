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

string user_keyword_input(string input)
{
    string keyword;
    // srand((unsigned) time(NULL));
    for(int i=0; i<input.length(); i++)
    {
        keyword += char(65+(rand()%20));
    }
    return keyword;
}

string encryption(string input, string key, char alpha[])
{
    string cipher_text;
    int arr[3][input.length()];
    for(int i=0; i<input.length(); i++)
    {
        for(int j=0; j<26; j++)
        {
            if(input[i] == alpha[j])
            {
                arr[0][i] = j;
                if(input[i] == key[i])
                {
                    arr[1][i] = j;
                }
            }
            else if(key[i] == alpha[j])
            {
                arr[1][i] = j;
            }
        }
        arr[2][i] = arr[0][i] ^ arr[1][i];
        if(arr[2][i] >= 26)
        {
            arr[2][i] = arr[2][i] - 26;
        }
        cipher_text += alpha[arr[2][i]];
    }
    
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<input.length(); j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    
    return cipher_text;
}

int main() {
    // Write C++ code here
    string output;
    string text = user_plain_text_input();
    string shift_key = user_keyword_input(text);
    cout << "The Random Generated Key is : " << shift_key << endl;
    
    char alpha[26];
    for(int j=0; j<26; j++)
    {
        alpha[j] = char(j+65);
        cout << alpha[j] << " ";
    }
    cout << endl ;
    for(int i=0; i<2; i++)
    {
        for(int j=0; j<text.length(); j++)
        {
            if(i==0)
                cout << text[j] << " ";
            else
                cout << shift_key[j] << " ";
        }
        cout << endl;
    }
    
    output = encryption(text, shift_key, alpha);
    cout << "Cipher Text is : " << output << endl;
    return 0;
}
