/*
 * #include<iostream>
 * #include<vector>
*/
#include<bits/stdc++.h>
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
using namespace std;

int main()
{
	int N,M,K;
	cin>>N>>M>>K;
	vector<int> a(M);

	rep(i,M)
	{
		cin>>a[i];
	}
	//map(連想配列)を使って計算量を軽減
	map<int,int> NG;
	rep(i,K)
	{
		int ng;
		cin>>ng;
		NG[ng]=1;
	}
	//一次元dpの初期化	
	vector<int> dp(N+1,false);
	rep(i,M)
	{
		//NG数とaiが同じではない時だけ、trueにする
		if(NG[a[i]]!=1) dp[a[i]]=true;
	}
	//dpの更新
	for(int i=1;i<N+1;i++)
	{
		rep(j,M)
		{
			//dp[i]にすることができてかつ、NG数出ないならtrue
			if(i*a[j]>N) continue;
			if(dp[i]&&NG[i]!=1) dp[i*a[j]]=true;	
		}
	}
	if(dp[N])
	{
		cout<<"Yes"<<endl;
	}
	else
	{
		cout<<"No"<<endl;
	}
}
