//
//  main.cpp
//  Hokuto 4.18
//
//  Created by 吉永大翔 on 2020/04/18.
//  Copyright © 2020 吉永大翔. All rights reserved.
//

#include <iostream>
using namespace std;
int main(){
    int a,b=0,c;
    cin>>a;
    for(int i=0;i<a;i++){
        cin>>c;
        if(c>b){
            b=c;
        }
    }
    cout<<b<<endl;
}
