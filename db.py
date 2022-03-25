import sqlite3
from os import system, name

DATABASE = "prosjekt_db_innlevering1.db"
cursor = None
def clear_terminal():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def clean_database():
	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()

	cursor.execute('DELETE FROM BonneFraGard;',)
	cursor.execute('DELETE FROM BonnerIParti',)
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

	# Foredlingsmetoder
	cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (1, 'Bærtørket', 'Når man bærtørker så får kaffen en helt spesiell aroma')''')
	cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (2, 'Vasket', 'Denne kan gjøre at bønnen kan føles litt kjedelig ut')''')

	# Gård
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (1, 'Nombre de Dios', '1500', 'Colombia', 'Santa Ana')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (2, 'Nombre de Trios', '1532', 'Colombia', 'Cúcuta')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (3, 'Nombre de Quatros', '1545', 'Rwanda', 'Kigali')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (4, 'Nombre de Cinco', '1689', 'Rwanda', 'Kigali')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (5, 'Nombre de Seis', '1669', 'Wales', 'Kanto')''')
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (6, 'Nombre de Siete', '1337', 'Wales', 'Johto')''')

	# Kaffebønne
	cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (1, 'coffea arabica')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (2, 'coffea robusta')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (3, 'coffea liberica')''')

	#Bønne fra gård
	cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (2, 1)''')

	# Bønner i parti
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (2, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (3, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (4, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (4, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (5, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (6, 2)''')

	# Bønne parti
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (1, 2009, 8, 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (2, 2013, 10, 2, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (3, 2015, 10, 3, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (4, 2012, 10, 4, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (5, 2015, 10, 5, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (6, 2017, 10, 6, 2)''')

	# Bruker
	cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (1, 'logan_paal@epost.no', 'superweakpw123', 'Paal Markus Bjørnstad')''')
	cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (2, 'torstein@epost.no', 'superbadpw123', 'Torstein Korten')''')
	cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (3, 'odd@epost.no', 'superstrongpw123', 'Odd Magne Gynnild')''')

	# Kaffebrenneri
	cursor.execute('''INSERT OR IGNORE INTO Kaffebrenneri VALUES (1, 'Jacobsen & Svart')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffebrenneri VALUES (2, 'The Barn')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffebrenneri VALUES (3, 'Coffee Supreme')''')

	# Kaffe
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (1, 'Høstkaffe 2019', 'Hint av aprikos', 55 , '2022-02-04', 'middels', 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (2, 'San Pedro', 'Smak av karamell', 67 , '2022-01-01', 'mørk', 2, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (3, 'Sommerkaffe 2021', 'Kjempeflott', 201 , '2021-02-02', 'lys', 3, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (4, 'Sommerkaffe 2022', 'Floral i smaken', 46 , '2021-02-02', 'lys', 1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (5, 'Sun Drop', 'Smak av appelsin og sjasmin', 32 , '2021-02-02', 'lys', 2, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (6, 'Boxer Blend', 'Fruktig og floral', 20 , '2021-02-02', 'lys', 3, 3)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (7, 'Sommerkaffe 2020', 'Sommerlig', 243 , '2021-02-02', 'lys', 1, 4)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (8, 'Our Plot Daterra', 'Vanilje og pære', 200 , '2021-02-02', 'lys', 2, 5)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (9, 'Magnifique', 'Mørk', 30 , '2021-02-02', 'lys', 3, 6)''')

	# Kaffesmaking
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (1, 'Aprikosen i kaffen gjør denne veldig god', 8 ,'2022-02-02', 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (2, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10 ,'2022-03-02', 1, 2)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (3, 'Fruktig og floral men gir meg ikke noe mer', 4 ,'2022-03-02', 2, 3)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (4, 'Litt for sterk', 3 ,'2022-03-02', 3, 4)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (5, 'Kjenner at denne kaffen er vasket, noe jeg ikke er noe glad i', 2 ,'2022-03-02', 3, 5)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (6, 'En opplevelse av rang, floral!', 9 ,'2022-03-02', 3, 6)''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (7, 'En veldig god kaffe', 7 ,'2022-03-02', 3, 1)''')
	

	con.commit()
	con.close()

# Brukerhistorie 1
def brukerhistorie_1(epost):
	clean_database()
	print("Databasen tømmes automatisk på brukerhistorie 1.")
	print("Du er logget inn som: " + epost + "\nLegg til et smaksnotat! \n")
	brenneri = input("Brenneri: ")
	kaffenavn = input("Kaffenavn: ")
	poeng = input("Poeng (0-10): ")
	smaksnotat = input("Smaksnotat: ")
	smaksdato = input("Smaksdato (yyyy-mm-dd): ")

	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()

	#Oppretter gård og kaffebønne
	cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (1, 'Nombre de Dios', '1500', 'Colombia', 'Santa Ana')''')
	cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (1, 'coffea arabica')''')
	cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (1, 1)''')

	#Lager foredingsmetode og bønneparti
	cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (1, 'Bærtørket', 'Disse bønnene er bærtørket.')''')
	cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (1, 2022, 8, 1, 1)''')
	cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 1)''')

	#Lager kaffebrenneri og kaffe
	cursor.execute(f'''INSERT OR IGNORE INTO Kaffebrenneri VALUES (1, ( ? ))''', [brenneri])
	cursor.execute(f'''INSERT OR IGNORE INTO Kaffe VALUES (1, ( ? ), 'Ingen beskrivelse', 600 , '2022-01-20', 'lys', 1, 1)''', [kaffenavn])

	#Lager Bruker og Kaffesmaking
	cursor.execute(f'''INSERT OR IGNORE INTO Bruker VALUES (1, ( ? ), 'passord123', 'Bruker Brukersen')''', [epost])
	cursor.execute(f'''INSERT OR IGNORE INTO Kaffesmaking VALUES (1, ( ? ), ( ? ), ( ? ), 1, 1)''', [smaksnotat, poeng, smaksdato])

	con.commit()
	clear_terminal()
	print("    Smaksnotat    ||     Kaffenavn    ")
	print("==================================")
	for row in cursor.execute('''SELECT smaksnotat, navn
		FROM Kaffesmaking INNER JOIN Kaffe ON Kaffesmaking.kaffeId = Kaffe.id'''):
		print(f'      {row[0] : <15}{row[1] : <30}  ')

	con.commit()
	con.close()


# Brukerhistorie 2
def brukerhistorie_2():
	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()
	print("    Fullt navn    ||     Antall smakstester    ")
	print("===============================================")
	for row in cursor.execute(
		'''SELECT fulltNavn, count(*) as smakstester
		FROM (
			SELECT DISTINCT Bruker.id, fulltNavn, kaffeId 
			FROM Bruker INNER JOIN Kaffesmaking ON Bruker.id = Kaffesmaking.brukerId
			WHERE date('now','start of year') <= date(Kaffesmaking.smaksdato)
		)
		Group by fulltNavn
		Order by smakstester desc'''):
		print(f'  {row[0] : <30}{row[1] : <30}  ')

	con.commit()
	con.close()

# Brukerhistorie 3
def brukerhistorie_3():
	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()
	print("    Gjennomsnittspoeng    ||     Kaffenavn     ||     KiloprisNOK     ||     Brennerinavn     ")
	print("==============================================================================================")
	for row in cursor.execute('''
		SELECT AVG(Kaffesmaking.poeng) as avgPoeng, Kaffe.navn, Kaffe.kiloprisNOK, Kaffebrenneri.navn
		FROM Kaffesmaking INNER JOIN Kaffe on (Kaffesmaking.kaffeId = Kaffe.id)
		INNER JOIN Kaffebrenneri on (Kaffe.brenneriId = Kaffebrenneri.id)
		GROUP BY Kaffe.id
		ORDER BY (avgPoeng/Kaffe.kiloprisNOK) DESC'''):
		print(f'  {row[0] : <25}{row[1] : <25}{row[2] : <25}{row[3] : <25}  ')

	con.commit()
	con.close()


# Brukerhistorie 4
def brukerhistorie_4(filter):
	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()
	print("    Brennerinavn    ||     Kaffenavn     ")
	print("=========================================")

	for row in cursor.execute(f'''
		SELECT DISTINCT Kaffebrenneri.navn as brennerinavn, Kaffe.navn as kaffenavn
		FROM Kaffe 
		INNER JOIN Kaffebrenneri on (Kaffe.brenneriId = Kaffebrenneri.id) 
		INNER JOIN Kaffesmaking on (Kaffesmaking.kaffeId = Kaffe.id)
		WHERE Kaffe.beskrivelse like ( ? ) OR Kaffesmaking.smaksnotat like ( ? )
		''', [filter, filter]):
		print(f'  {row[0] : <25}{row[1] : ^8}  ')

	con.commit()
	con.close()


# Brukerhistorie 5
def brukerhistorie_5(filter, nasjoner):
	con = sqlite3.connect(DATABASE)
	cursor = con.cursor()
	brukerhistorie_input = [filter] + nasjoner
	print("    Brennerinavn    ||     Kaffenavn     ")
	print("=========================================")

	for row in cursor.execute(f'''
		SELECT DISTINCT Kaffebrenneri.navn AS "brenninavn", Kaffe.navn AS "kaffenavn"
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
		print(f'  {row[0] : <25}{row[1] : ^10}  ')
	con.commit()
	con.close()

def velg_brukerhistorie():
	print('''VELG BRUKERHISTORIE\n
===================================
Brukerhistorie 1: Registrer en kaffesmaking
Brukerhistorie 2: Finn brukere med flest smakinger
Brukerhistorie 3: Se hvilken kaffe som gir mest for pengene
Brukerhistorie 4: Søk etter kaffe med beskrivelse
Brukerhistirie 5: Søk etter kaffe fra land og med foredlingsmetode\n\n''')
	brukerhistorie = int(input("Hvilken brukerhistorie vil du utføre? (1,2,3,4,5): "))
	clear_terminal()
	if brukerhistorie == 1:
		epost = input("Skriv inn din epostadresse: ")
		brukerhistorie_1(epost)

	elif brukerhistorie == 2:
		brukerhistorie_2()

	elif brukerhistorie == 3:
		brukerhistorie_3()

	elif brukerhistorie == 4:
		filter = input("Hvilket ord vil du filtrere på? (floral): ")
		filter = "%" + filter + "%"
		clear_terminal()
		brukerhistorie_4(filter)
		
		
	elif brukerhistorie == 5:
		print("Skriv inn nasjonene du vil finne kaffe fra. Skriv mellomrom mellom hvert land (Colombia Rwanda Wales): ", end="")
		nasjoner = [str(nasjon) for nasjon in input().split()]
		filter = input("Hvilken foredlingsmetode vil du \x1B[3mIKKE\x1B[0m se: ")
		clear_terminal()
		brukerhistorie_5(filter, nasjoner)
		
	elif brukerhistorie == 10:
		clean_database()
	else:
		print("Ugyldig input. Skriv inn et tall mellom 1 og 5")
	input("\n\n\n\nTrykk ENTER for å gå videre")

def main():
	clean_database()
	while True:
		tabell = input("Vil du fylle tabellene eller tømme de (t/f/ ): ")
		if tabell == "f":
			fill_database()
		elif tabell == "t":
			clean_database()
		clear_terminal()
		velg_brukerhistorie()
		clear_terminal()
		clean_database()

main()