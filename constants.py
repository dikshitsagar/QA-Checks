import pandas as pd

states_df = pd.read_csv("states.csv") 
C_default_val = 'IONCUST'
C_default_val_col = 'CUTM'
##############################
C_col_val_len = 5
C_val_len_col = 'CUNO'
##############################
C_multi_val_col = 'ECAR'
C_multi_val_lst = list(states_df['state'])
###############################
C_pmry_key = ['CUNO','CUTM']

if __name__ == "__main__":
    print("constants files loaded....")
