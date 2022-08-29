Seven deep learning models are proposed for classifying land cover. Six models were trained on RGB bands. The other was trained on all bands of the EuroSAT dataset. 
### RGB Bands

            1. ShuffleNet
            2. ResNet50 
            3. ResNet152v2
            4. VGG16
            5. EfficientNet-B0
            6. EfficientNet-B1

The models have the following extensions and saving methods:

    1. ShuffleNet: .h5 extension, model.save()
    2. ResNet50: .hdf5 extension, model.save()
    3. ResNet152v2: .hdf5 extension, model.save()
    4. VGG16: .hdf5 extension, model.save() 
    5. EfficientNet-B0: .bin extension, torch(PyTorch)'s save procedure
    6. EfficientNet-B1: .h5 extension, model.save()

### All Bands

            1. Custom CNN

## Trained Weight Files

- [RGB Models](https://drive.google.com/drive/folders/1Pg_U7xfR5Ko2L9ZbTT0k4ysaer2Qoukf?usp=sharing)

- [All-Band Models](https://drive.google.com/drive/folders/1Pg_U7xfR5Ko2L9ZbTT0k4ysaer2Qoukf?usp=sharing)
