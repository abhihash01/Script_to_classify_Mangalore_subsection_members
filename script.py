import pandas as pd
excel_file= 'Bangalore section DEc17 2019.xlsx'
file= pd.read_excel(excel_file)
df=pd.DataFrame(file)
f = open('mangalore_div_city_list.txt', 'r')
lines = f.read().split('\n')
f.close()
while("" in lines) : 
    lines.remove("") 
exp_list='(.*Udupi.*)'
for str in lines:
  exp_list=exp_list+'|(.*'+str+'.*)'
 df2=df[df['City'].str.contains(r''+exp_list+'')==True]
 df2.to_excel("output.xlsx")



