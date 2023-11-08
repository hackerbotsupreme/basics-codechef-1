# cook your dish here
def solution(expression):
    precedence = {'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = []
    output = []
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char in '+-*/^':
            while stack and precedence[char] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ''.join(output)


if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        expression = input()
        print(solution(expression))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#include <iostream>
#include <string>
using namespace std;

int main() {
	int t, n, i, top;
	string s;
	char *st;
	cin>>t;
	while(t--)
	{
	    cin>>s;
	    n= s.size();
	    st= new char[n];
	    top=0;
	    st[top]= '(';
	    for(i=0; i<n; i++)
	    {
	        if(s[i]=='(' || s[i]=='+' || s[i]=='-' || s[i]=='*' || s[i]=='/' || s[i]=='^')
	        {
	            top++;
	            st[top]= s[i];
	        }
	        else if(s[i]==')')
	        {
	            if(st[top]=='(')
	                top--;
	            else
	            {
	                while(st[top]!='(')
	                {
	                    cout<<st[top];
	                    top--;
	                }
	                top--;
	            }
	        }
	        else
	            cout<<s[i];
	    }
	    while(s[top]!='(')
	    {
	        cout<<s[i];
	        top--;
	    }
	    cout<<endl;
	}
	return 0;
}




























#include <iostream>
#include <string>
using namespace std;

int main() {
	int t, n, i, top;
	string s;
	char *st;
	cin>>t;
	while(t--)
	{
	    cin>>s;
	    n= s.size();
	    st= new char[n];
	    top=0;
	    st[top]= '(';
	    for(i=0; i<n; i++)
	    {
	        if(s[i]=='(' || s[i]=='+' || s[i]=='-' || s[i]=='*' || s[i]=='/' || s[i]=='^')
	        {
	            top++;
	            st[top]= s[i];
	        }
	        else if(s[i]==')')
	        {
	            if(st[top]=='(')
	                top--;
	            else
	            {
	                while(st[top]!='(')
	                {
	                    cout<<st[top];
	                    top--;
	                }
	                top--;
	            }
	        }
	        else
	            cout<<s[i];
	    }
	    while(s[top]!='(')
	    {
	        cout<<s[i];
	        top--;
	    }
	    cout<<endl;
	}
	return 0;
}