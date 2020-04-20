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
	int N,M;
	cin>>N>>M;
	vector<int> a(M);
	rep(i,M)
	{
		cin>>a[i];
	}

	//一次元dpの初期化
	vector<int> dp(N+1,0);
	dp[0]=1;
	//dpの更新
	rep(i,N)
	{
		//普通に1段登った場合を加算
		dp[i+1]+=dp[i];
		dp[i+1]%=MOD;
		rep(j,M)
		{
			//テレポートした場合を加算
			if(i+a[j]>N) continue;
			dp[i+a[j]]+=dp[i];
			dp[i+a[j]]%=MOD;
		}
	}
	cout<<dp[N]<<endl;
	return 0;
}
