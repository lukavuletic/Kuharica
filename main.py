import csv
import glob, os

#liste koje cemo koristiti
lista_jela = []
detalji_jela = []
ime_jela = []
sastojci_jela = []
pripravak_jela = []

#prvo jelo se ispisuje s 1
redni_broj_jela = 1

#int za provjeru tocnosti unosa ponudenog broja
odabir_jela = 10000

print("Izaberite: (1) predjelo, (2) glavno jelo, (3) desert")

#int za provjeru tocnosti unosa ponudenog broja
vrsta_jela = 0

#dok nije unesen jedan od ponudenih integera, nemoj ici dalje
while vrsta_jela not in (1, 2, 3):
	vrsta_jela = int(input())
	if vrsta_jela not in (1, 2, 3):
		print('Broj koji ste unijeli nije ponuden, pokusajte ponovo')

#ako je odabrano predjelo
if vrsta_jela == 1:
	#promijeni path u folder predjelo
	os.chdir("predjela")
	#ispisi mi svaki file koji se nalazi u tom folderu i dodaj ga u listu jela
	for file in glob.glob("*.csv"):
		lista_jela.append(file)

	#ispisi svako jelo skupa s rednim brojem za kasnije selekciju
	for i in lista_jela:
		print("{} - {}".format(redni_broj_jela,i[:-4]))
		redni_broj_jela += 1

	redni_broj_jela -= 1

	#provjeri je li redni broj jela tocan ili ne
	while odabir_jela > redni_broj_jela or odabir_jela <= 0:
		odabir_jela = int(input())
		if odabir_jela > redni_broj_jela or odabir_jela <= 0:
			print('Broj koji ste unijeli nije ponuden, pokusajte ponovo')

	#otvori .csv file odabranog jela i dodaj ga u listu detalji_jela
	with open('{}'.format(lista_jela[odabir_jela-1]), 'r') as f:
		reader = csv.reader(f)
		detalji_jela = list(reader)

	#ispuni detalje jela za lakse koristenje
	ime_jela = detalji_jela[0]
	sastojci_jela = detalji_jela[1]
	pripravak_jela = detalji_jela[2]

	#isprintaj ime, sastojke i pripavak u svakom redu zasebno
	print('IME JELA \n{}\n'.format(ime_jela[0]))
	print('SASTOJCI')
	print(*sastojci_jela, sep='\n')
	print('\nPRIPRAVAK')
	print(*pripravak_jela, sep='\n')

#ako je odabrano glavno jelo
if vrsta_jela == 2:
	#promijeni path u folder glavno jelo
	os.chdir("glavna jela")
	#ispisi mi svaki file koji se nalazi u tom folderu i dodaj ga u listu jela
	for file in glob.glob("*.csv"):
		lista_jela.append(file)

	#ispisi svako jelo skupa s rednim brojem za kasnije selekciju
	for i in lista_jela:
		print("{} - {}".format(redni_broj_jela,i[:-4]))
		redni_broj_jela += 1

	redni_broj_jela -= 1

	#provjeri je li redni broj jela tocan ili ne
	while odabir_jela > redni_broj_jela or odabir_jela <= 0:
		odabir_jela = int(input())
		if odabir_jela > redni_broj_jela or odabir_jela <= 0:
			print('Broj koji ste unijeli nije ponuden, pokusajte ponovo')

	#otvori .csv file odabranog jela i dodaj ga u listu detalji_jela
	with open('{}'.format(lista_jela[odabir_jela-1]), 'r') as f:
		reader = csv.reader(f)
		detalji_jela = list(reader)

	#ispuni detalje jela za lakse koristenje
	ime_jela = detalji_jela[0]
	sastojci_jela = detalji_jela[1]
	pripravak_jela = detalji_jela[2]

	#isprintaj ime, sastojke i pripavak u svakom redu zasebno
	print('IME JELA \n{}\n'.format(ime_jela[0]))
	print('SASTOJCI')
	print(*sastojci_jela, sep='\n')
	print('\nPRIPRAVAK')
	print(*pripravak_jela, sep='\n')

#ako je odabran desert
if vrsta_jela == 3:
	#promijeni path u folder deserti
	os.chdir("deserti")
	#ispisi mi svaki file koji se nalazi u tom folderu i dodaj ga u listu jela
	for file in glob.glob("*.csv"):
		lista_jela.append(file)

	#ispisi svako jelo skupa s rednim brojem za kasnije selekciju
	for i in lista_jela:
		print("{} - {}".format(redni_broj_jela,i[:-4]))
		redni_broj_jela += 1

	redni_broj_jela -= 1

	#provjeri je li redni broj jela tocan ili ne
	while odabir_jela > redni_broj_jela or odabir_jela <= 0:
		odabir_jela = int(input())
		if odabir_jela > redni_broj_jela or odabir_jela <= 0:
			print('Broj koji ste unijeli nije ponuden, pokusajte ponovo')

	#otvori .csv file odabranog jela i dodaj ga u listu detalji_jela
	with open('{}'.format(lista_jela[odabir_jela-1]), 'r') as f:
		reader = csv.reader(f)
		detalji_jela = list(reader)

	#ispuni detalje jela za lakse koristenje
	ime_jela = detalji_jela[0]
	sastojci_jela = detalji_jela[1]
	pripravak_jela = detalji_jela[2]

	#isprintaj ime, sastojke i pripavak u svakom redu zasebno
	print('IME JELA \n{}\n'.format(ime_jela[0]))
	print('SASTOJCI')
	print(*sastojci_jela, sep='\n')
	print('\nPRIPRAVAK')
	print(*pripravak_jela, sep='\n')