#include <bits/stdc++.h> 
using namespace std;

int *bubble_sort(int arr[], int s){
	for(int i = 0; i < s; i ++){ 		// loop thought out arr
		bool swapped = false;			// check if all had been swapped
		for(int j = 0; j < s-i-1; j++){ // loop to check each-two element
			if(arr[j] > arr[j+1]){
				swap(arr[j], arr[j+1]);
				swapped = true;
			}
		}
		if(!swapped) break;
	}
	return arr;
}

int main(){
	int mang[] = {9,2,2,3,1,3,4,5,7,6,8,0,0,8};
	int size = sizeof(mang)/sizeof(mang[0]);
	int *z = bubble_sort(mang, size);
	for(int x = 0; x < size; x++){
		cout << *(z + x) << endl;
	}
}
