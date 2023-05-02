#include <iostream>
#include <math.h>
using namespace std;

int n, x, o = 0;
float S = 0;

int main(){
    cout << "nhap n va x: ";
    cin >> n >> x;
    for (int i = 1; i <= n ; i++){
        o += i;
        S += pow(x,i)/o;
    }
    cout << "gia tri cua phep tinh la: " << S << endl;
}
