import speech_recognition as sr
import os
import pyaudio
print("Inicializando... um momento...")

# função de ouvir e reconhecer a fala
def ouvir_microfone():
    #habilitando o microfone do usuário
    microfone = sr.Recognizer()

    #usando o mic
    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)
        print("Diga Algo")
        audio = microfone.listen(source)

    try:
        print("Recognizando...")
        frase = microfone.recognize_google(audio, language='pt-BR')
        if "navegador" in frase:
            os.system('start Chrome.exe')
            return False
        elif "word" in frase:
            os.system('start Word.exe')
        elif "Encerrar" in frase:
            os.system(exit)
            return True
        print("Voce disse: "+ frase)

    except sr.UnknownValueError:
        print("Não entendi o que você disse. Tente novamente.")
    except sr.RequestError as e:
        print(f"Não foi possível solicitar os resultados do serviço de reconhecimento de fala; {e}")

ouvir_microfone()

        

