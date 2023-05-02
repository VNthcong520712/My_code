#include <iostream>
using namespace std;

string cd(long long a){
	string k = "";
	while(a > 0){
		k = char(a%2 + 48) + k; 
		a = (a/2);
	}
	return k;
}

int main(){
	int t;
	cin >> t;
	for(t; t > 0; t --){
		long long z;
		cin >> z;
		cout << cd(z) << endl;
	}
} 