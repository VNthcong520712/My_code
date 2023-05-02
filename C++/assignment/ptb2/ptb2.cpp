#include <iostream>
#include <math.h>

using namespace std;

int a, b, c, delta;
float x1, x2;

int main(){
    cout << "nhap gia tri a b va c: ";    
    cin >> a >> b >> c;
    if ((a == 0) && (b == 0)){
        cout << "phuong trinh vo nghiem" << endl;
    } else if((a == 0) && (b!=0)){
        cout << "phuong trinh co nghiem la x = " << (-c/b) << endl;
    } else {
        delta = b*b - 4*a*c;
        if (delta < 0){
            cout << "phuong trinh vo nghiem" << endl;
        } else {
            x1 = (float)(-b + sqrt(delta))/(2*a);
            x2 = (float)(-b - sqrt(delta))/(2*a);
            cout << "phuong tirnh co nghiem la x1: " << x1 << " x2: " << x2;
        }
    }
}
