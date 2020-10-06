#1. De la tastatură se întroduce numărul de rînd al culorii curcubeului. De afişat
#denumirea culorii. Convenim că culoarea roşie are numărul de rînd 1.
culoar=int(input("Introdu numarul de rand al culorii:"))

if culoar == 1:
    print("Ai ales culoarea rosie")
elif culoar == 2:
    print("Ai ales culoarea portocalie")
elif culoar == 3:
    print("Ai ales culoarea galbena")
elif culoar == 4:
    print("Ai ales culoarea verde")
elif culoar == 5:
    print("Ai ales culoarea albastra")
elif culoar == 6:
    print("Ai ales culoarea indigo")
elif culoar == 7:
    print("Ai ales culoarea violeta")
else:
    print("error") 
#2. Într-o tabără numărul de băieţi este cu 10 mai mare decât cel al fetelor. Dacă se citeşte
#de la tastatură numărul de fete, să se spună câţi elevi sunt în tabără. Exemplu: date de
#intrare: 50 date de ieşire: 110
a = int(input("Cate fete sunt in tabara ?:"))
b = a+10
if a  >=0:
    print("In tabara sunt "+ str(a)+ " fete " +" si "+  str(b) +" baieti" + ", adica in tabara sunt " + str(a+b) +" copii" )
else:
    print("Error")
#3. Într-un autobuz care pleacă în excursie sunt 7 copii. De la încă două şcoli urcă alţi
#copii, numărul acestora citindu-se de la tastatura. Câţi copii au plecat în excursie?
#Exemplu: Date de intrare: 15 20 Date de ieşire: 42 copii
a=7
b=int(input("Cati copii au urcat de la prima scoala ?:"))
c=int(input("Cati copii au urcat de la a doua scoala ?:"))
d=a+b+c
print("In total au urcat " + str(d) + " copii")
#4. Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. Numărul globuleţelor
#albe se citeşte de la tastatură. Câte globuleţe are brăduţul, ştiind că numărul de
#globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, iar globuleţele
#albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. Exemplu: Date de intrare:
#12 Date de ieşire: 52.
a= int(input("Cate globulete albe sunt ?:"))
r= a+3
b=(a+r)-2
print("In total sunt "+str(a+r+b)+ " globulete" )
#5. Ion şi Vasile joacă următorul joc: Ion spune un număr iar Vasile trebuie să găsească
#cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion.
#Exemplu : Ion spune 10, Vasile spune 8 9 10 11 12. Ajutaţi-l pe Vasile să găsească
#răspunsul mai repede.
nr=int(input("Ion a spus ca numarul este egal cu :"))
print("Vasile a spus "+ str(nr-2) + " "+str(nr-1)+" "+ str(nr)+" "+ str(nr+1)+" "+ str(nr+2))
#6. Doi copii au primit acelaşi număr de mere Introducând de la tastatură numărul de mere
#primte, afişaţi câte mere are fiecare copil după ce primul copil mănâncă un măr şi dă
#unul celuilalt copil. Exemplu : Date de intrare : 10 Date de ieşire : primul copil 8
#mere al doilea copil 11 mere. 
a=int(input("Primul copil a primit atatea mere:"))
b=a
print("Dupa ce primul copil mancat un mar si i-a dat un mar celui de-al doilea copil, lui i-au ramas:"  + str(a-2) +" mere" + " iar al doilea copil a ramas cu " + str(b+1) +" mere")
#7. Maria vrea să verifice dacă greutatea şi înălţimea ei corespund vârstei pe care o are. Ea
#a găsit într-o carte următoarele formule de calcul ale greutăţii şi înălţimii unui copil, v
#fiind vârsta : greutate=2*v+8 (în kg), înălţime=5*v+80 (în cm). Realizaţi un program
#care să citească vârsta unui copil şi să afişeze greutatea şi înălţimea ideală, folosind
#aceste formule. 
v=int(input("Cati ani ai ?:"))
print("Greutatea ta ideala este " + str(2*v+8) + " kg " + " si inaltimea ideala este " +str(5*v+80) + " cm")
#8. Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
#aceste cifre luate o singură dată. Exemplu : date de intrare : 3 4 2 Date de ieşire : 324
#342 243 234 432.
a=int(input("primul nr este"))
b=int(input("al doilea nr este"))
c=int(input("al treilea nr este"))
print(str(a)+str(b)+str(c)+" "+str(a)+str(c)+str(b)+" "+str(b)+str(a)+str(c)+" "+str(b)+str(c)+str(a)+" "+str(c)+str(a)+str(b)+" "+str(c)+str(b)+str(a))
#9. Date trei numere, să se calculeze toate sumele posibile de câte două numere. Afişarea
#să cuprindă şi termenii sumei, nu numai valoarea ei. Exemplu: Date de intrare : 2 13
#4 Date de ieşire: 2+13 =15 2+4=6 13+4=17.
a=int(input("primul nr este"))
b=int(input("al doilea nr este"))
c=int(input("al treilea nr este"))
print(str(a)+"+" +str(b)+ " = " + str(a+b)+  " " +str(a)+"+" +str(c)+" = " +str(a+c)+" " +str(b)+"+" +str(c)+" = "+ str(c+b))
#10.Afişaţi tabla înmulţirii cu numărul n. Exemplu: pentru n=5, se va afişa pe verticală
#1x5=5 2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 10x5=50.
n=int(input("Valoarea lui n este:"))
print(str(n)+"*"+"1 = " + str(n*1))
print(str(n)+"*"+"2 = " + str(n*2))
print(str(n)+"*"+"3 = " + str(n*3))
print(str(n)+"*"+"4 = " + str(n*4))
print(str(n)+"*"+"5 = " + str(n*5))
print(str(n)+"*"+"6 = " + str(n*6))
print(str(n)+"*"+"7 = " + str(n*7))
print(str(n)+"*"+"8 = " + str(n*8))
print(str(n)+"*"+"9 = " + str(n*9))
print(str(n)+"*"+"10 = " + str(n*10))
#11.Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
#începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
#realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
#iepuri sunt în crescătorie? Exemplu : Date de intrare : nr. Iepuri la început de luna 10
#nr. iepuri morti 2 nr. iepuri nascuti 6 Date de ieşire : 14 iepuri. 
a=int(input("Cati iepuri sunt la inceputul lunii"))
b=int(input("Cati iepuri au murit?"))
c=int(input("Cati iepuri s-au nascut ?"))
d=a+c-b
print("La sfarsitul lunei in crescatoare vor fi "+ str(d)+ " iepuri")
#12.Într-o gospodărie sunt 4 găini. Introduceţi în calculator prin variabilele a, b, c, d
#numărul de ouă pe care-l dă fiecare găină într-o zi. Afişaţi câte ouă se obţin într-o
#săptămână.
a=int(input("Cate oua a facut prima gaina intr-o zi ? "))
b=int(input("Cate oua a facut a doua gaina intr-o zi ? "))
c=int(input("Cate oua a facut a treia gaina intr-o zi ? "))
d=int(input("Cate oua a facut a patra gaina intr-o zi ? "))
d=(a+b+c+d)*7
print("Intr-o saptamana se obtin " + str(d) + " oua")

