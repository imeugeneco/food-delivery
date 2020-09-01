import time
import json
import pandas as pd

def baemin(driver, date):
    # driver.get_url("https://ceo.baemin.com/self-service/orders/history")
    if  driver.driver.title == "ERROR: The request could not be satisfied":
        return False


    url = "https://ceo.baemin.com/v1/orders?__ts=1598455546716&sort=ORDER_DATETIME&shopNo=&adInventoryKey=&purchaseType=&orderStatus=CLOSED&startDate={start}&endDate={end}&offset=0&limit={limit}&token="
    url = url.format(start = date, end = date, limit=1000)
    driver.get_url(url)
    pre = driver.find_by_tag("pre").text

    with open('data/dummy.json', 'w', encoding='UTF-8')as file:
        file.write(pre)



    with open('data/dummy.json', 'r', encoding='UTF-8')as file:
        x = json.load(file)['data']['histories']
        if len(x) == 0:
            print(date, "배민 주문 내역이 없습니다.")
            with open('data/baemin/' + date + '.json', 'w', encoding='UTF-8') as file2:
                temp = []
                file2.write(json.dumps(temp))

        else:
            df = pd.DataFrame(x)
            orders = list(df['orderNo'])

            urls  = ["https://ceo.baemin.com/v1/orders/"+  id + "?__ts=1598459367645" for id in orders]

            time.sleep(1)
            with open('data/baemin/' + date + '.json', 'w', encoding='UTF-8') as file:
                temp = []
                for i in urls:
                    driver.get_url(i)

                    if driver.driver.title == "ERROR: The request could not be satisfied":
                        return False

                    pre = driver.find_by_tag("pre").text
                    temp.append(json.loads(pre)['data'])
                file.write(json.dumps(temp))
    return driver