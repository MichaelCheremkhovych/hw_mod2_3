import time
from multiprocessing import Pool, cpu_count

def factorize_single(num):
    # Функція для знаходження множників числа num
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(*numbers):
    # Функція для паралельного розрахунку множників кількох чисел
    # Використовуємо кількість доступних ядер
    pool = Pool(cpu_count())
    result = pool.map(factorize_single, numbers)  # Використовуємо map для паралельного обчислення
    pool.close()  # Закриваємо пул процесів
    pool.join()   # Чекаємо, поки всі процеси завершаться
    return result

if __name__ == "__main__":
    start_time = time.time()
    factorize_parallel(128, 255, 99999, 10651060) 
    end_time = time.time()
    print("Паралельна версія виконана за {} секунд".format(end_time - start_time))
