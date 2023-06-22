/*
A array with n integer, find and print number is needed
---
get n
create array with n element and get input, in this loop listed number equal 2 or not divisible for 2(B array)

*/




#include <iostream>
using namespace std;

bool check(int num){
	int count = 0; 
	for(int i = 1; i <= sqrt(num); i++){
		if(num%i == 0){
			if(num % (int)(num/i) == 0 && i != (int)(num/i)) count += 2;
			else count ++;
		}
	}
	if(num != 1 && count == 2){
		return 1;
	} else {
		return 0;
	}
}

bool inarr(int *arr, int len, int num){
	bool out = false;
	for(int i = 0; i < len; i ++){
		if(num == arr[i]){
			out = true; 
			break;
		}
	}
	return out; 
}

void xuat(int * arr, int len){
	for(int i = 0; i < len; i ++){
	 	int min = arr[0];
		for(int z = 0; z < i; z ++){
			if(arr[z] < min){
				int p = min;
				min = arr[z];
				arr[z] = p;
			}
		}
		if(i > 0) cout << arr[i-1] << " ";
	}
	cout << arr[len-1];
}

int main(){
	int n; 
	cin >> n;
	int nguyento[n];
	for(int i = 0; i < n; i ++){
		int z;
		cin >> z;
		if(check(z) && inarr(nguyento, n, z)) cout << z << endl;
	}
}