# This Praat script:
#  1) Takes a longsound file with noise and a list of Sound files and
#  creates another list of sound files with noise.  
#  Before running the scrip fix these two variables:
#    - Desired_SNR: real
#    - folder: the folder where the resulting files will be saved
# Depending on what you want to do, you may have to add or not a suffix:
#    - suffix$ = "xxx"


# IMPORTANT: 
# - This script keeps the noise level fix, and modifies the levels of the signal. 
# - The noise file must be a longsound file

### Configuration variables

# Ratio SNR
desired_SNR = -12.0
suffix$ = "SNRm12"

# Output folder
folder$ = "/Users/ignaciomoreno-torres/Desktop/htk/temp/"

# Intensity 
nivelBasedBs = 70.0

# Step 1. Name the noise file and the targel signals 

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

select senyal
dursenyal = Get total duration
Scale intensity: nivelBasedBs

select senyal
curRMS = Get root-mean-square... 0 0

select ruido
dur_total_ruido = Get total duration

ini = randomInteger (0, dur_total_ruido-1.2)
fin = ini + dursenyal

# Extract noise of the duration of the signal

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
Save as WAV file... 'fullFilename$'
		
select ruidoParte
Remove

# TRACE
nombre$ = "'senyal$'" + "'suffix$'"
print 'nombre$'
printline
# End TRACE


endfor

