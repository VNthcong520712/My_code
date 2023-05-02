#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_N 1001

char * nhap(){
    static char st[MAX_N];
    gets(st);
    return st;
}

char * dao(char *a){
    int i,j;
    char temp;
    for(i=0,j=strlen(a)-1; i<j; i++,j--){
        temp=a[i];
        a[i]=a[j];
        a[j]=temp;
    }
    return a;
}

void hienthi(char *b){
    int i, j, cd = -1, cc = strlen(b);
    for(i = 0, j = strlen(b); i < strlen(b), j >= 0; i++, j--){ 
        if (b[i] == 48){
            cd = ((i > cd) && (abs(i - cd) == 1)) ? i : cd;
        }

        if (b[j] == 48){
            cc = ((j < cc) && (abs(j - cc) == 1)) ? j : cc;
        }
    }
    for (int z = cd+1; z < cc; z++){
        printf("%c",b[z]);
    }
}

int main(){
    char *s = nhap();
    double n;
    sscanf(s,"%lf",&n);
    if ((n > 0) && (strlen(s) <= 1000)){
        hienthi(dao(s));
    }
}