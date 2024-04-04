#1. IMPORTAMOS LAS LIBRERÍAS NECESARIAS
import os
import keras
from keras import layers
import tensorflow
from tensorflow import data
import numpy as np
import matplotlib.pyplot as plt

#2. CREAMOS LAS ÓRDENES DE LA APLICACIÓN
numero_saltos = 0
for folder_name in ("Cat","Dog"):
    folder_path = os.path.join("PetImages", folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path,fname)
        try:
            fobj = open(fpath, "rb")
            is_jfif = b"JFIF" in fobj.peek(10)
        finally:
            fobj.close()
        if not is_jfif:
            numero_saltos += 1
            os.remove(fpath)
print(f"Han sido borrados {numero_saltos} archivos")