#include<bits/stdc++.h>
#define ll long long int
using namespace std;

/*制約から、aiが最大で10^9であることから、全てかけてから素因数分解を行うのは不可能
  (Rubyなら可能だと思う)なので、それぞれを素因数分解してからそれらを足し合わせる。
  これは、素因数はもともと素数しか残らないので可能。よって、あとは、素因数分解の
  プログラムが書けるかどうかが肝となる。
*/

//素因数分解
vector<ll> prime_div(ll x)
{
	//素因数を保持しておく
	vector<ll> primes;

	//素因数分解で残るのは、2..√xまでしかない
	for(int i=2;i<=sqrt(x);i++)
	{
		//その数で割り切れるまで割り続ける
		while(x%i==0)
		{
			primes.push_back(i);
			x/=i;
		}
	}
	//最後に残った数が1でなければそれも素因数なので加える
	if(x!=1)primes.push_back(x);
	return primes;
}

int main()
{
	int N;
	cin>>N;
	ll ans=0;
	//各整数の素因数分解を行い、要素数を足し合わせていく
	for(int i=0;i<N;i++)
	{
		ll a;
		cin>>a;
		ans+=prime_div(a).size();
	}
	cout<<ans<<endl;
}
