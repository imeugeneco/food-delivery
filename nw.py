from selenium_class import Driver
import time
import json


def now_waiting(driver, date):
    url = "https://nowwaiting.co/api/v2/spots/5185/stats/orders?created_on={date}&page=1&count=1000&order_type=&payment_type=".format(date = date)
    login_url = "https://ceo.nowwaiting.co/order_sales/history"
    driver.get_url(login_url)

    driver.get_url(url)
    pre = driver.find_by_tag("pre").text
    j = json.loads(pre)['data']['orders']
    with open('data/now_waiting/' + date + '.json', 'w', encoding='UTF-8')as file:
        file.write(json.dumps(j))


    # import pandas as pd
    # with open('data/dummy.json', 'r', encoding='UTF-8')as file:
    #     x = json.load(file)['data']['orders']
    #     if len(x) == 0:
    #         print("주문 내역이 없습니다.")
    #         return driver
    #
    #     with open('data/now_waiting/' + date + '.json', 'w', encoding='UTF-8') as file2:
    #         file2.write(x)
    #
    #
    #     df = pd.DataFrame(x)
    #     df.to_csv('data/now_waiting/' + date + '.csv', index=False, mode='w', encoding='utf-8-sig')

    return driver

if __name__ == '__main__':
    driver = Driver()
    now_waiting(driver, '2020-08-25')
