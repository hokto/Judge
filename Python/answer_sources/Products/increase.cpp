#include<iostream>
#include<vector>
#include<queue>
#define ll long long int
#define rep(n) for(int i=0;i<n;i++)

int main()
{
	//(1)
	std::priority_queue< std::pair<ll,ll> > pq;
	int n,m;
	std::cin>>n>>m;
	std::vector<ll> a(n);
	rep(n)
	{
		std::cin>>a[i];
	}
	std::vector<ll> b(n);
	rep(n)
	{
		std::cin>>b[i];
	}
	rep(n)
	{
		//(2)
		a[i]*=-1;
		b[i]*=-1;
		std::pair<ll,ll> p=std::make_pair(a[i],b[i]);
		pq.push(p);
	}
	//(3)
	ll ans=0;
	while(true)
	{
		//(4)
		std::pair<ll,ll> p;
		p=pq.top();
		if(m>p.first*-1)
		{
			pq.pop();
			m+=p.first;
			p.first+=p.second;
			pq.push(p);	
			ans++;
		}
		else
		{
			break;
		}
	}
	std::cout<<ans<<std::endl;
}
