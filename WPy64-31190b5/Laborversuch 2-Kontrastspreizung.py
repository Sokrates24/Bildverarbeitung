import cv2
import numpy as np

def kontrastspreizung_kanalweise(img,settings):
   
    height, width = img.shape[:2]
    gespreizt = np.zeros_like(img, dtype=np.uint8)
    
    # Für jeden Farbkanal (BGR)
    for c in range(3):
        # Minimum und Maximum des Kanals finden
        min_val = float(np.min(img[:, :, c]))
        max_val = float(np.max(img[:, :, c]))
        
        print(f"Kanal {c}: Min={min_val}, Max={max_val}")
        
        # Kontrastspreizung durchführen
        if max_val > min_val:  # Vermeidung von Division durch Null
            gespreizt=np.uint8(settings[0] * (img - min_val) / (max_val - min_val)) #Setting 0 damit man Schieberegler benutzen kann. MAtrizen 

        else:
            # Wenn alle Werte gleich sind, einfach kopieren
            gespreizt[:, :, c] = img[:, :, c]
            print("Alle Werte gleich")
    return gespreizt

def kontrastspreizung_global(img,settings): # settings einfügen, dass vorhanden
   
    height, width = img.shape[:2]
    gespreizt = np.zeros_like(img, dtype=np.uint8)
    
    # Globales Minimum und Maximum über alle Kanäle finden
    min_val = float(np.min(img))
    max_val = float(np.max(img))
    
    print(f"Global: Min={min_val}, Max={max_val}")


    
    # Kontrastspreizung durchführen
    if max_val > min_val:
        gespreizt = np.uint8(settings[0] * (img - min_val) / (max_val - min_val))
    
    else:
        gespreizt = img.copy()
    
    return gespreizt

def falschfarben_unbuntgerade(img):
    """
    Weg: Schwarz -> Blau -> Magenta -> Rot -> Gelb -> Weiß
    """
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img.copy()
    
    # Normalisierung auf [0, 5]
    t = gray.astype(np.float32) / 255.0 * 5.0
    
    # BGR Kanäle initialisieren
    B = np.clip(np.minimum(t, 2.0 - t), 0, 1)  # Steigt 0-1, fällt 1-2
    R = np.clip(np.minimum(t - 1.0, 3.0 - t), 0, 1)  # Steigt 1-2, fällt 2-3
    G = np.clip(t - 3.0, 0, 1)  # Steigt ab 3
    
    # Bei t>4: Alle Kanäle auf 1
    mask = t > 4.0
    B[mask] = (t[mask] - 4.0)
    G[mask] = 1.0
    R[mask] = 1.0
    
    falschfarben = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    falschfarben[:, :, 0] = np.uint8(B * 255)
    falschfarben[:, :, 1] = np.uint8(G * 255)
    falschfarben[:, :, 2] = np.uint8(R * 255)
    
    return falschfarben


def weissabgleich(img):
    """
    Weißabgleich basierend auf dem hellsten Farbwert.
    Findet den hellsten Pixel (Grauwert) und skaliert alle Kanäle so,
    dass dieser Pixel weiß wird.
    """
    # In Graustufen konvertieren um hellsten Punkt zu finden
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Finde Position des hellsten Pixels
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
    
    print(f"Hellster Pixel bei Position {max_loc} mit Grauwert {max_val}")
    
    # Hole die RGB-Werte des hellsten Pixels
    y, x = max_loc[1], max_loc[0]
    hellster_pixel = img[y, x]  # BGR Werte
    
    B_max = float(hellster_pixel[0])
    G_max = float(hellster_pixel[1])
    R_max = float(hellster_pixel[2])
    
    print(f"RGB-Werte des hellsten Pixels: R={R_max}, G={G_max}, B={B_max}")
    
    # Erstelle Ausgabebild
    abgeglichen = np.zeros_like(img, dtype=np.float32)
    
    # Skaliere jeden Kanal mit seinem Faktor
    if B_max > 0:
        abgeglichen[:, :, 0] = img[:, :, 0].astype(np.float32) * (255.0 / B_max)
    else:
        abgeglichen[:, :, 0] = img[:, :, 0].astype(np.float32)
        
    if G_max > 0:
        abgeglichen[:, :, 1] = img[:, :, 1].astype(np.float32) * (255.0 / G_max)
    else:
        abgeglichen[:, :, 1] = img[:, :, 1].astype(np.float32)
        
    if R_max > 0:
        abgeglichen[:, :, 2] = img[:, :, 2].astype(np.float32) * (255.0 / R_max)
    else:
        abgeglichen[:, :, 2] = img[:, :, 2].astype(np.float32)
    
    # Clippen auf [0, 255] und zurück zu uint8
    abgeglichen = np.clip(abgeglichen, 0, 255)
    abgeglichen = abgeglichen.astype(np.uint8)
    
    return abgeglichen



def farbskala_einfuegen(img, breite=50):
    """Fügt vertikale Farbskala rechts ein"""
    height, width = img.shape[:2]
    neues_bild = np.zeros((height, width + breite + 20, 3), dtype=np.uint8)
    neues_bild[:, :width] = img
    
    # Erstelle Grauwert-Gradient für Skala
    gradient = np.linspace(255, 0, height).reshape(-1, 1)
    gradient = np.repeat(gradient, breite, axis=1).astype(np.uint8)
    
    skala_img = np.stack([gradient, gradient, gradient], axis=2)
    skala_colored = falschfarben_unbuntgerade(skala_img)
    
    neues_bild[:, width + 10:width + 10 + breite] = skala_colored
    
    # Rahmen und Text
    cv2.rectangle(neues_bild, (width + 10, 0), (width + 10 + breite, height), (255, 255, 255), 2)
    cv2.putText(neues_bild, "255", (width + 12, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(neues_bild, "0", (width + 12, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    return neues_bild








def run(image, result, settings=None):
    """Hauptfunktion zur Bildverarbeitung"""
    # Original Bild
    result.append({"name": "Original", "data": image})
    
    # Kontrastspreizung
    kontrast_gespreizt = kontrastspreizung_kanalweise(image,settings) #settings mit einfügen, damit settings vorhanden
    result.append({"name": "Kontrastspreizung Kanalweise", "data": kontrast_gespreizt})

     # Globale Kontrastspreizung
    kontrast_global = kontrastspreizung_global(image,settings)
    result.append({"name": "Kontrastspreizung Global", "data": kontrast_global})

    falschfarben = falschfarben_unbuntgerade(image)
    result.append({"name": "Falschfarben", "data": falschfarben})
    
    falschfarben_skala = farbskala_einfuegen(falschfarben, breite=50)
    result.append({"name": "Falschfarben mit Skala", "data": falschfarben_skala})

    weiss = weissabgleich(image)
    result.append({"name": "Weissabgleich", "data": weiss})


if __name__ == '__main__':
    # Bild einlesen
    image = cv2.imread("Images/19021.jpg")
    
    if image is None:
        print("Fehler: Bild konnte nicht geladen werden!")
    else:
        print(f"Bildgröße: {image.shape}")
        
        result = []
        run(image, result)
        
        # Alle Bilder anzeigen
        for ele in result:
            #cv2.namedWindow(ele["name"], cv2.WINDOW_NORMAL)
            cv2.imshow(ele["name"], ele["data"])
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()