/*
 * #include<iostream>
 * #include<vector>
 * #include<string>
*/
#include<bits/stdc++.h>
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
using namespace std;

int main()
{
	int H,W;
	cin>>H>>W;
	vector<string> c(H);
	//スタート地点、ゴール地点の座標を取得しておく
	int s[2];
	int g[2];
	rep(i,H)
	{
		cin>>c[i];
		rep(j,W)
		{
			if(c[i][j]=='s')
			{
				s[0]=j;
				s[1]=i;
			}
			else if(c[i][j]=='g')
			{
				g[0]=j;
				g[1]=i;
			}
		}
	}

	//二次元dpの初期化
	vector<vector<int>> dp(H,vector<int>(W,0));

	//スタート地点を１で初期化
	dp[s[1]][s[0]]=1;

	//右、下に移動するための配列
	int Dir[2][2]={{1,0},
			 {0,1}
			};
	//dpの更新
	rep(i,H)
	{
		rep(j,W)
		{
			rep(k,2)
			{
				//右、もしくは左に行くことができるなら加算
				int cx,cy;
				cx=j+Dir[k][0];
				cy=i+Dir[k][1];
				if(0>cx||cx>=W||0>cy||cy>=H) continue;
				if(c[cy][cx]=='#') continue;
				dp[cy][cx]+=dp[i][j];
				dp[cy][cx]%=MOD;
			}
		}
	}
	//ゴール地点での値が0ならば、スタートからゴールまでたどり着けない
	if(dp[g[1]][g[0]]==0)
	{
		cout<<-1<<endl;
	}
	else
	{
		cout<<dp[g[1]][g[0]]<<endl;
	}
	return 0;
}
