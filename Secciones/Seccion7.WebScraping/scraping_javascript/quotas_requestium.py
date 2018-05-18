import json

from requestium import Session

s = Session(webdriver_path='./chromedriver',                       
                browser='chrome',                          
                default_timeout=15,
                webdriver_options={'arguments': ['headless']})
)
s.driver.get("http://quotes.toscrape.com/js")


archivo_frases = open("frases.jl", "a", encoding="utf-8")

def procesar_frase(frase):
    texto_frase = frase.css("span.text::text").extract_first()
    autor = frase.css("small.author::text").extract_first()
    etiquetas = frase.css("div.tags>a::text").extract()
    return {
        "autor": autor,
        "frase": texto_frase,
        "etiquetas": etiquetas
    }


while 1:
    for frase in s.driver.css("div.quote"):                   
        datos_frase = procesar_frase(frase)
        print(datos_frase)
        datos_frase_json = json.dumps(datos_frase)
        archivo_frases.write(datos_frase_json)
        archivo_frases.write("\n")
    s.driver.ensure_element_by_css_selector("li.next>a", timeout=5).ensure_click()
