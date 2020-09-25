#include "Account.h"

using namespace std;
namespace fs = std::filesystem;

Account::Account(){}

bool Account::isMember(string path) {
	return !fs::exists("./user");
}

void Account::create(string path) {
	fs::create_directory("./user");
}

void Account::clear(string path) {
	fs::remove("./user");
}
