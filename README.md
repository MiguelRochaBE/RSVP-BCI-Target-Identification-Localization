# RSVP-BCI-Target-Identification-Localization

Project developed during my Master's Thesis in Biomedical Engineering at FEUP (FEUP_Dissertation_MiguelRocha_2024)

Some concepts detailed here were firstly tested with an online dataset comprising EEG data recorded in a similar paradigm, whose study is presented in PTL.pdf.

## **Goal:**

In this thesis, a BCI system was developed in the context of aerial visual search, accelerating target detection (in this case identification of humans) in a vast open field environment covered by drone images. This detection is carried out at a high frame rate (5 images per second) by analyzing the time domain of the Electroencephalogram of human observers. For this purpose, Event-Related Potentials (ERPs) associated with visual attention neural mechanisms, namely N2pc, N2pcb and P3, elicited by an object of interest within the images were used. Additionally, the use of N2pc and N2pcb was tested to estimate the location of the human target within the image in the horizontal (left vs. right) and vertical (top vs. bottom) dimensions, respectively.

To test this approach, two independent Rapid Serial Visual Presentation (RSVP) paradigms were designed and presented separately to 6 subjects after obtaining authorization from the institutional ethics committee for this human experimentation. These two paradigms were designed with very different characteristics, namely a different set of environments/terrain and human target characteristics, including its clothes and the distribution of their centroids within the images. The first paradigm (240 images with 24 targets) was used to train/validate the machine learning (ML) models and the second (160 images with 16 targets) was used exclusively to test them. In addition, the second paradigm was seen for the first time by the 6 subjects during the procedure, allowing the evaluation of the brain’s ability to discriminate targets in an unknown and unseen environment and human target characteristics. Customized ML models (specific to each subject) and generalized models (trained with the data of all subjects for the first paradigm and tested with the second) were tested.

## **System Architecture:**

The images simulating search and rescue scenarios were captured with a drone and then saved in a computer for image presentation. Despite being tested offline, this approach can be extrapolated to real-time scenarios where a drone will capture images of the environment and transfer them wirelessly to a computer iteratively, which is the ultimate application of BCIs. If the height of the drone is properly correlated with its velocity, 2 consecutive images captured will omit redundant space within the environment between those 2 images.

The BCI user visualizing the images will only need to be contextualized by the target type he is searching for in the stimuli. This is essential so that users can construct a visual representation within the working memory of the object required to be searched to properly allocate neural mechanisms related to the focus of attention for this object only. In this case, they were asked to visually search humans lying down. Then, specific ERPs related to visual attention are decoded to firstly detect the presence of the Target human and secondly, its location within the image along the horizontal and vertical dimensions and subsequently, the environment.

<img width="800" alt="SystArch" src="https://github.com/user-attachments/assets/e3fcb18e-c48f-455b-8895-fa7ce5be11ae">

## **EEG Acquisition parameters:** 

<img width="800" alt="EEG_dataset" src="https://github.com/user-attachments/assets/4032ff0a-e43b-4981-afc8-6f5c607fd36e">

## **Main Results:**

### ***Target (Sensitivity) vs Non-Target (Sensibility) classification:***

Model row legend:

SG - Subject Generalized

SS - Subject Specific

AC - All ERP channels model variation

BC - Best channels selected for each ERP

<img width="800" alt="T_vs_NT" src="https://github.com/user-attachments/assets/849e34cd-0663-4ad7-a9ab-55099cc1668c">

### ***Right Visual Field (RVF) vs Left Visual Field (LVF) Target classification:***

<img width="800" alt="n2pc" src="https://github.com/user-attachments/assets/8350db4e-2f95-4234-90a2-a9059226e7dc">

### ***Lateral Target centroid estimation (Neural Network) for one subject:***

<img width="800" alt="S1_x_estim" src="https://github.com/user-attachments/assets/3d45e906-08b9-4eeb-a15f-b13ca9718b30">

## **Conclusion:**

Because the results were identical and sometimes even better in the Testing images than in the Training images, these indicate that this type of high-frame-rate BCI system (hybrid, using human observers and ML techniques on the measured brain potentials) seems to generalize well when using N2pc and P3 ERPs. These results ensure the system can be extrapolated to novel environments and humans without losing performance, or in other words, in search and rescue images that neither the brain nor the ML models have seen.

## **Hardware development:**

A PCB was also designed to interface the EEG amplifier and the monitor where the images are presented, thus enabling the segmentation of each response in the continuous EEG. Additionally, the PCB encapsulation and a piece to fix the circuit to the monitor was also designed and 3D printed.

<img width="500" alt="PCBonMonitor" src="https://github.com/user-attachments/assets/69a51014-9f9b-4e80-9d57-2c6a6e2aa97a">



