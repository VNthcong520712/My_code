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
	int arr[] = {1,5,8,12,65,98,123,235,643,674,677,827, 982,36673};
	int n = sizeof(arr)/sizeof(arr[0]);
	int x = 36673;
	int result = linear_seach(arr, n, x);
	( result == -1)
		? cout << "not found"
		: cout << result;
}