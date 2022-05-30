# libreria wave para leer archivos wav
import wave
from tkinter import filedialog
from tkinter import messagebox as MessageBox

MessageBox.showinfo("Bienvenido","Elige el archivo que contiene el mensaje")

file_path = filedialog.askopenfilename(title="Elige el archivo que contiene el mensaje")
song = wave.open(file_path, mode='rb')
# convertir udio a un array de bytes
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

# extraer el ultimo bit mas significativo de cada byte que es donde se esconde el mensaje
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
# convertir array de bytes a texto
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
#print(string)
# Se separan los caracteres & de relleno y solo se escoge l primera posición del array
#  que corresponde al mensae
decoded = string.split("&&&")[0]

# Imprimimos el mensae
MessageBox.showinfo("Su mensaje: ", decoded)
song.close()