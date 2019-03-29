#include <iostream>
#include <fstream>
#include <streambuf>
#include <string>
#include <sstream>
#include <ctime>
#include <typeinfo>
#include <algorithm>

using namespace std;

//Klasse:
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
            setDimensions();  
        }

        void dimensions_matrix_right(Matrix m) {
            spaltenanz = m.getSpaltenanz() - 1;
            zeilenanz = m.getZeilenanz() + 1;  
            setDimensions();  
        }

};

//globale Variable:
int cursor = 0; 

// Prototypen:
string read_in(string filename);
int fill_matrix(Matrix m, int &cursor, string Angabe);
void calculate_node_sums(Matrix nodes, Matrix down, Matrix right);

// Main:
int main(int argc, char* argv[]) { 

    string Angabe = read_in(argv[1]);

    Matrix down_edges;
    down_edges.dimensions_matrix_down(Angabe);   

    Matrix right_edges;
    right_edges.dimensions_matrix_right(down_edges);

    fill_matrix(down_edges, cursor, Angabe);
    
    fill_matrix(right_edges, cursor, Angabe);

    Matrix knoten;
    knoten.setSpaltenanz(down_edges.getSpaltenanz());
    knoten.setZeilenanz(right_edges.getZeilenanz());
    knoten.setDimensions();

    calculate_node_sums(knoten, down_edges, right_edges);
}

string read_in(string filename) {
        ifstream input_file (filename); 
        
        stringstream buffer;
        buffer << input_file.rdbuf();
        input_file.close();

        return buffer.str();
       
}

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

void calculate_node_sums(Matrix nodes, Matrix down, Matrix right) {
    float value = 0.0;    
    
    for (int y = 0; y < nodes.getZeilenanz(); y++) {
        if (y == 0){
            nodes.setValue(0,0, 0.0);
        } else {
            value = nodes.getValue(0,y-1) + down.getValue(0,y-1);
            nodes.setValue(0,y, value);
            }
    }

    for (int x = 0; x < nodes.getSpaltenanz(); x++) {
        if (x == 0){
            nodes.setValue(0,0, 0.0);
        } else {
            value = nodes.getValue(x-1,0) + right.getValue(x-1,0);
            nodes.setValue(x,0, value);
            }
    }

    float value1 = 0;
    float value2 = 0;
    float max_value = 0;
    for (int y = 1; y < nodes.getSpaltenanz(); y++) {
        for (int x = 1; x < nodes.getZeilenanz(); x++) {
            value1 = nodes.getValue(x,y-1) + down.getValue(x, y-1);
            value2 = nodes.getValue(x-1,y) + right.getValue(x-1,y);
            max_value = max(value1, value2);
            nodes.setValue(x,y, max_value);
        }
    }
    cout << "weight of the longest path: " << nodes.getValue(nodes.getSpaltenanz()-1, nodes.getZeilenanz()-1) << endl;
}


