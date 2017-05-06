from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('httpsgoo.glformsoiiUQckJGJCe6ygA3')
browser.find_element_by_name('entry.712063927').send_keys(Emre Ovunc)
browser.find_element_by_xpath(.[@id='mG61Hd']divdiv[2]div[2]div[2]div[2]divdiv[1]divdiv[1]input).send_keys(info@emreovunc.com)
browser.find_element_by_xpath(.[@id='mG61Hd']divdiv[2]div[3]div[1]divdivcontentspan).click()
time.sleep(2)
browser.find_element_by_xpath(.[@id='mG61Hd']divdiv[2]div[2]div[3]div[2]divcontentdivlabel[4]divdiv[1]div[3]div).click()
browser.find_element_by_xpath(.[@id='mG61Hd']divdiv[2]div[2]div[4]div[2]divcontentdivlabel[1]divdiv[1]div[3]div).click()
browser.find_element_by_xpath(.[@id='mG61Hd']divdiv[2]div[3]div[1]divdiv[2]contentspan).click()