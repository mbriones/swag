# main.py

import json
from selenium import webdriver
from time import sleep


def main():
    config = json.load(open('config.json'))

    options = webdriver.ChromeOptions()

    # options.add_argument('headless')

    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Firefox()

    # wait for user to login
    # while "Login" in driver.title:
    #    sleep(2)


    # We must get to a non ssl page on this domain. ps fuck selenium
    driver.get('http://www.swagbucks.com/earn-money-online')
    driver.delete_all_cookies()

    ## The following are all required to avoid a redirect loop
    driver.add_cookie({'name' : '__urqm', 'value' : config["urqm"], 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : '__urqc', 'value' : config["urqc"], 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : 'SBSESSIONID', 'value' : config["SBSESSIONID"], 'path' : '/', 'domain' : 'www.swagbucks.com'})
    driver.add_cookie({'name' : '__appname', 'value' : 'app2', 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : '__lp', 'value' : '1', 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : 'sb5', 'value' : '1', 'path' : '/', 'domain' : '.swagbucks.com'})
    driver.add_cookie({'name' : 'G_ENABLED_IDPS', 'value' : 'google', 'path' : '/', 'domain' : '.www.swagbucks.com'})
    driver.get('http://www.swagbucks.com/')

    def playVid():

        # Play Editors Pick Plalist
        driver.get('http://www.swagbucks.com/watch/playlists/111/editors-pick')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Politics Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/333/news-politics')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Entertainment Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/133/entertainment')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Food Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/3/food')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Sports Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/17/sports')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Fashion Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/98/fashion')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Health Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/4/health')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Home-Garden Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/12/home-garden')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

        # Switch to Tech Playlist
        driver.get('http://www.swagbucks.com/watch/playlists/22/technology')
        driver.find_element_by_class_name('watchCard').click()
        while True:
            try:
                # if we are on the same vid for 5 mins refresh
                curr = driver.current_url
                sleep(360)

                if curr == driver.current_url:
                    break

                # if any of these are true then we are done
                driver.find_element_by_xpath("// *[contains(text(), \
                                             'we are sorry')]")
                return
            except Exception:
                sleep(2)

    while True:
        # main loop
        playVid()


if __name__ == "__main__":
    main()
