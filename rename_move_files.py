#Enumerate and move many files 
#by Peter Qz.
import glob 
import os
  
   
  
# Asigna el directorio a la variable files. 
files = glob.glob('/home/peter/Téléchargements/Nueva carpeta/*/*.jpg',  
                   recursive = True) 

# En el ciclo enumera los archivos, posterior los mueve  y cambia nombre al directorio.
for i, files in  enumerate(files): 
    os.rename(files,
          "/home/peter/Téléchargements/test/" + str("Imagen00")+ str(i) + ".jpg" )
    print(i,files) 
    
