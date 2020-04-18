#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int n=0;
	int m=0;
	int x=0;
	long long int y=0;
	cin>>n>>m;
	vector<long long int> a(n);
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
	}
	for(int i=0;i<m;i++)
	{
		cin>>x>>y;
		a[x-1]+=y;
	}
	for(int i=0;i<n;i++)
	{
		cout<<a[i]<<" ";
	}
	cout<<endl;
	return 0;
}