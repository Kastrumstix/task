import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.print_lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                with self.print_lock:
                    print(f"Пополнение: {amount}. Баланс: {self.balance}")
                if self.balance >= 500:
                    pass
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.print_lock:
                print(f"Запрос на {amount}")
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    with self.print_lock:
                        print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    with self.print_lock:
                        print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
