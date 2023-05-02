#include <iostream> 
using namespace std;

int n;

int main(){
    cout << "nhap vao n: ";
    cin >> n;
    cout << "cac uoc cua " << n << " la: " ;
    for (int i=-n; i <= n; i++){
        if (n%i == 0){
            cout << i <<" ";
        }
        if (i == -1){
            i++;
        }
    } 
}