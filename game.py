from time import sleep
def Brief():
    keuze2 = input("RENNEN!\n overgeven")
    if keuze2 == "RENNEN!":
        cliff()
    if keuze2 == "overgeven":
        print("nou je bent opgepakt door de engelsen ")
        sleep(2) 
        print("je word megenomen voor ondervraaging")
        ondervraaging()

def cliff():
    print("je sprint zo rechtdoor")
    sleep(2)
    print("maar je komt een clif tegen")
    sleep(2)
    keuzen1 = input("ga je naar\n links\nrechts")
    if keuzen1 == "links":
        print("goeden keuzen")
        sleep(2)
        print("je sprint verder na 10 minuten stop je ")
        sleep(2)
        print("volgensmij ben ik ze nu wel kwijt")
        sleep(2)
        print("je gaat lekker door op je tocht")
        langereis()

def ondervraaging():
    print("je word megenomen naar een kasteel")
    sleep(2)
    print("je word in een donkere kamer geplaatst")
    sleep(2)
    print("ze vraagen waar de brief is")
    sleep(2)
    keuze2 = input("wat zal je doen\nvertellen wat er in de brief zat\n still blijfen\n spuug in het gezicht van de ondervraager")
    if keuze2 == "vertellen":
        snitch()
    if keuze2 == "still":
        print("je besluit stil te blijven")
        sleep(4)
        print("je word gemarteld")
        sleep(3)
        print("na dagen lang martelen besluit een engelsman je te helpen")
        sleep(2)
        print("je krijgt een sluitel en besluit hem te smeeren")
        reis()
    if keuze2 =="spuug":
        print("De engelsen hebben genoeg van je gehad")
        sleep(2)
        print("je word opgehangen")
        einde2()
def einde2():
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    print("je bent dood")
    opnieuw()
    
def snitch():
    print("het klinkt allemaal als veel moeiten")
    sleep(2)
    print("je besluit maar gwoon te vertellen wat er in de brief stond")
    opnieuw()
def reis(): 
    print("Je bent eindlijk vrij")
    sleep(2)
    print("je besluit zo snellmogelijk voruit te zetten met je reis")
    sleep(2)
    print("maar nu is de vraag zal je aleen reizen of saen reizen")  
    sleep(2)
    keuzen3 = input ("solo\nsamen")
    if keuzen3 == "solo":
        print("je besluit dat aleen reizen toch beter is")
        sleep(2)
        print("ën je zet veder uit op je reis")
        brug()
    if keuzen3 == "samen":
        print("het kan zijn dat het handig is om een partner te hebben")
        sleep(2)
        print("je wilt al snell weer vertrekken")
        sleep(1)
        print("maar er moet natuurlijk wel eerst een drankje gedroken worden")
        sleep(2)
        print("dus julie gaan lekker naar de kroeg")
        
def kroeg():
    print("na een paar drankjes gedroken te hebben word julie een kamer aangeboden door de barman")
    keuzen4 = input("zullen we buiten kamp opzetten of in de aangeboode kamer slaapen?\nkamp\nkamer")
    if keuzen4 == "kamp":
        print("julie gaan toch lekker onder de sterren slaapen")
        sleep(2)
        print("je bent lekker aan het slaapen ")
        sleep(2)
        print("je hoor opeens een paar raaren geluiden")
        sleep(2)
        print("je ziet je nieuwe friend door je rugzak heen kijken")
        sleep(0.5)
        print("je vraagt wat hij aan het doen is")
        sleep(2)
        print("he reageert niet maar hij pakt wat uit zijn jas")
        sleep(2)
        print("een mes")
        sleep(1)
        print("hij steekt het mes zo in je hart")
        einde2()
    if keuzen4 == "kamer":
        print("een war bed is toch beter als buitenslaapen")
        sleep(2)
        print("lekker slaapen dus")
        sleep(3)
        print("na een lekker nachtje slaapen eten julie een ontbijdeje en gaan julie er vandoor")
        oh_nee()

def oh_nee():
    print("het begint je optevallen dat je nieuwe vriend vell vragen stelt")
    sleep(2)
    keuzen5 = input("zal je er wat van zeggen of niet\n ja\n nee")
    if keuzen5 == "ja":
        print("je besluit hem er me te benaaderden en hij begint opeens erg raar te doen")
        sleep(2)
        print("je besluit dat het risico het niet waard is en er vandoor te gaan solo")
        einde3()
    if keuzen5 == "nee":
        print("je dekt dat hij gwoon nieuwsiereg is")
        sleep(2)
        print("na een tijdje zien julie het kasteel in de verten")
        sleep(2)
        print("maar toen jouw vriend kon zien hoe dichtbij julie waren besloot hij actie te nemen")
        sleep(2)
        print("je voelt opeens een mes in je rug")
        sleep(2)
        print("ën je ziet je vriend samen met je rugzak er vandoor gaan terwijl je je laatsten hap lucht nemed")
        einde2()
def opnieuw():
    opnieuw = input("wil je opniew spelen\nja\nnee")
    if opnieuw == "ja":
        Brief()
    if opnieuw == "nee":
        exit()

def einde3():
    print("na oh zo lang reizen heb je eindelijk het kasteel berijkt.")
    sleep(2)
    code = input("je gaat naar de koning to en zegt 223445 of  22356")
    if code == "223445":
        print("fout dat was de foute coden alles was voor niets")
        opnieuw()
    if code == "22356":
        print ("goed je hebt het gedaan je bent de held en het is jouw gelukt")
        opnieuw()

def langereis():
    print("je gaat veder op je reis je slaapt soms onder de sterren.")
    sleep(2)
    print("soms in een warm bed")
    sleep(2)
    print("na een paar dagen reizen kom je een brug tegen")
    sleep(2)
    print("de brug heeft een hogen toll die je niet kan betaalen wat nu?")
    keuzen7 = input("omweg\nzwemmen")
    if keuzen7 == "omweg":
        print("je besluit om de rivier te volgen ")
        sleep(2)
        print("een paar dagen later ben je de brug over en weer op pat")
        sleep(2)
        print ("je bent ijndelijk bij het kasteel aangekomen maar je was telaat ")
        sleep(2)
        print("de engelsen hadden het kasteel al overgenomen")
        opnieuw()
    if keuzen7 == "zwemmen":
        zwemmen()

def zwemmen():
    keuzen8 = input("zal je je kleren aan of uit doen tijdens het zwemmen\n aan \n uit")
    if keuzen8 == "uit":
        print("je doet all je kleding uit en gaat zwemmen")
        sleep(2)
        print("het  was iets kouder als verwacht en je bent dood gevroren")
        opnieuw()
    if keuzen8 == "aan":
        print("je bent aan de overkant gekomen ")
        sleep(2)
        print("je bent nu wel drijfnat wat zal je doen")
        sleep(2)
        warmte()
        
def warmte():        
      keuzen9 = input ("doorzetten/kampvuur")
      if keuzen9 == "kamvuur":
        print("je ziet een lekker kampvuur met wat anderen mensen en besluit er te gaan zitten")
        sleep(2)
        print("maar het kon niet zo mooi zijn wat je werd gespot")
        sleep(2)
        print("terwijl je rustig aan het opdrogen was zie je opeens alemaal soldaten om je heen")
        sleep(2)
        print("je bent opgepakt")
        ondervraaging()

      
      if keuzen9 == "doorzetten":
        print("het  was iets kouder als verwacht en je bent dood gevroren")
        opnieuw()
print("je wordt wakker midden in het bos ")
sleep(2)
print("je bent op de grond gevallen en hebt een brief in je handen")
sleep(2)
print("je erinerd je dat jij een speciaale brief het voor de koning ")
sleep(2)
print("de brief met belanrijke info voor de oorlog tegen de engelsen")
sleep(2)
print("maar om ervoor te zorgen dat de brief nooit door iemand anders word gelezen besluit jij dat zelf maar gwoon te doen")
sleep(2)
print("wat je zag was een antal getallen 22356")
sleep(2)
print("nou dat is ook weer klaar je gaat weer lekker veder op voet maar je hoorde een raar gestomp")
sleep(2)
print("het klinkt als de engelsen wat nu")
Brief()




    



