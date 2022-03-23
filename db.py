import sqlite3
con = sqlite3.connect("prosjekt_db_innlevinger1.db")

cursor = con.cursor()

#INSERT OR IGNORE legger til rad i databasen bare hvis den ikke finnes fra før.
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (1, 2021, 8, 1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO Bonneparti VALUES (2, 2022, 10, 1, 1)''')

cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO BonneFraGard VALUES (2, 1)''')

cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO BonnerIParti VALUES (2, 1)''')

cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (1, 'logan_paal@epost.no', 'superweakpw123', 'Paal Markus Bjørnstad')''')
cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (2, 'torstein@epost.no', 'superbadpw123', 'Torstein Korten')''')
cursor.execute('''INSERT OR IGNORE INTO Bruker VALUES (3, 'odd@epost.no', 'superstrongpw123', 'Odd Magne Gynnild')''')

cursor.execute('''INSERT OR IGNORE INTO Foredlingsmetode VALUES (1, 'bourbon', 'Bærtørket')''')

cursor.execute('''INSERT OR IGNORE INTO Gard VALUES (1, 'Nombre de Dios', '1500', 'El Salvador', 'Santa Ana')''')

cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (1, 'arabica', 'arabica')''')
cursor.execute('''INSERT OR IGNORE INTO Kaffebonne VALUES (2, 'brabonne', 'brabonneart')''')

cursor.execute('''INSERT OR IGNORE INTO Kaffebrenneri VALUES (1, 'Jacobsen & Svart')''')

cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (1, 'Veldig god kaffe', 10 ,'2022-02-02', 1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (2, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10 ,'2022-03-02', 1, 2)''')
cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (3, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10 ,'2022-03-02', 2, 2)''')
cursor.execute('''INSERT OR IGNORE INTO Kaffesmaking VALUES (4, 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', 10 ,'2022-03-02', 3, 2)''')

cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (1, 'Vinterkaffe 2022', 'Veldig god', 100 , '2022-20-01', 3, 1, 1)''')
cursor.execute('''INSERT OR IGNORE INTO Kaffe VALUES (2, 'Sommerkaffe 2021', 'Kjempeflott', 200 , '2021-02-02', 2, 1, 2)''')

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

#Commiter endringer til databasen
con.commit()

# Close connection
con.close()
