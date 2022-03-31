from selenium.common.exceptions import NoSuchElementException

def click(driver, *args, **kwargs):
    xpath = kwargs.get("xpath")
    try:
        print(f"clicking on xpath {xpath}")
        driver.find_element_by_xpath(xpath).click()
    except NoSuchElementException:
        print(f"Not able to find xpath {xpath}")
    
    return driver.page_source

def back(driver, *args, **kwargs):
    print("moving one page back")
    driver.back()
    return driver.page_source