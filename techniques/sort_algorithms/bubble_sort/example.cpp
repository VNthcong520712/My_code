#include <bits/stdc++.h> 
using namespace std;

int *bubble_sort(int arr[], int n){
	for(int i = 0; i < n; i++){
		bool swapped = false;   // use to check if it is favorable array
								// mean that all elements are swapped
		for(int j = 0; i < n - j -1; j++){
			if(arr[j] > arr[j+1]){
				swap(arr[j], arr[j+1]);
				swapped = true;
			}
		}
		if(swapped == false) break;
	}
	return arr;
}

int main(){
	int mang[] = {9,2,2,3,1,3,4,5,7,6,8,0,0,8};
	int size = sizeof(mang)/sizeof(mang[0]);
	int *z = bubble_sort(mang, size);
	for(int x = 0; x < 10; x++){
		cout << *(z + x) << endl;
	}
}
