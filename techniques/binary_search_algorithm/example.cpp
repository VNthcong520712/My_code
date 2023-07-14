#include <iostream> 
using namespace std;

int binary_search(int arr[], int l, int r, int key){
	while(l <= r){
		int m = l+(r-1)/2;
		if(arr[m] == key){
			return m;
		}
		
		if(arr[m] < key){
			l = m+1;
		}else {
			r = m-1;
		}
	}
	return -1;
}

int main(){
	int n; 
	cin >> n;
	int arr[n];
	for(int i = 0; i < n; i++){
		cin >> arr[i];
	}
	int key; 
	cin >> key;
	int result = binary_search(arr, 0, n-1, key);
	if(result == -1) cout << "fail";
	else cout <<"result: " << result;
}
