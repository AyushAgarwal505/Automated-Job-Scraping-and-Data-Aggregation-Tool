from bs4 import BeautifulSoup
import requests
import time

unfamiliar_skills = input("Enter unfamiliar skills comma-seperated > ").split()
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if '1' in published_date or '3' in published_date or '2' in published_date:
            link = job.find('header',class_='clearfix').a['href']
            company_name = job.find('h3',class_='joblist-comp-name').text.strip() #for searching inside job, not soup
            skills = job.find('span', class_ = 'srp-skills').text.strip().replace('  , ',',')
            flag = 0
            for unfamiliar_skill in unfamiliar_skills:
                if unfamiliar_skill.strip() in skills:
                    flag = 1
                    break;
            if flag == 0:
                with open(f'posts{index}.csv','w') as f:
                    f.write(f'Company Name: {company_name}\n')
                    f.write(f"Skills: {skills}\n")
                    f.write(f"Link: {link}\n")
                    print("File Saved")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait*60} seconds...')
        time.sleep(time_wait*60)
