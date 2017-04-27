import json
import csv

with open("data1.json") as file:
	data = json.load(file)

with open("data.csv","w") as csvfile:
	fieldnames = ['company_name', 'exit','Seed','Series A','Series B','Series C','area','stage','employees','market']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for row in data['row']:
		#Acquire company name
		company1 = row['company_name']
		company = company1.replace("\n","")
		#Acquire exit
		exit = row['exit']
		#Acquire Seed
		seed = row['Seed']
		#Acquired Series A
		a = row['Series A']
		#Acquired Series B
		b = row['Series B']
		#Acquired Series C
		c = row['Series C']
		#area
		area = row['area']
		#stage
		stage1 = row['stage']
		stage = stage1.replace("\n","")
		#employees
		employee1 = row['employees']
		employee = employee1.replace("\n","")
		#market
		market = row['market']
		writer.writerow({'company_name': company, 'exit': exit, 'Seed': seed, 'Series A': a, 'Series B': b, 'Series C': c, 'area':area, 'stage':stage,'employees':employee, 'market': market})