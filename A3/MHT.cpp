#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <sstream>
#include <ctime>
#include <typeinfo>

using namespace std;

string read_in(string filename);

string Angabe = read_in("rmHV_10_12");

// Klasse Matrix
class Matrix {
    private:
        int werteanz;
        int spaltenanz;
        int zeilenanz;

    public:
        int getWerteanz() {
            return werteanz;
        }
        int getSpaltenanz() {
            return spaltenanz;
        }
        int getZeilenanz() {
            return zeilenanz;
        }

        void setZeilenanz(int za) {
            zeilenanz = za;
        }

        void setSpaltenanz(int sa) {
            spaltenanz = sa;
        }
        void setWerteanz(int wa) {
            werteanz = wa;
        }

};
// string eingabe;
    // cin >> eingabe;
    // string Angabe;
    // Angabe = read_in(eingabe);
string read_in(string filename) { // string read_in(string filename) {
        ifstream input_file (filename); //  ifstream input_file (filename);
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        return buffer.str();  // return buffer.str();
       
}


// Funktion vom Typ Matrix, die eine Matrix zurückgibt. hier werden zeilenanz etc berechnet....
Matrix values_matrix1(string Angabe) {

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
    int number_columns_matrix1 = number_values_matrix1 / number_rows_matrix1; // spalten = Werte / Reihen
    
    Matrix m1;
    m1.setSpaltenanz(number_columns_matrix1);
    m1.setZeilenanz(number_rows_matrix1);

    return m1;
}

Matrix values_matrix2(Matrix m) {
    int number_rows_matrix2 = m.getZeilenanz() + 1;
    int number_columns_matrix2 = m.getSpaltenanz() - 1;

    Matrix m2;
    m2.setZeilenanz(number_rows_matrix2);
    m2.setSpaltenanz(number_columns_matrix2);

    return m2;
}


int main() { 

    Matrix m1;
    m1.getSpaltenanz();
    m1.getZeilenanz();    

    cout << "Spaltenanz: " << values_matrix1(Angabe).getSpaltenanz() << "und Reihenanz: " << values_matrix1(Angabe).getZeilenanz() << endl;


   
  
       /* 

    // werte, Reihen, Spalten für matrix 2
    int number_values_matrix2 = number_values_matrix1;
    int number_rows_matrix2 = number_rows_matrix1 + 1;
    int number_columns_matrix2 = number_columns_matrix1 - 1;

    // matrix1 und matrix2 deklarieren
    float matrix1[number_rows_matrix1][number_columns_matrix1];
    float matrix2[number_rows_matrix2][number_columns_matrix2];
    
    // matrix 1   funktion draus machen
    int cursor = 0;
    for (int y = 0; y < number_rows_matrix1; y++) {
        for (int x = 0; x < number_columns_matrix1; x++) {
            while (Angabe[cursor] != 46) {
                cursor ++;                
            }
            
            char ch1 = Angabe[cursor - 1];
            char ch2 = Angabe[cursor];
            char ch3 = Angabe[cursor + 1];
            char ch4 = Angabe[cursor + 2];
            string value;
            value += ch1;
            value += ch2; 
            value += ch3;
            value += ch4;
            float float_value = stof(value);
            matrix1[x][y] = float_value;
            cursor ++;   
        }
    } */
    
}