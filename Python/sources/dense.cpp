#include<bits/stdc++.h>

#define ll long long int

using namespace std;
/*問題の通り、最大公約数が組めればいい*/

//最大公約数
ll gcd(ll a,ll b)
{
	if(a%b==0)
	{
		return b;
	}
	else
	{
		return gcd(b,a%b);
	}
}
int main()
{
	int A,B;
	cin>>A>>B;
	if(gcd(A,B)==1)
	{
		cout<<"Sparse"<<endl;
	}
	else
	{
		cout<<"Dense"<<endl;
	}
}
