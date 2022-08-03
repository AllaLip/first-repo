import time
from threading import Thread


def get_thread(thread_name):
	time.sleep(1)
	print(thread_name, end=' ')
    
   
threads = [Thread(target=get_thread, args=(i + 1,)) for i in range(5)]
time1 = time.time() 

for t in threads:
	t.start()
	t.join()
print('\n', f'Время последовательного выполнения: {time.time()-time1}')

threads = [Thread(target = get_thread, args = (i + 1,)) for i in range(5)]
time2 = time.time()

for t in threads:
	t.start()
for t in threads:
	t.join()
print('\n', f'Время параллельного выполнения: {time.time()-time2}')