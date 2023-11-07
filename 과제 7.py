'''burger_prices = [int(input()) for _ in range(3)]

drink_prices = [int(input()) for _ in range(2)]

set_menu_prices = [burger_price + drink_price - 50 for burger_price in burger_prices for drink_price in drink_prices]

min_set_menu_price = min(set_menu_prices)

print(min_set_menu_price)'''


'''remainders = [int(input()) % 42 for _ in range(10)]

unique_remainders = len(set(remainders))
print(unique_remainders)'''

# 주어진 문자열
text = "This is a more advanced comprehension exercise to practice"

# 문자열을 공백으로 분리하여 단어 리스트 생성
words = text.split()

# 길이가 5 이상인 단어의 알파벳을 역순으로 만들어 리스트 생성
reversed_words = [word[::-1] for word in words if len(word) >= 5]

# 결과 출력
print(reversed_words)


