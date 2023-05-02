#include <iostream>
using namespace std;

long long gt(short a, short b){
	long long t = 1;
	for(a; a <= b; a++){
		t *= a;
	}
	return t;
}

int main(){
	short n, k;
	cin >> n >> k;
	cout << (double) gt(n-k+1, n)/gt(1, k);
}