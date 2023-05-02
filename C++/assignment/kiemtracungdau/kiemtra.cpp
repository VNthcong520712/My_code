#include <iostream>
using namespace std;

float a, b;

int main(){
    cout << "nhap hai so de kiem tra: ";
    cin >> a >> b;
    if (a*b > 0){
        cout << "hai so nhap vao co cung dau" << endl;
    } else {
        cout << "hai so nhap vao khong cung dau" << endl;
    }

}