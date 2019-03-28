# How to format my project ?

## 1- Organizing your project

Your project should be organized as the example in project-example.

Your original image should be in an "images" folders, and your annotation in an "annotation" folder.

Images should be in .png format, format in uint8, not bigger than 800x800.
Annotations should be in .png format, format in uint8, same name than the corresponding images, same size. Each pixel is assigned to only one class. Each class correspond to one int. For example if the vegetation class is the integer 1, each vegetation pixels in the annotation mask should be equal to 1. As the image is signed in uint8, it will appear black on your screen but everything will be ok ;)

We recommand to generate a weak segmentation before so you save time in the process of annotations.

If you prefer to have the pre-annotation of several models, you can add folder named "XXX" (for example a "excess-green" folder and a "u-net" folder), with each prediction converted to an annotation (integer only), and declare each models in the example.json.

## 2- Generate your example.json

A script is provided to help your generate your example.json

## 3- Generate your own project

A script will be provided to help you validate the formatting of your data.
Whean ready ping Etienne or Jeremy on Slack to put your data on the server. We are the only one allowed to access the server so we protect your data.