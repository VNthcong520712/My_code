#include <iostream>
using namespace std;

float a, b;

int main(){
    cout << "nhap he so a va b cho phuong trinh ax + b = 0: ";
    cin >> a >> b;
    if (a != 0){
        cout << "phuong trinh co nghiem la: " << -b/a << endl;
    } else {
        if (b == 0){
            cout << "phuong trinh co vo so nghiem";
        } else {
            cout << "phuong trinh nay vo nghiem do co he so a bang 0 va b khac 0" << endl;
        }
    }
}