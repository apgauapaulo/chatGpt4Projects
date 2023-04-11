from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicializando o driver do Selenium
driver = webdriver.Chrome()

# Abrindo a página da Amazon
driver.get("https://www.amazon.com.br/Escada-Extensiva-Fibra-Vidro-3-60/dp/B08TRR5D9D/ref=sr_1_1_sspa?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2HG5XS1Q7D432&keywords=escada&qid=1681243706&sprefix=escad%2Caps%2C203&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.25548f35-0de7-44b3-b28e-0f56f3f96147&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUEVMQU4zVlNWQ0hQJmVuY3J5cHRlZElkPUEwMzYxODMyMkxSUk9KUzhLT0g2SSZlbmNyeXB0ZWRBZElkPUEwNjI0Njg4V003RDIzNDZNM0c5JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")

# Esperando 5 segundos para a página carregar completamente
time.sleep(5)

# Encontrando o elemento com a classe "a-text-price"
price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")

# Convertendo o preço para um float
price = float(price_element.text.replace("R$", "").replace(",", "."))

# Verificando se o preço é menor do que R$700
if price < 700:
    print("Comprar a escada")
else:
    print("Preço acima de R$700")

# Fechando o driver do Selenium
driver.quit()