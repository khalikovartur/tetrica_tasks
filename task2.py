# Please install requirements from requirements.txt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as CDM
from bs4 import BeautifulSoup as BS

URL = 'https://inlnk.ru/jElywR'

def get_list_names(url):  
    options = Options()
    options.add_argument('headless')
    driver = webdriver.Chrome(service=Service(CDM().install()),
                              options=options) 
    try:
        driver.get(url)
        list_names = []
        while True:
            source = driver.page_source
            bs = BS(source, 'lxml')
            names = bs.find(class_="mw-category mw-category-columns")\
                            .find_all('a')
            for item in names:
                list_names.append(item.text)
                    
            next_page_button = driver.find_element(by=By.XPATH, 
                                    value='//*[@id="mw-pages"]/a[2]')
            next_page_button.click()
                        
            if driver.find_element(by=By.XPATH, 
                    value='//*[@id="mw-pages"]/div/div/div/h3').text == 'A':
                break                 
    except Exception:
        print(Exception)        
    finally:
        driver.close()
        driver.quit()            
    return list_names

def make_result_dict(name_list):
    alphabet_string = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    list_letters = [letter for letter in alphabet_string]   
    result_dict = {}
    for letter in list_letters:
        counter = 0
        for name in name_list:
            if name.startswith(letter):
                counter += 1
        result_dict[letter] = counter
    return result_dict

def main():
    print('Please waiting for a while, task in the process...')
    
    list_names = get_list_names(URL)
    result_dict = make_result_dict(list_names)
            
    for letter, amount  in result_dict.items():
        print(f'{letter}:{amount}')
    
                 
if __name__ == "__main__":
    main()
    
    
    
    
    



    