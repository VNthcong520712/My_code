#include <bits/stdc++.h>
using namespace std;

int searching(int arr[], int n, int x);

int main(){
	int arr[] = {1,4,6,10,12,34,78};
	int x = 10;
	int len = sizeof(arr)/sizeof(arr[0]);
	int result = searching(arr, len, x);
	(result != -1)
		? cout << result
		: cout << "couldn't found this element";
}

int searching(int arr[], int n, int x){
	int prev, step = sqrt(n);
	for(step; arr[min(step, n)-1] < x; step += sqrt(n)){
		prev = step;
		if(prev >= n) return -1;
	}

	for(prev; arr[prev] < x; prev ++){
		if(prev == min(step, n)) return -1;
	}

	if(arr[prev] == x) return prev;
	return -1;
}
