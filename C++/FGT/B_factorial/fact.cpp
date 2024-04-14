#include <iostream>
using namespace std;

long long f[1000005];

long long fact(long long a){
    if(a == 0) return 1;
    if(f[a] != 0) return f[a];
    f[a] = (a * fact(a-1))%(1000000000+7);
    return f[a];
}

int main(){
    long long x;
    cin >> x;
    long long z[x];
    for(int i = 0; i < x; i++){
        cin >> z[i];
    }
    
    for(int j = 0; j < x; j++){
        cout << (long long)fact(z[j]) <<endl;
    }
}