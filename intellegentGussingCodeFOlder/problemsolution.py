import pandas as pd

df = pd.read_csv('intelligentGuessingDataSet.csv',encoding='latin-1')


for index in df.index:
   
    email_pattern = df["email"][index].split('@')[0]
    f11 = str(df["firstname"][index]).lower()
    l22 = str(df["lastname"][index]).lower()
    if f11  == email_pattern:
        
        df.loc[index, 'Email Pattern'] = '<11>'
    elif l22 == email_pattern:
        
        df.loc[index, 'Email Pattern'] = '<22>'
    elif len(l22.split(' ')) > 1:
        if (f11[0] + '.' + l22.split(' ')[1]) == email_pattern:
         
            df.loc[index, 'Email Pattern'] = '<1>.<21>'
            
        elif (f11[0] + l22.split(' ')[0] + l22.split(' ')[1]) == email_pattern:
        
            df.loc[index, 'Email Pattern'] = '<1><20><21>'
           
        elif (f11 + '.' + l22.split(' ')[1]) == email_pattern:
          
            df.loc[index, 'Email Pattern'] = '<11>.<21>'
           
        elif (f11 + '.' + l22.split(' ')[0] + l22.split(' ')[1]) == email_pattern:
          
            df.loc[index, 'Email Pattern'] = '<11>.<20><21>'
          
        elif (f11  + l22.split(' ')[0] + '.' + l22.split(' ')[1]) == email_pattern:
          
            df.loc[index, 'Email Pattern'] = '<11><20>.<21>'
          
        elif (f11 + '.'+ l22.split(' ')[0]+l22.split(' ')[1][0:6])  == email_pattern:
          
            df.loc[index, 'Email Pattern'] = '<11>.<220><221l>'
            
        elif len(l22.split(' ')[0].split("'")) > 1:
          if (f11 + '.' + l22.split(' ')[0].split("'")[0] + l22.split(' ')[0].split("'")[1]) == email_pattern:
       
            df.loc[index, 'Email Pattern'] = '<11>.<200><201>'
         
    elif (f11[0] + '.' + l22.split(' ')[0]) == email_pattern:
       
            df.loc[index, 'Email Pattern'] = '<1>.<20>'
         
    elif (f11[0] + l22.split(' ')[0]) == email_pattern:
       
            df.loc[index, 'Email Pattern'] = '<1><20>'
           
    elif (f11[0:2] + l22)  == email_pattern:
          
            df.loc[index, 'Email Pattern'] = '<11-f2l><22>'
           
    elif (f11 + '.'+ l22)  == email_pattern:
        
            df.loc[index, 'Email Pattern'] = '<11>.<22>'
           
    elif len(f11.split('-')) > 1:
        if (f11.split('-')[0] + f11.split('-')[1] + '.' + l22):
         
            df.loc[index, 'Email Pattern'] = '<110><111>.<22>'
           
    elif (f11 + '-'+ l22)  == email_pattern:
          
            df.loc[index, 'Email Pattern'] = '<11>-<22>'
          
   
df.to_csv("probelm1_submission.csv", index=False)
    

