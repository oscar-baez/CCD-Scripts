import matplotlib.pyplot as plt
import time 
import numpy as np
from astropy.io import fits
import os
import concurrent.futures
directorio='/Users/oscar/Documents/Documentos/Docs/LME/CCD/OscuraImagenes/'
contenido = os.listdir(directorio)

#Funcion a paralelizar demux
def demux(nombre):
    directorio='/Users/oscar/Documents/Documentos/Docs/LME/CCD/OscuraImagenes/'
    hdulist = fits.open(directorio+nombre)
    tamx=int(hdulist[4].header['NAXIS1'])
    tamy=int(hdulist[4].header['NAXIS2'])
    nsamp=int(hdulist[4].header['NSAMP'])
    scidata = hdulist[4].data
    img_total= np.zeros((tamy, tamx))
    print('Se termino la imagen ') 
    for i in range(0,nsamp):
        for k in range (0,int(tamx/nsamp)):
            img_total[:,k+i]=scidata[:,(k*nsamp)+i]
# x=range(1000)

# def pruebaparalelo(par):
#     print(par)
    
#Ejeucion en paralelo
t1 = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(demux, contenido)
t2 = time.perf_counter()

# t1 = time.perf_counter()
# for k in range(0,len(x)):
#     print(x[k])
# t2 = time.perf_counter()

# t1 = time.perf_counter()
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     executor.map(pruebaparalelo, x)
# t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')