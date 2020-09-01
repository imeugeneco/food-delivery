from selenium_class import Driver
import time
import datetime

def main(dates):
    driver = Driver()
    driver.driver.implicitly_wait(10)
    for i in range(len(dates)):
        date = dates[i]
        driver.get_url("https://ceo.baemin.com/self-service/orders/history")
        if driver.driver.title == "ERROR: The request could not be satisfied":
            return print("요청이 너무 많아 차단되었습니다. 잠시 후 다시 시도해주세요")
        if i == 0:
            id = driver.find_by_id("id")
            id.send_keys("sudaje1")

            pw = driver.find_by_id("pw")
            pw.send_keys("sujung4710!!")

            login = driver.find_by_id("btnLogin")
            driver.click(login)

        time.sleep(2)

        from baemin import baemin
        from result_df import to_csv
        from baemin_7 import baemin_7

        rq_date = list(map(int, date.split("-")))
        rq = datetime.datetime(rq_date[0], rq_date[1], rq_date[2])
        now = datetime.datetime.now()

        if (now - rq).days > 6:
            driver = baemin(driver, date)
            try:
                to_csv(date)
            except FileNotFoundError:
                pass
        else:
            driver = baemin_7(driver, date)
        if not driver:
            return print("요청이 너무 많아 차단되었습니다. 잠시 후 다시 시도해주세요")



        # from graph import graph
        # graph()
        if i  == 0:
            login_url = "https://ceo.nowwaiting.co/order_sales/history"
            driver.get_url(login_url)

            id_box = driver.find_by_id("email")
            id_box.send_keys("2753034@naver.com")

            pw_box = driver.find_by_id("password")
            pw_box.send_keys("@@a1s2d3f4\n")
        time.sleep(2)

        from now_waiting import now_waiting
        driver = now_waiting(driver, date)


        time.sleep(1)


        if i == 0:
            url = "https://web.albamapp.com/today"
            driver.get_url(url)
            id_box = driver.find_by_name("account")
            id_box.send_keys("01068863034")

            pw_box = driver.find_by_name("userPassword")
            pw_box.send_keys("@@a1s2d3f4")

            login_btn = driver.find_by_css("button.LoginButton")
            driver.click(login_btn)

            time.sleep(2)

            navs = driver.find_by_css("ul.nav")
            lis = driver.find_by_link_with_obj(navs, "급여")
            driver.click(lis)

        from albam import albam
        driver = albam(driver, date)
        print(date, "수집 완료")

    driver.close()



if __name__ == '__main__':
    # date = input("날짜를 입력해주세요(형식 : 2020-00-00) : ")
    # JSONDecodeError
    import datetime
    date = []
    x = datetime.datetime(2020, 8, 25)
    t = x + datetime.timedelta(days=1)
    while t.strftime('%Y-%m-%d') != "2020-08-31":
        date.append(t.strftime('%Y-%m-%d'))
        t = t + datetime.timedelta(days=1)
    try:
        main(date)
    except Exception as e:
        print(e)
