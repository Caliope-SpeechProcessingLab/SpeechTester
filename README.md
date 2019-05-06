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

   Run the bash file utils/Demo/speechTester.sh:

        bash utils/Demo/speechTester_demo.sh

  If this instruction doesn´t generate any error, you have all software requisites to develop your own experiment. In contrary, you must          review your installation. 



   ## 3.	Setting-up one simulation

   #### a.  Create the folder structure for the audio files
   These must be placed in the folder “audios”. Inside this folder you must create a folder for you experiment (for example   “my_experiment”). Inside this last folder you will have to place one folder per manipulated database. At this point we need just one of these folder. The full path to your database will be something like: audios/my_experiment /simulation1/. 

   #### b.  Set up your lexicon
   Edit the file speechTester.sh file to modify these three arrays: dicItems, wordlist, and lablist

      -	dicitems: lists the words (syllables in our case) of the dictionary with the corresponding phoneme sequence
      -	wordlist: has again the words in the dictionary 
      -	lablist: has the list of phonemes (monophones in HTK terminology) 
      
   #### c.  Set up your grammar
   Edit the file htk/Gramatica/gram.htk, according to HTK book section 12.3 and your set of words in your dictionary. In the context of our research, the software have been tested only with the grammar model explained in the introduction section (located in manual_speechTester.pdf). 
      
      
   #### d.	Set up your HTK label files

   HTK will need that each audio file is annotated in two different ways:

   -	At the phoneme level. These files (one per audio) should be saved in the htk/Entrenamiento/Parametros/

   -	At the word (syllable) level. These files (one per audio) should be saved in the htk/Testeo/Parametros/

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
   Verify that the names of .lab files are the same as the .wav files (in htk/Entrenamiento/parametros/ and In htk/Testeo/parametros/)

   If you want to know more about how to create the labels, we recommend you to read the HTK manual chapter 6. 

  #### e.  Tracking of errors 
   In order to be able to track errors through the terminal, the variable “N_Cores” in the bash script speechTester.sh must be set to 1, which centralize all simultions in one processing unit. Therefore, every instruction of the program is executed in a sequential manner instead of asynchronous. For the same purpose, the UPPER-CASE portion of the python code line in the main for loop, must be remove:
```
    python3 htk_Core$icore/htk_cross_val.py -c $icore -f ${folder_divided}$icore_folder 
    -i $folder_in -o $folder_out -l ${labList[@]} -w
    ${wordList[@]} -d ${dicItems[@]} > HTK_CORE$ICORE/LOGS/FOLDER_CORE$ICORE.LOG &
```



   #### f.	Create the folder structure for results files (confusion matrices)
   These will be created in the folder Resultados, but you will need to create the same folder structure that you made for the audios, adding another folder named “Por_simulacion”. For the example above:

        audios/experiment_name

        this should be the folder name:

        Resultados/experiment_name/Por_simulacion




   ## 4.	Run one simulation

   Execute speechTester.sh through a terminal:

        bash speechTester.sh





   ## 5.	Run multiple simulations

   1.	If the above steps doesn´t show any error, you can proceed to execute all your simulations. Place the rest of your simulations in different folders inside audios/experiment_name. As a result, in that location there will be a set of folders, each one having an audio transformed version of your corpus.


   2.	In the script speechTester.sh, set the variable “N_Cores” to the number of cores (processing units) you want to run your experiment (it depends on your device). And write the python code line in its previous version. That means add the UPPERCASE portion of code to the python line below.


    python3 htk_Core$icore/htk_cross_val.py -c $icore -f ${folder_divided}$icore_folder 
    -i $folder_in -o $folder_out -l ${labList[@]} -w
    ${wordList[@]} -d ${dicItems[@]} > HTK_CORE$ICORE/LOGS/FOLDER_CORE$ICORE.LOG &


   3.	Execute bash file speechTester.sh:

          “bash speechTester.sh”



