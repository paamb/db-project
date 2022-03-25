import sqlite3

DATABASE = "prosjekt_db_innlevering1.db"

def clean_database():
	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()

	cursor.execute('DELETE FROM BonneFraGard;',)
	cursor.execute('DELETE FROM Bonneparti;',)
	cursor.execute('DELETE FROM Bruker;',)
	cursor.execute('DELETE FROM Foredlingsmetode;',)
	cursor.execute('DELETE FROM Gard;',)
	cursor.execute('DELETE FROM Kaffebonne;',)
	cursor.execute('DELETE FROM Kaffebrenneri;',)
	cursor.execute('DELETE FROM Kaffesmaking;',)
	cursor.execute('DELETE FROM Kaffe;',)

	con.commit()
	con.close()

def fill_database():
	con = sqlite3.connect(DATABASE)

	cursor = con.cursor()

	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (1, 2021, 8, 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (2, 2022, 10, 2, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (3, 2022, 10, 3, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (4, 2022, 10, 4, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (5, 2022, 10, 5, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (6, 2022, 10, 6, 2)''')

	cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (2, 1)''')

	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (2, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (3, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (4, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (4, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (5, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (6, 2)''')

	cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (1, 'logan_paal@epost.no', 'superweakpw123', 'Paal Markus Bjørnstad')''')
	cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (2, 'torstein@epost.no', 'superbadpw123', 'Torstein Korten')''')
	cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (3, 'odd@epost.no', 'superstrongpw123', 'Odd Magne Gynnild')''')

	cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (1, 'Bærtørket', 'Naar man bærtørker saa faar kaffen en helt spesiell aroma')''')
	cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (2, 'Vasket', 'Denne kan gjøre at bønnen kan føles litt kjedelig ut')''')

	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (1, 'Nombre de Dios', '1500', 'Colombia', 'Santa Ana')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (2, 'Nombre de Trios', '1532', 'Colombia', 'Cúcuta')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (3, 'Nombre de Quatros', '1545', 'Rwanda', 'Kigali')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (4, 'Nombre de Cinco', '1689', 'Rwanda', 'Kigali')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (5, 'Nombre de Seis', '1669', 'Wales', 'Kanto')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (6, 'Nombre de Siete', '1337', 'Wales', 'Johto')''')

	cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (1, 'coffea arabica', 'arabica')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (2, 'coffea robusta', 'brabonneart')''')

	cursor.execute('''INSERT OR IGNORE INTO Kaffebrenneri VALUES (1, 'Jacobsen & Svart')''')

	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (1, 'Veldig god kaffe', 10 ,'2022-02-02', 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (2, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10 ,'2022-03-02', 1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (3, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10 ,'2022-03-02', 2, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (4, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10 ,'2022-03-02', 3, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (5, 'Vasket!', 10 ,'2022-03-02', 3, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (6, 'En opplevelse av rang, floral!', 10 ,'2022-03-02', 3, 3)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (7, 'En opplevelse av rang, floral!', 10 ,'2022-03-02', 3, 6)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (1, 'Vaar 2022', 'Veldig god', 100 , '2022-20-01', 'middels', 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (2, 'Sommerkaffe 2022', 'Veldig god', 500000 , '2022-20-01', 'mørk', 1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (3, 'Sommerkaffe 2021', 'Kjempeflott', 200 , '2021-02-02', 'lys', 1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (4, 'Sommerkaffe 2022', 'Kjempeflott floral i smaken', 200 , '2021-02-02', 'lys', 1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (5, 'Sommerkaffe 2023', 'Kjempeflott', 200 , '2021-02-02', 'lys', 1, 2)''')

	con.commit()
	con.close()

# Brukerhistorie 1
def brukerhistorie_1(bruker):
	clean_database()
	print("Du er logget inn som: " + bruker + "\nLegg til et smaksnotat! \n")
	brenneri = input("Brenneri: ")
	kaffenavn = input("Kaffenavn: ")
	poeng = input("Poeng (0-10): ")
	smaksnotat = input("Smaksnotat: ")

	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()

	#Oppretter gård og kaffebønn
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (1, 'Nombre de Dios', '1500', 'Colombia', 'Santa Ana')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (1, 'Bourbon', 'caffea arabica')''')
	cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (1, 1)''')

	#Lager foredingsmetode og kaffebønne
	cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (1, 'Bærtørket', 'Disse bønnene er bærtørket.')''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (1, 2022, 8, 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 1)''')

	#Lager kaffebrenneri og kaffe
	cursor.execute('''INSERT OR IGNORE INTO Kaffebrenneri VALUES (1, 'Jacobsen & Svart')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (1, 'Vinterkaffe 2022', 'Ingen beskrivelse', 600 , '2022-20-01', 'lys', 1, 1)''')



# Brukerhistorie 2
def brukerhistorie_2():
	for row in cursor.execute('''SELECT fulltNavn, count(*) as smakstester
	FROM (
	SELECT DISTINCT fulltNavn, kaffeId 
	FROM Bruker INNER JOIN Kaffesmaking ON Bruker.id = Kaffesmaking.brukerId
	)
	Group by fulltNavn
	Order by smakstester desc'''):
		print(row)

# Brukerhistorie 4
def brukerhistorie_4(filter):
	for row in cursor.execute(f'''SELECT Kaffebrenneri.navn as brennerinavn, Kaffe.navn as kaffenavn, Kaffe.id
	FROM Kaffe INNER JOIN Kaffebrenneri on(Kaffe.brenneriId = Kaffebrenneri.id)
	WHERE Kaffe.beskrivelse like ( ? )
	UNION
	SELECT Kaffebrenneri.navn as brennrinavn, Kaffe.navn as kaffenavn, Kaffe.id
	FROM Kaffesmaking INNER JOIN Kaffe on (Kaffesmaking.kaffeId = Kaffe.id) INNER JOIN Kaffebrenneri on (Kaffebrenneri.id = Kaffe.brenneriId)
	WHERE Kaffesmaking.smaksnotat like ( ? )''', [filter, filter]):
		print(row)

	# brukerhistorie_4_output= cursor.fetchall()
	# print(brukerhistorie_4_output)


# Brukerhistorie 5
def brukerhistorie_5(filter, nasjoner):

	brukerhistorie_input = [filter] + nasjoner
	# print(nasjoner)
	# Denne bruker f string men tror at ? gjør at det går fint
	# https://stackoverflow.com/questions/283645/python-list-in-sql-query-as-parameter
	for row in cursor.execute(f'''SELECT  Kaffebrenneri.navn AS "brenninavn", Kaffe.navn AS "kaffenavn"
	FROM Bonneparti INNER JOIN
	(SELECT *
	FROM Foredlingsmetode
	WHERE Foredlingsmetode.id NOT IN(SELECT Foredlingsmetode.id
		FROM Foredlingsmetode
		WHERE Foredlingsmetode.navn like ( ? )
		)) FiltrertForedlingsmetode
	ON (FiltrertForedlingsmetode.id = Bonneparti.foredlingsmetodeId)
	INNER JOIN Gard on (Gard.id = Bonneparti.gardId)
	INNER JOIN Kaffe on (Kaffe.partiId = Bonneparti.id)
	INNER JOIN Kaffebrenneri on (Kaffe.brenneriId = Kaffebrenneri.id)
	WHERE Gard.land IN ({','.join('?' for _ in brukerhistorie_input[1::])})
	''', (brukerhistorie_input)):
		print(row)



while True:
	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()
	
	tabell = input("Vil du fylle tabellene eller tømme de (t/f/ ): ")
	
	if tabell == "f":
		fill_database()
	elif tabell == "t":
		clean_database()


	brukerhistorie = int(input("Hvilken brukerhistorie vil du utføre? (1,2,3,4,5): "))
	
	if brukerhistorie == 1:
		bruker = input("Skriv inn ditt brukernavn: ")
		brukerhistorie_1(bruker)

	elif brukerhistorie == 2:
		brukerhistorie_2()

	elif brukerhistorie == 3:
		# brukerhistorie_3()
		pass

	elif brukerhistorie == 4:
		filter = input("Hvilket ord vil du filtrere på? (floral): ")
		filter = "%" + filter + "%"
		brukerhistorie_4(filter)
		
	elif brukerhistorie == 5:
		print("Skriv inn nasjonene du vil finne kaffe fra. Skriv mellomrom mellom hvert land (Colombia Nigeria Peru): ", end="")
		nasjoner = [str(nasjon) for nasjon in input().split()]
		filter = input("Hvilken foredlingsmetode vil du \x1B[3mIKKE\x1B[0m se: ")
		filter = "%" + filter + "%"
		brukerhistori_input = [filter] + nasjoner
		brukerhistorie_5(filter, nasjoner)
	elif brukerhistorie == 10:
		clean_database()
	else:
		print("Ugyldig input. Skriv inn et tall mellom 1 og 5")
	con.commit()
	# Close connection
	con.close()
	#Commiter endringer til databasen
	clean_database()


