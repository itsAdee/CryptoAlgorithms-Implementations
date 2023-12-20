#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;

string getEncryption(string keyword, int keyLength) {
    char duplicates[26];
    int pointer = 0;

    for (int i = 0; i < keyLength; i++) {
        int count = 1;
        for (int j = i + 1 ; j < keyLength; j++) {
            if (keyword[i] == keyword[j]) {
                count++;
            }
        }
        if (count > 1) {
            duplicates[pointer] = keyword[i];
            pointer++;
        }
    }

    for (int i = 0; i < pointer; i++) {
        for (int j = 0; j < keyLength; j++) {
            if (duplicates[i] == keyword[j]) {
                keyword.erase(j, 1);
                keyLength--;
            }
        }
    }

    string encrption = keyword;
    for (int i = 90; i >= 65; i--) {
        bool flag = true;
        for (int j = 0; j < keyLength; j++) {
            if (char(i) == keyword[j]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            encrption += char(i);
        }
    }

    return encrption;
}

string conversion(string from, string to, string text) {
    string ciphertext = "";
    for (int i = 0; i < text.length(); i++) {
        if (int(text[i]) >= 65 && int(text[i]) <= 90)
            ciphertext += to[from.find(text[i])];
        else
            ciphertext += text[i];
    }

    return ciphertext;
}

void toFile(string filename, string message) {
    ofstream MyFile(filename);
    MyFile << message;
    MyFile.close();
}

int main(int argc, char* argv[]) {
    string text = "";

    if (argc <= 1) {
        cout << "No file name entered. Exiting...";
        return -1;
    }
    ifstream infile(argv[1]); //open the file
    
    if (infile.is_open() && infile.good()) {
        string line = "";
        while (getline(infile, line)){
            text += line;
        }
    } else {
        cout << "Failed to open file..";
        return -1;
    }

    int choice = 1;
    do {
        cout << "1: Plaintext To Cipher\t2: Cipher To Plaintext\nEnter corressponding number: ";
        cin >> choice;
    } while (choice != 1 && choice != 2);
    
    cout << "Enter keyword: ";
    string keyword;
    cin >> keyword;

    int keyLength = keyword.length();
    int textLength = text.length();

    for (int x = 0; x < keyLength; x++)
        keyword[x] = toupper(keyword[x]);

    for (int x = 0; x < textLength; x++)
        text[x] = toupper(text[x]);

    string encrption = getEncryption(keyword, keyLength);

    if (choice == 1) {
        string cipherfile;
        cout << "Enter filename for Cipher Text: ";
        cin >> cipherfile;
        string ciphertext = conversion("ABCDEFGHIJKLMNOPQRSTUVWXYZ", encrption, text);
        toFile(cipherfile, ciphertext);
    } else {
        string plainfile;
        cout << "Enter filename for Plain Text: ";
        cin >> plainfile;
        string plaintext = conversion(encrption, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", text);
        toFile(plainfile, plaintext);
    }

    return 0;
}