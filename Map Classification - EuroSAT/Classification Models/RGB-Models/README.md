Three Deep Learning Models were used for classifying land cover using RGB images:
1. ShuffleNet
2. ResNet50
3. ResNet152v2
4. VGG16
5. EfficientNet-B0

## ShuffleNet

- Has an accuracy of 86.7% on unseen data.
- ~80% accuracy on residential and industrial areas 
- Cannot differentiate residential and non-residential areas well.
- Cannot differentiate between forest areas and water bodies.


## ResNet50

- Has an accuracy of 94.7% on unseen data.
- ~95% accuracy on residential and industrial areas 
- Can differentiate residential and non-residential areas well.
- Cannot differentiate forest area and water bodies as precisely as other pairs of classes.

## ResNet152v2

- Has an accuracy of 96% on unseen data.
- ~97% accuracy on industrial areas.    
- ~92% accuracy on residential areas.    
- Can differentiate residential and non-residential areas well.
- Better than ResNet50 at differentiating forest areas and water bodies well.

## VGG16

- Has an accuracy of 97% on unseen data.
- ~95% accuracy on industrial and residential areas.
- Can differentiate residential and non-residential areas well.
- Differentiates forest areas and water bodies better than ResNet50 but not as well as ResNet152v2.

## EfficientNet-B0

- Has an accuracy of 98% on unseen data.
- ~98% accuracy on industrial and residential areas.
- Can differentiate residential and non-residential areas well.
- Differentiates forest areas and water bodies better than ResNet50 but not as well as ResNet152v2.
- Has a very small size of only 16MB.

## EfficientNet-B1

- Has an accuracy of 99% on unseen data.
- ~99% accuracy on industrial and residential areas.
- Can differentiate residential and non-residential areas well.
- Differentiates forest areas and water bodies better than ResNet50 but not as well as ResNet152v2.
- Has a reasonable size of 80MB.
