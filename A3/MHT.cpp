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

class Matrix {
    private:
        int werteanz;
        int spaltenanz;
        int zeilenanz;
        float* matrix_values;
        float* matrix_nodes;
       
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
        float getValue(int x, int y) {
            return matrix_values[y * spaltenanz + x];
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
        void setValue(int x, int y, float value) {
            matrix_values[y * spaltenanz + x] = value;
        }       
         
        void dimensions_matrix_down(string Angabe) {

            int number_values_matrix1 = 0;
            int number_rows_matrix1 = 0;
                
            for (int k = 0; k < Angabe.length(); k++) {  // 45 = -, 46 = .  {}  []
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
            
            spaltenanz = number_values_matrix1 / number_rows_matrix1;       
            zeilenanz = number_rows_matrix1;
            //matrix_values = new float[zeilenanz * spaltenanz];
            setDimensions();  
        }

        void dimensions_matrix_right(Matrix m) {
            spaltenanz = m.getSpaltenanz() - 1;
            zeilenanz = m.getZeilenanz() + 1;
            //matrix_values = new float[zeilenanz * spaltenanz];  
            setDimensions();  
        }

};

string read_in(string filename) {
        ifstream input_file (filename); 
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        return buffer.str();
       
}

int cursor = 0;
  
int fill_matrix(Matrix m, int &cursor, string Angabe) {
    for (int y = 0; y < m.getZeilenanz(); y++) {
        for (int x = 0; x < m.getSpaltenanz(); x++) {
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
            m.setValue(x,y,float_value);
            cursor ++;   
        }
    }

    return cursor;

} 

int main() { 

    Matrix down_edges;
    down_edges.dimensions_matrix_down(read_in("rmHV_10_12"));   
    //cout << "Matrix 1" << endl;
    //cout << "Spaltenanz: " << down_edges.getSpaltenanz() << " und Reihenanz: " << down_edges.getZeilenanz() << endl;

    Matrix right_edges;
    right_edges.dimensions_matrix_right(down_edges);
    //cout << "Matrix 2" << endl;
    //cout << "Spalten: " << right_edges.getSpaltenanz() << " und Reihen: " << right_edges.getZeilenanz() << endl;

    fill_matrix(down_edges, cursor, Angabe);
    //cout << down_edges.getMatrixValue(9,8) << endl; // letzt Koordinate bei 9,8
    //cout << "cursor: " << cursor << endl; // cursor am schluss bei 648

    fill_matrix(right_edges, cursor, Angabe);
    //cout << right_edges.getMatrixValue(7,7) << endl; // letzte Koordinate bei 
    //cout << "cursor: " << cursor << endl; // cursor am schluss bei 1306

    Matrix knoten;
    knoten.setSpaltenanz(down_edges.getSpaltenanz());
    knoten.setZeilenanz(right_edges.getZeilenanz());
    knoten.setDimensions();
    //cout << " spalten: " << knoten.getSpaltenanz() << " und Zeilen: " << knoten.getZeilenanz() << endl;


    int value = 0;
    knoten.setValue(1,1, 0.5);
    cout << knoten.getValue(1,1);
    //cout << knoten.getknotenValue(1,1);
    /*
    for (int y = 1; y < knoten.getSpaltenanz(); y++) {  //
        value = knoten.getknotenValue(0,y-1);
        cout << value << ", " << endl;
        
        /*knoten.setknotenValue(0,y, value);
        cout << knoten.getknotenValue(0,y) << ", " << endl;*/
    


/*
    for (int y = 0; y < knoten.getZeilenanz(); y++) {
        for (int x = 0; x < knoten.getSpaltenanz(); x++) {
        }
    }*/

}


    




