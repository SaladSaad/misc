#include <iostream>
using namespace std;

int main() {
  int age;
  string name;
  cout << "enter name and age"<<endl;
  getline(cin, name);
  cin>>age;

  cout<<"Name: "<<name<<" age: "<<age<<endl;
}