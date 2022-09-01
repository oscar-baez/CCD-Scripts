import numpy as np
import matplotlib.pyplot as plt
import time 
#Get the start time
st = time.time()

from astropy.io import fits

hdu_list = fits.open('ANSAMP400_CleanAndReadSeq_2.fz')
hdu_list.info()

#print(hdu_list[1].header['NSAMP'])

scidata=hdu_list[4].data

fitz = np.zeros((100,1200)) 

for i in range(0,112):
    for k in range (0,1200):
        fitz[:,k]=scidata[:,(k*112)+i]
        
# for j in range (0,1200):
#     fitz[:,k]=scidata[:,(j*112)]
# hdu_list[1]=fitz
# hdu_list.writeto('NuevaImagen.fits')   
 
#Get the end time
et = time.time()
#Get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')