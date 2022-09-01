import matplotlib.pyplot as plt
import time 
import numpy as np
from astropy.io import fits
import os
import concurrent.futures


#Funcion a paralelizar demux
def demux(nombre):
    hdulist = fits.open(nombre)
    tamx=int(hdulist[4].header['NAXIS1'])
    tamy=int(hdulist[4].header['NAXIS2'])
    nsamp=int(hdulist[4].header['NSAMP'])
    scidata = hdulist[4].data
    img_total= np.zeros((tamy, tamx))
    for i in range(0,nsamp):
        for k in range (0,int(tamx/nsamp)):
            img_total[:,k+i]=scidata[:,(k*nsamp)+i]
    print('Se termino la imagen ') 

if __name__ == '__main__':    
    directorio='/Users/oscar/Documents/Documentos/Docs/LME/CCD/OscuraImagenes/'
    contenido = os.listdir(directorio)
    for j in range(0,len(contenido)):
        contenido[j]=directorio+contenido[j]
    t1 = time.perf_counter()
    #with concurrent.futures.ProcessPoolExecutor() as executor:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(demux, contenido)
    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')
