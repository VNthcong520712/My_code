#include <bits/stdc++.h>
using namespace std;

const int mod = 1000000007;
// unsigned long long Ex[1000000006];

unsigned long long expo(long long n, long long m){
	if (m == 0) return 1;
	unsigned long long kq = expo(n, m/2);
	if (m%2 == 0) return kq*kq % mod;
	return ((kq*kq )% mod * n )% mod;
}

int main(){
	long long a, b;
	cin >> a >> b;
	cout << expo(a, b);
}