#include <iostream>
#include <math.h>
using namespace std;

int main(){
	long long n, dem = 0;
	cin >> n;
	if(n < 2) cout <<"NO";
	else{
		for(long long i = 1; i <= sqrt(n); i++){
			if(n % i == 0){
				dem += 2;
			}
		}
		if(dem == 2) cout << "YES";
		else cout << "NO";
	}
}