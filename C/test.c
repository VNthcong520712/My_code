#include <stdio.h>

double nhiphan(unsigned long long a){
    if ( a == 0){
        return 0;
    }
    int d = a%2;
    long long n = (a-d)/2;
    return (nhiphan(n)*10 + d);
}

int main(){
	long T;
    scanf("%ld", &T);
    if ((1 <= T) && (T <= 100000)){
        unsigned long long n[T];
        double kq[T];
        for (int i = 0; i < T; i++){
            scanf("%lld", &n[i]);
            if ((n[i] < 1) || (n[i] > 1000000000000000000)){
                break;
            }
            kq[i] = nhiphan(n[i]);
        }
        for (int i = 0; i < T; i ++){
            printf("%.0lf\n", kq[i]);
        }
    }
}