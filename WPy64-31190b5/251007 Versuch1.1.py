import cv2
import numpy as np

def run(image, result, settings=None):  # Funktion zur Bildverarbeitung
    # Graubild erzeugen
    image3 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    result.append({"name": "Gray", "data": image3})
    
    # Bild spiegeln an der Y-Achse
    gespiegelt = spiegeln_y_achse(image)
    result.append({"name": "Gespiegelt Y-Achse", "data": gespiegelt})

     # Grauwerte invertieren
    grau_invertiert = invertieren_grauwerte(image3)
    result.append({"name": "Grauwerte invertiert", "data": grau_invertiert})

    farb_invertiert = invertieren_grauwerte(image3)
    result.append({"name": "Farbwertr invertiert", "data": farb_invertiert})
#Rotation Cosinus 
    size = 512 #Größe Bild
    x = np.linspace(-1,1,size)
    y = np.linspace(-1,1,size)
    X,Y= np.meshgrid(x,y)
    r=np.sqrt(X**2 + Y**2)
    cos_image = 0.5 +0.5 * np.cos(40*np.pi *r)
    cos_image=np.uint8(cos_image*255)
    result.append({"name": "Cos_Gray", "data": cos_image})


def spiegeln_y_achse(img):
    """Spiegelt das Bild an der Y-Achse (horizontal)"""
    height, width = img.shape[:2]
    gespiegelt = img.copy()
    
    for y in range(height):
        for x in range(width):
            gespiegelt[y, x] = img[y, width - 1 - x]
    
    return gespiegelt

# Bild Grauwerte invertieren

def invertieren_grauwerte(img):
    height, width = img.shape[:2]
    invertiert = img.copy()

    for y in range(height):
        for x in range(width):
            invertiert[y,x] = 255 - img[y, x]

    return invertiert

def invertieren_farbwerte(img):
    """Invertiert die Farbwerte des Bildes (BGR)"""
    height, width = img.shape[:2]
    invertiert = img.copy()
    
    for y in range(height):
        for x in range(width):
            for c in range(3):  # BGR Kanäle
                invertiert[y, x, c] = 255 - img[y, x, c]
    
    return invertiert


if __name__ == '__main__':  # Wird das Skript mit python Basis.py aufgerufen, ist diese Bedingung erfüllt
    image = cv2.imread("Images/210px-Zonenplatte_Cosinus.png")
    print(image.shape)
    result = []
    run(image, result)
    for ele in result:
        cv2.imshow(ele["name"], ele["data"])


   

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    