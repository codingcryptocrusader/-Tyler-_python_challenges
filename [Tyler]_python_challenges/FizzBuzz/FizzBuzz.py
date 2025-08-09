 def custom_fizzbuzz():
    rules = {
        3: "Fizz",
        5: "Buzz",
        7: "Bang",
        11: "Bong",
        13: "Boing",
        17: "Bonk"
    }

    for num in range(1, 101):
        output = ''.join(word for div, word in rules.items() if num % div == 0)
        print(output or num)

if __name__ == "__main__":
    custom_fizzbuzz()
