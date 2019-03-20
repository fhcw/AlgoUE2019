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
    
    int number_values_matrix1 = 0;
    int number_rows_matrix1 = 0;
        
    for (int k = 0; k < Angabe.length(); k++) {  // 45 = -, 46 = .
        if (Angabe[k] == 46) {
            number_values_matrix1 += 1;
        } 
        if (Angabe[k] == '\n') {
            number_rows_matrix1 += 1;
        }
        if (Angabe[k] == '-') {
            break;
        }
    }
    number_rows_matrix1 -= 1;
    int number_columns_matrix1 = number_values_matrix1 / number_rows_matrix1;

    int number_values_matrix2 = number_values_matrix1;
    int number_rows_matrix2 = number_rows_matrix1 + 1;
    int number_columns_matrix2 = number_columns_matrix1 - 1;

    // matrix1 und matrix2 definieren {}  []

    float matrix1[number_rows_matrix1][number_columns_matrix1];
    float matrix2[number_rows_matrix2][number_columns_matrix2];
    // matrix 1
    
    for (int c = 0; c < 90; c++) {
        if (Angabe[c] == '.') {
            int temporary = Angabe[c-1] + Angabe[c] + Angabe[c+1] + Angabe[c+2];
            cout << temporary << endl;
        }
    }
}