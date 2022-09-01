
import time 
import numpy as np
from astropy.io import fits
import os
import numba
#Prueba con NUMBA
#Funcion a paralelizar demux

def demux(item):
    hdulist = fits.open(item)
    tamx=int(hdulist[4].header['NAXIS1'])
    tamy=int(hdulist[4].header['NAXIS2'])
    nsamp=int(hdulist[4].header['NSAMP'])
    scidata = hdulist[4].data
    img_total= np.zeros((tamy, tamx))
    for i in range(0,nsamp):
        for k in range (0,int(tamx/nsamp)):
            img_total[:,k+i]=scidata[:,(k*nsamp)+i]
    print('Se termino la imagen ',item)   



if __name__ == '__main__':
    directorio='/Users/oscar/Documents/Documentos/Docs/LME/CCD/OscuraImagenes/'
    contenido = os.listdir(directorio) 
    for j in range(0,len(contenido)):
        contenido[j]=directorio+contenido[j]
    st = time.time()
    for item in range(0,len(contenido)): #For para cada item del directorio
        #print("El item esss ",contenido[item])
        demux(contenido[item])

        
        
        
        
        
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')