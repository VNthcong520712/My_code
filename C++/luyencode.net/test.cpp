#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, b, c, delta;
    double x1, x2;
    cin>>a>>b>>c;
    delta = pow(b,2) - 4*a*c;
    if(b==0&&c==0) { // Phuong trinh co vo so nghiem
        cout<<"INF";
    } else {
    if(a==0) { // Giai phuong trinh bac 1 (a==0)
    if(b==0 && c!=0) {
        cout<<"NO";
    } else {
        cout<< fixed << setprecision(2) << (double) -c/b;
    }        
    } 
	else { // Giai phuong trinh bac 2 (a!=0)
	if(delta<0) {
        cout<<"NO";
    } else if(delta==0) {
        cout<<fixed << setprecision(2)<< (double) -b/2*a;
    } else {
        x1 = (-b - sqrt(delta)) / (2*a); 
        x2 = (-b + sqrt(delta)) / (2*a);
        cout<<fixed << setprecision(2) << x1 <<" "<< fixed << setprecision(2) << x2 <<endl;
    }        
    }}
    return 0;
}