# Computer Vision for Playing Cards

abstract
  This project is a real time image classifier of playing cards. It currently recognizes 6 classes, them being 8, 9, 10, Jack, Queen, King.  We trained the Tensorflow's official models using a few hundred images of playing cards with an appropriate amount of noise. Specifically we trained on Tensorflow's faster-rcnn-inception-v2 model. 
  The real time 

contributors
Edward Zhong
Fluellen Arman Umali

motivation


methodology
    Data Collection
      We gathered our data by taking a few thousand images of cards on an Iphone 10. We then uploaded the images, compressed it to 720x1080. This generally meaning that each image is less than 200 kilobytes. 
      We labeled our images using labelimg. labelimg allows one to create boxes that contain a specific class. labelimg saves this data as xml files, which will be used as generate inputs for TensorFlows trainer. Before we train our classifier, 
    Modeling
      We used Tensorflow's official models and trained our images on it. The specific model used is Tensorflow's faster-rcnn-inception-v2. 
      We downloaded Tensorflow's Object Detection API and and trained our imagesusing the faster-rccn.
        A brief over view of Faster RCNN
          While CNN's are used for image classification, RCNN's are used for object detection. The RCNN focuses the CNN on a region of an image. The faster RCNN determines where to focus the CNN by using it's RPN to quickly scan every region of the image and determine which region needs further processing.
       
          
Summary and Resources

Key Results

Future Works
