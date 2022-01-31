import csv
from itertools import imap


#Think i can read the html files for the maps and import into this!!!
#Map = [Mapcode, Dropzone coords", "Rooms"] --> not worth it for size of map. 
Map1 = ["()" ]



with open("Scenario1.map", "r") as file:
	rows = imap(str.split, file)
	for row in rows:
		if row[0] != ""




Map2 =
Map3 =