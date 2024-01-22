#include <iostream>
#include <math.h>
using namespace std; 

bool ktnt(int a){
	int dem = 0;
	for(int i = 1; i <= sqrt(a); i ++){
		if(a % i == 0){
			if(a % (a/i) == 0){
				dem += 2;
			}
			else dem ++;
		}
		
	}
	return (dem == 2 && 2 <= a);
}

int main(){
	int n; 
	cin >> n;
	int a[n];
	bool sol[1000] = {false};
	int max = 0;
	for(int i = 0; i < n; i++){
		cin >> a[i];
		if(ktnt(a[i])){
			sol[a[i]] = true;
			if (a[i] > max){
				max = a[i];
			}
		}
	}
	for(int i = 0; i <= max; i++){
		if(sol[i]){
			cout << i;
			if(i < max) cout << " ";
		}
	}
}