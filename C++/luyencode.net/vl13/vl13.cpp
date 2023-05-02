#include <iostream>
#include <math.h>
using namespace std;

int main(){
	int n, tong = 0; 
	cin >> n;
	if(n > 0){
		for(int i = 1; i <= sqrt(n); i ++){
			if(n % i == 0){
				if(i != n/i){
					tong += (i+n/i);
				} else tong += i;
			}
		}
		tong -= n;
		if (tong == n) cout << "YES";
		else cout << "NO";
	} else cout << "NO";
}