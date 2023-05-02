#include <iostream>
#include <math.h>
using namespace std;

float a, b, c;

int main(){
    cout << "nhap 3 so thuc: ";
    cin >> a >> b >> c;
    if (a < 0){
        a = abs(a);
    }
    if (c < 0){
        c = abs(c);
    }
    if (b < 0){
        b = abs(b);
    }
    cout <<"a = "<< a <<" ;b = "<< b <<" ;c = "<< c << endl;
}