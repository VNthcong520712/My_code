#include <iostream>
#include <string.h>
using namespace std;

int main(){
	string a, b; 
	getline(cin, a);
	bool kt = true;
	for(int i = a.length()-1; i >= 0; i--){
		if(a[i] != '0') kt = false;
		if(kt == false) cout << a[i];
	}	
}