#include <bits/stdc++.h>
using namespace std;

unsigned long long Tb[100005];
int mod = 1000000007;



unsigned long long tribo(int a){
    if(a <= 3) return a;
    if(Tb[a] != 0) return Tb[a];
    Tb[a] = (((tribo(a-1)%mod + tribo(a-2)%mod +tribo(a-3)%mod)%mod)%mod)%mod;
    return Tb[a];
}

int main(){
    int t;
    cin >> t;
    int inp[t];
    for(int i = 0; i < t; i++){
        cin >> inp[i];
    }
    for(int i = 0; i < t; i++){
        cout << tribo(inp[i]) << endl;
    }
}