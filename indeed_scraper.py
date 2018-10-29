# Import packages 
import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

#import warnings
#warnings.filterwarnings("ignore")

start_time = time.clock()

url_template = "http://www.indeed.com/jobs?q={}&l={}&start={}"

max_results_per_city = 1000 # Set this to a high-value (5000) to generate more results. 

job_set = ['data+scientist']#,'quantitative+analyst']
cities=['New+York','Mechanicsburg', 'Harrisburg','Los+Angeles', 'New+York', 'Chicago', 
		'San+Francisco', 'San+Jose', 'San+Diego',  
        'Washington%2C+DC', 'Boston', 'Pittsburgh', 'Philadelphia', 'Atlanta', 'Cincinnati',
        'St.+Louis', 'Tampa', 'Oakland', 'Austin', 'Houston', 'Dallas', 'Seattle', 'Portland',
        'Denver', 'Phoenix', 'Minneapolis', 'Miami', 'Charlotte', 'Jacksonville', 'Indianapolis',
        'Nashville', 'Kansas+City', 'Columbus']
columns = ['city_key', 'Title', 'Company', 'Location', 'Summary', 'Salary']



# Crawling more results, will also take much longer. First test your code on a small number of results and then expand.
i = 0
results = []
df_more = pd.DataFrame(columns=columns)
for city in set(cities):
    for start in range(0, max_results_per_city, 10):
        #print(city+" pg"+str(start/10.)) #to keep track of progress
        # Grab the results from the request (as above)
        url = url_template.format(job_set,city, start)
        # Append to the full set of results
        html = requests.get(url)
        time.sleep(1)
        soup = BeautifulSoup(html.content, 'html.parser', from_encoding="utf-8")
        for each in soup.find_all(class_= "result" ):
            try:
                city=city
            except:
                city = ''
            try: 
                title = each.find(class_='jobtitle').text.replace('\n', '')
            except:
                title = ''
            try:
                location = each.find('span', {'class':"location" }).text.replace('\n', '')
            except:
                location = ''
            try: 
                company = each.find(class_='company').text.replace('\n', '')
            except:
                company = ''
            try:
                salary = each.find('span', {'class':'no-wrap'}).text.strip()
            except:
                salary = ''
            try:
                summary = each.find('span', {'class':'summary'}).text.replace('\n', '')
            except:
                synopsis = ''
            df_more = df_more.append({'city_key':city,'Title':title,'Company':company, 'Location':location,'Summary':summary,'Salary':salary}, ignore_index=True)
            i += 1
            if i % 1000 == 0: 
                print('You have ' + str(i) + ' results.')
print('You have total '+str(df_more.shape[0])+ ' jobs. ' +str(df_more.dropna().drop_duplicates().shape[0]) + " of these aren't rubbish.")
print('Execution time is: %s seconds'%(time.clock() - start_time))
df_more.to_csv('Indeed_not_cleaned_long.csv', encoding='utf-8')

