#pragma once
#include <filesystem>
#include <iostream>
#include <string>


using namespace std;

class Account {
private:
	int name;
	int sex;
	int age;
	int height;
	int weight;

public:
	Account();
	bool isMember(string path);
	void create(string path);
	void clear(string path);
	//void modify();
};