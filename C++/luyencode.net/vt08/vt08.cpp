#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n; 
	int a[n];
	for(int i = 0; i <= n; i++){
		if (i < n) cin >> a[i];
		int l = 0, r = 0; 
		if(1 < i) l = a[i-2]; 
		if(i < n) r = a[i];
		if(i % 2 == 0 && i != 0){
			a[i-1] += abs(l-r);
		}
		if (i > 0) {
			cout << a[i-1];
			if (i-1 < n) cout << " ";
		}
	}
}

// 1 *2 3 *4
// 1 *2 3 *4 5