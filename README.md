# Computer Vision for Playing Cards

abstract
---
  This project is a real time image classifier of playing cards. It currently recognizes 6 classes, them being 8, 9, 10, Jack, Queen, King.  We trained the Tensorflow's official models using a few hundred images of playing cards with an appropriate amount of noise. Specifically we trained on Tensorflow's faster-rcnn-inception-v2 model. 
  The real time 

contributors
---
- Edward Zhong
- Fluellen Arman Umali

motivation
---
A strong interest in computer vision lead us to the idea for this project. Growing up as a young lad in the California Bay Area, I always saw self-driving cars being tested, and I wondered how they would work. Learning computer vision through a card project would provide insight into how it does function, and although driving is undoubtedly more complicated than playing a card game, perhaps learning how cards are detected and differentiated can allow us to begin to see how a car detects people and lines on the road. Additionally, building a program that can play a card game given only a video feed would be a very interesting project in itself, and would provide a fine result.

methodology
---
    Data Collection
      We gathered our data by taking a few thousand images of cards on an Iphone 10. We then uploaded the images, compressed it to 720x1080. This generally meaning that each image is less than 200 kilobytes. 
      We labeled our images using labelimg. labelimg allows one to create boxes that contain a specific class. labelimg saves this data as xml files, which will be used as generate inputs for TensorFlows trainer. 
      We splitted our image data into training and testing directory, with a rough ratio of 80%-20%.
    Modeling
    
      We used Tensorflow's official models and trained our images on it. The specific model used is Tensorflow's faster-rcnn-inception-v2. We edit the configs of the faster-rcnn to allow for the detection of our specified classes. That being the playing cards value and suits.  
        A brief over view of Faster RCNN
          While CNN's are used for image classification, RCNN's are used for object detection. The RCNN focuses the CNN on a region of an image. The faster RCNN determines where to focus the CNN by using it's RPN to quickly scan every region of the image and determine which region needs further processing.
          
      After data collection and configuring the faster-rcnn, we trained our data on the faster-rcnn. By keeping our image data below/around 200 kb and using a low resolution, we were able to optimize the speed of training to a degree.  
       
          
Summary and Resources
---

Ongoning Progress
---
Currently we have a working prototype, however, there are a number of limitations that will be listed as follows:
- it takes 16 hours to train and it runs very slowly (<1 fps)
- it can only detect 6 classes: 9, 10, J, Q, K, A, without the suits
- it is not completely accurate, the most common issue being confusing different face cards with Jack
- it does not handle overlapped cards very well, often getting them wrong

<img src="img/proto.png" alt="example of prototype working" title="example of prototype working">
