#include<iostream>
using namespace std;

int linear_seach(int arr[], int N, int key){
	for(int i = 0; i < N; i++){
		if (arr[i] == key){
			return i;
		}
	}
	return(-1);
}

int main(){
	int a;
	cin >> a;
	int arr[a];
	for(int i = 0; i < a; i++){
		cin >> arr[i]; 
	}
	int result = linear_seach(arr, a, 4);
	( result == -1)
		? cout << "Could not find that element"
		: cout << result;
}