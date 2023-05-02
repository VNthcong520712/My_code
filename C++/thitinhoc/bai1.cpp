#include <fstream>
#include <iostream>
#include <string.h>
using namespace std;
int main(){
	ifstream input("D:\\Documents\\My Documents\\Programming languages\\C++\\hsgtin2022\\bai1.inp");
	ofstream output("D:\\Documents\\My Documents\\Programming languages\\C++\\hsgtin2022\\bai1.out");
	int n; 
	input >> n;
	int mang[n], dem = 1;
	bool trangthai = false;
	for(int u = 0; u < n; u++){
		input >> mang[u];
		if(u > 0){
			if(mang[u] > mang[u-1]){
				trangthai = 1;
			}
			if((mang[u] < mang[u - 1] && trangthai == 1)||(u == n-1 && trangthai == 1)){
				trangthai = 0;
				dem ++;
			}
		}
	}
	output << dem;
}