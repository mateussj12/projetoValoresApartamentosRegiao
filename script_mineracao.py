import logging
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import pandas as pd
import time
import datetime


print("""
        ██╗███████╗███████╗██╗   ██╗███████╗
        ██║██╔════╝██╔════╝██║   ██║██╔════╝
        ██║█████╗  ███████╗██║   ██║███████╗
   ██   ██║██╔══╝  ╚════██║██║   ██║╚════██║
   ╚█████╔╝███████╗███████║╚██████╔╝███████║
    ╚════╝ ╚══════╝╚══════╝ ╚═════╝ ╚══════╝
                                                 
    """)
print("""
    **Estado**: Brasilia - DF 
    **Desenvolvedor responsável**: Mateus Santos de Jesus
    **Objetivo**: Esse script acessa o site do Quinto Andar, 
    faz a coleta de informações com base nos requisitos de desenvolvimento,
    converte as informações para um dataframe,
    transcreve para um arquivo csv...
    """)

print("# Configurando coleta de logs")
# Configuração de logging
logging.basicConfig(filename='log_file.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicia o driver inicia
def carregarDriver():
    print("# Iniciando o Driver do Firefox")
    gecko_driver_path = 'C:\\Users\\Jesus\\Desktop\\projetoA\\valoresApartamentosRegiao\\firefoxdriver-win64\\geckodriver.exe'
    firefox_options = Options()
    firefox_options.add_argument("--headless")  
    firefox_service = FirefoxService(executable_path=gecko_driver_path)
    driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    return driver
            

# Abre o site do quinto andar
def iniciarNavegador(driver, url):
    print("# Abrindo o site do Quinto Andar")
    driver.get(url)
    driver.maximize_window()


# Percorrer cidades e coletar dados
def coletarDadosAnuncio(driver, bairros, cidades):
    print("# Abre o site do Quinto Andar, coleta os dados e salva as informações em um arquivo csv")
    dataAnuncios = datetime.datetime.now().strftime('%Y-%m-%d')
    dadosAnuncios = []

    for bairro in bairros:
        try:
            elementoCidade = driver.find_element(by=By.XPATH, value="//input[@name='landing-city-input']")
            elementoCidade.click()
            elementoCidade = driver.find_element(by=By.XPATH, value=f"//p[contains(text(), '{cidades}')]")
            elementoCidade.click()
            time.sleep(5)
            
            elementoBairros = driver.find_element(by=By.XPATH, value="//input[@name='landing-neighborhood-input']")
            elementoBairros.click()
            elementoBairros = driver.find_element(by=By.XPATH, value=f"//p[contains(text(), '{bairro}')]")
            elementoBairros.click()
            time.sleep(5)
            
            elementoButton = driver.find_element(by=By.XPATH, value="//button[@type='submit']")
            elementoButton.click()
            time.sleep(5)
            
            try:
                elementoLink = driver.find_element(by=By.XPATH, value=f"//span[contains(text(), 'Pular tudo')]")
                elementoLink.click()
                time.sleep(5)
            except NoSuchElementException:
                logging.warning("O elemento 'Pular tudo' nao foi encontrado. Continuando sem clicar.")

        except NoSuchElementException:
            logging.error("Alguns elementos nao foram encontrados na página.")

        resultados = driver.find_elements(by=By.XPATH, value="//div[@data-testid='house-card-container-rent']")

        for resultado in resultados[:10]:
            time.sleep(6)
            try:
                elementoA = resultado.find_element(By.TAG_NAME, 'a')
                tituloAnuncio = elementoA.get_attribute('title')
                
                tipoAnuncio = resultado.find_element(by=By.XPATH, value=".//span[@data-testid='house-card-type']")
                
                enderecoAnuncio = resultado.find_element(by=By.XPATH, value=".//span[@data-testid='house-card-address']")
                
                regiaoAnuncio = resultado.find_element(by=By.XPATH, value=".//span[@data-testid='house-card-region']")

                elementoH3 = resultado.find_element(By.XPATH, value=".//h3[@data-testid='house-card-rent']")
                valorAluguelAnuncio = elementoH3.find_element(By.TAG_NAME, 'span').text

                dadosAnuncios.append({
                    'Titulo': tituloAnuncio,
                    'Tipo': tipoAnuncio.text,  
                    'Endereco': enderecoAnuncio.text,  
                    'Regiao': regiaoAnuncio.text, 
                    'Preco': valorAluguelAnuncio,
                    'Data de coleta' : dataAnuncios  
                })
                
            except NoSuchElementException:
                logging.error("Alguns elementos nao foram encontrados dentro do anúncio.")
        
        try:
            time.sleep(3)
            elementoIniciar = driver.find_element(by=By.XPATH, value="//a[contains(text(), 'Início')]")
            elementoIniciar.click()
        except NoSuchElementException:
            logging.error("O elemento 'Inicio' nao foi encontrado. Continuando sem clicar.")

    
    df = pd.DataFrame(dadosAnuncios)
    print(df)
    
    dataCSV = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')         
    df.to_csv(f"valoresMoradia_{dataCSV}.csv", index=False)

# Função MAIN responsável por receber os valores nas variáveis.    
def main():
    # Header
    driver = carregarDriver()
    url = 'https://www.quintoandar.com.br/'
    cidades = 'Brasília'
    bairros = ['Asa Sul', 'Asa Norte', 'Guará', 'Taguatinga', 'Ceilândia']

    # Funções de ação
    iniciarNavegador(driver, url)
    
    #definirEstado(driver, cidades)
    coletarDadosAnuncio(driver, bairros, cidades)

    driver.quit()

if __name__ == "__main__":
    main()