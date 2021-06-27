# Pandas Profiling
## Contributors
**Kshitij Kumar<br/>**
**Khelawan Singh<br/>**
**Lokesh Khande<br/>**

![](https://camo.githubusercontent.com/8a45c0936d6113b12b7b32942f448270eda8f714665ba8629f36c291f0ccd5fd/68747470733a2f2f70616e6461732d70726f66696c696e672e6769746875622e696f2f70616e6461732d70726f66696c696e672f646f63732f6173736574732f6c6f676f5f6865616465722e706e67)


### Introduction
Pandas profiling is an open source Python module with which we can quickly do an exploratory data analysis(EDA) with just a few lines of code. Besides, if this is not enough to convince us to use this tool, it also generates interactive reports in web format that can be presented to any person.In short, what pandas profiling does is save us all the work of visualizing and understanding the distribution of each variable. It generates a report with all the information easily available.Pandas allows importing data from various file formats such as CSV, JSON, Microsoft Excel.<br/>

**Exploratory Data Analysis**-In statistics, exploratory data analysis is an approach of analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods. A statistical model can be used or not, but primarily EDA is for seeing what the data can tell us beyond the formal modeling or hypothesis testing task.<br/>
One of the nice points of the generated report is the warnings that appear at the beginning. It tells us the variables that contain NaN values, variables with many zeros, categorical variables etc.Pandas Profilling is a very nice package which can help to those who are new to Data Science and can start their carrier by exploring these generated report and learn many new terms about statistics.
## Installation of pandas and pandas-profiling package
### Using pip
#### Install using pip package manager by running-
`pip install pandas`<br/>
`pip install pandas-profiling`
### Using conda
#### Install using the conda package manager by running-
`conda install -c conda-forge pandas`<br/>
`conda install -c conda-forge pandas-profiling`
## Getting Started
We can generate report through two interfaces-through widgets and through a HTML report.But here we will generate report through HTML file.
#### Start by importing packages such as-pandas and pandas profiling-
`import pandas as pd`<br/>
`from pandas_profiling import ProfileReport`<br/>
#### For reading data from specified file follow the given command(give extension accordingly depending on the file type)-
`df=pd.read_csv(r"covidindia.csv")`
#### Forming profile report and saving as html file with output file name 'CovidIndia.html'
`profile=df.profile_report(title="Covid India Analysis Report",plot={"dpi": 800, "image_format": "png"})`<br/>
`profile.to_file(output_file='CovidIndia.html')`<br/>

Now we can see that the it generates profile reports with the file name covidindia in the form of HTML file.Through `profile.to_widgets` the HTML report can be included in a Jupyter notebook.We can also obtain a json file through _.json_ extension.We can also specify the resolution and format of the image.<br/>

For large datasets we use minimal mode-This is a default configuration that disables expensive computations (such as correlations and duplicate row detection).<br/>
Syntax-<br/>

`profile = ProfileReport(df, minimal=True)`<br/>
`profile.to_file("CovidIndia.html")`<br/>

For large datsets we can also take samples of the data.<br/>
Syntax-<br/>

`sample=covidindia.sample(1000)`<br/>
`profile=df.profile_report(minimal=True)`

We can also select a sample of data to generate a profile report.For example-to select the first n rows of data if actual data is too large.
## Analysis of Profile Report-Here we are going to learn almost everything about profile report.

**Reproduction**:Analysis started,Analysis finished,Duration,Version,Command line,Download configuration<br/>
**Warnings**<br/>
**Type inference**: detect the types of columns in a dataframe such as Boolean, Numerical, Date, Categorical, URL, Path, File and Image.<br/>
**Dataset statistics**: Number of variable,Number of observation,Missing cells,Missing cells(%),Duplicate rows,Duplicate rows(%),Total size in memory 
Average record size in memory<br/>
**Essentials**: type,unique values,missing values,infinite<br/>
**Quantile statistics**: minimum value,5th percentile,Q1,median,Q3,95th percentile,maximum,range,interquartile range<br/>
**Descriptive statistics**: mean,median,standard deviation,variance,sum,median absolute deviation,coefficient of variation,kurtosis,skewness<br/>
**Most frequent values**<br/>
**Histogram**<br/>
**Extreme Values**:minimum and maximum five values<br/>
**Correlations**: Spearman,Pearson,Kendall,Phik<br/>
**Missing values matrix,distinct count,heatmap,dendrogram**<br/>

![](https://camo.githubusercontent.com/3392724b4472de56f2d73463174aea97aa51af30fba50ec0e87273d39a496b3d/68747470733a2f2f70616e6461732d70726f66696c696e672e6769746875622e696f2f70616e6461732d70726f66696c696e672f646f63732f6d61737465722f6173736574732f696672616d652e676966)

Meanings of some of the important terms in profile report:

* **Range**-It is the difference between highest and lowest value.
* **Mean**-It is the average of the dataset.
* **Median**-It is the middle of the set of numbers.
* **Mode**-Frequently or mostly occuring numbers in the dataset.
* **Median Absolute Deviation(MAD)**-It is a robust(they are not affected by very high or low value) measure of how spread out a set of data is.It is absolute value of the difference between the value and the median.
* **Standard Deviation**-It is a measure of dispersion of observations within a data set about mean.
* **Variance**-It is the numerical value, which describes how variable the observations are about mean.
* **95th percentile**-It is a number that is greater than 95% of the numbers in a given set or It is the highest value left when the top 5% of a numerically sorted set of collected data is discarded.Percentiles can be calculated using the formula n = (P/100) x N, where P = percentile, N = number of values in a data set.
* **Coefficient of variation(CV)**-It shows the extent of variability in relation to the mean of the population.It is the ratio of standard deviation to the mean.The higher the coefficient of variation, the greater the level of dispersion around the mean.
* **Interquartile range(IQR)**-It describes the middle 50% of values when ordered from lowest to highest.To find the interquartile range (IQR), ​first find the median (middle value) of the lower and upper half of the data. These values are quartile 1 (Q1=25th percentile) and quartile 3 (Q3=75th percentile).Q2(=50th percentile) is the median of the dataset.
* **Skewness**-It is the tendency of a distribution that determines its symmetry about the mean.Types-Positive skewed and Negative skewness.
* **Kurtosis**- It means the measure of the sharpness of the peak of probablity distribution curve.
* **Dendrogram**-It is a branching diagram that represents the relationships of similarity among a group of entities.
* **Heatmap**-It is a graphical representation of data that uses a system of color-coding to represent different values.
* **Correlation**-It is a statistical measure that expresses the extent to which two variables are linearly related.The value of the correlation coefficient varies between +1 and -1.As the correlation coefficient value goes towards 0, the relationship between the two variables will be weaker. The direction of the relationship is indicated by the sign of the coefficient; a + sign indicates a positive relationship and a - sign indicates a negative relationship.
* **Pearson's r Correlation**-The Pearson's correlation coefficient(r) is a measure of linear correlation between two variables.It's value lies between -1 and +1, -1 indicating total negative linear correlation, 0 indicating no linear correlation and 1 indicating total positive linear correlation.
* **Spearman's ρ Correlation**-The Spearman's rank correlation coefficient (ρ) is a measure of monotonic correlation between two variables, and is therefore better in catching nonlinear monotonic correlations than Pearson's r.
* **Kendall's τ Correlation**- The Kendall rank correlation coefficient (τ) measures ordinal association between two variables.
* **Phik(φk) Correlation**-Phik (φk) is a new and practical correlation coefficient that works consistently between categorical, ordinal and interval variables, captures non-linear dependency and reverts to the Pearson correlation coefficient in case of a bivariate normal input distribution.

So,here we are going to analyse about the various information about covid-19 in India and can get a wonderful results through pandas-profiling package. 
## Conclusion
Hence pandas-profiling is a good package but it cannot be used to solve all the problems as the information inside it is too much and sometimes we does not need that much information.Generally with the increase in the size of the data the time to generate the report also increases a lot and for that we should have a powerful computer for getting our work to be done faster.Sometimes we can also take sample of the data to analyse it and through generated report we can understand it and can take major decision about what will happen in future.

## Dependencies
The profile report is written in HTML and CSS, which means pandas-profiling requires a modern browser.
We need Python 3 to run this package.

**_For more reference visit:https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/pages/introduction.html_**
