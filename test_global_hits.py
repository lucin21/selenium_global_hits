import unittest

from data.base.webdriver import WebdriverHandler
from helpers.download_csv_from_url import download_csv_from_url
from helpers.count_word_in_csv import count_word_in_csv
from page_object.catalog_data.browse_results import browse_results
from page_object.catalog_data.obtain_number_from_text import obtain_number_from_text
from page_object.catalog_data.search import search


class MyTestCase(unittest.TestCase, WebdriverHandler):

    def setUp(self):
        self.my_class_instance = MyTestCase()
        # Inicia  el navegador.
        WebdriverHandler.__init__(self)
        self.driver.get("https://catalog.data.gov/dataset/")




    def tearDown(self):
        # Este método se ejecuta después de cada prueba
        self.driver.quit()



    def test_count_word_in_csv(self):
        total_results_string = search(self.driver, self.wait, "electric car")
        total_result_int = obtain_number_from_text(total_results_string)
        url_csv_buttom = browse_results(self.driver, self.wait, total_result_int, "Electric Vehicle Population Data")
        download_csv_from_url(url_csv_buttom, "Electric_Vehicle_Population_Data.csv")
        count_word = count_word_in_csv("Electric_Vehicle_Population_Data.csv", "TESLA")
        self.assertEqual(count_word, 80819, "Los valores no coinciden")
