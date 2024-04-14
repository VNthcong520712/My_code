#include <bits/stdc++.h>
using namespace std;

/*
sinh to hop chap se sinh ra cau hinh lien tiep theo thu tu cua to hop 
do
gia tri dau co dang la 1 ... k 
gia tri cuoi co dang la n-k+1 ... n-k+k
=> gia tri max o vi tri i la n-k+i
cac gia tri phia sau se bang gia tri truoc do +1
*/

int n, k, ok = 0, a[1010] = {0};

void sinh(){
	int i = k;
	while( i >= 1 && a[i] == n-k+i){
		--i;
	}
	if(i == 0){
		ok = -1;
	}else {
		a[i] ++;
		for(int j = i+1; j <= k; j++){
			a[j] = a[j-1]+1;
		}
	}
}

int main(){
	cin >> n >> k;
	for(int i = 1; i <= k; i++){
		cin >> a[i];
	}
	sinh();
	if(ok == -1) cout << ok;
	else{
		for(int f = 1; f <= k; f++){
			cout << a[f]<<' ';
		}
	}
}