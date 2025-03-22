from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")
input("🔍 Escaneie o QR Code e pressione Enter para continuar...")  # Manualmente escanear o QR Code

def enviar_mensagem(grupo, mensagem):
    try:
        print(f"🔍 Buscando grupo: {grupo}...")

        
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox' and @contenteditable='true']"))
        )
        search_box.clear()  
        search_box.send_keys(grupo)  
        time.sleep(3)  
        search_box.send_keys(Keys.ENTER)  

        time.sleep(3) 

        
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true' and @data-tab='10']"))
        )
        message_box.send_keys(mensagem)  
        time.sleep(1)
        message_box.send_keys(Keys.ENTER)  

        print(f"✅ Mensagem enviada para {grupo}: {mensagem}")

    except Exception as e:
        print(f"❌ Erro ao enviar mensagem para {grupo}: {str(e)}")


schedule.every().day.at("19:00").do(enviar_mensagem, "143 TOP GUN™", "⚔️ Atenção, cavaleiros da legião! 🌟 O Boss apareceu! 🛡️ Preparem-se para a batalha e mostrem sua força! 🚀 Juntos, a vitória será nossa!")

print("⏳ Bot iniciado! Aguardando o horário das mensagens...")
while True:
    schedule.run_pending()
    time.sleep(30)  
