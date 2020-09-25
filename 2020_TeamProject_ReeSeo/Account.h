#pragma once

class Account {
private:
	int name;
	int sex;
	int age;
	int height;
	int weight;

public:
	Account();
	void isMember();
	void clear();
	void create();
	void modify();
};