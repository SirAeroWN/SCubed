stringVariables[0].set('183500000')
tk.Entry(window, textvariable = stringVariables[0]).grid(row = 0, column = 2)
tk.Label(window, text = 'N').grid(row = 0, column = 1)
tk.Label(window, text = 'Total Population').grid(row = 0, column = 0)
stringVariables[1].set('0.000000016123288')
tk.Entry(window, textvariable = stringVariables[1]).grid(row = 1, column = 2)
tk.Label(window, text = 'B').grid(row = 1, column = 1)
tk.Label(window, text = 'Force of Infection').grid(row = 1, column = 0)
stringVariables[2].set('0.0016348773841961854')
tk.Entry(window, textvariable = stringVariables[2]).grid(row = 2, column = 2)
tk.Label(window, text = 'u').grid(row = 2, column = 1)
tk.Label(window, text = 'Death Rate in Overall Population').grid(row = 2, column = 0)
stringVariables[3].set('0.5')
tk.Entry(window, textvariable = stringVariables[3]).grid(row = 3, column = 2)
tk.Label(window, text = 'y').grid(row = 3, column = 1)
tk.Label(window, text = 'Recovery Rate').grid(row = 3, column = 0)
stringVariables[4].set('0.8')
tk.Entry(window, textvariable = stringVariables[4]).grid(row = 4, column = 2)
tk.Label(window, text = 'e').grid(row = 4, column = 1)
tk.Label(window, text = 'Vaccine Take, Percentage that are Protected').grid(row = 4, column = 0)
stringVariables[5].set('0.830076')
tk.Entry(window, textvariable = stringVariables[5]).grid(row = 5, column = 2)
tk.Label(window, text = 'p').grid(row = 5, column = 1)
tk.Label(window, text = 'Percentage Vaccinated at Birth').grid(row = 5, column = 0)
stringVariables[6].set('0')
tk.Entry(window, textvariable = stringVariables[6]).grid(row = 6, column = 2)
tk.Label(window, text = 'v').grid(row = 6, column = 1)
tk.Label(window, text = 'Vaccinated Population').grid(row = 6, column = 0)
stringVariables[7].set('100')
tk.Entry(window, textvariable = stringVariables[7]).grid(row = 7, column = 2)
tk.Label(window, text = 'I').grid(row = 7, column = 1)
tk.Label(window, text = 'Infected Population').grid(row = 7, column = 0)
stringVariables[8].set('0')
tk.Entry(window, textvariable = stringVariables[8]).grid(row = 8, column = 2)
tk.Label(window, text = 'R').grid(row = 8, column = 1)
tk.Label(window, text = 'Recovered Population').grid(row = 8, column = 0)
stringVariables[9].set('0.25')
tk.Entry(window, textvariable = stringVariables[9]).grid(row = 9, column = 2)
tk.Label(window, text = 'k').grid(row = 9, column = 1)
tk.Label(window, text = 'Death Rate from Malaria').grid(row = 9, column = 0)
