#include <iostream>
using namespace std;

int main(){
	int a, n, max, max2, sa;
	cin >> n;
	cin >> a;
	max = a;
	max2 = -1000000001;
	for(int i = 1; i < n; i++){
		if (i < n) cin >> a;
		if (a > max){
			max2 = max;
			max = a;
		}else if(a < max && a > max2){
			max2 = a;
		}
	}
	if(max2 == -1000000001) cout << "NOT FOUND";
	else cout << max2;
}
