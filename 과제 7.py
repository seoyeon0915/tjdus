'''burger_prices = [int(input()) for _ in range(3)]

drink_prices = [int(input()) for _ in range(2)]

set_menu_prices = [burger_price + drink_price - 50 for burger_price in burger_prices for drink_price in drink_prices]

min_set_menu_price = min(set_menu_prices)

print(min_set_menu_price)'''


'''remainders = [int(input()) % 42 for _ in range(10)]

unique_remainders = len(set(remainders))
print(unique_remainders)'''

text = "This is a more advanced comprehension exercise to practice"

words = text.split()

reversed_words = [word[::-1] for word in words if len(word) >= 5]

print(reversed_words)


