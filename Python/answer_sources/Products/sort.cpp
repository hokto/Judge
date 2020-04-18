#include<iostream>
#include<vector>

#define ll long long int
#define rep(n) for(int i=0;i<n;i++)
//(1)
class BIT
{
	public:
		//(2)
		std::vector<ll> node;
		ll n_;
		BIT(ll n)
		{
			n_=n;
			node.resize(n+1,0);
		}

		//(3)
		void add(ll i,ll x)
		{
			while(i<=n_)
			{
				node[i]+=x;
				i+=i&-i;
			}
		}

		//(4)
		ll sum(ll i)
		{
			ll s=0;
			while(i>0)
			{
				s+=node[i];
				i-=i&-i;
			}
			return s;
		}
};

int main()
{
	ll n;
	std::cin>>n;
	std::vector<ll> v(n);
	std::vector<ll> p(n);
	BIT *bit_v=new BIT(n);
	BIT *bit_p=new BIT(n);	
	ll cnt_v=0;
	ll cnt_p=0;
	//(5)
	rep(n)
	{
		int v;
		std::cin>>v;
		cnt_v+=i-bit_v->sum(v);
		bit_v->add(v,1);
	}
	//(6)
	rep(n)
	{
		int p;
		std::cin>>p;
		cnt_p+=i-bit_p->sum(p);
		bit_p->add(p,1);
	}
	std::cout<<cnt_v-cnt_p<<std::endl;
	return 0;
}
