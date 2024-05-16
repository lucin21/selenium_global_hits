def browse_results(driver, wait,total_result_int, title_article):
    number_of_articles_per_page = 21  # En realidad son 20 articulos por pagina pero le sumo 1 para que el ciclo for llegue hasta 20
    total_number_of_pages = (total_result_int // 20) + 1
    for page_number in range(total_number_of_pages):
        for article_n in range(1, number_of_articles_per_page):
            article = wait.waitForElement(
                locator=f'//*[@id="content"]/div[2]/div/section[1]/div[2]/ul/li[{article_n}]/div/h3/a',
                locatorType='xpath')
            article_string = wait.get_text(article)
            if article_string == title_article:
                csv_buttom = wait.waitForElement(
                    locator=f'//*[@id="content"]/div[2]/div/section[1]/div[2]/ul/li[{article_n}]/div/ul/li[1]/a',
                    locatorType='xpath')
                csv_buttom_string = wait.get_text(csv_buttom)
                if csv_buttom_string == "CSV":
                    url_csv_buttom = wait.get_attribute("href", csv_buttom)
                    return url_csv_buttom
        driver.get(f"https://catalog.data.gov/dataset/?page={page_number}")