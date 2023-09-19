transactions_in_cents = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125, -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]
print("Transactions (cents):")
print(transactions_in_cents)

transactions = [transaction / 100 for transaction in transactions_in_cents]
print("Transactions (dollars):")
print(transactions)

transactions.sort()
print("Sorted Transactions:")
print(transactions)

deposits = [transaction for transaction in transactions if transaction >= 0]
withdrawals = [transaction for transaction in transactions if transaction < 0]

print("Deposits:")
print(deposits)
print("Withdrawals:")
print(withdrawals)

def invert_negative_num(negative_num):
  positive_num = negative_num * -1
  return positive_num

withdrawals =  [invert_negative_num(withdrawal) for withdrawal in withdrawals]
print("Withdrawals (positive values):")
print(withdrawals)

largest_withdrawals = withdrawals[:5]
print("Largest Withdrawals:")
print(largest_withdrawals)

average_deposit = sum(deposits) / len(deposits)
average_withdrawal =  sum(withdrawals) / len(withdrawals)

average_deposit = int(average_deposit)
average_withdrawal = int(average_withdrawal)

print("Average Deposit (int):")
print(average_deposit)
print("Average Withdrawal (int):")
print(average_withdrawal)

balance = sum(transactions)

print("Balance:")
print(balance)

total_transactions = len(transactions_in_cents)
print("Total Transactions:")
print(total_transactions)

balance = 0
balances = []

for transaction in transactions_in_cents:
    balance += transaction
    balances.append(balance)

print("Balances after Each Transaction:")
print(balances)

# PL----------------------------------------------------------------

transakcje_w_centach = [1000, -450, 7500, -3475, 13000, -8150, 25000, -850, 0, -1125, -600, 102550, -25025, 6500, -3850, -2500, 1875, 4000]
print("Transakcje (centy):")
print(transakcje_w_centach)

transakcje = [transakcja / 100 for transakcja in transakcje_w_centach]
print("Transakcje (dolary):")
print(transakcje)

transakcje.sort()
print("Posortowane transakcje:")
print(transakcje)

wplaty = [transakcja for transakcja in transakcje if transakcja >= 0]
wyplaty = [transakcja for transakcja in transakcje if transakcja < 0]

print("Wpłaty:")
print(wplaty)
print("Wypłaty:")
print(wyplaty)

def odwroc_liczbe_ujemna(liczba_ujemna):
  liczba_dodatnia = liczba_ujemna * -1
  return liczba_dodatnia

wyplaty = [odwroc_liczbe_ujemna(wyplata) for wyplata in wyplaty]
print("Wypłaty (wartości dodatnie):")
print(wyplaty)

najwieksze_wyplaty = wyplaty[:5]
print("Największe wypłaty:")
print(najwieksze_wyplaty)

srednia_wplata = sum(wplaty) / len(wplaty)
srednia_wyplata = sum(wyplaty) / len(wyplaty)

srednia_wplata = int(srednia_wplata)
srednia_wyplata = int(srednia_wyplata)

print("Średnia wpłata (całkowita):")
print(srednia_wplata)
print("Średnia wypłata (całkowita):")
print(srednia_wyplata)

saldo = sum(transakcje)

print("Saldo:")
print(saldo)

liczba_transakcji = len(transakcje_w_centach)
print("Liczba transakcji:")
print(liczba_transakcji)

saldo = 0
salda = []

for transakcja in transakcje_w_centach:
    saldo += transakcja
    salda.append(saldo)

print("Salda po każdej transakcji:")
print(salda)
