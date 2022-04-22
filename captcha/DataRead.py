from pathlib import Path
import pandas as pd

def readData():
    # Verileri alacağımız dataSet dizinindeki tüm resimler alma
    data_dir = Path("./dataSet/")
    images = list(data_dir.glob("*.png"))
    
    characters = set()

    len_captcha = []

    captcha_dataset = []
    
    for img_path in images:
        
        #Verileri etiketlerine göre ayrıştırma
        label = img_path.name.split(".png")[0]
        len_captcha.append(len(label))
        
        captcha_dataset.append((str(img_path), label))

        # Veride bulunan karakterleri tuttuğumuz dizi
        for character in label:
            characters.add(character)
            
    characters = sorted(characters)
    
    df_captcha = pd.DataFrame(captcha_dataset, columns=["path", "label"], index=None)
    df_captcha = df_captcha.sample(frac=1.).reset_index(drop=True)
    
    return characters, df_captcha,images
    
    
    