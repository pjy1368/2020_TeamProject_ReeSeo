#include "Account.h"

using namespace std;
namespace fs = std::filesystem;

Account::Account(){}

bool Account::isMember(string path) {
	return !fs::exists("./user");
}

void Account::create(string path) {
	fs::create_directory("./user");
	ofstream out("./user/test.txt");
	if (out.is_open()) {
		string temp;
		cout << "����: ";
		cin >> temp;
		out << temp;
		cout << "����\n";
		cin >> temp;
		out << temp;
		cout << "�̸�\n";
		cin >> temp;
		out << temp;
		cout << "������\n";
		cin >> temp;
		out << temp;
	}
}

void Account::clear(string path) {
	fs::remove("./user");
}
