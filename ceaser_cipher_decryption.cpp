#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string user_input()
{
    string cipher_text;
    cout << "Enter Text : ";
    getline(cin, cipher_text);
    // cout << plain_text << endl;
    int l = cipher_text.length();
    int c = count(cipher_text.begin(), cipher_text.end(), ' ');
    remove(cipher_text.begin(), cipher_text.end(), ' ');
    cipher_text.resize(l-c);
    // cout << plain_text << endl;
    return cipher_text;
}

int user_key_input()
{
    int key;
    cout << "Enter Key Value : ";
    cin >> key;
    return key;
}

string decryption(string text)
{
    string plain_text;
    int val;
    int count = 0;
    for(int i = 0; i < text.length(); i++)
    {
        val = (int(text[i])-3) % 126;
        if(val < 65)
        {
            val = 88 + count;
            count++;
        }
        plain_text += char(val);
    }
    
    return plain_text;
}

int main() {
    string input = user_input();
    int shift_key = user_key_input();
    string output = decryption(input);
    
    cout << "Shift Key value is : " << shift_key << endl;
    cout << "Cipher Text is : " << input << endl;
    cout << "Plain Text is : " << output << endl;

    return 0;
}
