from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from collections import Counter
import math

def home(request):
	return render(request,'wordCounter/home.html',{})

def counter_function(request):
	if request.GET:
		print("text came to backend")
		text = request.GET.get('text').strip()
		if text != '':
			characters = 0
			lines = 0 
			for i in text:
				if " " and "\n" not in i: 
					characters += 1
			words = len(text.split());
			sentences = len(text.split("."))
			new_line_split = text.split("\n")
			for x in new_line_split:
				if len(x) != 0:
					lines += 1

			#calculating num of paragraph
			space_pos_list = []
			count = 0
			for i,x in enumerate(new_line_split):
				if len(x) == 0:
					space_pos_list.append(i)
			count = 0  
			for i,x in enumerate(space_pos_list):
				if i < len(space_pos_list)-1 and x+1 == space_pos_list[i+1]:
					count += 1
			paragraphs = len(space_pos_list) - count + 1

			#considering average readin speed to be 158 words per minute
			read_speed = words/158
			if read_speed > 1:
				read_speed = math.ceil(read_speed)  # +1 minute for error
				read_speed = str(read_speed) + " min read"
			else:
				read_speed = math.ceil(read_speed * 60)
				read_speed = str(read_speed) + " sec read"

			frequentWord = Counter(text.lower().split())
			most_occur = frequentWord.most_common(5)
			most_occur_str = ''
			for counter,_list in enumerate(most_occur):
				for i,val in enumerate(_list):
					most_occur_str += str(val)
					if i == 0:
						most_occur_str += ' : '
				if counter < len(most_occur) - 1:
					most_occur_str += ' , '
			data = {'success':True,'words':words,'sentences':sentences,'characters':characters,'lines':lines,'paragraphs':paragraphs,'read_speed':read_speed,'most_occur':most_occur_str}
			return JsonResponse(data)
	else:
		data = {'successfull':False}
		return JsonResponse(data)