#include<iostream>
#include<string.h>
#include<map>
#include <bits/stdc++.h>
#include <unistd.h>
#define MAX 26
using namespace std;
//declaring map
map<char,char> mapname;
void shuffle_array(char arr[], int n) 
{ 
  
    //using seed as 8
    unsigned seed = 8; 
  
    
    shuffle(arr, arr + n, 
            default_random_engine(seed)); 
  
   
    
}

//encryption logic
void encrypt(string s){
	for(int i=0;s[i]!='\0';i++){
		s[i]=mapname[s[i]];	
	}
	
	cout<<s<<endl;
}


//main function
int main(){
	
	
	
    	char alphabet[MAX] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
                          'h', 'i', 'j', 'k', 'l', 'm', 'n',  
                          'o', 'p', 'q', 'r', 's', 't', 'u', 
                          'v', 'w', 'x', 'y', 'z' };
	
	char shuffled[MAX] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
                          'h', 'i', 'j', 'k', 'l', 'm', 'n',  
                          'o', 'p', 'q', 'r', 's', 't', 'u', 
                          'v', 'w', 'x', 'y', 'z' };
	
	int n = sizeof(shuffled) / sizeof(shuffled[0]); 
  
    	shuffle_array(shuffled, n); 
	
	for (int i = 0; i < 26; i++){
		char ch=alphabet[i];
		char ch1=shuffled[i];
		cout<<ch<<" = "<<ch1<<endl;
		mapname[ch]=ch1;
	}
	
	cout<<"Enter Plain Text"<<":";
	string in;
	cin>>in;
	cout<<"Encryption in Progress"<<endl;
	encrypt(in);
	
	
	  
}
