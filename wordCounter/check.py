
_list = ['dfds', 'dsf', '', 'dsf', '', '', '', 'dsfdsfds', '', 'dsf', 'dsgfdsf','','mohit','','','sf','sdf','','sdg']
new_list = []
count = 0 
print(len(_list))
for i,x in enumerate(_list):
	if len(x) == 0:
		new_list.append(i)

print(new_list)
#[2, 4, 5, 6, 8, 11]

count = 0  
for i,x in enumerate(new_list):
	if i < len(new_list)-1 and x+1 == new_list[i+1]:
		count += 1

num_of_para = len(new_list) - count + 1
print(num_of_para)
		

from collections import Counter 
  
data_set = "Welcome to the world of Geeks" \
"This portal has been created to provide well written well" \
"thought and well explained solutions for selected questions " \
"If you like Geeks for Geeks and would like to contribute " \
"here is your chance You can write article and mail your article " \
" to contribute at geeksforgeeks org See your article appearing on " \
"the Geeks for Geeks main page and help thousands of other Geeks. " \
  
# split() returns list of all the words in the string 
split_it = data_set.split() 
  
# Pass the split_it list to instance of Counter class. 
Counter = Counter(split_it) 
  
# most_common() produces k frequently encountered 
# input values and their respective counts. 
most_occur = Counter.most_common(4) 
  

print(most_occur) 

most_occur_str = ''
for cnt,i in enumerate(most_occur):
	for y,x in enumerate(i):
		most_occur_str += str(x)
		if y == 0:
			most_occur_str += ' : '
	if cnt < len(most_occur)-1:
		most_occur_str += ' , '

print(most_occur_str)