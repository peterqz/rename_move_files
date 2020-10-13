#!/usr/bin/env python
# coding: utf-8

# In[32]:


import glob 
import os
  
   
  
# Asigna el directorio a la variable files. 
print("Using glob.glob()") 
files = glob.glob('/home/peter/Téléchargements/Nueva carpeta/*/*.jpg',  
                   recursive = True) 

print(files) 
# En el ciclo enumera los archivos, posterior los mueve  y cambia nombre al directorio.
for i, files in  enumerate(files): 
    os.rename(files,
          "/home/peter/Téléchargements/test/" + str("Imagen00")+ str(i) + ".jpg" )
    print(i,files) 
    


# In[ ]:





# In[ ]:





# In[3]:




