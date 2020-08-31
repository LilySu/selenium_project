from scrape_jobs import load_fields_to_csv
from browse_web import login_to_linkedin


driver = login_to_linkedin()

for i in range(1000):
    load_fields_to_csv(driver)
    results_list = load_fields_to_csv(driver)
    if results_list.count('NaN') == 10:
        driver = login_to_linkedin()
        load_fields_to_csv(driver)
        results_list = load_fields_to_csv(driver)
