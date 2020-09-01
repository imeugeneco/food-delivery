import pandas as pd

def graph():
    df = pd.read_csv('누적데이터.csv', encoding='utf-8-sig'
                     )
    df = df.fillna('')

    menus = ['이너프 샐러드', '닭가슴살 샐러드', '숲속 샐러드', '목살 샐러드', '훈제연어 샐러드']

    temp = list(df['항목'].values)
    items = []
    for x in temp:
        items.extend(x.split(', '))

    menu_data = []
    for i in menus:
        menu_data.append(items.count(i))

    index = pd.MultiIndex.from_product([['항목'], menus])
    columns = ['수량']

    menu_df = pd.DataFrame(menu_data, index=index, columns=columns)
    menu = pd.DataFrame(menu_data, index=menus, columns=columns)

    extra = ['숲속토핑 (110g)', '닭가슴살 (100g)', '목살 (100g)', '고구마 (50g)', '삶은 달걀',
             ]


    temp = list(df['추가선택'].values)
    items = []
    for x in temp:
        items.extend(x.split(', '))

    extra_data = []
    for i in extra:
        extra_data.append(items.count(i))

    index = pd.MultiIndex.from_product([['추가선택'], extra])
    columns = ['수량']
    extra_df = pd.DataFrame(extra_data, index=index, columns=columns)
    extra = pd.DataFrame(extra_data, index=extra, columns=columns)


    extra2 = ['발사믹', '렌치', '오리엔탈']

    temp = list(df['드레싱'].values)
    items = []
    for x in temp:
        items.extend(x.split(', '))

    extra2_data = []
    for i in extra2:
        extra2_data.append(items.count(i))

    index = pd.MultiIndex.from_product([['드레싱'], extra2])
    columns = ['수량']

    extra2_df = pd.DataFrame(extra2_data, index=index, columns=columns)
    extra2 = pd.DataFrame(extra2_data, index=extra2, columns=columns)

    frames = [menu_df, extra_df, extra2_df]
    result = pd.concat(frames)

    result.to_csv('통계데이터.csv', mode='w', encoding='utf-8-sig')

    # import matplotlib.pyplot as plt
    #
    # plt.rcParams["font.family"] = 'nanummyeongjo'
    #
    # menu.plot(kind='pie', y='수량', autopct='%1.2f%%',
    #           shadow=True,
    #           startangle=90)
    # plt.title('주메뉴', fontsize=20)
    #
    # extra.plot(kind='pie', y='수량', autopct='%1.2f%%',
    #            shadow=True,
    #            startangle=90)
    # plt.title('추가메뉴', fontsize=20)
    #
    # extra2.plot(kind='pie', y='수량', autopct='%1.2f%%',
    #             shadow=True,
    #             startangle=90)
    # plt.title('드레싱', fontsize=20)
    # plt.show()
