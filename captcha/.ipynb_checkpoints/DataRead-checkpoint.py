{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "030b2084",
   "metadata": {},
   "source": [
    "# Veri Setini Okuma"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8268a45d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from pathlib import Path\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0f0f19b",
   "metadata": {},
   "source": [
    "Bu notebookta veri seti üzerinden okuma yapılarak. Dataframe üzerine veriler eklenmektedir. Ayrıca veri etiketleri ayrıştırılmıştır."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37d126ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "def readData():\n",
    "    # Verileri alacağımız dataSet dizinindeki tüm resimler alma\n",
    "    data_dir = Path(\"./dataSet/\")\n",
    "    images = list(data_dir.glob(\"*.png\"))\n",
    "    \n",
    "    characters = set()\n",
    "\n",
    "    len_captcha = []\n",
    "\n",
    "    captcha_dataset = []\n",
    "    \n",
    "    for img_path in images:\n",
    "        \n",
    "        #Verileri etiketlerine göre ayrıştırma\n",
    "        label = img_path.name.split(\".png\")[0]\n",
    "        len_captcha.append(len(label))\n",
    "        \n",
    "        captcha_dataset.append((str(img_path), label))\n",
    "\n",
    "        # Veride bulunan karakterleri tuttuğumuz dizi\n",
    "        for character in label:\n",
    "            characters.add(character)\n",
    "            \n",
    "    characters = sorted(characters)\n",
    "    \n",
    "    df_captcha = pd.DataFrame(captcha_dataset, columns=[\"path\", \"label\"], index=None)\n",
    "    \n",
    "    return characters, df_captcha\n",
    "    \n",
    "    \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
