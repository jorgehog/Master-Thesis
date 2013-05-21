#include <iostream>
using namespace std;

class superClass{
public:
	// virtual = 0 implies pure virtual
	virtual void pureVirtual() = 0; 
	virtual void justVirtual() {cout << "superclass virtual"    << endl;}
	void notVirtual()          {cout << "superclass notVirtual" << endl;}
};

class subClass : public superClass{
public:	
	void pureVirtual() {cout << "subclass pure virtual override"     << endl;}
	void justVirtual() {cout << "subclass standard virtual override" << endl;}
	void notVirtual()  {cout << "subclass non virtual"               << endl;}
};

//Testfunc is set to retrieve a superClass pointer, then calls all the functions.
void testFunc(superClass* someObject){
	someObject->pureVirtual(); someObject->justVirtual(); someObject->notVirtual();
}


