number = 1
while number <= 100:
    string = "";
    if number % 3 == 0:
        string = string + "Fizz";
    if number % 5 == 0:
        string = string + "Buzz";
    if string == "":
        string = string + str(number)
    print(string)
    number += 1
