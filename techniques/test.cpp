#include <bits/stdc++.h> 
using namespace std;

int how(int l, int m, int r){
	cout << "     " << l << " " << m << " " << r << endl;
}

int test(int a, int b){
	int mid = a + (b-a)/2;
	if(b <= a){
		return 0;
	}
		cout << a << " " << b << endl;
	test(a, mid);
	cout << endl ;
	test(mid+1, b);
	how(a, mid, b);
}

int main(){
	test(0, 5);
}