#include<bits/stdc++.h>
#include<numeric>
#define ll long long int
using namespace std;

/*この問題は、よく見れば、「各棒の長さの最小公倍数をとる」と読み替えられる
  ため、最小公倍数を求めるプログラムが書けるかが肝。もっとも簡単な方法は、
  ライブラリを使う方法だが、2数をかけたものを2数の最大公約数で割っても出るため
  どちらかで組めれば正解*/

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
//最小公倍数
ll lcm(ll a,ll b)
{
	return a*b/gcd(a,b);
}
int main()
{
	int N;
	cin>>N;
	//初期値は1
	//->0だとlcmが常に0になるため
	ll ans=1;
	//全てのlcmをとるには、順にlcmをとっていけばいい
	for(int i=0;i<N;i++)
	{
		ll l;
		cin>>l;
		ans=lcm(ans,l);
	}
	cout<<ans<<endl;
	return 0;
}
