import schedule
import time
from tbselenium.tbdriver import TorBrowserDriver
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from flask import Flask
import threading

#quantumBlog and qulin blog

app = Flask(__name__)

status=[0,1]
urgent=[1,0]
links=[]

def job1():
    



    with TorBrowserDriver("/home/ritik/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:

        driver.get('http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/')
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        

        r=driver.page_source
        soup=BeautifulSoup(r,"html.parser")
        time.sleep(4)

        temp="http://kbsqoivihgdmwczmxkbovk7ss2dcynitwhhfu5yw725dboqo5kthfaad.onion/"
        
        Dates=[]

        a=driver.find_elements(By.XPATH,'//div[@class="item_box"]/div[1]/div[2]/a')
        d=driver.find_elements(By.XPATH,'//div[@class="item_box"]/div[1]/div[1]/div/div[2]/div[1]/div[2]')
        for i in a:
            links.append(i.get_attribute('href'))
        for j in d:
            Dates.append(j.text)
        
        Company_name=[]
        Description=[]
        

        
        

        for i in range(len(links)):
            driver.get(links[i])
            soup2=(driver.page_source,"html.parser")
            time.sleep(5)
            
            t=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/div")
            Company_name.append(t.text)

            d=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div/div[2]/div/div[2]')
            Description.append(d.text)

        links.clear()
        return "runnned"



def job2():

    with TorBrowserDriver("/home/ritik/Downloads/tor-browser-linux64-12.0.1_ALL/tor-browser") as driver:
        driver.get('http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion')
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(4)
        data_amount=[]
        dates=[]
        headings=[]
        description=[]
        


        r=driver.page_source
        soup=BeautifulSoup(r,'html.parser')
        
        outer=soup.select('section.blog-post div div.panel-body')
        date=soup.select('section.blog-post div div.panel-body div.blog-post-meta p')
        data=soup.select('section.blog-post div div.panel-body div.blog-post-meta span')
        head=soup.select('section.blog-post div div.panel-body div.blog-post-content a h2')
        desc=soup.select('section.blog-post div div.panel-body div.blog-post-content p')
        link=soup.select('section.blog-post div div.panel-body div.blog-post-content h2')
        temp="http://quantum445bh3gzuyilxdzs5xdepf3b7lkcupswvkryf3n7hgzpxebid.onion"
        for y in link:
            links.append(temp+y.parent.get('href'))
        for g in desc:
            description.append(g.text)
        for l in head:
            headings.append(l.text)
        
        for j in data:
            data_amount.append(j.text)
        for i in date:
            dates.append(i.text)
        
        Desc=[]
        for x in range(len(links)):
            time.sleep(5)
            driver.get(links[x])
            r=driver.page_source
            soup2=BeautifulSoup(r,'html.parser')
            c=soup2.select_one('section.blog-post')
            
            

            Desc.append(c.get_text())
        
        print(Desc)
        print(links)
        links.clear()



if len(links)==0:
    for i in range(2):
        if urgent[i]==1:
            if i==0:
                schedule.every(1).minutes.do(job1)
            else:
                schedule.every(1).minutes.do(job2)
    for j in range(2):
        if status[j]==1:
            if j==0:
                schedule.every(1).minutes.do(job1)
            else:
                schedule.every(1).minutes.do(job2)



def main():
    while True:
        schedule.run_pending()
     
p1 =threading.Thread(target =main,args=())
p1.start()


@app.route('/')

def hello_world():
	return 'Hello World'



if __name__ == '__main__':
	app.run()