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

bool inarr(int *arr, int x){
	bool out = false;
	for(int i = 0; i < sizeof(arr)/sizeof(int); i ++){
		if(x == arr[i]){
			out = true; 
			break;
		}
	}
	return out; 
}

void xuat(int * arr){
	int len = sizeof(arr)/sizeof(arr[0]);
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
	// int n; 
	// cin >> n;
	// for(int i = 0; i < n; i ++){
	// 	int z;
	// 	cin >> z;
	// 	if(check(z)) cout << z << endl;
	// }
	int a[5] = {1, 4, 2, 4, 4};
	cout << inarr(a, 4);
	// int a[6] = {7, 2, 3, 5, 1, 5};
	// // xuat(a);
	// cout << inarr(a, 5);
}