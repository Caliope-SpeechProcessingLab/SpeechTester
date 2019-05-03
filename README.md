# SpeechTester

Note: Extended information about this software in manual_speechTester.pdf

Speech Tester is a set of Python scripts conceived as an extension to HTK Automatic Speech Recognition system (Young et al., 2002). Speech Tester aims to help language researchers and engineers to measure the intelligibility of transformed audio signals. Here the termed “transform” may describe any process that alters a speech signal or its reception by a potential listener. For instance, any type of audio compression, noise background and/or reverberation, vocoding (to simulate cochlear implants), partial auditory loss, or any combination of these and other imaginable transformations. Intelligibility refers to the capacity of a listener to recognize a transformed signal. In the rest of this introduction we describe the motivation to develop Speech Tester to measure speech intelligibility. Then, we present a basic guide to Speech Tester.

Speech tester can help you automatize the process of running a large number of simulations (up to various thousands, it depends on your processing capacity). Before you can use speech tester you will need some tool to transform the original stimuli. This could be done, among others, with Praat or Matlab. Next, it will be necessary to adapt Speech Tester to your experiment.  


#- Using Speech Tester

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
    o	Prepare and placing the manipulated audio database in its folder
    o	Define the lexicon and grammar
    o	Annotate the audio files for training
    o	Annotate the audio files for testing
  4.	Run one simulation.
  5.	Run multiple simulations.
