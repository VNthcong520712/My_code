#include <iostream>
using namespace std;

int n, S=0;

int main(){
    cout << "nhap gia tri n: ";
    cin >> n;
    for (int i=1 ; i <= n; i+=2){
        S += i;
    }
    cout << "tong cac so le tu 0 den n la: " << S << endl;
}