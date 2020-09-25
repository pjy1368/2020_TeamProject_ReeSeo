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
		cout << "나이: ";
		cin >> temp;
		out << temp;
		cout << "성별\n";
		cin >> temp;
		out << temp;
		cout << "이름\n";
		cin >> temp;
		out << temp;
		cout << "몸무게\n";
		cin >> temp;
		out << temp;
	}
}

void Account::clear(string path) {
	fs::remove("./user");
}
