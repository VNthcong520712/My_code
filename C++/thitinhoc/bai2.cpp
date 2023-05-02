#include <iostream>
#include <fstream>
using namespace std;

int gt(int a){
	if(a == 1){
		return 1;
	}
	return a*gt(a-1);
}

int main(){
	ifstream vao("D:\\Documents\\My Documents\\Programming languages\\C++\\hsgtin2022\\bai2.in");
	ofstream ra("D:\\Documents\\My Documents\\Programming languages\\C++\\hsgtin2022\\bai2.out");
	int n, pos = 0;
	cin >> n;
	int a[n], a0[n];
	for(int i = 0; i < n; i++){
		cin >> a[i];
		if(a[i] == 0){
			a0[pos] = i;
			pos ++;
		}
	}
	long long soluong = gt(pos - 1);
	int kq[soluong], o = 0;
	for(int z = 0; z < pos - 2; z++){
		long tong = 0;
		for(int j = a0[z]; j < a0[z+1]; j++){
			tong += a[j];
		}
		kq[o] = tong;
		cout << kq[o] << endl;
		o++;
	}

}