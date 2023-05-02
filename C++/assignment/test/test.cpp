#include <iostream>
#include <String>
using namespace std;

int main(){
    cout << "\nQUYET TAM CUA BAN LA GI?\n" << endl;
    string quyettam;
    getline(cin, quyettam);
    for(int i = 0; i <= 1000; i++){
      cout << quyettam << endl;
    }
    cout << "\nDUNG NGAI CHONG GAI, SAN SANG BUOC TIEP, TUONG LAI NAM TRONG TAM TAY BAN\n\n" << endl;
}
