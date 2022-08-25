Four deep learning models are proposed for classifying land cover. Three models were trained on RGB bands. The other was trained on all bands of the EuroSAT dataset. 
### RGB Bands

            1. ResNet50 
            2. ResNet152v2
            3. VGG16
            4. EfficientNet-B0

The models have the following extensions and saving methods:
    1. ResNet50: .hdf5 extension, ResNet50()'s save procedure
    2. ResNet152v2: .hdf5 extension, ResNet152v2()'s save procedure
    3. VGG16: .hdf5 extension, VGG16()'s save procedure 
    4. EfficientNet-B0: .bin extension, torch(PyTorch)'s save procedure

### All Bands

            1. Custom CNN

## Trained Weight Files

- [RGB Models](https://drive.google.com/drive/folders/1Pg_U7xfR5Ko2L9ZbTT0k4ysaer2Qoukf?usp=sharing)

- [All-Band Models](https://drive.google.com/drive/folders/1Pg_U7xfR5Ko2L9ZbTT0k4ysaer2Qoukf?usp=sharing)
