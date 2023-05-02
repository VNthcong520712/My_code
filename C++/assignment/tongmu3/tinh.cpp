#include <iostream>
#include <math.h>
using namespace std;

int n;
float S = 0;

int main(){
    cout << "nhap vao so n: ";
    cin >> n;
    for (n; n > 0; n --){
        S += pow(n,3);
    }
    cout << "tong lap phuong den n la: " << S << endl;
}