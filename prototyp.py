from sense_hat import SenseHat
import time

sense = SenseHat()
global sense

def miganie():
    for i in range(3):        
        sense.clear()
        red = (255, 0, 0)
        lista = [red if i < 64 else red for i in range(64)]
        sense.set_pixels(lista)
        time.sleep(1)
        i += 1
        sense.clear()
        time.sleep(1)
        
def wyswietlanie():
        miganie()
        sense.show_message("Pomiar rozpoczyna sie!", text_colour = [0, 0, 128], scroll_speed = 0.06)

def akcelerator():
    for i in range(5):
        wynik_acc = sense.get_accelerometer_raw()
        x = round(wynik_acc.get("x"), 3)
        y = round(wynik_acc.get("y"), 3)
        z = round(wynik_acc.get("z"), 3)
        x = str(x)
        y = str(y)
        z = str(z)
        print("x: {0}, y: {1}, z: {2}".format(x, y, z))
        time.sleep(1)
        i += 1

def main():
    try:
        while True:
            wyswietlanie()
            akcelerator()
    except KeyboardInterrupt:
        pass
main()


        
                

