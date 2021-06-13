#importing packages
import pandas as pd 
from pandas_profiling import ProfileReport
#Reading data from specified file
df=pd.read_csv(r"C:\Users\kshit\OneDrive\Documents\covidindia.csv")
#Forming dataframe and printing
data=pd.DataFrame(df)
print(df)
#Forming profile report and saving as html file
profile=ProfileReport(df)
profile.to_file(output_file='covidindia.html')