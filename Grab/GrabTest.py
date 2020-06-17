# -*- coding: utf-8 -*-
import mechanize

def main(self):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookies = mechanize.CookieJar()
    browser.set_cookiejar(cookies)
    browser.addheaders = [('User-agent', 'Chrome/73.0.3683.86')]
    browser.set_handle_refresh(False)

    url = 'http://www.facebook.com/login.php'
    self.browser.open(url)
    self.browser.select_form(nr = 0)       #This is login-password form -> nr = number = 0
    self.browser.form['email'] = egorpl1205@gmail.com
    self.browser.form['pass'] = rjk,fcrf12051999
    response = self.browser.submit()
    print (response.read())



if __name__ == "__main__":
    main()



