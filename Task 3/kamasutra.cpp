#include <iostream>
#include <string>
#include <fstream>
using namespace std;

void writeToFile(string filename, string content)
{
    ofstream outFile;
    outFile.open(filename);
    if (outFile.is_open())
    {
        outFile << content;
        outFile.close();
    }
    else
    {
        cout << "Error: Unable to open file " << filename << " for writing." << endl;
    }
}

string createKey() {
    string alp = "";
    for (int i = 97; i <= 122; i++) {
        alp += char(i);
    }

    srand(time(0));
    string key = "";
    while (alp.length() > 0) {
        int index = rand() % alp.length();
        key += alp[index];
        alp.erase(index, 1);
    }

    return key;
}

string readFile(string filename) {
    string content = "";

    ifstream infile(filename); //open the file
    
    if (infile.is_open() && infile.good()) {
        string line = "";
        while (getline(infile, line)){
            content += line;
        }
    } 
    else {
        cout << "Error: File not found";
    }
    return content;
}

void convert(string inputfile, string outputfile, string keyfile) {
    string key = readFile(keyfile);
    char flippedPair;
    if (key.find('f')%2) flippedPair = key[key.find('f') - 1];
    else flippedPair = key[key.find('f') + 1];

    string input = readFile(inputfile);
    string output = "";
    for (int i = 0; i < input.length(); i++) {
        if (int(input[i]) >= 97 && int(input[i]) <= 122 && input[i]!='f' && input[i]!=flippedPair) {
            if (key.find(input[i])%2) {
                output += key[key.find(input[i]) - 1];
            }
            else {
                output += key[key.find(input[i]) + 1];
            }
        }
        else {
            output += input[i];
        }
    }
    writeToFile(outputfile, output);
}

int main(int argc, char *argv[])
{
    if (argc != 3 && argc != 5)
    {
        cout << "Error: Invalid number of arguments." << endl;
        cout << "Usage: kamasutra -e/-d/-k keyfile.txt plaintext.txt ciphertext.txt" << endl;
        return 1;
    }

    string operation = argv[1];
    if (operation != "-e" && operation != "-d" && operation != "-k")
    {
        cout << "Error: Invalid operation." << endl;
        return 1;
    }

    string keyfile = argv[2];

    if (operation == "-k")
    {
        string key = "";
        key = createKey();
        writeToFile(keyfile, key);
    }

    string input, output;
    if (operation == "-e" || operation == "-d")
    {
        input = argv[3];
        output = argv[4];
        convert(input, output, keyfile);
    }

    cout << "Operation Complete!" << endl;

    return 0;
}
