from bs4 import BeautifulSoup as bs
from selenium import webdriver


print("****WAIT BROWSER IS LOADING****")
req=webdriver.Chrome("C:/Users/Shradha/PycharmProjects/NXG/chromedriver")

Base_Url="http://igrmaharashtra.gov.in/eASR/"

District_name = input("Enter district Name: ")

print("**********PROCESSING***********")

"""
if len(District_name)>1:
    req.get("http://igrmaharashtra.gov.in/eASR/eASRCommon.aspx?h/DistName="+District_name)
"""

#To load to the page
req.get(Base_Url+"/eASRCommon.aspx?hDistName="+District_name)

soup = bs(req.page_source,'lxml')

"""
demo=soup.find_all('span',{'id':'ctl00_ContentPlaceHolder5_lblTaluka'})
content=soup.find_all('select',{'id':'ctl00_ContentPlaceHolder5_ddlTaluka'})
"""

"""
Select_Taluka = req.find_element({'id':'ctl00_ContentPlaceHolder5_ddlTaluka'})
Select_Taluka.send_keys('Parbhani')
"""

"""
list_of_talukas=[]
for i in range(1,14):
    list_of_talukas.append(soup.find_all('option',{'value':i}))
    for j in list_of_talukas:
        if (len(j)==0):
            list_of_talukas.remove(j)
print(list_of_talukas)
"""

text_list_dummy= []
for option in soup.select('table > tbody > tr > td > select > option'):
    for text in option.stripped_strings:
        element=str(text)
        #print(element)
        text_list_dummy.append(element)
#print(text_list_dummy)

text_list = text_list_dummy[16:30]
print(text_list)


#print(soup.find('select',attrs={'title':'परभणी'}))

#to get list of the villages in the taluka
"""
list_of_villages=[]
for k in range(400,600):
    list_of_villages.append(soup.find_all('option',{'value':k}))
print(list_of_villages)
"""

#creating a file which will store talukas in the district
f=open(District_name+'_taluka.txt',"w",encoding='utf-8')
for x in text_list:
    f.write(x+'\n')
    print(x)

#closing the connection to the file
f.close()

