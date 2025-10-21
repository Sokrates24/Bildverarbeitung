# import cv2

#def run(image, result,settings=None): #Funktion zur Bildverarbeitung
    #Graubild erzeugen
 #   image3=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
  #  result.append({"name":"Gray","data":image3})

#if __name__ == '__main__': #Wird das Skript mit python Basis.py aufgerufen, ist diese Bedingung erfüllt
 #   image=cv2.imread("Images/210px-Zonenplatte_Cosinus.png")
  #  print(image.shape)
   # result=[]
    #run(image,result)
  #  for ele in result:
   #     cv2.imshow(ele["name"],ele["data"])
    #cv2.waitKey(0)
  #  cv2.destroyAllWindows()


#Bild aufrufen:

from PIL import Image

# Bildpfad
img_path = "Images/sample1.jpg"

# Bild öffnen
#
img = Image.open(img_path)

# Bild anzeigen
img.show() 

