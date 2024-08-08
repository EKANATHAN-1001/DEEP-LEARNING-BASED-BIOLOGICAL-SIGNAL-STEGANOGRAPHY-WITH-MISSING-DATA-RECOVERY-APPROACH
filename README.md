# DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH

## Development Team
**Batch Members**
- **Ekanathan SA**
- **Rajasekar M**
- **SaiVijay S**

## Project Overview

### Aim
To develop a robust system for encryption and decryption of bio-signal with a focus on lost-data recovery using Deep Learning techniques.

### Problem
Bio-signals may get lost or tampered with during transmission, posing significant risks to data integrity and patient safety.

### Solution
Reconstruction of lost bio-signals with the help of a deep learning approach.

### Objectives
- To implement a bio-signal encryption process using secret bit insertion.
- To design a decryption mechanism for secret bit extraction for bio-signal recovery.
- To apply the Hippopotamus Optimization Algorithm (HOA) to optimize the position and feature extraction of missed data blocks.
- To integrate Long Short-Term Memory (LSTM) and Multilayer Perceptron Neural Network (MLPNN) to reconstruct missing data blocks during transmission errors.

### Novelty
- Generation of new Hermite functions.
- Utilization of hash functions for robust password generation and security enhancement.
- Implementation of the Hippopotamus Optimization Algorithm for block position optimization.
- Integration of arrhythmia detection algorithms for early diagnosis in healthcare systems.

## Screenshots and Descriptions

### Issue In Cloud
One of the main challenges faced during the implementation was the issue in cloud data transmission where bio-signals often get corrupted or lost, leading to significant data integrity issues.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/251f7706-3e29-4fe4-baf5-9d99c2e5bdf5)

### Block Diagram
The following block diagram illustrates the overall architecture of our system, from signal encryption to decryption and missing data recovery.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/5b82e173-830b-48ac-a359-b3d2abf4d218)

### Su-LSTM Network
We implemented a Su-LSTM network to enhance the robustness of our data recovery approach. This network is specially designed to handle sequential data with missing entries.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/c17985af-6447-4fa1-9773-5d7b49fec367)

### Encryption Phase
The encryption phase involves inserting secret bits into the bio-signal to ensure secure transmission. The following image shows the encryption process.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/32448ca0-4185-439d-a629-6fee955d70c9)

### Decryption - No Tampering
In scenarios where there is no tampering, the decryption process accurately retrieves the original bio-signal. Below is a depiction of this process.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/1bd9d503-9c90-4fed-abba-ffcd1b90da26)

### Decryption - Tampering
In cases of tampering, our system can still recover the signal to a significant extent, as shown in the following example.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/6d9c2178-7463-4be1-b2e4-fd1c516fba4e)

### Data Prediction - PSO
The Particle Swarm Optimization (PSO) algorithm was used to predict and reconstruct missing data points. The following image demonstrates its effectiveness.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/ccbe2384-1f79-4ecc-8b5c-b794ff452927)

### Data Prediction - HOA
The Hippopotamus Optimization Algorithm (HOA) further enhances the accuracy of data reconstruction. Below is a sample of its application.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/e69aa479-73e8-4a24-b3cd-f789f4fb9991)

### Experimental Result - ECG
Our system was tested on ECG signals to verify its efficacy. The results are depicted below.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/2cc59c04-e673-4df0-b7c2-aa04cf96768a)

### Experimental Result - EEG
Similar tests were conducted on EEG signals to ensure the robustness of our approach.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/b1054ed1-7d86-4ddc-bf48-59c0d6fa5134)

### Experimental Result - PPG
PPG signals were also included in our experiments, with the results shown below.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/b2e96a76-0d86-4cb1-a0d5-4c98999ac016)

### Arrhythmia Training Model
The arrhythmia training model is a critical component of our system, used to train our network for arrhythmia detection.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/58d49ea5-bbdc-486e-97f4-89cbdb61b7e3)

### Arrhythmia Detection
Our system is capable of detecting arrhythmias in bio-signals, providing early diagnosis for healthcare applications.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/9c069ed8-fba9-4882-b6bd-b7f6d8f648ee)

### Arrhythmia Detection - Normal
The following image shows the detection of a normal heartbeat, indicating no arrhythmia.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/74e2575e-97ce-4402-94d7-1490cbb79f3e)

### Arrhythmia Detection - Arrhythmia
This image shows the detection of an arrhythmia, highlighting the effectiveness of our detection model.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/af7097f5-d9f5-49b9-aaf9-aa56bb364d30)

### Imperceptibility - No Tampering
Our system ensures that encrypted bio-signals remain imperceptible when there is no tampering.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/be1aa9e1-5033-4e10-8017-28fe34535544)

### Imperceptibility - Tampering
Even when tampering occurs, our system maintains a high level of imperceptibility to protect data integrity.

![image](https://github.com/EKANATHAN-1001/DEEP-LEARNING-BASED-BIOLOGICAL-SIGNAL-STEGANOGRAPHY-WITH-MISSING-DATA-RECOVERY-APPROACH/assets/116795679/387ef808-8263-4571-819e-1321006e0f63)

### Customization
The project can be customized to fit specific requirements. Additional features and functionalities can be added as needed. Ensure that the necessary libraries and dependencies are included in the project's build path.

### Documentation
Further documentation is available in the docs/ directory, including detailed descriptions of the algorithms and methodologies used.

### Contribution
We welcome contributions! Please fork the repository and submit a pull request.

### Contact
For any inquiries or issues, please contact the development team:

Ekanathan SA: ekanathanragu6245@gmail.com  
Rajasekar M: Rajasekar.rj100@gmail.com  
SaiVijay S: saivijays2599@gmail.com
