#include <iostream>
using namespace std;

float a,b,c,d,e,f,x,y;

int main(){
    cout << "nhap cac he so a b c d e f cho he phuong trinh: \n{ ax + by = c \n{ dx + ey = f \nnhap a b c d e f: ";
    cin >> a >> b >> c >> d >> e >> f;
    y = (d*c - a*f)/(d*b-a*e);
    x = (c-b*y)/a;
    cout << "nghiem he phuong trinh la: x= " << x << " ; y= " << y << endl;
}