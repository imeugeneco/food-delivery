import pandas as pd
import json


def to_csv(date):
    with open('data/baemin/' + date + '.json', 'r', encoding='UTF-8')as file:
        x = json.load(file)
    if len(x) == 0:
        return
    df = pd.DataFrame(x)

    cols = ['orderNo',
            'deliveryType',
            'purchaseType',
            'items',
            'serviceType',
            'orderAmount',
            'charge',
            'orderDatetime',
            'acceptDatetime',
           'arriveDatetime',
             'orderer',
            'memo',
            'memos']

    df = df[cols]

    df.rename(columns = {
        'orderNo' : '주문번호', 'serviceType' : '서비스타입',
        'deliveryType' : "수령방법", 'purchaseType' : '결제방법', 'orderAmount' : '주문금액',
            'orderDatetime' : "주문시각", 'acceptDatetime' : "접수시각",
           'arriveDatetime' : "배달시각", 'charge' : "배달팁", 'items' : "항목",
     'orderer' : "주소", 'memo' : '요청사항', 'memos' : '배달요청사항'}, inplace = True)

    df.loc[df['서비스타입'] == "BAEMIN", "서비스타입"] = "배민"
    df.loc[df['수령방법'] == "DELIVERY", "수령방법"] = "배달"
    df.loc[df['수령방법'] == "TAKEOUT", "수령방법"] = "포장"
    df.loc[df['결제방법'] == "BARO", "결제방법"] = "바로결제"
    df.loc[df['결제방법'] == "MEET", "결제방법"] = "만나서결제"

    n = len(df)

    for i in range(n):
        df.iloc[i, 6] = df.iloc[i]['배달팁']['deliveryTip']

    for i in range(n):
        df.iloc[i, 10] = df.iloc[i]['주소']['streetAddress']
    for i in range(n):
        df.iloc[i, 11] = ''.join(df.iloc[i]['요청사항']['delivery'])

    for i in range(n):
        if len(df.iloc[i]['배달요청사항']):
            df.iloc[i, 12] = df.iloc[i]['배달요청사항'][0]['memo']

    for i in range(n):
        items = []
        extra = []
        dr = []
        temp = df.iloc[i]['항목']
        for x in temp:
            for k in range(x['quantity']):
                if '추가' in x['name']:
                    dr.append(x['name'].split(" 추가")[0][2:])
                else:
                    items.append(x['name'])
            options = x['options']
            for k in options:
                if k['group'] == "추가선택":
                    for y in k['items']:
                        for q in range(y['quantity']):
                            extra.append(y['name'].split(" 추가")[0])
                if k['group'] == "드레싱 선택":
                    for y in k['items']:
                        for q in range(y['quantity']):
                            dr.append(y['name'].split()[0])

        df.iloc[i, 3] = ', '.join(items)

        df.loc[i, '추가선택'] = ', '.join(extra)
        df.loc[i, '드레싱'] = ', '.join(dr)

    df['결제금액'] = df['주문금액'] + df['배달팁']

    cols = [ '주문번호', '수령방법', '결제방법', '항목', '추가선택', '드레싱', '서비스타입', '주문금액', '배달팁', '결제금액', '주문시각',
           '접수시각', '배달시각', '주소', '요청사항', '배달요청사항']
    df = df[cols]
    import os

    if os.path.isfile('배민누적데이터.csv'):
        prev = pd.read_csv('배민누적데이터.csv')
        dup = prev[prev['주문시각'].str.contains(date)].index
        prev = prev.drop(dup)
        df = pd.concat([prev, df], sort=False)
    df = df.sort_values(by=['주문시각'])

    df.to_csv('배민누적데이터.csv', index=False, mode='w', encoding='utf-8-sig')

    # os.startfile('누적데이터.csv')



"""
    path = './data/baemin/'
    files = glob.glob(path + "/*.json")
    li = []
    print(files)

    for file in files:
        with open(file, 'r', encoding='utf-8-sig') as file:
            x = json.load(file)
            if len(x) == 0:
                continue
            df = pd.DataFrame(x)
            li.append(df)

    df = pd.concat(li, axis=0, ignore_index=True)
    """