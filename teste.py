from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

class WhatsAppBot:
    def __init__(self):
        self.navegador = webdriver.Firefox()

    def enviar_mensagem_com_botoes(self, numero, mensagem, opcoes):
        self.navegador.get("https://web.whatsapp.com/")

        while len(self.navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)

        texto = urllib.parse.quote(f"{mensagem}\n\nOpções:\n1. {opcoes[0]}\n2. {opcoes[1]}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        self.navegador.get(link)

        while len(self.navegador.find_elements_by_id("side")) < 1:
            time.sleep(1)

        input_box = self.navegador.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
        input_box.send_keys(Keys.ENTER)

    def fechar_navegador(self):
        self.navegador.quit()

# Exemplo de uso
bot = WhatsAppBot()
numero = "+5569984611669"  # Substitua pelo número de telefone correto
mensagem = "Olá! Você deseja continuar?"
opcoes = ["Sim", "Não"]

bot.enviar_mensagem_com_botoes(numero, mensagem, opcoes)
bot.fechar_navegador()
