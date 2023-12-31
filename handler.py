import os
import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance


model = pickle.load( open('models/model_LGBM.pkl','rb'))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def health_insurance_predict():
    test_json = request.get_json()
    
    if test_json:
        # unique example
        if isinstance( test_json, dict ): 
            test_raw = pd.DataFrame( test_json, index=[0] )
        # multiple example   
        else: 
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            # Instantiate Rossmann class
        pipeline = HealthInsurance()
        
        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # data preparation
        df3 = pipeline.data_preparation( df2 )
        
        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
    
    else:
        return Response( '{}', status=200, mimetype='application/json' )
    
if __name__ == '__main__':   
    port = os.environ.get('PORT', 5000)
    app.run( host='0.0.0.0', debug=True, port=port )
    
