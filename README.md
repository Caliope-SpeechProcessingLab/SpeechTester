# Table of Content:

- [SpeechTester](#speechtester)
- [Using Speech Tester](#using-speech-tester)
  * [1. Download software](#1-download-software)
  * [2. Checking software pre-requisites:](#2-checking-software-pre-requisites-)
  * [3.    Setting-up one simulation](#3----setting-up-one-simulation)
      - [a.  Create the folder structure for the audio files](#a--create-the-folder-structure-for-the-audio-files)
      - [b.  Set up your audio paths](#b--set-up-your-audio-paths)
      - [c.  Set up your lexicon](#c--set-up-your-lexicon)
      - [d.  Set up your grammar](#d--set-up-your-grammar)
      - [e.  Set up your HTK label files](#e--set-up-your-htk-label-files)
      - [f.  Tracking of errors](#f--tracking-of-errors)
      - [g.  Set up your locutor array](#g--set-up-your-locutor-array)
      - [h.  Create the folder structure for results files (confusion matrices)](#h--create-the-folder-structure-for-results-files--confusion-matrices-)
  * [4.    Run one simulation](#4----run-one-simulation)
  * [5.    Run multiple simulations](#5----run-multiple-simulations)
- [Authors and grants](#Authors-and-grants)
  

# SpeechTester

Speech Tester is a set of Python scripts conceived as an extension to HTK Automatic Speech Recognition system (Young et al., 2002). Speech Tester aims to help language researchers and engineers to measure the intelligibility of transformed audio signals. Here the termed “transform” may describe any process that alters a speech signal or its reception by a potential listener. For instance, any type of audio compression, noise background and/or reverberation, vocoding (to simulate cochlear implants), partial auditory loss, or any combination of these and other imaginable transformations. Intelligibility refers to the capacity of a listener to recognize a transformed signal. Extended information of this introduction can be found in manual_speechTester.pdf

Speech tester can help you automatize the process of running a large number of simulations (up to various thousands, it depends on your processing capacity). Before you can use speech tester you will need some tool to transform the original stimuli. This could be done, among others, with Praat or Matlab. Next, it will be necessary to adapt Speech Tester to your experiment.  


# Using Speech Tester

  Pre-requisites to running Speech Tester:
   - Operative system: UNIX-type
   - Git
   - ASR system: HTK 
   - Python 3. You will need these non standard packages: Path, numpy.
   - Prior knowledge with ASR systems and preferably with HTK.
   - Transformed versions of the original stimuli must be available 


  We recommend you follow these steps:
  1.	Download software.
  2.	Check software pre-requisites.
  3.	Setting-up one simulation:
    - Prepare and placing the manipulated audio database in its folder
    - Define the lexicon and grammar
    - Annotate the audio files for training
    - Annotate the audio files for testing
  4.	Run one simulation.
  5.	Run multiple simulations.
  
  
  ## 1.	Download software
  
  Clone this repo to your local machine using:

     git clone https://github.com/Caliope-SpeechProcessingLab/SpeechTester.git

  ## 2.	Checking software pre-requisites:

   Run the bash file ```utils/Demo/speechTester.sh```:

        bash utils/Demo/speechTester_demo.sh

  If this instruction doesn´t generate any error, you have all software requisites to develop your own experiment. In contrary, you must          review your pre-requisites. 



   ## 3.	Setting-up one simulation
   
   #### a. Your audiofile list
   Every audio file in each simulation folder must have a certain syntax. Each filename is composed of fields which are separated by "\_" characters. First field must indicate the word recorded. The second one has to show the speaker identifier, which can be any sequence of letters that you prefer. The rest of the audio filename is free-writing. An example could be:
   
        ba_S01_extraFields.wav
        
 In that case, your word recorded is "ba", and the "S01" is the speaker identifier. Next fields could add relevant information for you.
   

   #### b.  Create the folder structure for the audio files
   These must be placed in the folder ```audios```, which is placed in the main folder ```speechTester```. Inside this folder you must create a folder for you experiment (for example   “my_experiment”). Inside this last folder you will have to place one folder per manipulated database. At this point we need just one of these folder. The full path to your database will be something like: ```audios/my_experiment/simulation1/```. 

   #### c.  Set up your audio paths
   Edit the file  ```speechTester.sh``` to modify these two string variables: folder_in, folder_out
   
      - folder_in: path where set of simulated corpus (audios) must be placed.
      - folder_out: path where results of simulations are placed.
      
   At first, this variables are:
   
       
        folder_in=../audios/my_experiment/
        folder_out=../Resultados/my_experiment/Por_simulacion/
        
        
   Then, to modify these variable for your case, you must replace the name ```my_experiment``` by the real name of your experiment folder created in setp 3.a.
      
   #### d.  Set up your lexicon
   Edit the file ```speechTester.sh``` to modify these three arrays: dicItems, wordlist, and lablist

      -	dicitems: lists the words (syllables in our case) of the dictionary with the corresponding phoneme sequence
      -	wordlist: has again the words in the dictionary 
      -	lablist: has the list of phonemes (monophones in HTK terminology) 
      
   #### e.  Set up your grammar
   Edit the file ```htk/Gramatica/gram.htk```, according to HTK book section 12.3 and your set of words in your dictionary. In the context of our research, the software has been tested only with the grammar model explained in the introduction section (located in manual_speechTester.pdf). 
      
      
   #### f.	Set up your HTK label files

   HTK will need that each audio file is annotated in two different ways:

   -	At the phoneme level. These files (one per audio) should be saved in the ```htk/Entrenamiento/Parametros/```

   -	At the word (syllable) level. These files (one per audio) should be saved in the ```htk/Testeo/Parametros/```

        Below you can see one example of each for the syllable /ba/: 
        ```
          For training: 
          000000000 000088911 silence
          000088911 000247854 b	
          000247854 000418718 a	
          000418718 000509437 silence

          For testing:
          000000000 000088911 silence
          000088911 000418718 ba	
          000418718 000509437 silence
         ```

   Note: 
   Verify that the names of .lab files are the same as the .wav files in ```htk/Entrenamiento/parametros/ and In htk/Testeo/parametros/```

   If you want to know more about how to create the labels, we recommend you to read the HTK manual chapter 6. 

  #### g.  Tracking of errors 
   In order to be able to track errors through the terminal, the variable ```N_Cores``` in the bash script speechTester.sh must be set to 1, which centralize all simulations in one processing unit. Therefore, every instruction of the program is executed in a sequential manner instead of asynchronous. For the same purpose, the ```UPPER-CASE``` portion of the python code line in the main for loop, must be removed:
```
    python3 htk_Core$icore/htk_cross_val.py -c $icore -f ${folder_divided}$icore_folder 
    -i $folder_in -o $folder_out -l ${labList[@]} -w
    ${wordList[@]} -d ${dicItems[@]} > HTK_CORE$ICORE/LOGS/FOLDER_CORE$ICORE.LOG &
```

   #### h.  Set up your speaker array
   
   This array is located in the file speechTester.sh. The name of the variable is "tsujs" and is composed of all speaker identifiers. A speaker identifier is a portion of the audio filename that identifies a unique speaker of your experiment. This allows to make an structured cross-validation in the testing stage of the recognition experiment. An audio filename must exposed a certain structured. For example, you may have several .wav files with the following names: ba_S01.wav, be_S01.wav, be_S02.wav, or bi_S05.wav. In this case, the speaker identifiers would be "S01", "S02", and "S05". An example of such speaker array for this case would be:
   
   
    tsujs=('S01' 'S02' 'S05')


   #### i.	Create the folder structure for results files (confusion matrices)
   These will be created in the folder Resultados, but you will need to create the same folder structure that you made for the audios, adding another folder named ```Por_simulacion```. For the example above:

        audios/experiment_name

  This should be the folder name:

        Resultados/experiment_name/Por_simulacion




   ## 4.	Run one simulation

   1. Run speechTester.sh through a terminal:

          bash speechTester.sh
        
   2. If the above steps don´t show any error, you can proceed to execute all your simulations
   3. Go to file ```Resultados/experiment_name/Por_simulacion/simulation_name/simulation_name.htk```, and review your results with the confusion matrix help. In case the results don´t make sense, review all previous steps.





   ## 5.	Run multiple simulations

   1. Place the audios for all the simulations (one folder per simulation) in the folder inside ```audios/experiment_name```. As a result, in that location there will be a set of folders, each one having an audio transformed version of your corpus.
   
   Note: ```It is important to all audio filenames equal from one folder simulation to another. ```


   2.	In the script speechTester.sh, set the variable ```N_Cores``` to the number of cores (processing units) you want to run your experiment (it depends on your device). Then, restore the UPPERCASE portion of the code that you removed earlier.


    python3 htk_Core$icore/htk_cross_val.py -c $icore -f ${folder_divided}$icore_folder 
    -i $folder_in -o $folder_out -l ${labList[@]} -w
    ${wordList[@]} -d ${dicItems[@]} > HTK_CORE$ICORE/LOGS/FOLDER_CORE$ICORE.LOG &


   3.	Execute bash file speechTester.sh:
   
    
    bash speechTester.sh
    
     

If everything goes well your ```Resultados``` folder will have two files per simulation. One will contain the confusion matrix, the other will list the errors in that simulation.


# Authors and grants

The present set of scripts has been developed with the participation of:
- Salvador Florido (Desiged the bulk of the system and wrote the majority of the code until march 2020)
- Andrés Lozano (Programmer: april 2020 - may 2021)
- Ignacio Moreno-Torres and Enrique Nava: Supervision

This work was supported by a grant from the Spanish Ministerio de Ciencia e Innovación to Ignacio Moreno-Torres and Enrique Nava (RTI2018-094846-B-I00) 
