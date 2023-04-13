def return_a_string(int):
    answer = str(int)
    return answer

def fizz_divisible_by_3(int):
    if int % 3 == 0:
        return "Fizz"
    
def buzz_divisible_by_5(int):
    if int % 5 == 0:
        return "Buzz"
    
def fizz_buzz_divisible_by_15(int):
    if int % 15 == 0:
        return "Fizz Buzz"
    

def fizzbuzz_game(game_range):
    for number in range(game_range):
        if fizz_buzz_divisible_by_15(number):
            print("FizzBuzz")
        elif buzz_divisible_by_5(number):
            print("Buzz")
        elif fizz_divisible_by_3(number):
            print("Fizz")
        else:
            print(str(number))
            
        

