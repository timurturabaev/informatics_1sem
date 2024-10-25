n = 120
#a = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000]
a = [10, 60, 100]
k = len(a)

INF = 1e10; # Значение константы "бесконечность"
F = [0] * (n + 1)
F[0] = 0

for m in range(1, n + 1): # заполняем массив A
                       # m - сумма, которую нужно выдать
    F[m] = INF         # помечаем, что сумму i выдать нельзя
    for i in range(k): # перебираем все номиналы банкнот
        if m >= a[i] and F[m - a[i]] + 1 < F[m]:
            F[m] = F[m-a[i]]+1 # изменяем значение F[m], если нашли лучший способ выдать сумму m

if F[n] == INF:
    print("Требуемую сумму выдать невозможно")
else:
    while n > 0:
        for i in range(k):
            if F[n - a[i]] == F[n] - 1:
                print(a[i], end=' ')
                n -= a[i]
                break
    print('\n', end='')

# Моё самописное решение -- более изящное и "питонистское", на мой взгляд
# Во-первых, мы не перебираем каждую сумму денег от 1 до n + 1, а лишь те, что можно выдать комбинацией наших банкнот
# Во-вторых, для хранения данных используем словарь, где каждой рассмотренной сумме ставим в соответствие купюру,
# добавлением которой сумма получена -- это позволяет более явно получить разложение суммы по банкнотам после решения задачи
'''
amount = 125
bills = [10, 60, 100]

cash_dictionary = {0: 0}
cash_sums_added = 1
while amount not in cash_dictionary and cash_sums_added:
    cash_sums_added = 0
    current_sums = list(cash_dictionary.items()).copy()
    for cash in current_sums:
        for bill in bills:
            if cash[0] + bill not in cash_dictionary and cash[0] + bill < amount:
                cash_dictionary[cash[0] + bill] = bill
                cash_sums_added += 1

print(amount in cash_dictionary)
if amount in cash_dictionary:
    while amount > 0:
        print(cash_dictionary[amount], end=' ')
        amount -= cash_dictionary[amount]
    print('\n', end='')
'''