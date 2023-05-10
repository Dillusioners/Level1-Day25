# function to print the list
def printList(list_, sep):
    # looping through the list and printing the current index
    for i in list_:
        print(i, end=sep)

# execution begins from this function
def main():
    # asking user for total strings
    total = input("How many string do you want to print?: ")
    list_ = [] # the list which will store all the strings
    
    # try-catch block to ensure user input was infact a string
    try:
        total = int(total)
        
    except ValueError:
        print("That is not a valid integer!")
        return
     
    # looping for the given total  
    for i in range(1, total + 1):
        # asking user for the strings
        inp = input(f"Enter string no.{i}: ")
        list_.append(inp)
    
    # printing list before sorting 
    print("\nList before sorting:")
    printList(list_, " ")
    
    # sorting the list and printing it
    print("\nList after sorting:")
    list_.sort()
    printList(list_, " ") 

# running the program  
if __name__ == "__main__":
    main()
