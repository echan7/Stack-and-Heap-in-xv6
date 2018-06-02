#include "types.h"
#include "stat.h"
#include "user.h"


int main(){
        char* p = (char*)&main;
	*p = 'x';
        exit();
}

