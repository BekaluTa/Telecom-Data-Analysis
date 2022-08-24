#Creating Function to Preprocess the given Data
def missing_values_table(df):
        # Summing of all the missing value using SUM function
        mis_val = df.isnull().sum()
        
        # calculate the Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Creating a table with the results of total missing value and percentage missing values
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Renameing the names of the  columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing in  descending order
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # Displaying  summary informations
        print ("Selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns