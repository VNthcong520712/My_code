#include <iostream>
using namespace std;

long long mod;

unsigned long long time(long long a, long long b){
	if(b <= 1) return b*a;
	if (b % 2 == 0) {
		long long xt = time(a, b/2);
		return (xt+xt)%mod;
	}
	else return (a + time(a, (b-1)))%mod;
}

unsigned long long expo(long long n, long long m){
	if (m == 0) return 1;
	unsigned long long kq = expo(n, m/2);
	if (m%2 == 0) return time(kq, kq) % mod;
	return time(time(kq, kq)% mod, n )% mod;
}

int main(){
	long long a, b;
	cin >> a >> b >> mod;
	cout << expo(a, b);
}