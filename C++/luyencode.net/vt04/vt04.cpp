#include <iostream>
using namespace std;

int main(){
	int n, x;
	string out = "NO";
	bool check = 0;
	cin >> n >> x;
	for(int i = 0; i < n; i++){
		int z;
		cin >> z;
		if(z == x && check == 0){
			out = "YES";
			check = 1;
		}
	}
	cout << out;
}