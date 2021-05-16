import colored
from gtts import gTTS
def Text_to_voice():
    print(colored.stylize("Enter Your Text :",colored.fg("dodger_blue_3")))
    user1 = input(colored.stylize(" ┌─[" + "erfanbanaei" + "~" + "@Text to Voice" + """]
 └──╼ """ + "卐 ", colored.fg("cyan_1"))).lower()
    mytext = user1
    language = 'en'
    print(colored.stylize("Enter Your Name File :",colored.fg("light_green")))
    user2 = input(colored.stylize(" ┌─[" + "erfanbanaei" + "~" + "@Text to Voice" + """]
 └──╼ """ + "卐 ", colored.fg("cyan_1"))).lower()
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(user2+".mp3")
    print(colored.stylize("Saved file :)",colored.fg("red_3b")))

Text_to_voice()