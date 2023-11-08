T=int(input())
for o in range(T):
    scores=dict()
    for j in range(4):
        team,score=map(str,input().split(" "))
        score=int(score)
        scores[team]=score
    if scores["RealMadrid"]<scores["Malaga"] and scores["Barcelona"]>scores["Eibar"]:
        print("Barcelona")
    else:
        print("RealMadrid")
        
        
        
        
        
        
        
        
        
        
        
        
        
# cook your dish here
for _ in range(int(input())):
    e=0
    b=0
    r=0
    m=0
    for i in range(4):
        
        dic=(input().split(" "))
        if "Eibar" in dic:
            e=int(dic[1])
        elif("Barcelona" in dic):
            b=int(dic[1])
        elif("Malaga" in dic):
            m=int(dic[1])
        else:
            r=int(dic[1])
    if(b>e and r<m):
        print("Barcelona")
    else:
        print("RealMadrid")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
using namespace std;

int main() {
    int t;  cin>>t;
    int bg, mg, rg, eg;
    string team;
    while(t--){
        
            for(int i=1; i<=4; i++){
                cin>>team;
                if(team == "Barcelona") cin>>bg;
                else if(team == "Malaga") cin>>mg;
                else if(team == "RealMadrid") cin>>rg;
                else if(team == "Eibar") cin>>eg;
            }
            
            if(bg>eg && rg<mg) cout<<"Barcelona\n";
            else cout<<"RealMadrid\n";
        
    }
	
	return 0;
}


















#include <iostream>
using namespace std;

int main() {
    int t;  cin>>t;
    int bg, mg, rg, eg;
    string team;
    while(t--){
        
            for(int i=1; i<=4; i++){
                cin>>team;
                if(team == "Barcelona") cin>>bg;
                else if(team == "Malaga") cin>>mg;
                else if(team == "RealMadrid") cin>>rg;
                else if(team == "Eibar") cin>>eg;
            }
            
            if(bg>eg && rg<mg) cout<<"Barcelona\n";
            else cout<<"RealMadrid\n";
        
    }
	
	return 0;
}
