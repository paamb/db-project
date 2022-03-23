import sqlite3

con = sqlite3.connect("prosjekt_db_innlevinger1.db")



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


con = sqlite3.connect("prosjekt_db_innlevinger1.db")

cursor = con.cursor()
#INSERT OR IGNORE legger til rad i databasen bare hvis den ikke finnes fra før.
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (1, 2021, 8, 1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (2, 2022, 10, 2, 5)''')
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (4, 2022, 10, 3, 3)''')
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (5, 2022, 10, 3, 2)''')
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (6, 2022, 10, 3, 1)''')
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (7, 2022, 10, 2, 1)''')

cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (2, 1)''')

cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (2, 1)''')

cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (1, 'logan_paal@epost.no', 'superweakpw123', 'Paal Markus Bjørnstad')''')
cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (2, 'torstein@epost.no', 'superbadpw123', 'Torstein Korten')''')
cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (3, 'odd@epost.no', 'superstrongpw123', 'Odd Magne Gynnild')''')

# Denne er feil
cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (1, 'bourbon', 'Bærtørket')''')
cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (2, 'magnifique', 'Vasket')''')
cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (3, 'belle', 'Vasket')''')
cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (4, 'Bærtørket', 'Naar man bærtørker saa faar kaffen en helt spessiel arooma')''')
cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (5, 'Vasket', 'Denne kan gjøre at bønnen kan føles litt kjedelig ut')''')




cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (1, 'Nombre de Dios', '1500', 'Colombia', 'Santa Ana')''')
cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (2, 'Nombre de Trios', '1532', 'Colombia', 'Cúcuta')''')
cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (3, 'Nombre de Quatros', '1545', 'Rwanda', 'Kigali')''')
cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (4, 'Nombre de Cinco', '1689', 'Rwanda', 'Kigali')''')

# cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (4, 'Nombre de Dios', '1500', 'El Salvador', 'Santa Ana')''')


cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (1, 'arabica', 'arabica')''')
cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (2, 'brabonne', 'brabonneart')''')

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


# Brukerhistorie 2
cursor.execute('''SELECT fulltNavn, count(*) as smakstester
FROM (
SELECT DISTINCT fulltNavn, kaffeId 
FROM Bruker INNER JOIN Kaffesmaking ON Bruker.id = Kaffesmaking.brukerId
)
Group by fulltNavn
Order by smakstester desc''')

brukerhistorie_to = cursor.fetchall()
print(brukerhistorie_to)

# Brukerhistorie 4
cursor.execute('''SELECT Kaffebrenneri.navn as brennerinavn, Kaffe.navn as kaffenavn, Kaffe.id
FROM Kaffe INNER JOIN Kaffebrenneri on(Kaffe.brenneriId = Kaffebrenneri.id)
WHERE Kaffe.beskrivelse like "%floral%"
UNION
SELECT Kaffebrenneri.navn as brennrinavn, Kaffe.navn as kaffenavn, Kaffe.id
FROM Kaffesmaking INNER JOIN Kaffe on (Kaffesmaking.kaffeId = Kaffe.id) INNER JOIN Kaffebrenneri on (Kaffebrenneri.id = Kaffe.brenneriId)
WHERE Kaffesmaking.smaksnotat like "%floral%"''')

brukerhistorie_fire = cursor.fetchall()
print(brukerhistorie_fire)

# Brukerhistorie 5
cursor.execute('''SELECT  Kaffebrenneri.navn AS "brenninavn", Kaffe.navn AS "kaffenavn"
FROM Bonneparti INNER JOIN
(SELECT *
FROM Foredlingsmetode
WHERE Foredlingsmetode.id NOT IN(SELECT Foredlingsmetode.id
	FROM Foredlingsmetode
	WHERE Foredlingsmetode.navn like "%Vasket%"
	)) FiltrertForedlingsmetode
ON (FiltrertForedlingsmetode.id = Bonneparti.foredlingsmetodeId)
INNER JOIN Gard on (Gard.id = Bonneparti.gardId)
INNER JOIN Kaffe on (Kaffe.partiId = Bonneparti.id)
INNER JOIN Kaffebrenneri on (Kaffe.brenneriId = Kaffebrenneri.id)
WHERE Gard.land = "Rwanda" or Gard.land = "Colombia"
''')

#Commiter endringer til databasen
con.commit()
# Close connection
con.close()
