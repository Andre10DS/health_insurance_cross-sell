import pickle
import numpy as np
import pandas as pd
import inflection

class HealthInsurance:
    def __init__(self):
        self.home_path = ''
        self.annual_premium_scaler            =   pickle.load(open(self.home_path + 'features/annual_premium_scaler.pkl', 'rb'))
        self.age_scaler                       =   pickle.load(open(self.home_path + 'features/age_scaler.pkl','rb'))
        self.vintage_scaler                   =   pickle.load(open(self.home_path + 'features/vintage_scaler.pkl','rb'))
        self.target_encode_gender_scaler      =   pickle.load(open(self.home_path + 'features/target_encode_gender_scaler.pkl','rb'))
        self.target_encode_region_code_scaler =   pickle.load(open(self.home_path + 'features/target_encode_region_code_scaler.pkl','rb'))
        self.fe_policy_sales_channel_scaler   =   pickle.load(open(self.home_path + 'features/fe_policy_sales_channel_scaler.pkl','rb'))
        
    
    def data_cleaning(self, df1):
        cols_old = ['id', 'Gender', 'Age', 'Driving_License', 'Region_Code',
       'Previously_Insured', 'Vehicle_Age', 'Vehicle_Damage', 'Annual_Premium',
       'Policy_Sales_Channel', 'Vintage', 'Response']

        snakecase = lambda x: inflection.underscore(x)
        cols_new = list( map(snakecase, cols_old) )

        df1.columns = cols_new
        
        return df1
    
    def feature_engineering(self, df2):
        
        # vehicle age
        df2['vehicle_age'] = df2['vehicle_age'].apply( lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_year'
                                             if x == '1-2 Year' else 'below_1_year')

        # vehicle damage
        df2['vehicle_damage'] = df2['vehicle_damage'].apply( lambda x: 1 if x =='Yes' else 0)
        
        return df2
    
    def data_preparation(self, df5):
        
        # anual premium - StandarScaler
        df5['annual_premium'] = self.annual_premium_scaler.transform( df5[['annual_premium']].values)
        
        # Age - MinMaxScaler        
        df5['age'] = self.age_scaler.transform( df5[['age']].values)

        # Vintage - MinMaxScaler
        df5['vintage'] =self.vintage_scaler.transform( df5[['vintage']].values)
        
        # Vintage - MinMaxScaler
        df5.loc[:, 'gender'] = df5['gender'].map(self.target_encode_gender_scaler)
                
        ## region_code-> Target Encoding
        df5.loc[:, 'region_code'] = df5['region_code'].map( self.target_encode_region_code_scaler )
       
    
        ## vehicle_age -> One Hot Encoding
        df5 = pd.get_dummies( df5, prefix='vehicle_age', columns=['vehicle_age'])
        
        
        ## policy_sales_channel -> Frequency Encoding
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map( self.fe_policy_sales_channel_scaler  )
        
        
        cols_selected = ['vintage' , 'annual_premium', 'age', 'region_code' ,'vehicle_damage' , 'policy_sales_channel','previously_insured']

        return df5[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        # model prediction
        pred = model.predict_proba( test_data )
        
        
        # join predict into original data
        original_data['score'] = pred[:,1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso')
        