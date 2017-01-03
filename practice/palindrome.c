#include "stdio.h"

int find_palindrome(char * palindrome, int size){
	int x =0;
	for(x=0;x<=size/2;x++){
		if (palindrome[x] == palindrome[size-x-1]){
			//we gucci
			continue;
		}
		else
			return 0;
	}
	return 1;
}

int find_palindrome_bit(char * palindrome, int size,  int start){
	int x =0;
	for(x=start;x<=size;x++){
		if (palindrome[x] == palindrome[size-x-1]){
			//we gucci
			continue;
		}
		else
			return 0;
	}
	return 1;
}


void find_longest_palindrome(char * palindrome, int size){
	int x,y,z;
	for(x=0;x<size;x++){
		for(y=0;y<size;y++){
			if(find_palindrome_bit(palindrome, size -y, x) == 1){
				printf("found palindrome section \n");
				for(z=x;z<size-y;z++)
					printf("%c", palindrome[z]);
				printf("\n");
			}
		}
	}
}



void main(){
	char * my_palindrome = "aba"; 
	//my_palindrome = "abcde";
	int x = 0;
	while (*my_palindrome!='\0'){
		printf("%c", *my_palindrome);
		my_palindrome++;
		x++;
	}
	my_palindrome = my_palindrome - x;
	printf("\n");
	if (find_palindrome(my_palindrome, x)==1)
		printf("It is an Palindrome! \n");
	else
		printf("It is not an Palindrome! \n");
	find_longest_palindrome(my_palindrome, x);
}
