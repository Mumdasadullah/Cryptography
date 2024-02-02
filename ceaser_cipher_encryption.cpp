#include <iostream>
#include <bits/stdc++.h>
using namespace std;

string user_input()
{
    string plain_text;
    cout << "Enter Text : ";
    getline(cin, plain_text);
    // cout << plain_text << endl;
    int l = plain_text.length();
    int c = count(plain_text.begin(), plain_text.end(), ' ');
    remove(plain_text.begin(), plain_text.end(), ' ');
    plain_text.resize(l-c);
    // cout << plain_text << endl;
    return plain_text;
}

int user_key_input()
{
    int key;
    cout << "Enter Key Value : ";
    cin >> key;
    return key;
}

string encryption(string text)
{
    string cipher_text;
    int val;
    int count = 0;
    for(int i = 0; i < text.length(); i++)
    {
        val = (int(text[i]) + 3) % 126;
        if(val > 90)
        {
            val = 65 + count;
            count++;
        }
        cipher_text += char(val);
    }
    
    return cipher_text;
}

int main() {
    
    string input = user_input();
    int shift_key = user_key_input();
    string output = encryption(input);
    
    cout << "Shift Key value is : " << shift_key << endl;
    cout << "Plain Text : " << input << endl;
    cout << "Cipher Text : " << output << endl;
    
    return 0;
}
