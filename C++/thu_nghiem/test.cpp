#include <iostream>
using namespace std;

int abs(int u){
	if (u < 0){
		u = -u;
	}
	return u; 
}

int max(int x, int y){
	int max = (int) (abs(x-y) + x + y)/2;
	return max;
}

int min(int x, int y){
	int min = (int) (abs(x-y) - x - y)/2;
	return min;
}

int main(){
	int a, b, c;
	cin >> a >> b >> c;
	cout << max(max(a,b),c) << "\n" << min(min(a, b), c);

}