#include <iostream>
using namespace std;

int binary_search(int arr[], int l, int h, int x){
	while(l <= h){
		int m = l + (h-l)/2;
		if(arr[m] == x) return m;
		if(arr[m] < x){
			l = m+1;
		} else {
			h = m-1;
		}
	}
	return -1;
}

int main(){
	int arr[] = {1,5,8,12,65,98,123,235,643,674,677,827, 982,36673};
	int n = sizeof(arr)/sizeof(arr[0]);
	int x = 36673;
	int result = binary_search(arr, 0, n-1, x);
	(result == -1)? cout << "not found"
				  : cout << result;
}