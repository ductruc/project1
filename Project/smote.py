import pandas as pd
from collections import Counter
# Revert to older version (1.2.2) of scikit-learn for program to work:
import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn==1.2.2'])
from imblearn.over_sampling import SMOTENC

data = pd.read_csv("/Users/thomaspagulatos/Documents/R_stuff/train.csv")

#Obatin column index for categorical features
cat_col_index = [1]
X_data = data.drop(columns=['Category'])
y_data = data[['Category']].copy()

# We want to balance the data, while trying to avoid introducing bias to the positive class
donor_num = int(y_data.shape[0])
divider = 4
disease_nums = [donor_num // divider + (1 if x < donor_num % divider else 0)  for x in range(divider)]

# Dictionary of the ratios we need
sampling_ratios = {
  "0=Blood Donor": donor_num,
  "1=Hepatitis": disease_nums[0],
  "2=Fibrosis": disease_nums[1],
  "3=Cirrhosis": disease_nums[2]
}

#Instantiate SMOTENC algorith
sm = SMOTENC(categorical_features=cat_col_index, 
	sampling_strategy = sampling_ratios, random_state=123)
sm_data, y_data_new = sm.fit_resample(X_data, y_data)
sm_data['Category'] = y_data_new
first_column = sm_data.pop('Category')
  
# insert column using insert(position,column_name,first_column) function 
sm_data.insert(0, 'Category', first_column)

"""
Count instances of each category element -- uncomment to see 
master_list = data["Category"]
print(Counter(master_list))
master_list_new = y_data_new["Category"]
print(Counter(master_list_new))
"""

compression_opts = dict(method='zip',
                        archive_name='sm_train.csv')  

sm_data.to_csv('sm_train.zip', index=False,
          compression=compression_opts)

# View synthetic dataset
# print(sm_data)

