#include <bits/stdc++.h>
using namespace std;

int n, k, a[1000] = {0}, cnt, ok;

void kto(int x){
	int n = x/28;
	int d = x%28;
	if(n == 0){
		a[1] = x - 2;
		a[2] = 1;
		a[3] = 1;
	} else if(n == 1){
		a[1] = 26;
		a[2] = d - 1;
		a[3] = 1;
	} else{
		a[1] = 26;
		a[2] = 26;
		a[3] = x - 52;
	}
}

bool cc(int n){
	int o = n%3;
	int m = n/3;
	in fi = m, se = m, th = m;
	if(o == 1){
		
	}
	return false;
}

void sinh(int n){
	int i = cnt;
	while(i > 0 && a[i] == 1){
		--i;
	}
	if(cc(n) || i == 0) ok = 1;
	else{
		a[i] --;
		int d = cnt - i + 1;
		int q = d/a[i];
		int r = d%a[i];
		cnt = i;
		if(q > 0){
			for(int j = 0; j < q; j++){
				cnt ++;
				a[cnt] = a[i];								
			}
		}
		if(r > 0){
			cnt ++;
			a[cnt] = r;
		}
	}
}

int main(){
	cin >> n;
	ok = 0;
	kto(n);
	cnt = 3;
	while(!ok){
		for(int i = 1; i <= cnt; i ++){
			cout << a[i] << ' ';
		}
		cout << endl;
		sinh(n);
	}
}