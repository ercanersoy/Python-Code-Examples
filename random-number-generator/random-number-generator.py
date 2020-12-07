from random import uniform

random_number_count = int(input("How many random number: "))
minimum_random_value = float(input("Minimum random value: "))
maximum_random_value = float(input("Maximum random value: "))

while random_number_count != 0:
    print(uniform(minimum_random_value, maximum_random_value))

    random_number_count -= 1