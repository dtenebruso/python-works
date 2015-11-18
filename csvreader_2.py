import csv
import time

with open('example.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter =',')

	dates = []
	sassoc = []
	colors = []
	sales = []

	for row in readCSV:
		date = row[0]
		salepers = row[1]
		color = row[2]
		saleNum = row[3]

		dates.append(date)
		sassoc.append(salepers.lower())
		colors.append(color.lower())
		sales.append(saleNum)

	#print(dates)
	#print(sassoc)
	#print(colors)
	#print(sales)

	def search_by_date(searchVal,dates,sassoc,colors,sales):
		
		coldex = [i for i, x in enumerate(dates) if x == searchVal]
		
		label=1
		for i in coldex:
			salesAssoc = sassoc[i]
			salesColor = colors[i]
			salesQuant = sales[i]
			print('\n',label,')  The number of sales on ', searchVal,' of the color ',salesColor, ' is ', salesQuant, ' by ',salesAssoc)
			time.sleep(1.5)
			label+=1

	def search_by_name(searchVal,dates,sassoc,colors,sales):
		
		coldex = [i for i, x in enumerate(sassoc) if x == searchVal.lower()]
		
		label=1
		for i in coldex:
			salesDate = dates[i]
			salesColor = colors[i]
			salesQuant = sales[i]
			print('\n',label,')  Sales by ', searchVal,' on ',salesDate, ' of the color ', salesColor, ' are ', salesQuant)
			time.sleep(1.5)
			label+=1

	def search_by_color(searchVal,dates,sassoc,colors,sales):
		
		coldex = [i for i, x in enumerate(colors) if x == searchVal.lower()]
		
		label=1
		for i in coldex:
			salesDate = dates[i]
			salesAssoc = sassoc[i]
			salesQuant = sales[i]
			print('\n',label,')  The number of sales for the color ', searchVal,' by ', salesAssoc,' is ',salesQuant, ' on', salesDate)
			time.sleep(1.5)
			label+=1

	def search_by_sales(searchVal,dates,sassoc,colors,sales):
		
		coldex = [i for i, x in enumerate(sales) if x == searchVal]

		label=1
		for i in coldex:
			salesDate = dates[i]
			salesAssoc = sassoc[i]
			salesColor = colors[i]
			print('\n',searchVal,') sales were made by ',salesAssoc, ' in the color ', salesColor,' on ', salesDate)
			time.sleep(1.5)
			label+=1


	clearance = 0

	while clearance != 1:
		ans = input('\n\nHow would you like to search through the data?\n(date,name,color,quantity)\n --Enter text here-----> ')
		if ans == 'date':
			print("\nWhat is the date you would like to look up?(m/d/year): ")
			searchVal = input('')
			search_by_date(searchVal,dates,sassoc,colors,sales)
			clearance+=1

		elif ans == 'name':
			print("\nWhat is the name you would like to look up?: ")
			searchVal = input('')
			search_by_name(searchVal,dates,sassoc,colors,sales)
			clearance+=1

		elif ans == 'color':
			print("\nWhat is the product color you wish to look up?: ")
			searchVal = input('')
			search_by_color(searchVal,dates,sassoc,colors,sales)
			clearance+=1

		elif ans == 'quantity':
			print("\nWhat is the total sales quantitiy you wish to look up?(example. 33 or 5.4):  ")
			searchVal = input('')
			search_by_sales(searchVal,dates,sassoc,colors,sales)
			clearance+=1
		else:
			print("\n\n----->Invalid Entry<------\n\n")
			

	




