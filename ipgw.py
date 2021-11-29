#!/usr/bin/env python
# coding: utf-8
import base64

import argparse
import os
import sys

import numpy as np
from PIL import Image

from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--logout', action='store_true')
    args = parser.parse_args()

    workPath = os.path.dirname(sys.argv[0])

    qrcode = os.path.join(workPath, 'QRcode.jpg')
    screenshot = os.path.join(workPath, 'ipgw.png')

    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    browser.implicitly_wait(30)
    try:
        if not args.logout:
            url = 'https://pass.neu.edu.cn/tpass/login?service=http%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_portal_sso%3Fac_id%3D'
            browser.get(url)
            WebDriverWait(browser, 60, 1).until(EC.visibility_of_element_located((By.ID, 'qrcode_login')))
            browser.find_element('id', 'qrcode_login').click()

            print("请使用微信扫码验证...")

            WebDriverWait(browser, 180, 1).until(EC.visibility_of_element_located((By.ID, 'qrcode')))
            screenshot_as_base64 = browser.find_element('id', 'qrcode').screenshot_as_base64
            img = base64.b64decode(screenshot_as_base64)
            with open(qrcode, 'wb') as f:
                f.write(img)
            img = Image.open(qrcode)
            img = np.asarray(img)[1:-1, 1:-1, 0]
            img = np.delete(img, [18, 36, 52, 71, -52, -36, -18, -1], axis=0)
            img = np.delete(img, [18, 36, 52, 71, -52, -36, -18, -1], axis=1)
            img = img[1::3, 1::3]
            for line in img:
                print(''.join(['██' if p == 0 else '  ' for p in line]))
            WebDriverWait(browser, 60, 1).until(EC.visibility_of_element_located((By.ID, 'username')))
            username = browser.find_element(By.ID, 'username').text
            print("用户" + username + "登录成功！")
        else:
            url = 'http://ipgw.neu.edu.cn/srun_portal_success?ac_id='
            browser.get(url)

            WebDriverWait(browser, 60, 1).until(EC.visibility_of_element_located((By.ID, 'logout')))
            browser.find_element(By.ID, 'logout').click()

            WebDriverWait(browser, 60, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-confirm')))
            browser.find_element(By.CLASS_NAME, 'btn-confirm').click()

            WebDriverWait(browser, 120, 1).until(EC.visibility_of_element_located((By.ID, 'login-sso')))
            print("注销成功！")
    finally:
        browser.save_screenshot(screenshot)
        browser.close()
