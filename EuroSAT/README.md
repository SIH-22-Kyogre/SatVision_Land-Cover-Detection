## The EuroSAT Dataset

[Link to dataset](https://github.com/phelber/EuroSAT)

- The dataset consists of 64x64 images captured by Sentinel-2A satellite and it has over 27000 images spread across 10 classes.

- The original data consists of hyperspectral images with 13 spectral bands.

- Images are geo-referenced.


### Exploratory Data Analysis

- Urban areas (Residential, Industrial and Highways) all have roads and buildings.

- AnnualCrops and PermanentCrops are made up of convex agricultural fields.

- HerbaceaousVegetation, Pasture, and Forests feature natural land cover.

- It may be difficult to distinguish sea bodies (SeaLake, Rivers) from the HerbaceaousVegetation and Forests classes.

### Disadvantage of not having additional bands

- NIR can be used to create an index, visualising the radiation that is present (or not present) in a picture.
This dataset does not contain the NIR wavelength bands, so this option will not be explored.
