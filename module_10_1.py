import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.05)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени перед вызовом функций
start_time = time.time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени после выполнения функций
end_time = time.time()
print(f"Работа функций {time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")

# Функция для создания потоков
def threaded_write_words(word_count, file_name):
    thread = threading.Thread(target=write_words, args=(word_count, file_name))
    return thread

# Взятие текущего времени перед запуском потоков
start_time_threads = time.time()

# Создание и запуск потоков с аргументами из задачи
threads = []
threads.append(threaded_write_words(10, 'example5.txt'))
threads.append(threaded_write_words(30, 'example6.txt'))
threads.append(threaded_write_words(200, 'example7.txt'))
threads.append(threaded_write_words(100, 'example8.txt'))

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени после завершения потоков
end_time_threads = time.time()
print(f"Работа потоков {time.strftime('%H:%M:%S', time.gmtime(end_time_threads - start_time_threads))}")