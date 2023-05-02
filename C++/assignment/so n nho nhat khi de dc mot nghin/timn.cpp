#include <iostream>
using namespace std;

int n, S = 0; 

int main(){
    cout << "tim so n nho nhat de tong day den n > 10000" <<endl;
    for (n = 0; S < 10000; n++){
        S += n;
    }
    cout << "so thoa man la: " << n-1 << endl;
}