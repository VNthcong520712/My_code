#include <iostream>
#include <fstream>
using namespace std;

int sapxep()

int main(){
	ifstream vao("vao.inp");
	ofstream ra("ra.out");
	int n;
	vao >> n;
	vao.ignore();
	int a[n], b[n]; 
	for(int i = 0; i < n; i++){
		vao >> a[i];
		vao >> b[i];
	}

	for(int i = 0; i < n; i++){
		cout << a[i] << " " << b[i] << endl;
	}
}