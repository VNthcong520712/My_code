#include <iostream> 
using namespace std;

int interpolation_search(int arr[], int lo, int hi, int key){
	int pos; 
	
	if(lo <= hi && key >= arr[lo] && key <= arr[hi]){
		pos = lo + (((double)(hi-lo)/(arr[hi] - arr[lo]))*(key-arr[lo]));
		if(arr[pos] == key) return pos;
		if(arr[pos] < key) return interpolation_search(arr, pos+1, hi, key);
		if(arr[pos] > key) return interpolation_search(arr, lo, pos-1, key);
	}
	return -1;
}

int main(){
	int arr[] = {1,5,8,12,65,98,123,235,643,674,677,827, 982,36673};
	int n = sizeof(arr)/sizeof(arr[0]);
	int x = 1;
	int result = interpolation_search(arr, 0, n-1, x);
	(result == -1)? cout << "not found"
				  : cout << result; 
}
