def rounder(number, round_to_near):
    """This function is used to round the integer to the desired nearest value
    So if you want to round the integer to multiple of 5 => 38->40 and 31->30
    You can use the function as rounder(38,5)=>return 40 and rounder(31,5)=>return 30
    """

    def round_up(number):
        while number % round_to_near != 0:
            number += 1
        return number

    def round_down(number):
        while number % round_to_near != 0:
            number -= 1
        return number

    if number % 10 in [1, 2, 6, 7]:
        return round_down(number)
    if number % 10 in [3, 4, 5, 8, 9]:
        return round_up(number)

#Sample call to the function
print(rounder(32, 10))
