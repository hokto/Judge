#include<iostream>
#include<vector>

#define ll long long int
#define rep(n) for(int i=0;i<n;i++)

//(1)
class LazySegTree
{
	public:
		//(2)
		std::vector<ll> node;
		std::vector<ll> lazy;
		ll n_;
		LazySegTree(ll n)
		{
			n_=1;
			while(n_<n)
			{
				n_*=2;
			}
			node.resize(2*n_-1);
			rep(2*n_-1)
			{
				node[i]=0;
			}
			lazy.resize(2*n_-1);
			rep(2*n_-1)
			{
				lazy[i]=0;
			}
		}
		//(3)
		void lazy_eval(ll i,ll l,ll r)
		{
			if(lazy[i]!=0)
			{
				node[i]+=lazy[i];
				if(r-l>1)
				{
					lazy[i*2+1]+=lazy[i]/2;
					lazy[i*2+2]+=lazy[i]/2;
				}
				lazy[i]=0;
			}
		}
		//(4)
		void Add(ll s,ll t,ll x,ll i,ll l,ll r)
		{
			lazy_eval(i,l,r);
			if(r<=s || t<=l)
			{
				return;
			}
			if(s<=l && r<=t)
			{
				lazy[i]=x*(r-l);
				lazy_eval(i,l,r);
			}
			else
			{
				ll mid=(l+r)/2;
				Add(s,t,x,i*2+1,l,mid);
				Add(s,t,x,i*2+2,mid,r);
				node[i]=node[i*2+1]+node[i*2+2];
			}
		}

		//(5)
		ll getSum(ll s,ll t,ll i,ll l,ll r)
		{
			if(r<=s || t<=l)
			{
				return 0;
			}
			lazy_eval(i,l,r);
			if(s<=l && r<=t)
			{
				return node[i];
			}

			ll mid=(l+r)/2;
			ll leaf_l=getSum(s,t,i*2+1,l,mid);
			ll leaf_r=getSum(s,t,i*2+2,mid,r);
			return leaf_l+leaf_r;
		}
};
int main()
{
	ll n,m;
	std::cin>>n>>m;
	LazySegTree *lst=new LazySegTree(n);
	//(6)
	rep(n)
	{
		ll a;
		std::cin>>a;
		lst->Add(i,i+1,a,0,0,lst->n_);
	}
	rep(m)
	{
		ll l,r,x;
		std::cin>>l>>r>>x;
		l--;
		r--;
		//(7)
		std::cout<<lst->getSum(l,r+1,0,0,lst->n_)<<std::endl;
		//(8)
		lst->Add(l,r+1,x,0,0,lst->n_);
	}
	return 0;
}
