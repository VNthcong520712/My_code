#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	float a[3] = {};
    cout << "nhap 3 so can sap xep: ";
    cin >> a[0] >> a[1] >> a[2];
    sort(a, a + 3);
    cout << "sap xep cac so nhap vao: \n "<< a[0] << " " <<a[1] << " " << a[2] << endl;
}
