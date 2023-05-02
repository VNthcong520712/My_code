#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream vao("vao.inp");
	ofstream ra("ra.out");
	
	int a; 
	string u;
	vao >> a;
	vao.ignore();
	for(int i = 0; i < a; i++){
		getline(vao, u);
		if(u.length() > 10){
			ra << u << endl;
		}
	}
}