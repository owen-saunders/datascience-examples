# Datascience Examples
This repository contains a series of informative notebooks drawing conclusions from a variety of small data sets.

Each subdirectory in this repository contains both the dataset and a Jupyter notebook which consists of a full breakdown of the sequential process.

### Current Examples:

#### Pokemon
The dataset contains information on a range of pokemon types, and contains specific data such as the name, attributes and element of each pokemon.

The notebook focuses on exploring the attributes of the pokemon due to them being numerical and easily compared. Instead of dimensionality reduction, a radar plot is used for a unique approach to see the varying attributes of different clusters of pokemon. The algorithm used for cluster creation is K-Means (scikit implementation).

#### WikiScraping
The data is retrieved from two wiki pages and focuses on the method of converting these pages into a single set of features and subsequent predictions of new samples of text using the model created from clustering these features into two groups, which are hoped to represent the two separate wiki pages.

### Current Method Examples:

#### KMeans
A python file showing KMeans on a generated dataset. No visualisations. Not converted to notebook.

#### MeanShift
A notebook showing MeanShift in its simplest form. Visualisations are included.
