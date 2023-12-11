# Sistema de coleta de valores de apartamentos e casas
Esse projeto faz a coleta dos valores de apartamentos e casas do site Quinto Andar.

A coleta é feita com base em cidades por Estados onde ele retorna os dez primeiros resultados de cada cidade estabelecida.

Por fim, os resultado são armazenados em um arquivo CSV para consulta e manipulação.

### Conceitos abordados:
Nesse projeto foram abordados os conceitos de Web Scrapping para coleta de informações em um determinado site,
afim de realizar tomadas de decisões em cima dos resultados coletados.

### Requisitos:
- Instalar o Python3
- Instalar as bibliotecas, selenium, pandas, time, datetime 
- Driver do navegador Firefox
- Navegador Firefox atualizado

### Estrutura de pasta:
```
.
│   log_file.log
│   README.md
│   script_mineracao.py
│   valoresMoradia_2023-12-09_105404.csv
│
└───firefoxdriver-win64
        geckodriver.exe
    
```

### Uso:
Para usar basta executar os comandos: 

``` $ git clone https://github.com/mateussj12/projetoAutomacaoMonitoramento.git ```

``` $ python script_mineracao.py ```

Além disso, é possível personalizar o script para trazer resultados mais adequados para sua consulta.  

### Considerações finais:
- **@Desenvolvedor:** Mateus Santos de Jesus
- **@Linkedin:** https://www.linkedin.com/in/mateus-santos-de-jesus-9819a8186


