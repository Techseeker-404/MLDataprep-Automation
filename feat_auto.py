class Featselect:
    def __init__(self,df,features,handle_na=False):
        self.df = df
        self.handle_na = handle_na
        self.features = features

        #filling null values

        if self.handle_na:
            for c in self.df.columns:
                if self.df[c].isnull:
                    if self.df[c].dtype == object:                        
                            self.df[c] = self.df[c].fillna(df[c].mode()[0])                    
                    else:
                        self.df[c] = self.df[c].fillna(df[c].mean())

    #converting features into numerical and object wise
    # and doing onehotcoding or creating dummmy variables out
    #of categorical features

    def featureselect(self):
        feature = self.df.select_dtypes(include=['object']).copy()
        feature = pd.get_dummies(feature,drop_first=True)             
        num_feat = self.df.select_dtypes(include=['int','float']).copy() 
        concat_data = pd.concat([feature,num_feat] ,axis=1)  #concatinating the data                                                                     #and doing one hot encoding simultaneously
        return concat_data
    
if __name__ == "__main__":
    import pandas as pd
    #pd.set_option('display.max_columns',None)
    #reading data
    df = pd.read_csv('trial.csv')  
    col = [c for c in df.columns]
    features = Featselect(df,features=col,handle_na=True)
    data = features.featureselect()
    print(data)