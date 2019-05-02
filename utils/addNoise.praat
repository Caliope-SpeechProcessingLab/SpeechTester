# Este script:
#  1) toma un sonido de una duración X
#  2) extrae un fragmento de  duración X de un longsound con ruido de fondo
#  3) Los combina con el SNR especificado y la extensión al nombre 

# En la versión actual, pongo a 60dB ambos sonidos antes de sumarlos

# IMPORTANTE: 
# Este script mantiene fijo el nivel de RUIDO, y aumenta el de
# LA SÍLABA.

# Ratio SNR
desired_SNR = -12.0
suffix$ = "SNRm12"

# Carpeta de destino
folder$ = "/Users/ignaciomoreno-torres/Desktop/htk/temp/Noise/SNR105/"

# Intensidad de referencia
nivelBasedBs = 70.0



# folder$ = "/Users/imt/Desktop/Temp/"

# Selección de ruido y sonido

ruido = selected ("LongSound", 1)

n = numberOfSelected ("Sound")
for i from 1 to n
    senyal'i' = selected ("Sound", i)
    senyal'i'$ = selected$ ("Sound", i)
endfor

# Main loop

for i from 1 to n

senyal = senyal'i' 
senyal$ = senyal'i'$ 

# Creo un ruido de la duración de la sílaba

select senyal
dursenyal = Get total duration
Scale intensity: nivelBasedBs

# dur_prepostSenyal = (1.22 - dursenyal) / 2
# Create Sound from formula: "sineWithNoise", 1, 0, dur_prepostSenyal, 48000, "0"
# presenyal = selected ("Sound")
# postsenyal = selected ("Sound") 
# select presenyal
# plus senyal
# Concatenate with overlap: 0.01
# temp1 = selected ("Sound")

# plus postsenyal
# Concatenate with overlap: 0.01
# senyal12 = selected ("Sound")

select senyal
curRMS = Get root-mean-square... 0 0

select ruido
dur_total_ruido = Get total duration

ini = randomInteger (0, dur_total_ruido-1.2)
fin = ini + dursenyal

# Extraigo ruido del tamaño de la señal

Extract part... ini fin no
ruidoParte = selected("Sound")
Scale intensity: nivelBasedBs

noiseRMS = Get root-mean-square... 0 0

noiseAdjustCoef = (curRMS / (10^(desired_SNR/20))) / noiseRMS
silAdjustCoef = 1 / noiseAdjustCoef

select senyal
Copy: "silabaConRuido_2"
Formula: "self[col] * 'silAdjustCoef' + Object_'ruidoParte'[col]"

Rename... 'senyal$''suffix$'
Scale intensity: nivelBasedBs

fullFilename$ = "'folder$'" + "'senyal$'" + "'suffix$'"+ ".wav"
# Save as WAV file... 'fullFilename$'
		
select ruidoParte
Remove

# TRACE
nombre$ = "'senyal$'" + "'suffix$'"
print 'nombre$'
printline
# FIN TRACE


# select senyal12
# plus presenyal
# plus temp1
# plus ruido120
# plus ruido121
# plus ruido123
# Remove

endfor

