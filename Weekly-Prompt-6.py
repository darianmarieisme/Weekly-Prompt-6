'''Weekly Prompt 6 Option 2
Darian Marie Bruce
02/22/2026
Discuss the input() function and its limitation in assigning a value to a variable. 
What is a common cast to convert a string to another data type?


Saving variables from the input functions saves the data only as
a string type. This means that no matter what is typed into the input
field, the program will treat it as a string. This can cause problems
if you are asking for numbers and are wanting to use the input in mathematical
functions. 

Using the int() function is a way to get around this limitation because using int()
around the string variable will convert the string into an integer, only with the case that
all numbers in the string are numeric values. Leading and trailing white spaces are also
interpreted by the int() function and removed, returning the integer value. However decimals
are not interpreted and this would require a float() function.

'''