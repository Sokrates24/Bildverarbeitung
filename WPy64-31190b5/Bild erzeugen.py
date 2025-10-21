import cv2
import numpy as np

def run(image, result, settings=None):  # Funktion zur Bildverarbeitung
    # Graubild erzeugen
    image3 = cv2.cvtColor(image, cv2)
    result.append({"name": "Color", "data": image3})
    

if __name__ == '__main__':  # Wird das Skript mit python Basis.py aufgerufen, ist diese Bedingung erfüllt
    image = cv2.imread("Images/210px-Zonenplatte_Cosinus.png")
    print(image.shape)
    result = []
    run(image, result)
    for ele in result:
        cv2.imshow(ele["name"], ele["data"])


   

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    