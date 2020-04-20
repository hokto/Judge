/*
 * #include<iostream>
 * #include<vector>
*/
#include<bits/stdc++.h>
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
using namespace std;

//a,bのうち大きい方を返す
auto max(auto a,auto b)
{
	return a>b ? b : a;
}

int main()
{
	int N;
	cin>>N;
	vector<int> a(N);
	rep(i,N)
	{
		cin>>a[i];
	}
	//０次元dpの初期化
	int dp=0;

	rep(i,N)
	{
		//dpの漸化式(dpの更新)
		dp=max(dp,a[i]);
	}
	cout<<dp<<endl;
	return 0;
}
