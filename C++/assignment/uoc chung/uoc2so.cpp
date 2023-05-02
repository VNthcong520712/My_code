#include <iostream>
using namespace std;

int U = 0, n, m, sn;

int main(){
    cout << "nhap hai so n va m: ";
    cin >> m >> n;
    if (n > m){
        sn = m;
    } else if (m > n){
        sn = n;
    } else {
        U = n;
    }
    if (U == 0){
        for (int i = 1; i <= sn+1; i++){
            if ((m%i==0) && (n%i==0) && (i > U)){
                U = i;
            }
        }
    }
    
    cout << "uoc chung lon nhat cua hai so " << n << " va " << m << " la: " << U << endl;
}