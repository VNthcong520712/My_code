#include <iostream>
using namespace std;

int n, S = 0; 

int main(){
    cout << "Nhap so n: ";
    cin >> n;
    for (n; n > 0; n--){
        S += n;
    }
    cout << "Tong day so la: " << S << endl;
}