#include <iostream>
#include <math.h>
using namespace std;

int n, d = 0;

int main(){
    cout << "nhap vao so n: ";
    cin >> n;
    int i = n;
    n = abs(n);
    for(n; n > 0; n /= 10){
        n = int(n);
        d ++;
    }
    cout <<"so " << i << " co " << d << " chu so"<<endl;
}