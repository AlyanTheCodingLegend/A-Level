from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome webdriver
driver = webdriver.Chrome()

# Open Zoopla website
driver.get("https://www.zoopla.co.uk/find-agents/estate-agents/")

# Find the search bar and enter a location (e.g., London)
search_bar = driver.find_element_by_id("search-input-location")
search_bar.clear()
search_bar.send_keys("London")
search_bar.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# Extract agency details
agency_list = driver.find_elements_by_class_name("ui-card")

# Function to extract all branches of an agency
def extract_branches(agency_url):
    driver.get(agency_url)
    time.sleep(3)  # Let the page load

    branch_list = driver.find_elements_by_class_name("ui-card")

    branches = []
    for branch in branch_list:
        branch_name = branch.find_element_by_class_name("ui-card__title").text.strip()
        branch_address = branch.find_element_by_class_name("ui-card__content").text.strip()
        branch_phone = branch.find_element_by_class_name("ui-link").text.strip()

        branches.append({
            "Name": branch_name,
            "Address": branch_address,
            "Phone": branch_phone
        })

    return branches

# Write agency details and their branches to a text file
with open("agency_details.txt", "w") as file:
    for idx, agency in enumerate(agency_list, start=1):
        agency_name = agency.find_element_by_class_name("ui-card__title").text.strip()
        agency_address = agency.find_element_by_class_name("ui-card__content").text.strip()
        agency_phone = agency.find_element_by_class_name("ui-link").text.strip()
        agency_url = agency.find_element_by_class_name("ui-link").get_attribute("href")

        record = f"{idx}. Name: {agency_name}, Address: {agency_address}, Phone: {agency_phone}\n"
        file.write(record)

        # Extract and write branches
        branches = extract_branches(agency_url)
        for branch in branches:
            file.write(f"\tBranch Name: {branch['Name']}, Address: {branch['Address']}, Phone: {branch['Phone']}\n")

# Close the webdriver
driver.quit()
