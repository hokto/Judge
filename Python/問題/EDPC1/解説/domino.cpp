/*
 * #include<iostream>
 * #include<vector>
*/
#include<bits/stdc++.h>
#define MOD 1000000007
#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
using namespace std;

void reverseLIS(int N,vector<int> a)
{
	//aの並びを逆転させる
	reverse(a.begin(),a.end());
	//dpの初期化
	vector<int> dp;
	//dpの大きさを持っておく
	int n=0;
	rep(i,N)
	{
		//dpに何も入っていない or 最後の要素よりもaiの方が小さい時にpushする
		if(n==0||dp[n-1]<a[i])
		{
			dp.push_back(a[i]);
			n++;
		}
		else
		{
			//そうでなければ、二分探索(ただし、dpは昇順整列)して、最もa[i]に近い値を更新する
			auto iter=lower_bound(dp.begin(),dp.end(),a[i]);
			*iter=a[i];
		}
	}
	cout<<n<<endl;
}
void LDS(int N,vector<int> a)
{
	//dpの初期化
	vector<int> dp;
	//dpの大きさを持っておく
	int n=0;
	rep(i,N)
	{
		//dpに何も入っていない or 最後の要素よりもaiの方が小さい時にpushする
		if(n==0||dp[n-1]>a[i])
		{
			dp.push_back(a[i]);
			n++;
		}
		else
		{
			//そうでなければ、二分探索(ただし、dpは降順整列)して、最もa[i]に近い値を更新する
			int head=0;
			int tail=n-1;
			rep(j,100)
			{
				int mid=(head+tail)/2;
				if(dp[mid]<=a[i])
				{
					tail=mid;
				}
				else
				{
					head=mid;
				}
			}
			dp[tail]=a[i];
		}
	}
	cout<<n<<endl;
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
	//方法１
	reverseLIS(N,a);

	//方法２
	//LDS(N,a);
}
