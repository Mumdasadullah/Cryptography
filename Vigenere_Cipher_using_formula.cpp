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
        j++;
    }
    
    for(int m=0; m<input.length(); m++)
    {
        cipher_text += char((((int(arr[0][m])%26) + (int(arr[1][m])%26))%26) + 65);
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
