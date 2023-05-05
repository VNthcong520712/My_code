#include <iostream>
#include <math.h>
using namespace std;

bool check(int a){
	int count = 0; 
	for(int i = 1; i <= sqrt(a); i++){
		if(a%i == 0){
			if(a % (int)(a/i) == 0 && i != (int)(a/i)) count += 2;
			else count ++;
		}
	}
	if(a != 1 && count == 2){
		return 1;
	} else {
		return 0;
	}
}

int main(){
	int n; 
	cin >> n;
	for(int i = 0; i < n; i ++){
		int z;
		cin >> z;
		if(check(z)) cout << z << endl;
	}
}