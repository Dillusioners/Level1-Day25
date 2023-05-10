# include <iostream>

// execution starts from here
int main(int argc, char** argv){
	// variable declaration here
	int passed, total;
	float perc;
	
	// asking for the total students from user
	std::cout << "How many students were total in the exam?: ";
	std::cin >> total;
	
	// asking for the passed count from user
	std::cout << "How many of them passed?: ";
	std::cin >> passed;
	
	// checking if passed or total count is negative, then making them posititve
	if(passed < 0) passed *= -1;
	if(total < 0) total *= -1; 	
	// checking if more students passed than the total
	if(passed > total){
		std::cout << "Passed students cannot be more than total students.\n";
		return 0;	
	}
	// checking if the total is zero, to prevent Zero Division Error
	if(total == 0){
		std::cout << "No need to calculate the percentage if noone came.";
		return 0;
	}
	
	// calculates the floating part of the passed by total
	// and multiplies the result by 100
	perc = (passed / (float)total) * 100;
	// printing the percentage
	std::cout << "Total percentage of passed students is " << perc << "%\n";
	
	return 0;	
}
