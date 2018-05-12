/***gcc -o libpycall.so -shared -fPIC pycall.c*/ 
 
#include <iostream>
using namespace std;

extern "C" { 
	void dosomething(int n){
		for(int i = 0; i < n; i++) i *= 2;
	}
}