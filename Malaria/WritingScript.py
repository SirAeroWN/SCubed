# # declare window and give it a title
# 	window = tk.Tk()
# 	window.title('Options')
# 	# Variables as strings for display
# 	
	
# 	# loop through lists to produce tkinter widgets with relavent data
# 	for i in range(0, 10):
# 		stringVariables[i].set(defaults[i])
# 		tk.Entry(window, textvariable = stringVariables[i]).grid(row = i, column = 2)
# 		tk.Label(window, text = variables[i]).grid(row = i, column = 1)
# 		tk.Label(window, text = descriptors[i]).grid(row = i, column = 0)

# 	tk.Button(window, text = 'Graph', command = lambda stringVariables=stringVariables: main(stringVariables)).grid(row = i + 1, columnspan = 3)

variables = ['\'N\'', '\'B\'', '\'u\'', '\'y\'', '\'e\'', '\'p\'', '\'v\'', '\'I\'', '\'R\'', '\'k\'']
descriptors = ['\'Total Population\'', '\'Force of Infection\'', '\'Death Rate in Overall Population\'', '\'Recovery Rate\'', '\'Vaccine Take, Percentage that are Protected\'', '\'Percentage Vaccinated at Birth\'', '\'Vaccinated Population\'', '\'Infected Population\'', '\'Recovered Population\'', '\'Death Rate from Malaria\'']
stringVariables = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
defaults = ['\'183500000\'', '\'0.000000016123288\'', '\'0.0016348773841961854\'', '\'0.5\'', '\'0.8\'', '\'0.830076\'', '\'0\'', '\'100\'', '\'0\'', '\'0.25\'']

wFile = open('EfficientTkinter.py', 'w')
for i in range(0, 10):
	str1 = 'stringVariables[' + str(i) + '].set(' + defaults[i] + ')'
	str2 = 'tk.Entry(window, textvariable = stringVariables[' + str(i) + ']).grid(row = ' + str(i) + ', column = 2)'
	str3 = 'tk.Label(window, text = ' + variables[i] + ').grid(row = ' + str(i) + ', column = 1)'
	str4 = 'tk.Label(window, text = ' + descriptors[i] + ').grid(row = ' + str(i) + ', column = 0)'
	print(str1, file = wFile)
	print(str2, file = wFile)
	print(str3, file = wFile)
	print(str4, file = wFile)
wFile.close()