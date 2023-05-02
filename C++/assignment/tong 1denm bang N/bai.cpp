#include <iostream>
using namespace std;

int N, m, S =0;

int main(){
    cout << "nhap vao gia tri cua tong day so N: ";
    cin >> N;
    for (m = 1; S < N; m ++){
        S += m;
    }
    if (S == N){
        m -= 1;
    } else if(S> N){
        m -=2;
    }
    cout << "gia tri lon nhat cua m de 1+2+...+m < N la: " << m << endl;
}