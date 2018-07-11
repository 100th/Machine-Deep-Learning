from selenium import webdriver

url = "https://nid.naver.com/nidlogin.login"
# PhantomJS 드라이버 추출하기 --- (※1)
browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

# 로그인 하는 부분
browser.get(url)
element_id = browser.find_element_by_id("id")
element_id.clear()
element_id.send_keys("ID")
element_pw = browser.find_element_by_id("pw")
element_pw.clear()
element_pw.send_keys("PW")

browser.save_screenshot("Website_C.png")

button = browser.find_element_by_css_selector("input.btn_global[type=submit]")
button.submit()

#메일 페이지 열기
browser.get("https://mail.naver.com")
browser.save_screenshot("Website_D.png")

titles = browser.find_elements_by_css_selector("strong.mail_title")
for title in titles:
    print("-", title.text)

# 브라우저 종료하기 --- (※5)
browser.quit()
