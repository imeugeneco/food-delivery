from selenium_class import Driver
import datetime
import pandas as pd
import  time

def albam(driver, date):

    url = "https://web.albamapp.com/today"
    driver.get_url(url)

    navs = driver.find_by_css("ul.nav")
    lis = driver.find_by_link_with_obj(navs, "급여")
    driver.click(lis)

    time.sleep(0.5)
    date_pickers = driver.find_all_by_css("div.react-datepicker__input-container > button")
    start_date = list(map(int, (date_pickers[0].text.split()[0].split("-"))))
    start_date = datetime.datetime(start_date[0], start_date[1], start_date[2])

    end_date = list(map(int, (date_pickers[1].text.split()[0].split("-"))))
    end_date = datetime.datetime(end_date[0], end_date[1], end_date[2])

    now_date = list(map(int, date.split("-")))
    now = datetime.datetime(now_date[0], now_date[1], now_date[2])

    if start_date != now or end_date != now:
        for i in range(2):
            driver.click(date_pickers[i])
            month = int(driver.find_by_css("div.react-datepicker__current-month").text.split()[0][:-1])
            year = int(driver.find_by_css("div.react-datepicker__current-month").text.split()[1])
            dff = (year - now_date[0]) * 12 + (month - now_date[1])
            if dff:
                prev = driver.find_by_css("button.react-datepicker__navigation--previous")

                for i in range(dff):
                    driver.click(prev)


            day = driver.find_by_css("div.react-datepicker__month")
            day = driver.find_all_by_css_with_obj(day, "div[aria-label=day-{day}]".format(day = now_date[2]))
            if now_date[2] > 15 and len(day) != 1:
                day = day[1]
            else:
                day = day[0]
            driver.click(day)

    fitting = driver.find_by_css("div.resize-grid-btn > button:nth-child(2)")
    driver.click(fitting)

    result = []
    while True:
        container = driver.find_by_css("div.ag-body-container")
        if len(container.text.strip()) == 0:
            labels = ['이름', '시급', '연장근무', '야간근무', '휴일근무', '근무인정시간', '총급여']
            df = pd.DataFrame(result, columns=labels)
            df.to_csv('data/albam/' + date + '.csv', index=False, mode='w', encoding='utf-8-sig')
            return driver
        try:
            rows = driver.find_all_by_css_with_obj(container, "div.ag-row-position-absolute")
        except:
            labels = ['이름', '시급', '연장근무', '야간근무', '휴일근무', '근무인정시간', '총급여']
            df = pd.DataFrame(result, columns=labels)
            df.to_csv('data/albam/' + date + '.csv', index=False, mode='w', encoding='utf-8-sig')
            return driver

        for i in rows:
            username = driver.find_by_css_with_obj(i, "div[col-id=username]").text.strip()
            total_time_work = driver.find_by_css_with_obj(i, "div[col-id=\'5\']").text.strip().split('\n')
            work_time = total_time_work[0]

            total_wage = 0
            if total_time_work[1] != "(-)":
                total_wage = int(total_time_work[1][:-1].replace(",", ""))

            wage = int(driver.find_by_css_with_obj(i, "div[col-id=\'0\']").text.strip().split('\n')[1][:-1].replace(",", ""))
            weekend = int(driver.find_by_css_with_obj(i, "div[col-id=\'10\']").text.strip()[:-1].replace(",", ""))
            total_money = total_wage + weekend


            result.append([username, wage, work_time, total_wage, weekend, total_money])
        next_btn = driver.find_by_css("button[ref=btNext]")
        if next_btn.get_attribute("disabled"):
            break
        driver.click(next_btn)


    labels = ['이름', '시급', '근무인정시간', '기본급여', '주휴수당', '총급여']
    df = pd.DataFrame(result, columns=labels)
    df.to_csv('data/albam/' + date + '.csv', index=False, mode='w', encoding='utf-8-sig')

    return driver

if __name__ == '__main__':
    albam(Driver(), '2020-08-25')
