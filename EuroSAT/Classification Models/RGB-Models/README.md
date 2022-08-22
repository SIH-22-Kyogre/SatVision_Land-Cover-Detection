Three Deep Learning Models were used for classifying the land cover using RGB images:
1. ResNet50
2. ResNet152v2
3. VGG16

## ResNet50

- Has an accuracy of 94.7% on unseen data.
- ~95% accuracy on residential and industrial areas 
- Can differentiate residential and non-residential areas well.
- Cannot differentiate forest area and water bodies as precisely as other classes.

## ResNet152v2

- Has an accuracy of 96% on unseen data.
- ~97% accuracy on industrial areas.    
- ~92% accuracy on residential areas.    
- Can differentiate residential and non-residential areas well.
- Better than ResNet50 at differentiating forest areas and water bodies.

## VGG16

- Has an accuracy of 97% on unseen data.
- ~95% accuracy on industrial and residential areas.
- Can differentiate residential and non-residential areas well.
- Differentiates forest areas and water bodies better than ResNet50 but not as well as ResNet152v2.
