# wave sirve para leer archivos wav
#tkinter  es la libreria que nos permite desplegar dialogos 
import wave
import os
import  tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox as MessageBox
root = tk.Tk()
root.withdraw()
#abrimos el buscdor de archivos para seleccionar el archivo wav
MessageBox.showinfo("Bienvenido","Elige el archivo .WAV en donde se escondera el mensaje.")
file_path = filedialog.askopenfilename(title="Elige el archivo .WAV en donde se escondera el mensaje")
file_name= os.path.splitext(os.path.basename(file_path))[0]
# abrimos el archivo wav
song = wave.open(file_path, mode='rb')
# leemos los frames y los convertimos en un array de bytes
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# ingresamos el mensae a esconder
string=simpledialog.askstring(title="Bienvenido",
                                  prompt="Mensaje a ocultar:")
# rellenamos el mensae con caracteres '&' para alcansar la longitud del array de bytes
string = string + int((len(frame_bytes)-(len(string)*64))/8) *'&'
# convertimos el texto en un array de bits
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

# remplazamos el ultimo bit de cada byte del archivo de audio por un bit del texto 
for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
# obtenemos los bytes modificados por el texto
frame_modified = bytes(frame_bytes)

#se obtiene la ruta donde se va a guardar el audio con el mensaje

MessageBox.showinfo("Bienvenido","Elija la carpeta donde desea guardar el audio con el mensaje")
path = filedialog.askdirectory(title="carpeta donde quiere guardar el audio con el mensaje:")

folder=path+'/'

#nombre del nuevo audio, el nuevo archivo mantiene el nombre original del audio y se le grega 
# la palabra hidden 

new_Name=folder+file_name+'_hidden.wav'


# escribimos los bytes modificados en un archivo nuevo de audio 

with wave.open(new_Name, 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()

MessageBox.showinfo("Hasta pronto","Audio guardado con exito")