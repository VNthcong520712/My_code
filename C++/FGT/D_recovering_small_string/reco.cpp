#include <bits/stdc++.h>
#include <string>
using namespace std;

int n, k, a[1000] = {0}, cnt, ok, tes[100];
string temp = "", lst = "", saed[100] = {""};

void fmin(int c, int b, int a){
	temp = "";
	temp += char(a+96);
	temp += char(b+96);
	temp += char(c+96);
	lst = (temp.compare(lst) < 0)?temp:lst;
}

void kto(int x){
	int n = x/26;
	int d = x%26;
	if(n == 0){
		a[1] = x - 2;
		a[2] = 1;
		a[3] = 1;
	} else if(n == 1){
		if(d >= 2){	
			a[1] = 26;
			a[2] = x - 1;
			a[3] = 1;
		} else {
			a[1] = x - 2;
			a[2] = 1;
			a[3] = 1;
		}
	} else {
		if(d >= 2 || n == 3){
			a[1] = 26;
			a[2] = 26;
			a[3] = x - 52;
		} else {
			a[1] = 26;
			a[2] = x - 1;
			a[3] = 1;
		}
	}
}

bool cc(int n, int a, int b, int c){
	int o = n%3;
	int m = n/3;
	int fi = (o >= 1)?(m+1):m, se = (o == 2)?(m+1):m, th = m;
	if(a == fi && b == se && c == th) return true;
	return false;
}

void sinh(int n){
	for(int i = a[1]; i <= 26; i--){
		for(int j = 1; j <= i; j++){
			for(int k = 1; k <= j; k++){
				if(i + j + k == n){
					fmin(i, j, k);
					if(cc(n, i, j, k)) return;
				}
			}
		}
	}
}

int main(){
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> tes[i];
	}
	for(int i = 0; i < n; i++){
		int ts = tes[i];
		if(saed[ts].compare("") == 0){
			ok = 0;
			kto(ts);
			cnt = 3;
			lst = "";
			for(int i = 3; i > 0; i --){
				lst += char(a[i] + 96);
			}sinh(ts);
			saed[ts] = lst;
		}
		cout << saed[ts] << '\n';
	}
}