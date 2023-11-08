#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int a,b;
	    cin>>a>>b;
	    int c=a/(b*b);
	    if(c<=18)
	      cout<<1<<endl;
	    else if(c>=19 and c<=24)
	      cout<<2<<endl;
	    else if(c>=25 and c<=29)
	      cout<<3<<endl;
	    else
	      cout<<4<<endl;
	}
	return 0;
}






#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int m,h;
	    cin>>m>>h;
	    int BMI = (m/(h*h));
	    if(BMI<=18)
	    cout<<"1"<<endl;
	    else if(BMI>=19 && BMI<=24)
	    cout<<"2"<<endl;
	    else if(BMI>=25 && BMI<=29)
	    cout<<"3"<<endl;
	    else if(BMI>=30)
	    cout<<"4"<<endl;
	}
	return 0;
}







#include <iostream>
using namespace std;

int main() {
	int t,m,h;
	cin >>t;
	while(t--){
	    cin >>m>>h;
	    if(m/(h*h)<=18)
	    cout <<"1"<<endl;
	    else if(m/(h*h)<25)
	    cout <<"2"<<endl;
	    else if(m/(h*h)<30)
	    cout <<"3"<<endl;
	    else 
	    cout <<"4"<<endl;
	}
	return 0;
}














#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int m,h,x;
        cin>>m>>h;
        x=m/(h*h);
        if (x<=18)
        cout<<"1"<<endl;
        else if (x==19||x==20||x==21||x==22||x==23||x==24)
        cout<<"2"<<endl;
        else if (x==25||x==26||x==27||x==28||x==29)
        cout<<"3"<<endl;
        else 
        cout<<"4"<<endl;
    }
	// your code goes here
	return 0;
}










#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int m,h;
	    cin>>m>>h;
	    int n=(m/(h*h));
	    if(n<=18){
	        cout<<"1"<<endl;
	    }
	    else if(n>=19 && n<=24){
	        cout<<"2"<<endl;
	    }
	    else if(n>=25 && n<=29){
	        cout<<"3"<<endl;
	    }
	    else if(n>=30){
	        cout<<"4"<<endl;
	    }
	}
	return 0;
}


