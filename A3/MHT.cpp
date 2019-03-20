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
    int number_values_matrix1 = 0;
    int number_rows_matrix1 = 0;
    
    for (int i = 0; i < Angabe.length(); i++) {  // 45 = -

        if (Angabe[i] == 46) {
            number_values_matrix1 += 1;
        } 
        if (Angabe[i] == '\n') {
            number_rows_matrix1 += 1;
        }
        if (Angabe[i] == '-') {
            break;
        }
    }
    number_rows_matrix1 -= 1;
    int number_columns_matrix1 = number_values_matrix1 / number_rows_matrix1;

    cout << "values: " << number_values_matrix1 << " and rows: " << number_rows_matrix1 << " and columns: " << number_columns_matrix1 << endl;
    cout << Angabe << endl;

    int number_values_matrix2 = number_values_matrix1;
    int number_rows_matrix2 = number_rows_matrix1 + 1;
    int number_columns_matrix2 = number_columns_matrix1 - 1;

    cout << "values: " << number_values_matrix2 << " and rows: " << number_rows_matrix2 << " and columns: " << number_columns_matrix2 << endl;    
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