#include <stdio.h>
#include <iostream>
using namespace std;
int main(void){
	int a,b,c,d;
	int s;
	cin>>a >>b >>c >>d;
	if (a < b)
		s+=a;
	else
		s+=b;

	if (c < d)
		s+=c;
	else
		s+=d;
	printf("%d",s);
	return 0;
}
