#include <bits/stdc++.h> 
using namespace std;

int *insertion_sort(int arr[], int n){
	int key, j;
	for(int i = 0; i < n; i++){
		key = arr[i];
		j = i-1;
		while (j >= 0 && arr[j] > key){
			arr[j+1] = arr[j];
			j = j-1;
		}
		arr[j+1] = key;
	}
	return arr;
}

int main(){
	int arr[]={1,4,0,2,4,7,3,4,0,8,8,9,13,5,0};
	int size = sizeof(arr)/sizeof(arr[0]);
	int *result = insertion_sort(arr, size);
	for(int i = 0; i < size; i++){
		cout << *(result + i) << endl;
	}
}
