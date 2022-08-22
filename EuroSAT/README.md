## The EuroSAT Dataset

[Link to dataset](https://github.com/phelber/EuroSAT)

- The dataset consists of 64x64 images captured by Sentinel-2A satellite and it has over 27000 images spread across 10 classes.

- The original data consists of hyperspectral images with 13 spectral bands.

- Images are geo-referenced.


### Exploratory Data Analysis

- Urban areas (Residential, Industrial and Highways) have roads and buildings.

- AnnualCrops and PermanentCrops are made up of convex agricultural fields.

- HerbaceaousVegetation, Pasture, and Forests feature natural land cover.

- Sea bodies(SeaLake, Rivers) and forest cover(HerbaceaousVegetation, Forests) appear to be quite similar. The models need to be trained accordingly to distinguish the two.

### Note: No Near Infra-Red(NIR) Band

- NIR can be used to create an index to visualize the presence or absence of radiation in a picture. Unfortunately, the dataset does not have NIR bands.
