import pandas as pd
import glob
import json

path = './data/now_waiting/'
files = glob.glob(path + "/*.json")
li = []

for file in files:
    with open(file, 'r', encoding='utf-8-sig') as file:
        x = json.load(file)
    df = pd.DataFrame(x)
    li.append(df)

now_waiting = pd.concat(li, axis=0, ignore_index=True)

target = pd.read_csv('./누적데이터.csv')

cols = ['id','serving_type', 'amount', 'amount_to_pay', 'user_comment']
df = now_waiting[cols]
df = df.rename(columns={'id':'주문번호',
                                 'source_type':'결제방법',
                                 'serving_type': '서비스타입',
                                 'amount':'주문금액',
                                 'amount_to_pay':'결제금액',
                                 'user_comment':'요청사항'})

import datetime


def get_timestamps(timestamp_list):
    registered_ts = timestamp_list.get('registered') / 1000
    registered_dt = datetime.datetime.fromtimestamp(int(registered_ts)).strftime('%Y-%m-%d %H:%M:%S')

    return pd.Series((registered_dt))


def get_order_details(order_list):
    method = []
    items = []
    toppings = []
    sauce = []

    for order in order_list:
        order_type = order.get('type')
        order_content = order.get('content')
        quantity = order.get('quantity')

        if order_type == 'product':
            items = items + [order.get('name')] * quantity
        elif order_type == 'product_option_item':
            if '수령방식' in order_content:
                method.append(order_content[order_content.find(' ') + 1:])
            elif '소스' in order_content:
                sauce.append(order_content[order_content.find(' ') + 1:])
            else:
                toppings = toppings + [order.get('name')] * quantity

    method = (', ').join(method)
    items = (', ').join(items)
    toppings = (', ').join(toppings)
    sauce = (', ').join(sauce)

    return pd.Series((method, items, toppings, sauce))

df[['수령방법', '항목', '추가선택', '드레싱']] = now_waiting.apply(lambda row: pd.Series(get_order_details(row['order_items'])), axis=1)
df[['주문시각']] = now_waiting.apply(lambda row: pd.Series(get_timestamps(row['timestamps'])), axis=1)

target_cols = target.columns
df['주소'] = 'X'
df['배달팁'] = 0
df['결제방법'] = '나우웨이팅 POS'
df['접수시각'] = '-'
df['배달시각'] = '-'
df['배달요청사항'] = '-'
df = df[target_cols]

with open('./누적데이터.csv', 'a') as old_file: df.to_csv('./전체_데이터.csv', index=False, encoding='utf-8-sig')