# FullStackDataScienceApplication
Take a Dataset-EDA-process data - Build a Deep Neural Network (ANN) (CNN) - Train the Model - Build Full Stack Web App : Back end to deploy The Model - Sever - Frontend for Using The Model-
THERE ARE TWO APPLICATION USES GOING FROM DATA SET TO TRAINED MODEL AND FULLSTACK DEPLOYMENT 

PHASE 1) DATA SCIENCE -DEEP LEARNING: THIS
APPLICATION #1) DIGIT RECOGNITION
Context:
One of the most interesting tasks in deep learning is to recognize objects in natural scenes. The ability to process visual information using machine learning algorithms can be very useful as demonstrated in various applications.

The SVHN dataset contains over 600,000 labeled digits cropped from street-level photos. It is one of the most popular image recognition datasets. It has been used in neural networks created by Google to improve the map quality by automatically transcribing the address numbers from a patch of pixels. The transcribed number with a known street address helps pinpoint the location of the building it represents.


Objective:
Our objective is to predict the number depicted inside the image by using Artificial or Fully Connected Feed Forward Neural Networks and Convolutional Neural Networks. We will go through various models of each and finally select the one that is giving us the best performance. 

APPLICATION  #2) FACIAL EXPRESSION AND EMOTION RECOGNITION
Dataset:
Our dataset is present in .h5 format. We will use a subset of our dataset to save ourselves a lot of computation time.

Please do not change the variable names to avoid hassles while executing the code.
You can raise your issues on the project discussion forum on Olympus
Capstone Project: Facial Emotion Recognition Context Deep Learning has found applications in many predictive tasks relating to more unstructured forms of data over the last few years, such as images, text, audio, and video. Many of these tasks seem to be in the vein of a larger direction of predictive modeling that aims to match human-level performance on such tasks, because humans have evolved to specialize in performing intelligent actions on such unstructured data. As a specific branch of AI (also called Affective Computing or Emotion AI) Artificial Emotional Intelligence stands for the study and development of technologies and computers that can read human emotions by means of analyzing body gestures, facial expressions, voice tone, etc., and react appropriately to them. In the field of human-machine interaction, facial expression recognition is critical. From recent research, it has been found that as much as 55% of communication of sentiment takes place through facial expressions and other visual cues. Therefore, training a model to identify facial emotions accurately is an important step towards the development of emotionally intelligent behavior in machines with AI capabilities. Automatic facial expression recognition systems could have many applications, including but not limited to any use case that requires human behavior understanding, detection of mental disorders, and creating a higher quality of virtual assistant for customer-facing businesses.


Objective: The goal of this project is to use Deep Learning and Artificial Intelligence techniques to create a computer vision model that can accurately detect facial emotions. The model should be able to perform multi-class classification on images of facial expressions, to classify the expressions according to the associated emotion

The data set consists of 3 folders, i.e., 'test', 'train', and 'validation'. Each of these folders has four subfolders:

‘happy’: Images of people who have happy facial expressions.
‘sad’: Images of people with sad or upset facial expressions.
‘surprise’: Images of people who have shocked or surprised facial expressions.
‘neutral’: Images of people showing no prominent emotion in their facial expression at all.

ONCE BOTH APPLICATION TASKS HAVE BEEN COMPLETED- THE DEEP LEARNING PHASE IS COMPLETE - NERUAL NETWORK MODEL AND WEIGHTS WILL BE EXPORTED AND BUILT INTO A FULL STACK WEB APPLICATION

PHASE #2) FULL STACK DEPLOYMENT OF APPLICATION 1 (Digit Recogmition) and APPLICATION 2 (Expression Classification)
  FULL STACK WEB APPLICATION - MERN STACK - REACT - NODEJS - JS - HTML - CSS - REDUX 

  FRONT END: VITE-APPLICATION: npx create vite@latest - 
  BACK END : MONGODB DATABASE: - 
  SERVER: HEROKU OR VERCEL OR DIGITAL OCEAN (to be determined)

  FRONT END: User interface for activating either functional use case (APPLICATION 1 OR APPLICATION 2 OR BOTH AT THE SAME TIME)
        -SAVES DETECTION RESULTS TO THE DATA BASE, 
        -USER CAN CREATE PROFILE TO USE / SAVE / AND SEE PAST DETECTIONS ALONG WITH TIME AND LOCATION WHEN MADE. 
        
