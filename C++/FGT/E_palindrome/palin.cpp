#include <iostream>
using namespace std;

void symm(string inp){
	int leng = inp.length();
	int mid = leng/2;
	for(int i = 0; i < mid; i++){
		if((char)inp[i] != (char)inp[leng - 1 - i]){
			cout << "NO";
			return;
		}
	}
	cout << "YES";
}

int main(){
	string s;
	getline(cin, s);
	symm(s);
}