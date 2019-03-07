#coding=utf-8
from selenium import webdriver
import os

#设置浏览器驱动，chromedriver.exe为我本机下载好的浏览器驱动
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

#最大化窗口
driver.maximize_window()
jenkinsPage = 'http://10.10.2.222:8082/'
#jenkinsPage = 'http://10.10.4.176:8089/view/test-206/'
#jenkinsPage='http://10.10.4.176:8089/view/server-11-176/'
#jenkinsPage='http://10.10.4.176:8089/view/user-54-87/'

projectFileName = 'jenkinsProject.csv'

def login():
    driver.find_element_by_id('j_username').send_keys('yangbizhen')
    driver.find_element_by_css_selector('body > div > div > form > div:nth-child(2) > input').send_keys('rrtv1230D')
    driver.find_element_by_css_selector("body > div > div > form > div.submit.formRow > input").click()	
	
def getProjects(driver, tb_list):
    projects = []
    project_tr_list =  driver.find_element_by_id('projectstatus').find_elements_by_tag_name("tr")
    for i in range(len(project_tr_list)):
        project_tr = project_tr_list[i]
        
        #print (project_tr.text)
        text = project_tr.text
        project_td_list = [str(n) for n in text.split()]  
        #projects.append(projectName)
        if len(project_td_list) > 0 and i!=0:
            tb_list.append(project_td_list[0])

def is_element_exist(css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        return False
    elif len(s) == 1:
        return True

def getBranch(driver, defaultProject):
    for i in  range(len(defaultProject)):
        url = jenkinsPage + 'job/' +defaultProject[i]+ '/configure'
        driver.get(url)
        
        #if driver.find_element_by_css_selector('#main-panel > div > div > div > form > table > tbody > tr:nth-child(101) > td.setting-main > div > div.repeated-chunk.first.last.only > table > tbody > tr:nth-child(1) > td.setting-main') :
        if is_element_exist('#main-panel > div > div > div > form > table > tbody > tr:nth-child(112) > td.setting-main > div > div.repeated-chunk.first.last.only > table > tbody > tr:nth-child(1) > td.setting-main > input'):
            value = driver.find_element_by_css_selector('#main-panel > div > div > div > form > table > tbody > tr:nth-child(112) > td.setting-main > div > div.repeated-chunk.first.last.only > table > tbody > tr:nth-child(1) > td.setting-main > input').get_attribute('value')
            defaultProject[i] = defaultProject[i].replace("\n", "")
            #if value != "*/master":
            print ('项目'+defaultProject[i]+'的分支为： '+value)


driver.get(jenkinsPage)
login()
tb_list = [] 
getProjects(driver, tb_list)
getBranch(driver, tb_list)
