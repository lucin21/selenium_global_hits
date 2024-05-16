from selenium.webdriver import Keys


def search(driver, wait,search_word):
    search_bar = wait.waitForElement(locator='search-big', locatorType='id')
    wait.sendKeys(search_word, search_bar)
    wait.sendKeys(Keys.RETURN, search_bar)
    total_results = wait.waitForElement(locator=f"//div[contains(text(), 'datasets found for \"{search_word}\"')]",
                                             locatorType='xpath')
    total_results_string = wait.get_text(total_results)
    return total_results_string