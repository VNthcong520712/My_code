#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int gt(short a){
	int t = 1;
	for(int i = 1; i <= a; i++){
		t*=i;
	}
	return t;
}

int main(){
	short x, n; 
	cin >> x >> n;
	double k = 0;
	for(int j = 1; j <= n; j++){
		k+= (double) pow(x, j)/gt(j);
	}
	cout << fixed << setprecision(2) << k;
}