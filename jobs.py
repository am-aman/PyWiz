# a python program that scraps the job site www.timesjob.com and finds the freshres jobs for python developer in chennai and prints them in a excel sheet.

from bs4 import BeautifulSoup
import openpyxl
import requests

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="topjobatchennai"
sheet.append(['Title','Company Name','Publish Date'])


#https://www.imdb.com/chart/top
#https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=


try:
    response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=chennai&cboWorkExp1=0').text

    soup = BeautifulSoup(response,'lxml')

    jobs = soup.findAll('li',class_='clearfix job-bx wht-shd-bx')


    for job in jobs:
        # job title
        title = job.find('header', class_='clearfix').findNext('h2').findNext('a').text.strip()
        # company name
        comp_name = job.find('h3',class_='joblist-comp-name').text.strip()
        #publish date
        publish=job.find('span',class_='sim-posted').text.strip()

        print(f'''
            Job Title    : {title}
            Company Name : {comp_name}
            publish date : {publish}
        '''
            )

        sheet.append([title,comp_name,publish])
except Exception as ex:
    print(ex)

excel.save("joblist@chennai.xlsx")