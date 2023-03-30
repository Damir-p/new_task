"""Для этого необходимо собрать исторические данные о цене ETHUSDT и BTCUSDT за определенный период времени. 
Затем можно построить модель, в которой зависимой переменной будет цена ETHUSDT, а независимыми 
переменными - цена BTCUSDT и другие факторы, которые могут влиять на цену ETHUSDT, например, объем 
торгов, количество открытых позиций, новости и т.д.

Далее необходимо провести статистический анализ модели и оценить коэффициенты регрессии. Если коэффициент 
при переменной BTCUSDT значимо отличается от нуля, то это говорит о наличии связи между ценами ETHUSDT 
и BTCUSDT. В таком случае можно использовать остатки регрессии, чтобы определить собственные движения 
цены ETHUSDT, исключив из них движения, вызванные влиянием цены BTCUSDT.

Подбор параметров для модели множественной регрессии зависит от выбора метода оценки параметров, например,
метода наименьших квадратов или метода максимального правдоподобия. Также важно выбрать период 
исторических данных для построения модели, который должен быть достаточно длинным, чтобы учесть 
различные макроэкономические и фундаментальные факторы, влияющие на цену криптовалюты."""

import time
import requests

percent_change_threshold = 1
time_window = 60 * 60  
def get_eth_price():
    url = 'https://api.binance.com/api/v1/ticker/price?symbol=ETHUSDT'
    response = requests.get(url)
    data = response.json()
    return float(data['price'])

current_price = get_eth_price()
last_check_time = time.time()
while True:
    new_price = get_eth_price()
    price_change = (new_price - current_price) / current_price * 100
    current_time = time.time()
    time_since_last_check = current_time - last_check_time
    if price_change > percent_change_threshold and time_since_last_check > time_window:
        print(f"Price change: {price_change}% over the last {time_window/60} minutes")
        last_check_time = current_time
    current_price = new_price
    time.sleep(5)