#include <iostream>
#include <math.h>
using namespace std;

int main(){
	short a, dem = 0;
	cin >> a;
	a = abs(a);
	for(int i = 1; i <= sqrt(a); i++){
		if(a % a/i == 0 && a % i == 0){
			if (i != a/i) dem += 2;
			else dem += 1;
		}
	}
	cout << dem ;
}