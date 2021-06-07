import pandas as pd
import numpy as np 
user_input = int(input('Please input the ammount of users you would like and press enter:'))
users_dict = {'id':[],'user_id':[], 'user_login':[],'user_password':[], 'user_email':[],'first_name':[], 'last_name':[], 'roles':[]}
for i in range(user_input):
    users_dict['user_id'].append(f'test-user-{str(i+1).zfill(6)}')
    users_dict['user_login'].append(f'user-{str(i+1).zfill(6)}')
    users_dict['user_password'].append('FakePassword')
    users_dict['user_email'].append(f'user-{str(i+1).zfill(6)}@company.com{str(i+1).zfill(6)}')
    users_dict['first_name'].append(f'user-first-{str(i+1).zfill(6)}')
    users_dict['last_name'].append(f'user-last-{str(i+1).zfill(6)}')
    users_dict['roles'].append('user_role')
    
count = 0
tens = 0
hundreds = 0
id_list = []
done = False

while count < user_input:

    for y in range(50):
        #tens += 1

        for ones in range(19):
            print(f"{count}: {hundreds}_{y}_{ones}")
            users_dict['id'].append(f"{hundreds}_{y}_{ones}")
            count += 1

            if count > user_input-1:
                # Do whatever processing here
                
                #exit()
                done = True
               
            if done:
                break
                
        if done:
            break
    hundreds += 1
user_grid = pd.DataFrame(users_dict)
user_grid.set_index('id', inplace = True)
user_grid.to_csv('server_testing_grid.csv')