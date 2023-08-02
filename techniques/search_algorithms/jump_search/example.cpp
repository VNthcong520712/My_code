#include <bits/stdc++.h>
using namespace std;

int jump_search(int arr[], int key, int n){
	int step = sqrt(n);
	int prev = 0;
	while(arr[min(step, n)-1] < key){
		prev = step;
		step += sqrt(n);
		if (prev >= n) return -1;		
	}

	while (arr[prev] < key){
		prev ++;
		if (prev == min(step, n)) return -1;
	}

	if (arr[prev] == key) return prev;

	return -1;
}

int main(){
	int arr[] = {1,5,8,12,65,98,123,235,643,674,677,827, 982,36673};
	int n = sizeof(arr)/sizeof(arr[0]);
	int x = 36673;
	int result = jump_search(arr, x, n-1);
	(result == -1)? cout << "not found"
				  : cout << result;
}
