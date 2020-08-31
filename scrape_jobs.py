import csv
import random
import parameters
from time import sleep
from selenium import webdriver
from parsel import Selector


def validate_field(field): #if field is present pass
    if not field:
        field = 'NaN'
    return field


def load_fields_to_csv(driver):
    recommended_links = []
    for tries in range(20):
        page = random.randint(0, 20) * 25
        driver.get(f'https://www.linkedin.com/jobs/search/?f_TPR=r604800&keywords=junior%20data%20scientist&start={page}')
        # driver.get(f'https://www.linkedin.com/jobs/search/?f_TPR=r604800&keywords=junior%20data%20scientist&location=New%20York%20City%20Metropolitan%20Area&start={page}')
        sel = Selector(text=driver.page_source)
        job_listings = sel.xpath('//a[contains(@href, "/jobs/view/")]/@href').getall()
        # alternate method:
        # sel.xpath('//a[has-class("disabled ember-view job-card-container__link job-card-list__title")]/@href').getall()
        job_listings = list(dict.fromkeys(job_listings))# remove duplicates
        sleep(round(random.uniform(3, 20), 2))
        for listing in reversed(job_listings):
            if len(recommended_links) != 0:
                listing = recommended_links[0]
                recommended_links.pop(0)
            driver.get('https://www.linkedin.com' + listing)
            url = driver.current_url
            if 'linkedin.comhttps' in url:
                driver.get(listing)
            sleep(2)
            sel = Selector(text=driver.page_source)
            #######################################################
            job_title = sel.xpath('//h1[has-class("jobs-top-card__job-title t-24")]/text()').get()
            if job_title:
                job_title = ''.join(job_title)
                if type(job_title) == str:
                    job_title = job_title.strip()
                elif type(job_title) == list:
                    job_title = ''.join(job_title)
                    try:
                        job_title = job_title.strip()
                    except:
                        continue
            job_title = validate_field(job_title)
            company_name = sel.xpath('//a[has-class("jobs-top-card__company-url ember-view")]/text()').get()
            if company_name:
                company_name = ''.join(company_name)
                if type(company_name) == str:
                    company_name = company_name.strip()
                elif type(company_name) == list:
                    company_name = ''.join(company_name)
                    try:
                        company_name = company_name.strip()
                    except:
                        continue
            company_name = validate_field(company_name)
            location = sel.xpath('//a[has-class("jobs-top-card__exact-location t-black--light link-without-visited-state")]/text()').getall()
            if location:
                location = ''.join(location)
                if type(location) == str:
                    location = location.strip()
                elif type(location) == list:
                    location = ''.join(location)
                    try:
                        location = location.strip()
                    except:
                        continue
                location = validate_field(location)
            posted_days_ago = sel.xpath('//p[has-class("mt1 full-width flex-grow-1 t-14 t-black--light")]').get()
            if posted_days_ago:
                posted_days_ago = ''.join(posted_days_ago)
                if type(posted_days_ago) == str:
                    posted_days_ago = posted_days_ago.strip()
                elif type(posted_days_ago) == list:
                    posted_days_ago = ''.join(posted_days_ago)
                    try:
                        posted_days_ago = posted_days_ago.strip()
                    except:
                        continue
            posted_days_ago = validate_field(posted_days_ago)
            seniority_level = sel.xpath('//p[has-class("jobs-box__body js-formatted-exp-body")]/text()').getall()
            if seniority_level:
                seniority_level = ''.join(seniority_level)
                if type(seniority_level) == str:
                    seniority_level = seniority_level.strip()
                elif type(seniority_level) == list:
                    seniority_level = ''.join(seniority_level)
                    try:
                        seniority_level = seniority_level.strip()
                    except:
                        continue
            seniority_level = validate_field(seniority_level)
            industry_job_functions = sel.xpath('//li[has-class("jobs-box__list-item jobs-description-details__list-item")]/text()').getall()
            if industry_job_functions:
                industry_job_functions = ''.join(industry_job_functions)
                if type(industry_job_functions) == str:
                    industry_job_functions = industry_job_functions.strip()
                elif type(industry_job_functions) == list:
                    industry_job_functions = ''.join(industry_job_functions)
                    try:
                        industry_job_functions = industry_job_functions.strip()
                    except:
                        continue
            industry_job_functions = validate_field(industry_job_functions)
            employment_type = sel.xpath('//p[has-class("jobs-box__body js-formatted-employment-status-body")]/text()').get()
            if employment_type:
                employment_type = ''.join(employment_type)
                if type(employment_type) == str:
                    employment_type = employment_type.strip()
                elif type(employment_type) == list:
                    employment_type = ''.join(employment_type)
                    try:
                        employment_type = employment_type.strip()
                    except:
                        continue
            employment_type = validate_field(employment_type)
            job_description = sel.xpath('//div[has-class("jobs-box__html-content jobs-description-content__text t-14 t-normal")]').getall()
            if job_description:
                job_description = ''.join(job_description)
                if type(job_description) == str:
                    job_description = job_description.strip()
                elif type(job_description) == list:
                    job_description = ''.join(job_description)
                    try:
                        job_description = job_description.strip()
                    except:
                        continue
            job_description = validate_field(job_description)
            base_salary = sel.xpath('//p[has-class("salary-main-rail__data-amount t-24 t-black t-normal")]/text()').get()
            if base_salary:
                base_salary = ''.join(base_salary)
                if type(base_salary) == str:
                    base_salary = base_salary.strip()
                elif type(base_salary) == list:
                    base_salary = ''.join(base_salary)
                    try:
                        base_salary = base_salary.strip()
                    except:
                        continue
            base_salary = validate_field(base_salary)
            applicants = sel.xpath('//span[has-class("ml1")]/text()').get()
            if applicants:
                applicants = ''.join(applicants)
                if type(applicants) == str:
                    applicants = applicants.strip()
                elif type(applicants) == list:
                    applicants = ''.join(applicants)
            applicants = validate_field(applicants)
            all_similar_job_links = sel.xpath('//a[has-class("job-card__link-wrapper js-focusable-card ember-view")]').getall()
            all_similar_job_links = validate_field(all_similar_job_links)
            if all_similar_job_links != 'NaN':
                for similar_job in all_similar_job_links:
                    start = similar_job.find('<')
                    end = similar_job.find('href="')
                    if start != -1 and end != -1:
                        result = similar_job[start:end + 6]
                        similar_job = similar_job.replace(result, '')
                        end_quote = similar_job.find('"')
                        rec_url = similar_job[0:end_quote]
                        recommended_links.append(rec_url)
            url = driver.current_url
            url = validate_field(url)
            try:
                with open(parameters.file_name, 'a', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([job_title,company_name,location,posted_days_ago,seniority_level,industry_job_functions,employment_type,job_description,base_salary,applicants,all_similar_job_links,url])
            except:
                continue
            sleep(round(random.uniform(3, 10), 2))
            return [job_title,company_name,location,posted_days_ago,seniority_level,industry_job_functions,employment_type,job_description,base_salary,applicants,all_similar_job_links,url]
# driver.quit()