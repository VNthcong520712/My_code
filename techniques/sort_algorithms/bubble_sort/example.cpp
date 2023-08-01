#include <bits/stdc++.h> 
using namespace std;

int *bubble_sort(int arr[], int n){
	for(int i = 0; i < n; i++){
		bool swapped = false;   // use to check if it is favorable array
								// mean that all elements are swapped
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
	int mang[] = {1,7,3,4,0,5,9,2,6,8};
	int *z = bubble_sort(mang, 10);
	for(int x = 0; x < 10; x++){
		cout << *(z + x) << endl;
	}
}
