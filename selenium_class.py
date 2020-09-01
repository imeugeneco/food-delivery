from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_argument('--start-fullscreen')
        options.add_argument(
            "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


    def __call__(self):
        return self.driver

    def get_url(self, url): # 새 창으로 url 열기
        self.driver.get(url)

    def get_default(self):
        while True:
            try:
                self.driver.switch_to_default_content()
                return
            except:
                print('default frame 이동')
                pass

    def get_fra(self, name):
        while True:
            try:
                self.driver.switch_to_frame(name)
                break
            except:
                self.get_default()
                print(name, 'frame 이동')
                continue

    def get_top(self):
        while True:
            try:
                self.driver.switch_to_frame('top')
                break
            except:
                self.get_fra('body')
                print('body', 'frame 이동')
                continue

    def find_by_xpath(self, xpath): # Xpath로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, xpath)))
    def find_by_name(self, name): # name로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.NAME, name)))
    def find_by_class(self, class_name): # class name으로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, class_name)))

    def find_by_id(self, id): # class name으로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.ID, id)))

    def find_by_tag(self, tag): # tag로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, tag)))

    def find_by_css(self, css): # tag로 단일 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css)))


    def find_all_by_class(self, class_name): # class name으로 모든 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, class_name)))

    def find_all_by_css(self, css): # class name으로 모든 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, css)))

    def find_all_by_tag(self, tag): # tag로 모든 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, tag)))

    def find_all_by_name(self, name): # name으로 모든 요소 찾기
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.NAME, name)))

    def find_all_by_tag_with_obj(self, obj, name): # name으로 모든 요소 찾기
        return WebDriverWait(obj, 20).until(
            EC.presence_of_all_elements_located(
                (By.TAG_NAME, name)))

    def find_all_by_css_with_obj(self, obj, css):
        return WebDriverWait(obj, 20).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, css)))

    def find_by_tag_with_obj(self, obj, name): # name으로 요소 찾기
        return WebDriverWait(obj, 20).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, name)))

    def find_by_xpath_with_obj(self, obj, path):
        return WebDriverWait(obj, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, path)))

    def find_by_class_with_obj(self, obj, class_name):
        return WebDriverWait(obj, 20).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, class_name)))

    def find_by_css_with_obj(self, obj, css): # tag로 단일 요소 찾기
        return WebDriverWait(obj, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css)))


    def find_by_link(self, text):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, text)))


    def find_by_link_with_obj(self, obj, text):
        return WebDriverWait(obj, 10).until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, text)))


    def click(self, btn):
        self.driver.execute_script("arguments[0].click();", btn)

    def close(self):
        self.driver.close()
