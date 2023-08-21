<<<<<<< HEAD
#include <iostream>
using namespace std;

int main(){
	
}
=======
#include<iostream>

using namespace std;

int main() {
    int n, max;
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++){
        cin >> a[i];
        if(i == 0) {
            max = a[0];
            continue;
        }else{
            if(a[i] > max) max = a[i];
        } 
    }
    cout << max;
    return 0;
}
>>>>>>> a855551 (TC code)
