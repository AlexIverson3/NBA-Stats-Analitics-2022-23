cT = 0			# --[ Contador Team ]--
cG = 0			# --[ Contador Game ]--
file = ""

"
for team in teamsNBA:											# --[ Recorro cada uno de los equipo NBA de la lista 'teamsNBA' ]--

	for id in idsGames[cT]:										# --[ Recorro cada uno de los IDs de cada partido de la lista 'idsGames' ]--

		file += team + ", "
		idField = str()
		idField += str( id )
		file += ( idField + ", " +
			  datesGames[cT][cG] + ", " +
			  oppGames[cT][cG] + ", " +
			  resultsGames[cT][cG] + ", " +
			  arenasGames[cT][cG] + ", " +
			  str( weekNotesGames[cT][cG] ) + 
			  "\n" )
		cG += 1

     	cT += 1
	cG = 0



# print(file)		# --[ Linea de Control de Contenido ]--



#  Guardar contenido string de 'file' en documento CSV:
#--------------------------------------------------------
archive = open("allGames.csv","w")
archive.write(file)
archive.close()
#--------------------------------------------------------
