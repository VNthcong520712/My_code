#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	int a[n];
	for(int i = 0; i < n; i++){
		cin >> a[i];
		if(i % 2 == 0 && i != 0){
			if(n % 2 != 0) a[i-1] += abs(a[i-2] - a[i]);
			else{
				int z = (i == n-1)?(a[i]):(0);
				a[i-1] += abs(a[i-2] - z);
			}
		}
		if(i > 0) cout << a[i-1] << " ";
	}
	cout << a[n-1];
}

// 1 *2 3 *4
// 1 *2 3 *4 5