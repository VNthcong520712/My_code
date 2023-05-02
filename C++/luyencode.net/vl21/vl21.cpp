#include <iostream>
#include <math.h>
using namespace std; 

int main(){
	int n, t = 0; 
	cin >> n;
	int i;
	for(i = 1; t <= n; i++){
		t+= i;
	}
	cout << i-2;
}