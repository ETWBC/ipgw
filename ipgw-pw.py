import argparse
import getpass
import os
import sys

from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='login&username')
    parser.add_argument('--logout', action='store_true')
    parser.add_argument('--username', type=str, help='username', default='')
    parser.add_argument('--password', type=str, help='password', default='')
    args = parser.parse_args()

    workPath = os.path.dirname(sys.argv[0])
    screenshot = os.path.join(workPath, 'ipgw-pw.png')
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(30)
    try:
        if not args.logout:
            url = 'https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_portal_sso%3Fac_id%3D'
            browser.get(url)

            if args.username and args.password:
                username = args.username
                password = args.password
            else:
                username = input("username:")
                password = getpass.getpass("password:")

            WebDriverWait(browser, 60, 1).until(EC.visibility_of_element_located((By.ID, 'un')))
            browser.find_element('id', 'un').send_keys(username)
            browser.find_element('id', 'pd').send_keys(password)
            browser.find_element('id', 'index_login_btn').click()
            WebDriverWait(browser, 10, 1).until(EC.visibility_of_element_located((By.ID, 'username')))
            username = browser.find_element(By.ID, 'username').text
            print("用户" + username + "登录成功！")
        else:
            url = 'http://ipgw.neu.edu.cn/srun_portal_success?ac_id='
            browser.get(url)

            WebDriverWait(browser, 10, 1).until(EC.visibility_of_element_located((By.ID, 'logout')))
            browser.find_element(By.ID, 'logout').click()

            WebDriverWait(browser, 10, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-confirm')))
            browser.find_element(By.CLASS_NAME, 'btn-confirm').click()

            WebDriverWait(browser, 10, 1).until(EC.visibility_of_element_located((By.ID, 'login-sso')))
            print("注销成功！")
    finally:
        browser.save_screenshot(screenshot)
        browser.close()
