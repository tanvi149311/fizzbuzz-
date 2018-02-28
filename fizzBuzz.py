class fizzBuzz:
    def getList(self, n):
        #creates an empty list
        result = [];
        
        #for loop checks divisibility conditions and appends values to the list to be returned
        for i in range(1, n+1):
            #checks if divisible by both 3 & 5
            if(i%3 == 0 and i%5 == 0):
                result.append("FizzBuzz");
            #checks if divisible by 3 
            elif(i%3 == 0 ):
                result.append("Fizz");
            #checks if divisible by 5
            elif(i%3 != 0 ):
                result.append("Buzz");
            #if number is not divisible by either
            else:
                result.append(str(i));
                
        return result

def mainMenu():
    #takes input from user and converts it to int
    n = int(input("Enter a whole number"));
    
    #creates an instance of fizzBuzz class
    soln = fizzBuzz();
    
    print(soln.getList(n));

mainMenu();
