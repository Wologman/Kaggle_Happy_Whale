# Kaggle Happy Whale

[Happywhale - Whale and Dolphin Identification](https://www.kaggle.com/competitions/happy-whale-and-dolphin)

Individual identification from whale and dolphin images

The code here is mostly what I used to generate cropped images from the original dataset.  I hand annotated 2000 whale images using CVAT, with classes Left, Right and Unknown.  I had planned to use those classes to flip the images horizontally, or train left and right sided whales seperately.  In the end I didn't get that far, and reduced the annotations to a single class.

The annotated images were used to make a YOLOv5 model, and then crop the remaining 70,000 images in the training and test set.

The best approaches to this competition were to use ArcFACE, with a variety of cropping and augmentation strategies, then ensemble the models.  

I have included the code I used on the Kaggle platform to generate the TFRecords datasets, for efficient training on TPUs.
