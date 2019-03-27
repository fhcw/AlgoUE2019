#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <sstream>
#include <ctime>
#include <typeinfo>

using namespace std;

string read_in(string filename);

class Matrix {
    private:
        int werteanz;
        int spaltenanz;
        int zeilenanz;
        float* matrix_values;
       
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
        void setDimensions() {
            matrix_values = new float[zeilenanz * spaltenanz];
        }

        void dimensions_matrix1(string Angabe) {

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
            
            spaltenanz = number_values_matrix1 / number_rows_matrix1;   // spalten = Werte / Reihen        
            zeilenanz = number_rows_matrix1;
            matrix_values = new float[zeilenanz * spaltenanz];
        }

        void dimensions_matrix2(Matrix m) {
            //int number_rows_matrix2 = 
            //int number_columns_matrix2 = 

            spaltenanz = m.getSpaltenanz() - 1;
            zeilenanz = m.getZeilenanz() + 1;
           
    
        }

};

string read_in(string filename) {
        ifstream input_file (filename); 
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        return buffer.str();
       
}

int main() { 

    Matrix m1;
    m1.dimensions_matrix1(read_in("rmHV_10_12"));
   
    cout << "Matrix 1" << endl;
    cout << "Spaltenanz: " << m1.getSpaltenanz() << " und Reihenanz: " << m1.getZeilenanz() << endl;


    Matrix m2;
    m2.dimensions_matrix2(m1);

    cout << "Matrix 2" << endl;
    //cout << "Spalten: " << m2.dimensions_matrix2(m1).spaltenanz << " und Reihen: " << m2.dimensions_matrix2(m1).zeilenanz << endl;
    cout << "Spalten: " << m2.getSpaltenanz() << " und Reihen: " << m2.getZeilenanz() << endl;
  
       /*

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
            matrix1[x][y] = float_value;   // m1.setMatrixValues(x, y, float_value);
            cursor ++;   
        }
    } */
    
}