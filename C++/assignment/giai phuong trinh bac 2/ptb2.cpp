#include <iostream>
#include <math.h>
using namespace std;

float a, b, c, del, x1, x2, sn;

int main(){
    cout << "nhap vao he so a, b, c cho phuong tirnh bac hai ax^2 + bx + c = 0:  ";
    cin >> a >> b >> c;
    if (a != 0){
        del = pow(b,2) - 4*a*c;
        if (del > 0){
            sn = 2;
            x1 = (-b + sqrt(del))/(2*a);
            x2 = (-b - sqrt(del))/(2*a);
        } else if (del == 0){
            sn = 1;
            x1 = -b/(2*a);
            x2 = x1;
        } else sn = 0;
    } else sn = 0;
    if (sn == 2){
        cout << "phuong trinh co " << sn << " nghiem: x1 = " << x1 << "; x2 = " << x2 << endl;
    } else if (sn == 1){
        cout << "phuong trinh co " << sn << " nghiem: x1 = x2 = " << x1 << endl;
    } else cout << "phuong trinh vo nghiem" << endl;
}