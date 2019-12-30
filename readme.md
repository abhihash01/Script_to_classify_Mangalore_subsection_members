The only noticeable criteria to classify members on the basis of subesection was the city.
I used a pandas dataframe unique funtion to list out all the unique fields in the cities column. Then i manually made a list of all the places which fall in the DK, Udupi, UK, Kodagu and Shivamogga districts. This list has been named mangalore_div_city_list.txt. 

Then a string array is made out of all the unique places in the list mentioned previously. This is converted into a regular expression, which runs on the cities column of the main Banglore member list excel file. Then the resultant is put into output.xlsx file.

To add new files, just open the mangalore_div_city_list.txt files and append the new places at the end of the file, each city in a new line. 


working

pip install -r requirements.txt
python script.py



