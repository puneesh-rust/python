# pandas
    Pandas is a powerful open-source data analysis and manipulation 
     library for Python. It provides data structures like Series and 
      DataFrame that are designed to handle structured data efficiently. 
       Pandas is widely used for data cleaning, transformation, and 
        analysis.

# method of import 
         import pandas as pd 


# NOTE 

     urllib.request is a Python module that helps you interact with web 
       resources (like URLs and APIs). It is part of the standard urllib 
         package, which provides a way to work with URLs. Specifically, 
          urllib.request is used to open and read URLs, handle HTTP 
               requests, and even download files from the internet.


    urlretrieve is a function from the urllib.request module in Python, 
     which allows you to download a file from a URL and save it to a 
       local file.   

      from urllib.request import retrieve   

    urllib.request.urlretrieve(url, filename=None, reporthook=None, 
     data=None)        

# reading file 

          pd.read_csv(file name )     

# writing in file 
              df.to_csv(file , value)

# df.info() method 
             its describe the file info.             

# search value
      .at[column name][column_value]             

# Note 
       we can create a subset data set from the file data which is stored in 
       new data_frame 

       new_df = old_df[['col1' , 'col2']]      

# access Row 
         .loc method is used for accessing row .

# .sum()                
        it is used for adding all data of the same column 

# querying And SOrting 
      we can operate the sorting operation by pandas 
       
      data_df = old_df.column or row operator  condition   

    ex . 
        var_df = data_df[data_df.col > condition]  


# Display setting for reading the whole data 

         from IPython .display import display 
         with pd.option_context('display.max_rows' , 100):
         # write whataever you print and read data


# .drop method 
              is used for removing the col data. 

# .sort_value method 
                  is used for sort the col data in ascending and descending    
                    order  
               ex  
                  data_df.sort_values('col' , ascending =           
                  True/False).head/tail(length)     

# before/After data
         data_df.loc[starting , ending]            

# working with date 

          data column is present in object type , pandas is not recoginzed this 
          so first we can convert into the 
            datetime by helping of______
             data_df['date_col'] = pd.to_datetime[data_df.date]
# merging data from multiple source              
              merged_df = first_dataset.merge(second_dataset , on = 'where store 
                /col')

                
