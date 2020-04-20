#include<iostream>
#include<utility>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<deque>
#include<cstring>
#define lint long long int
#define rep(i,n) for(int i=0;i<int(n);i++)
#define per(i,n) for(int i=n-1;i>=0;i--)
#define arep(i,a,n) for(int i=a;i<n;i++)
#define sort(a) sort(a.begin(),a.end())
#define reverse(a) reverse(a.begin(),a.end())
#define fill(a,x) fill(a.begin(),a.end(),x)
#define eb(data) emplace_back(data)
#define pb(data) emplace_back(data)
#define mp make_pair
#define ALNUM 26
#define vint vector<int>
#define F first
#define S second
#define ALL(data) data.begin(),data.end()
using namespace std;
template<typename Rast>inline void out(Rast rast){cout<<rast<<"\n";return;}
template<typename Rast>inline void in(Rast& rast){cin>>rast;return;}
template<typename T>istream& operator >> (istream& is, vector<T>& vec){for(T& x: vec) is >> x;return is;}
template<typename First, typename... Rest>void in(First& first, Rest&... rest){cin >> first;in(rest...);return;}
template<typename First, typename... Rest>void out(First first, Rest... rest){cout << first<<" ";out(rest...);return;}
template<typename T>T gcd( T a,T b){if(b==0)return a;return gcd(b,a%b);}
template<typename T1,typename T2>bool chmax(T1& a,T2 b){if(a<b){a=b;return true;}else{return false;}}
template<typename T1,typename T2>bool chmin(T1& a,T2 b){if(a>b){a=b;return true;}else{return false;}}
template<typename T>T lcm(T a, T b){return a * b / gcd(a, b);}
static const double pi = 3.141592653589793;
lint power(lint N, lint P, lint M){if(P==0) return 1;if(P%2==0){lint t = power(N, P/2, M);return t*t % M;}return N * power(N, P-1, M);}
lint MOD=pow(10,9)+7;
//lint MOD=998244353;
lint inf=pow(2,50);
int intinf=pow(2,30);
/**/int dirx[]={1,0};int diry[]={0,1};//*///右、下
/**int dirx[]={0,1,0,-1};int diry[]={-1,0,1,0};//*///四方位
/**int dirx[]={-1,0,1,1,1,0,-1,-1};int diry[]={-1,-1,-1,0,1,1,1,0};//*///八方位

class unionfind{
public:
	vector<int> table;
	vector<int> wod;
	void init(int size){
		table.resize(size);
		wod.resize(size);
		rep(i,size)table[i]=i,wod[i]=i;
	};
	int root(int index){
		if(table[index]==index)return index;
		else{
			int hoge=root(table[index]);
			table[index]=hoge;
			return hoge;
		}
	};
	bool same(int x,int y){
		return(root(x)==root(y));
	};
	int marge(int x,int y){
		int yroot=root(y);
		int xroot=root(x);
		if(xroot==yroot)return 0;
		table[yroot]=xroot;
		return 0;
	}
};


int main(){
	int h,w;
	in(h,w);
	char table[h][w];
	auto st=mp(0,0);
	auto go=mp(0,0);
	rep(i,h)rep(j,w){
		in(table[i][j]);
		if(table[i][j]=='s')st=mp(i,j);
		if(table[i][j]=='g')go=mp(i,j);
	}
	queue<pair<int,int>> q;
	q.push(st);
	lint hoge[h][w];
	memset(hoge,-1,sizeof(hoge));
	hoge[st.F][st.S]=1;
	rep(i,h)rep(j,w){
		if(i-1<0 || j-1<0 || table[i][j]=='#')continue;
		hoge[i][j]=(hoge[i-1][j]+hoge[i][j-1])%MOD;
	}
	out(hoge[go.F][go.S]);
	return 0;
}
