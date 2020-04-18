/*
 * #include<iostream>
 * #include<vector>
*/
#include<bits/stdc++.h>
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
using namespace std;

#define INF 2<<30-1

//a,bのうち、小さい方を返す
auto min(auto a,auto b)
{
	return a>b ? b : a;
}
int main()
{
	string s,t;
	cin>>s;
	cin>>t;
	//S,Tの大きさを持っておく
	int Ns=s.size();
	int Nt=t.size();
	//二次元dpの初期化
	vector<vector<int>> dp(Ns+1,vector<int>(Nt+1,INF));
	dp[0][0]=0;
	//dpの更新
	rep(i,Ns)
	{
		rep(j,Nt)
		{
			//si,tjが同じなら、cを1、違うならcを0にする
			int c=(s[i]==t[j]) ? 0 : 1;
			dp[i+1][j+1]=min(dp[i][j+1],dp[i+1][j])+1;
			dp[i+1][j+1]=min(dp[i+1][j+1],dp[i][j]+c);
		}
	}
	cout<<dp[Ns][Nt]<<endl;
	return 0;
}
