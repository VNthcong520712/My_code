#include <iostream>
using namespace std;

int f[1000005];

int fibo(int a){
    if(a == 1 || a == 2) return 1;
    if(f[a] != 0) return f[a];
    f[a] = (fibo(a-1) + fibo(a-2))%(1000000000+7);
    return f[a];
}

int main(){
    int x;
    cin >> x;
    int z[x];
    for(int i = 0; i < x; i++){
        cin >> z[i];
    }
    
    for(int j = 0; j < x; j++){
        cout << fibo(z[j]) <<endl;
    }
}