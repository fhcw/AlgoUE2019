#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <sstream>
#include <ctime>

using namespace std;

string Angabe;

void read_in() {
        ifstream input_file ("rmHV_10_12");
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        Angabe = buffer.str();
       
}


int main() {
    
    read_in();
    // groesse rausfinden
    string character = "-";
    int count_points = 0;
    int count_lines = 0;

    for (int i = 0; i < Angabe.length(); i++) {  // 45 = -

        if (Angabe[i] == 46) {
            count_points += 1;
        } 
        if (Angabe[i] == '\n') {
            count_lines += 1;
        }
        
    }
    cout << "points: " << count_points << " and lines: " << count_lines << endl;
    cout << Angabe.length() << endl;
    cout << Angabe << endl;
    /*
    // matrix1 und matrix2 definieren
    float i;
    float j;
    matrix1[][];

    char = 0;
    while (char != 46) {   // 46 = .
        continue;
        char++;
        if (char == 46) {
            matrix[0][0] = 
        }
    } */
}