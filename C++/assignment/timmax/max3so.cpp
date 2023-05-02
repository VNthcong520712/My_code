#include <iostream>
#include <conio.h>
using namespace std;

float a, b, c;

int main(){
    cout << "nhap 3 so thuc de so sanh: " ;
    cin >> a >> b >> c;
    float max = a; 
    if (b > max){
        max = b;
    }
    if (c > max) {
        max = c;
    }
    cout << "max cua 3 so nhap vao la: " << max << endl;
    getch();
}