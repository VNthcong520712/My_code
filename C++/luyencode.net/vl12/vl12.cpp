#include <iostream>
#include <math.h>
using namespace std;

int main(){
	short n, sn = 0;
	cin >> n;
	n = abs(n);
	short nho[(int) sqrt(n) + 1], dem = 0;
	if(n == 0) {
		cout << "INF";
		exit(0);
	}

	for(short i = n; i >= sqrt(n); i--){
		if(n % i == 0){
			cout << i <<" ";
			if (i != n/i) {nho[sn] = n/i; sn ++;}
		}
	}
	for(short z = sn-1; z >= 0; z--) cout << nho[z] << " ";
}