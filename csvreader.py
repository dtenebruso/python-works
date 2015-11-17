import csv

with open('example.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter =',')

	dates = []
	colors = []
	sales = []

	for row in readCSV:
		date = row[0]
		color = row[2]
		saleNum = row[3]

		dates.append(date)
		colors.append(color)
		sales.append(saleNum)

	print(dates)
	print(colors)
	print(sales)

	coldex = []
	searchVal = input('What color would you like to see sales numbers for? ')
	coldex = [i for i, x in enumerate(colors) if x == searchVal.lower()]
		
	for i in coldex:
		salesDate = dates[i]
		salesColor = colors[i]
		salesQuant = sales[i]
		print('The number of sales for the color ', searchVal,' is ',salesQuant, ' on', salesDate)
