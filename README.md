Project developed during my Master's Thesis in Biomedical Engineering at FEUP (FEUP_Dissertation_MiguelRocha_2024)

**Goal:**

In this thesis, a BCI system was developed in the context of aerial visual search, accelerating target detection (in this case identification of humans) in a vast open field environment covered by drone images. This detection is carried out at a high frame rate (5 images per second) by analyzing the time domain of the Electroencephalogram of human observers. For this purpose, Event-Related Potentials (ERPs) associated with visual attention neural mechanisms, namely N2pc, N2pcb and P3, elicited by an object of interest within the images were used. Additionally, the use of N2pc and N2pcb was tested to estimate the location of the human target within the image in the horizontal (left vs. right) and vertical (top vs. bottom) dimensions, respectively.

To test this approach, two independent Rapid Serial Visual Presentation (RSVP) paradigms were designed and presented separately to 6 subjects after obtaining authorization from the institutional ethics committee for this human experimentation. These two paradigms were designed with very different characteristics, namely a different set of environments/terrain and human target characteristics, including its clothes and the distribution of their centroids within the images. The first paradigm (240 images with 24 targets) was used to train/validate the machine learning (ML) models and the second (160 images with 16 targets) was used exclusively to test them. In addition, the second paradigm was seen for the first time by the 6 subjects during the procedure, allowing the evaluation of the brain’s ability to discriminate targets in an unknown and unseen environment and human target characteristics. Customized ML models (specific to each subject) and generalized models (trained with the data of all subjects for the first paradigm and tested with the second) were tested.

**System Architecture:**

The images simulating search and rescue scenarios were captured with a drone and then saved in a computer for image presentation. Despite being tested offline, this approach can be extrapolated to real-time scenarios where a drone will capture images of the environment and transfer them wirelessly to a computer iteratively, which is the ultimate application of BCIs. If the height of the drone is properly correlated with its velocity, 2 consecutive images captured will omit redundant space within the environment between those 2 images.

The BCI user visualizing the images will only need to be contextualized by the target type he is searching for in the stimuli. This is essential so that users can construct a visual representation within the working memory of the object required to be searched to properly allocate neural mechanisms related to the focus of attention for this object only. In this case, they were asked to visually search humans lying down. Then, specific ERPs related to visual attention are decoded to firstly detect the presence of the Target human and secondly, its location within the image along the horizontal and vertical dimensions and subsequently, the environment.

<img width="800" alt="SystArch" src="https://github.com/user-attachments/assets/1063afcd-1e7c-4f8b-8edf-1c8423300c11">

**EEG Acquisition parameters:** 

<img width="800" alt="EEG_dataset" src="https://github.com/user-attachments/assets/4032ff0a-e43b-4981-afc8-6f5c607fd36e">

These results indicate that this type of high-frame rate BCI system (hybrid, using human observers and ML techniques on the measured brain potentials) seems to generalize well when using N2pc and P3 ERPs. Thus, we believe we have carried out a proof of concept that this type of system can be used in real search and rescue scenarios, adding fast target detection to its location in the image and with the potential to have better performance and generalization capabilities than other computational approaches, demanding much less resources.

