import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

url = "https://www.businesssellcanada.com/sale/buymain.htm?reload=898"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
arr = []
arr2 = []
dic= {}
j = 0
print(j)
main = soup.find('div',class_='selllist')
for i in main.find_all("tr"):
    
    try:
        # For Descrition
        try:
            obj = i.find("a",class_='buy-ti')
            dic['Description'] = obj.text
        except Exception as e:
            pass
        
        # for price            
        try:
            obj2 = i.find("a",class_='buy-sp')
            dic['Price'] = obj2.text
        except Exception as e:
            pass
        
        # for location
        try:
            obj3 = i.find("td",class_='buy-pc')
            dic['Location'] = obj3.text
        except Exception as e:
            pass
        
        # adding href to array
        try:
            tag = i.find("a",href=True)
            arr.append(tag['href'])
        except Exception as e:
            pass

        # using array and fetching link of each user(more details)
        try:
            if j>0:
                link = "https://www.businesssellcanada.com{}".format(arr[j])
                l = requests.get(link, headers=headers)
                boot = BeautifulSoup(l.text, 'html.parser')
                cnt = 0
                for var in boot.find_all('td', class_='notes'):
                    if cnt==0:
                        dic['Business'] = var.text
                        cnt += 1
                    elif cnt == 1:
                        if var.text == "\n":
                            pass
                        else:
                            dic['Financial info'] = var.text
                        cnt += 1
                    elif cnt == 2:
                        if var.find_all('blockquote') or var.find('li'):
                            dic['Options'] = var.text
                        else:
                            if var.text == "\n":
                                pass                                
                            else:
                                dic['Competition'] = var.text
                        cnt += 1
                    else:
                        if var.text == "\n\n":
                            pass
                        else:
                            dic['Options'] = var.text
            j += 1
            
        except Exception as e:
            pass
    
        if bool(dic):
            with open("data2.json", "a") as jsonFile:
                json.dump(dic, jsonFile,indent=2)
        
        dic.clear()
    except Exception as e:
        pass


# for other pages 
page = ['02','03','04','05','06','07','08','09','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29']
for p in page:
    url = "https://www.businesssellcanada.com/sale/bumain{}.htm".format(p)
    r2 = requests.get(url, headers=headers)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    arr.clear()
    j=0
    main2 = soup2.find('div',class_='selllist')
    for k in main2.find_all("tr"):
        try:
            # For Descrition
            try:
                obj = k.find("a",class_='buy-ti')
                dic['Description'] = obj.text
            except Exception as e:
                pass
            # for price            
            try:
                obj2 = k.find("a",class_='buy-sp')
                dic['Price'] = obj2.text

            except Exception as e:
                pass
            # for location
            try:
                obj3 = k.find("td",class_='buy-pc')
                dic['Location'] = obj3.text
            except Exception as e:
                pass
            
            # adding href to array
            try:
                tag = k.find("a",href=True)
                arr.append(tag['href'])
            except Exception as e:
                pass

            # using array and fetching link of each user(more details)
            try:
                if j>0:
                    link = "https://www.businesssellcanada.com{}".format(arr[j])
                    l = requests.get(link, headers=headers)
                    boot = BeautifulSoup(l.text, 'html.parser')
                    cnt = 0
                    for var in boot.find_all('td', class_='notes'):
                        if cnt==0:
                            dic['Business'] = var.text                            
                            cnt += 1
                        elif cnt == 1:
                            if var.text == "\n":                
                                pass
                            else:                                
                                dic['Financial info'] = var.text
                            cnt += 1
                        elif cnt == 2:
                            if var.find_all('blockquote') or var.find('li'):
                                dic['Options'] = var.text
                            else:
                                if var.text == "\n":
                                    pass
                                else:
                                    dic['Competition'] = var.text
                            cnt += 1
                        else:
                            if var.text == "\n\n":
                                pass
                            else:
                                dic['Options'] = var.text
                j += 1

            except Exception as e:
                pass
            
            if bool(dic):
                with open("data2.json", "a") as jsonFile:
                    json.dump(dic, jsonFile,indent=2)
            dic.clear()
            
        except Exception as e:
            pass
