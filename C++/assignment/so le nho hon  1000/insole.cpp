#include <iostream>
using namespace std;

int main(){
    cout << "cac so le nho hon 1000 va khac 5, 7, 93: " << endl;
    for (int i = 0; i < 1000; i ++ ){
        if ((i != 5) && (i != 7) && (i != 93) && ( i % 2 != 0)){
            cout << i << "  ";
        }
    }
}