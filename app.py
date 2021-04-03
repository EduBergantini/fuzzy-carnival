import random
from selenium import webdriver
from faker import Faker
import os


def get_random_answer(min, total_options):
    rndv = random.randint(min, total_options)
    return rndv

def autofill_form():
    chrome_driver = os.getenv('CHROME_DRIVER')
    if (chrome_driver == None):
        print("Variavel de ambiente não encontrada")
        return

    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);
    #option.add_argument("--headless")
    option.add_argument("disable-gpu")
    browser = webdriver.Chrome(executable_path=chrome_driver, options=option)

    radioButtonsCount = [4, 9, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    browser.get("https://forms.gle/MMNAxiktZDStcYPE9")

    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    text_areas = browser.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")

    min_index = 0
    for x in radioButtonsCount:
        max_index = min_index+x-1
        selected = get_random_answer(min_index, max_index)
        radiobuttons[selected].click()
        min_index = min_index + x

    fake = Faker("pt_BR")
    # fullfil a user e-mail
    textboxes[0].send_keys(fake.email())
    # fulfill sem os area de atuação
    textboxes[1].send_keys( fake.job())

    for text_area in text_areas:
        text_area.send_keys(fake.text())

    browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonEl").click()

    browser.close()


for x in range(10):
    print("Iniciando processamento.")
    try:
        autofill_form()
    except:
        print("Falha na execução.")