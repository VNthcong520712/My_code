#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int x, S;
string i;

int main(){
    cout << "\nnhap x de tinh 2 phuong trinh: \n + 2x^2 + 5x + 9 khi x >= 5 \n + -2x^2 + 4x - 9 khi x < 5 \nnhap x = ";
    cin >> x;
    if (x >= 5){
        S = 2*pow(x,2) + 5*x + 9;
        i = "vi x >= 5 nen gia tri la: ";
    } else if (x < 5 ){
        S = -2*pow(x,2) + 4*x -9;
        i = "vi x < 5 nen gia tri la: ";
    }
    cout << i << S << endl; 
}