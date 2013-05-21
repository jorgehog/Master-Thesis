int main(){

	cout << "-Calling subClass object of type superClass*" << endl; 
	superClass* object = new subClass(); testFunc(object);

	cout << endl <<	"-Calling subClass object of type subClass*" << endl;
	subClass* object2 = new subClass(); testFunc(object);
	
	cout << endl << "-Directly calling object of type subclass*" << endl;
	object2->pureVirtual(); object2->justVirtual(); object2->notVirtual();
	
	return 0;
}