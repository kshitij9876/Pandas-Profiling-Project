#importing packages
import pandas as pd 
from pandas_profiling import ProfileReport

#Reading data from specified file
df=pd.read_csv(r"C:\Users\kshit\OneDrive\Documents\covidindia.csv")
print(df)

#Forming profile report
profile=df.profile_report(title="Covid India Dataset",plot={"dpi": 800, "image_format": "png"})

#Giving profile report an interactive outlook
profile.set_variable("html.style",{"theme":'flatly'})
profile.set_variable("html.style",{"full_width":True})

#Saving as HTML file
profile.to_file(output_file='CovidIndia.html')