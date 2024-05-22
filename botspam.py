import pyautogui as pag
import keyboard
import time

tempodipausa = 5


def stop():
    print("programma fermato")
    time.sleep(3)
    pag.keyUp("ctrl")

def inizio():
    for x in range(5,0,-1):
        print(f"il programma partira tra {x}!") 
        time.sleep(1)

def sceltatasto():
   while True:
      if keyboard.get_hotkey_name() != "":
         tasto = keyboard.get_hotkey_name()
         return tasto




print("scegli il tasto per fermare e avviare il programma")

tasto = (sceltatasto())


print(f"premi ({tasto}) per fermare e avviare il programma")

time.sleep(2) 

while True:

  if keyboard.is_pressed(tasto) == True:

    inizio()

      
    while keyboard.is_pressed(tasto) != True:

      pag.keyDown("ctrl")
      pag.press(["V"])
      pag.press(["enter"])

      if pag.pixel(1050,570)[2] == 242 or pag.pixel(1050,570)[2] == 196:
         pag.moveTo(1050,570)
         pag.click()
         time.sleep(tempodipausa)
         print("DISCORD LEVATI DAL CAZZO")

    stop()

#* con tanto affetto da Fitonix per Arancia