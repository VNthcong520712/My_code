#include <iostream>
#include <string>
using namespace std;

pair<int,int> line[100006];
bool used[100006] = {false};
int n, s, t;
string out = "";

void fin(int st, int lo){
	if(line[lo].second == t && line[lo].first == st) {
		out += char(line[lo].first+48);
		out += ' ';
		out += char(line[lo].second+48);
		return;
	}
	else if(lo > n-1) return;
	int nst;
	for(int i = 0; i < n-1; i++){
		if(!used[i] && line[i].first == st){
			nst = line[i].second;
			used[i] = true;
			break;
		}
	}
	// cout << st << ' ' << nst << ' ' << lo << endl;
	out += char(st + 48);
	out += ' ';
	fin(nst, lo+1);
	return;
}

int main(){
	cin >> n >> s >> t;
	for(int i = 0; i < n-1; i++ ){
		cin >> line[i].first >> line[i].second;
	}
	fin(s, 0);
	cout << out;
}