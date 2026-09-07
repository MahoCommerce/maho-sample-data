"""The store view translations of the Maho Store website, keyed by the English string.

The Maho Store website (packs/store) carries four store views: English, French, German and
Italian. tools/build-store-pack.py looks every English string up here and writes a store scoped
row for each language it finds. A string that is missing stays in English, and the build prints
how many are still missing, so the file can be filled a pack at a time.

The catalog itself lives in the industry packs, so the keys are the English strings of those
packs: category names and descriptions, product names and descriptions, review titles and bodies.
The attribute option labels are not here: they are shared by several industries and live in
packs/_shared/attribute_options.csv, next to the labels they translate.

The keys must match the English text character for character.
"""

# Category names and descriptions of the store tree.
CATEGORIES = {
    'Default Category': ('Catégorie par défaut', 'Standardkategorie', 'Categoria predefinita'),
    'Every product of the ten Maho demo stores, on the default theme.': (
        'Tous les produits des dix boutiques de démonstration Maho, sur le thème par défaut.',
        'Jedes Produkt der zehn Maho-Demoshops, auf dem Standard-Theme.',
        'Ogni prodotto dei dieci negozi dimostrativi Maho, sul tema predefinito.'),

    # Fashion
    'Fashion': ('Mode', 'Mode', 'Moda'),
    'Travel-wear and lifestyle pieces for the journey.': (
        'Des vêtements de voyage et des pièces du quotidien, pour la route.',
        'Reisekleidung und Lieblingsstücke für unterwegs.',
        'Capi da viaggio e pezzi di tutti i giorni, per la strada.'),
    'Women': ('Femme', 'Damen', 'Donna'),
    'New Arrivals': ('Nouveautés', 'Neuheiten', 'Novità'),
    'Tops & Blouses': ('Hauts et chemisiers', 'Tops und Blusen', 'Top e camicette'),
    'Pants & Denim': ('Pantalons et jeans', 'Hosen und Jeans', 'Pantaloni e jeans'),
    'Dresses & Skirts': ('Robes et jupes', 'Kleider und Röcke', 'Abiti e gonne'),
    'Men': ('Homme', 'Herren', 'Uomo'),
    'Shirts': ('Chemises', 'Hemden', 'Camicie'),
    'Tees, Knits and Polos': ('T-shirts, mailles et polos', 'Shirts, Strick und Polos', 'T-shirt, maglieria e polo'),
    'Blazers': ('Vestes', 'Sakkos', 'Giacche'),
    'Accessories': ('Accessoires', 'Accessoires', 'Accessori'),
    'Eyewear': ('Lunettes', 'Brillen', 'Occhiali'),
    'Shoes': ('Chaussures', 'Schuhe', 'Scarpe'),
    'Bags & Luggage': ('Sacs et bagages', 'Taschen und Gepäck', 'Borse e valigie'),
    'Sale': ('Soldes', 'Sale', 'Saldi'),

    # Electronics
    'Electronics': ('Électronique', 'Elektronik', 'Elettronica'),
    'Audio, computing, cameras and smart home gear, tested by people who use it.': (
        "Audio, informatique, photo et maison connectée, testés par ceux qui s'en servent.",
        'Audio, Computer, Kameras und Smart Home, getestet von Menschen, die es benutzen.',
        'Audio, informatica, fotografia e casa connessa, provati da chi li usa.'),
    'Audio': ('Audio', 'Audio', 'Audio'),
    'Computing': ('Informatique', 'Computer', 'Informatica'),
    'Cameras': ('Photo', 'Kameras', 'Fotografia'),
    'Smart Home': ('Maison connectée', 'Smart Home', 'Casa connessa'),
    'Wearables': ('Objets connectés', 'Wearables', 'Indossabili'),

    # Food
    'Food': ('Épicerie', 'Lebensmittel', 'Alimentari'),
    'Small-batch food from farms and makers we know by name.': (
        "Des produits en petites quantités, de fermes et d'artisans que nous connaissons par leur nom.",
        'Lebensmittel in kleinen Mengen, von Höfen und Herstellern, die wir beim Namen kennen.',
        'Cibo in piccole quantità, da fattorie e artigiani che conosciamo per nome.'),
    'Pantry': ('Garde-manger', 'Vorrat', 'Dispensa'),
    'Bakery': ('Boulangerie', 'Bäckerei', 'Panetteria'),
    'Cheese & Charcuterie': ('Fromages et charcuterie', 'Käse und Wurst', 'Formaggi e salumi'),
    'Coffee & Tea': ('Café et thé', 'Kaffee und Tee', 'Caffè e tè'),
    'Drinks': ('Boissons', 'Getränke', 'Bevande'),
    'Gift Boxes': ('Coffrets cadeaux', 'Geschenkboxen', 'Confezioni regalo'),

    # Books
    'Books': ('Livres', 'Bücher', 'Libri'),
    'An independent bookshop with a short shelf and long opinions.': (
        "Une librairie indépendante, peu de rayons et beaucoup d'avis.",
        'Eine unabhängige Buchhandlung mit kurzem Regal und langen Meinungen.',
        'Una libreria indipendente, con pochi scaffali e molte opinioni.'),
    'Fiction': ('Romans', 'Belletristik', 'Narrativa'),
    'Crime & Thrillers': ('Policiers et thrillers', 'Krimis und Thriller', 'Gialli e thriller'),
    'Science & Nature': ('Science et nature', 'Wissenschaft und Natur', 'Scienza e natura'),
    'History': ('Histoire', 'Geschichte', 'Storia'),
    'Cooking': ('Cuisine', 'Kochen', 'Cucina'),
    'Children': ('Enfants', 'Kinder', 'Bambini'),

    # Jewelry
    'Jewelry': ('Bijoux', 'Schmuck', 'Gioielli'),
    'Fine and everyday jewelry, made in a small workshop from recycled metals.': (
        'Des bijoux fins et de tous les jours, faits dans un petit atelier avec des métaux recyclés.',
        'Feiner und alltäglicher Schmuck, in einer kleinen Werkstatt aus recycelten Metallen gefertigt.',
        'Gioielli fini e di tutti i giorni, fatti in un piccolo laboratorio con metalli riciclati.'),
    'Rings': ('Bagues', 'Ringe', 'Anelli'),
    'Necklaces': ('Colliers', 'Ketten', 'Collane'),
    'Earrings': ("Boucles d'oreilles", 'Ohrringe', 'Orecchini'),
    'Bracelets': ('Bracelets', 'Armbänder', 'Bracciali'),
    'Engagement': ('Fiançailles', 'Verlobung', 'Fidanzamento'),
    'Gifts': ('Cadeaux', 'Geschenke', 'Regali'),

    # Beauty
    'Beauty': ('Beauté', 'Beauty', 'Bellezza'),
    'Skincare, body care and fragrance made in small batches with short ingredient lists.': (
        "Soins du visage, soins du corps et parfums, en petites séries et avec peu d'ingrédients.",
        'Gesichtspflege, Körperpflege und Duft, in kleinen Mengen und mit kurzen Zutatenlisten.',
        'Cura del viso, cura del corpo e profumi, in piccole serie e con pochi ingredienti.'),
    'Cleansers': ('Nettoyants', 'Reinigung', 'Detergenti'),
    'Serums': ('Sérums', 'Seren', 'Sieri'),
    'Moisturisers': ('Hydratants', 'Feuchtigkeitspflege', 'Idratanti'),
    'Body': ('Corps', 'Körper', 'Corpo'),
    'Fragrance': ('Parfums', 'Duft', 'Profumi'),
    'Sets': ('Coffrets', 'Sets', 'Cofanetti'),

    # Home
    'Home': ('Maison', 'Wohnen', 'Casa'),
    'Furniture, textiles and objects for a calm home, made by workshops we visit.': (
        'Meubles, textiles et objets pour une maison calme, faits par des ateliers que nous visitons.',
        'Möbel, Textilien und Objekte für ein ruhiges Zuhause, aus Werkstätten, die wir besuchen.',
        'Mobili, tessuti e oggetti per una casa tranquilla, da laboratori che visitiamo.'),
    'Furniture': ('Meubles', 'Möbel', 'Mobili'),
    'Seating': ('Assises', 'Sitzmöbel', 'Sedute'),
    'Bedding': ('Linge de lit', 'Bettwaren', 'Biancheria da letto'),
    'Kitchen & Dining': ('Cuisine et table', 'Küche und Esszimmer', 'Cucina e tavola'),
    'Lighting': ('Luminaires', 'Leuchten', 'Illuminazione'),
    'Decor': ('Décoration', 'Deko', 'Decorazioni'),

    # Sports
    'Sports': ('Sport', 'Sport', 'Sport'),
    'Gear for running, cycling, the gym and the trail, tested by people who train.': (
        "De l'équipement pour la course, le vélo, la salle et le sentier, testé par ceux qui s'entraînent.",
        'Ausrüstung für Laufen, Radfahren, Studio und Trail, getestet von Menschen, die trainieren.',
        'Attrezzatura per la corsa, la bici, la palestra e il sentiero, provata da chi si allena.'),
    'Running': ('Course', 'Laufen', 'Corsa'),
    'Cycling': ('Vélo', 'Radfahren', 'Ciclismo'),
    'Gym & Training': ('Salle et entraînement', 'Studio und Training', 'Palestra e allenamento'),
    'Yoga & Recovery': ('Yoga et récupération', 'Yoga und Regeneration', 'Yoga e recupero'),
    'Hiking': ('Randonnée', 'Wandern', 'Escursionismo'),
    'Swimming': ('Natation', 'Schwimmen', 'Nuoto'),

    # Kids
    'Kids': ('Enfants', 'Kinder', 'Bambini'),
    'Toys, clothes and things for small rooms, chosen to last more than one child.': (
        "Jouets, vêtements et objets pour petites chambres, choisis pour durer plus d'un enfant.",
        'Spielzeug, Kleidung und Dinge für kleine Zimmer, gewählt für mehr als ein Kind.',
        'Giochi, vestiti e oggetti per stanze piccole, scelti per durare più di un bambino.'),
    'Toys': ('Jouets', 'Spielzeug', 'Giochi'),
    'Clothing': ('Vêtements', 'Kleidung', 'Abbigliamento'),
    'Nursery': ('Chambre de bébé', 'Kinderzimmer', 'Cameretta'),
    'Outdoor': ('Plein air', 'Draußen', "All'aperto"),

    # Garden
    'Garden': ('Jardin', 'Garten', 'Giardino'),
    'Plants, seeds, pots and tools from a nursery that grows what it sells.': (
        "Plantes, graines, pots et outils d'une pépinière qui cultive ce qu'elle vend.",
        'Pflanzen, Samen, Töpfe und Werkzeug aus einer Gärtnerei, die anbaut, was sie verkauft.',
        'Piante, semi, vasi e attrezzi da un vivaio che coltiva quello che vende.'),
    'Houseplants': ("Plantes d'intérieur", 'Zimmerpflanzen', 'Piante da interno'),
    'Outdoor Plants': ("Plantes d'extérieur", 'Gartenpflanzen', 'Piante da esterno'),
    'Seeds & Bulbs': ('Graines et bulbes', 'Samen und Zwiebeln', 'Semi e bulbi'),
    'Pots & Planters': ('Pots et jardinières', 'Töpfe und Kübel', 'Vasi e fioriere'),
    'Tools': ('Outils', 'Werkzeug', 'Attrezzi'),
    'Outdoor Furniture': ('Mobilier de jardin', 'Gartenmöbel', 'Mobili da giardino'),
}

# Review titles and bodies.
REVIEWS = {
    # Fashion
    'Exactly as pictured': ('Exactement comme sur la photo', 'Genau wie abgebildet', 'Esattamente come in foto'),
    'Fits true to size and the fabric feels expensive. Washed twice, no change.': (
        'Taille juste et le tissu fait cher. Lavé deux fois, aucun changement.',
        'Fällt normal aus und der Stoff fühlt sich teuer an. Zweimal gewaschen, keine Veränderung.',
        'Veste come da taglia e il tessuto sembra costoso. Lavato due volte, nessun cambiamento.'),
    'Ties stay put': ('Les liens tiennent', 'Die Bänder halten', 'I lacci tengono'),
    'The wrap does not come loose during the day. Shipping was quick.': (
        'Le cache-cœur ne se défait pas dans la journée. Livraison rapide.',
        'Das Wickelteil geht tagsüber nicht auf. Schneller Versand.',
        "L'incrocio non si apre durante il giorno. Spedizione veloce."),
    'My new favourite': ('Mon nouveau préféré', 'Mein neuer Liebling', 'Il mio nuovo preferito'),
    'Comfortable, light and it goes with everything I own.': (
        "Confortable, léger et il va avec tout ce que j'ai.",
        'Bequem, leicht und es passt zu allem, was ich habe.',
        'Comodo, leggero e sta bene con tutto quello che ho.'),
    'Good, not perfect': ('Bien, sans être parfait', 'Gut, nicht perfekt', 'Buono, non perfetto'),
    'Nice cut and colour. The sizing runs a little large, so size down.': (
        'Belle coupe et belle couleur. La taille est un peu grande, prenez en dessous.',
        'Schöner Schnitt und schöne Farbe. Fällt etwas groß aus, also eine Nummer kleiner wählen.',
        "Bel taglio e bel colore. La taglia è un po' grande, prendine una in meno."),
    'Bought it for a wedding': ('Acheté pour un mariage', 'Für eine Hochzeit gekauft', 'Comprato per un matrimonio'),
    'Wore it to a summer wedding and got asked about it four times.': (
        "Porté à un mariage d'été, on m'a demandé quatre fois où je l'avais trouvé.",
        'Bei einer Sommerhochzeit getragen und vier Mal darauf angesprochen worden.',
        "Indossato a un matrimonio d'estate e me lo hanno chiesto quattro volte."),
    'Creases, but that is linen': ("Il froisse, mais c'est du lin", 'Es knittert, aber das ist Leinen', 'Si stropiccia, ma è lino'),
    'Looks best a little crumpled. Cool on a hot day and dries in an hour.': (
        "Il est plus beau un peu froissé. Frais quand il fait chaud et sec en une heure.",
        'Es sieht leicht zerknittert am besten aus. Kühl an heißen Tagen und in einer Stunde trocken.',
        "Sta meglio un po' spiegazzato. Fresco quando fa caldo e asciuga in un'ora."),
    'Packed it for three weeks': ('Emporté pendant trois semaines', 'Drei Wochen im Koffer', 'In valigia per tre settimane'),
    'Came out of the bag ready to wear every time. Would buy again.': (
        'Il sortait du sac prêt à porter à chaque fois. Je rachèterai.',
        'Kam jedes Mal tragefertig aus der Tasche. Ich kaufe es wieder.',
        'Usciva dalla borsa pronto da indossare ogni volta. Lo ricomprerei.'),
    'Collar holds its shape': ('Le col garde sa forme', 'Der Kragen hält die Form', 'Il colletto tiene la forma'),
    'Buttoned down, no curling after a dozen washes. Proper oxford cloth.': (
        "Col boutonné, aucun rebord après une douzaine de lavages. Du vrai tissu oxford.",
        'Button-down, keine Wellen nach einem Dutzend Wäschen. Echter Oxford-Stoff.',
        'Button-down, nessuna arricciatura dopo una dozzina di lavaggi. Vero tessuto oxford.'),
    'Sleeves a touch long': ('Manches un peu longues', 'Ärmel etwas zu lang', "Maniche un po' lunghe"),
    'Good shirt, but the sleeves are long on me. A cuff roll fixes it.': (
        'Bonne chemise, mais les manches sont longues pour moi. Un revers règle le problème.',
        'Gutes Hemd, aber die Ärmel sind mir zu lang. Einmal umschlagen löst das.',
        'Bella camicia, ma le maniche sono lunghe per me. Un risvolto risolve.'),
    'Solid basics': ('Des basiques solides', 'Solide Basics', 'Capi base che durano'),
    'Heavy cotton, no see-through, neck has not stretched. Bought three.': (
        "Coton épais, pas transparent, le col n'a pas bougé. J'en ai acheté trois.",
        'Schwere Baumwolle, nicht durchsichtig, der Ausschnitt ist nicht ausgeleiert. Drei gekauft.',
        'Cotone pesante, non trasparente, il collo non si è allargato. Ne ho presi tre.'),
    'Warm without bulk': ('Chaud sans volume', 'Warm ohne aufzutragen', 'Caldo senza volume'),
    'Merino at its best. Fits under a jacket and over a shirt.': (
        'Du mérinos au meilleur niveau. Il passe sous une veste et sur une chemise.',
        'Merino von seiner besten Seite. Passt unter eine Jacke und über ein Hemd.',
        'Merino al meglio. Sta sotto una giacca e sopra una camicia.'),
    'Buttons are horn': ('Des boutons en corne', 'Knöpfe aus Horn', 'Bottoni in corno'),
    'Real horn buttons and a proper placket. Small things, done right.': (
        'De vrais boutons en corne et une patte de boutonnage soignée. Les détails, bien faits.',
        'Echte Hornknöpfe und eine ordentliche Knopfleiste. Kleine Dinge, richtig gemacht.',
        'Bottoni in vero corno e un bel cannoncino. Piccole cose, fatte bene.'),
    'Stiff at first': ('Rigide au début', 'Anfangs steif', "Rigidi all'inizio"),
    'Two weeks of wear and they gave in. Now they fit like a glove.': (
        'Deux semaines de port et ils se sont assouplis. Maintenant ils vont comme un gant.',
        'Zwei Wochen getragen und sie haben nachgegeben. Jetzt sitzen sie wie angegossen.',
        'Due settimane di uso e si sono ammorbiditi. Ora calzano a pennello.'),
    'Travel blazer': ('La veste de voyage', 'Der Reiseblazer', 'La giacca da viaggio'),
    'Rolled it in a suitcase, shook it out, wore it to dinner.': (
        'Roulée dans une valise, secouée, portée au dîner.',
        'Im Koffer gerollt, ausgeschüttelt, zum Abendessen getragen.',
        'Arrotolata in valigia, scossa, indossata a cena.'),
    'Lining is light': ('Doublure légère', 'Leichtes Futter', 'Fodera leggera'),
    'Half lined, so it breathes. Perfect for a warm office.': (
        'Demi-doublée, donc elle respire. Parfaite pour un bureau chaud.',
        'Halb gefüttert, also atmet er. Perfekt für ein warmes Büro.',
        'Mezza foderata, quindi respira. Perfetta per un ufficio caldo.'),
    'Lenses are dark enough': ('Des verres assez foncés', 'Die Gläser sind dunkel genug', 'Lenti abbastanza scure'),
    'Proper category three lenses and no distortion at the edges.': (
        'De vrais verres de catégorie trois, sans déformation sur les bords.',
        'Echte Gläser der Kategorie drei und keine Verzerrung am Rand.',
        'Vere lenti di categoria tre e nessuna distorsione ai bordi.'),
    'Cheap and cheerful': ('Simple et efficace', 'Günstig und gut', 'Economico e fa il suo'),
    'Clear lenses, light frame, a spare pair for the car.': (
        'Verres clairs, monture légère, une paire de secours pour la voiture.',
        'Klare Gläser, leichter Rahmen, ein Ersatzpaar fürs Auto.',
        "Lenti chiare, montatura leggera, un paio di scorta per l'auto."),
    'Case is included': ("L'étui est inclus", 'Etui ist dabei', 'La custodia è inclusa'),
    'Hard case in the box. Did not expect that at this price.': (
        "Un étui rigide dans la boîte. Je ne m'y attendais pas à ce prix.",
        'Hartschalenetui in der Box. Damit hatte ich zu dem Preis nicht gerechnet.',
        "Custodia rigida nella scatola. Non me l'aspettavo a questo prezzo."),
    'Light on the ear': ("Légères à l'oreille", 'Leicht am Ohr', "Leggeri all'orecchio"),
    'Hollow hoops, so no drag after a full day.': (
        'Des créoles creuses, donc aucune tension après une journée entière.',
        'Hohle Creolen, also kein Ziehen nach einem ganzen Tag.',
        'Cerchi cavi, quindi nessun peso dopo un giorno intero.'),
    'Broke in fast': ('Vite assouplies', 'Schnell eingelaufen', 'Si sono ammorbidite subito'),
    'Two days and no rubbing. The rubber sole grips well in the rain.': (
        'Deux jours et plus aucun frottement. La semelle en caoutchouc accroche bien sous la pluie.',
        'Zwei Tage und kein Scheuern mehr. Die Gummisohle greift auch im Regen.',
        'Due giorni e niente sfregamento. La suola di gomma tiene bene sotto la pioggia.'),
    'Runs half a size big': ('Taille une demi-pointure au-dessus', 'Fällt eine halbe Nummer größer aus', 'Veste mezza taglia in più'),
    'Great shoe, order half a size down. The white stays white with a wipe.': (
        'Très bonne chaussure, prenez une demi-pointure en dessous. Le blanc reste blanc avec un coup de chiffon.',
        'Toller Schuh, eine halbe Nummer kleiner bestellen. Das Weiß bleibt weiß, ein Wischen reicht.',
        'Ottima scarpa, ordina mezza taglia in meno. Il bianco resta bianco con una passata.'),
    'Elastic is strong': ("L'élastique tient bien", 'Das Gummi hält', "L'elastico tiene"),
    'Slip on, slip off, and the elastic has not sagged after a winter.': (
        "On les enfile, on les enlève, et l'élastique n'a pas cédé après un hiver.",
        'Reinschlüpfen, rausschlüpfen, und das Gummi ist nach einem Winter nicht ausgeleiert.',
        "Si infilano, si sfilano, e l'elastico non ha ceduto dopo un inverno."),
    'Carries a laptop': ('Il porte un ordinateur portable', 'Trägt einen Laptop', 'Porta un portatile'),
    'Fifteen inch laptop, a book and lunch. The straps do not dig in.': (
        'Un portable de quinze pouces, un livre et le déjeuner. Les bretelles ne rentrent pas dans les épaules.',
        'Fünfzehn-Zoll-Laptop, ein Buch und das Mittagessen. Die Gurte schneiden nicht ein.',
        'Portatile da quindici pollici, un libro e il pranzo. Gli spallacci non segnano.'),
    'Canvas is thick': ('La toile est épaisse', 'Das Segeltuch ist dick', 'La tela è spessa'),
    'Stands up on its own. Wish it had an inside pocket.': (
        'Il tient debout tout seul. Il manque juste une poche intérieure.',
        'Steht von allein. Eine Innentasche fehlt mir.',
        'Sta in piedi da sola. Le manca una tasca interna.'),

    # Electronics
    'Does what the chart says': ('Conforme à la fiche technique', 'Macht, was das Diagramm sagt', 'Fa quello che dice la scheda'),
    'The measurements matched what I heard. Rare honesty.': (
        "Les mesures correspondaient à ce que j'entendais. Une honnêteté rare.",
        'Die Messwerte passten zu dem, was ich gehört habe. Seltene Ehrlichkeit.',
        'Le misure corrispondevano a quello che ho sentito. Onestà rara.'),
    'Solid, a bit pricey': ('Solide, un peu cher', 'Solide, etwas teuer', "Robusto, un po' caro"),
    'Great build. You pay for the testing, and it shows.': (
        'Très bonne fabrication. On paie les tests, et cela se voit.',
        'Sehr gute Verarbeitung. Man bezahlt die Tests, und das sieht man.',
        'Ottima costruzione. Si paga il collaudo, e si vede.'),
    'Fast delivery, no fuss': ('Livraison rapide, sans histoires', 'Schnelle Lieferung, ohne Umstände', 'Consegna veloce, senza problemi'),
    'Arrived next day, double boxed. Works perfectly.': (
        'Arrivé le lendemain, en double carton. Fonctionne parfaitement.',
        'Am nächsten Tag da, doppelt verpackt. Funktioniert einwandfrei.',
        'Arrivato il giorno dopo, in doppia scatola. Funziona perfettamente.'),
    'Replaced under warranty': ('Remplacé sous garantie', 'Auf Garantie ersetzt', 'Sostituito in garanzia'),
    'A port failed after a year. New unit in three days.': (
        'Un port est tombé en panne après un an. Nouvel appareil en trois jours.',
        'Ein Anschluss fiel nach einem Jahr aus. Neues Gerät in drei Tagen.',
        'Una porta si è guastata dopo un anno. Unità nuova in tre giorni.'),
    'Battery lasts all week': ('La batterie tient la semaine', 'Der Akku hält die ganze Woche', 'La batteria dura tutta la settimana'),
    'Charged on Sunday, still going Friday night.': (
        'Chargé le dimanche, encore en marche le vendredi soir.',
        'Am Sonntag geladen, am Freitagabend läuft er noch.',
        'Caricato domenica, ancora acceso venerdì sera.'),
    'Firmware update fixed it': ('La mise à jour a réglé le problème', 'Das Firmware-Update hat es behoben', "L'aggiornamento ha risolto"),
    'Dropouts at first. One update later, rock solid.': (
        'Des coupures au début. Une mise à jour plus tard, tout est stable.',
        'Zuerst Aussetzer. Ein Update später, absolut stabil.',
        "Interruzioni all'inizio. Un aggiornamento dopo, stabilissimo."),
    'Cable is too short': ('Le câble est trop court', 'Das Kabel ist zu kurz', 'Il cavo è troppo corto'),
    'Great device, but the included cable is a metre. Buy a longer one.': (
        "Très bon appareil, mais le câble fourni fait un mètre. Achetez-en un plus long.",
        'Sehr gutes Gerät, aber das mitgelieferte Kabel ist einen Meter lang. Kaufen Sie ein längeres.',
        'Ottimo dispositivo, ma il cavo incluso è di un metro. Comprane uno più lungo.'),
    'Clear mids': ('Des médiums nets', 'Klare Mitten', 'Medi puliti'),
    'Vocals sit where they should. Bass is honest, not boosted.': (
        'Les voix sont à leur place. Les basses sont justes, pas gonflées.',
        'Stimmen sitzen dort, wo sie hingehören. Der Bass ist ehrlich, nicht aufgeblasen.',
        'Le voci stanno dove devono. I bassi sono onesti, non gonfiati.'),
    'No app needed': ("Pas besoin d'application", 'Keine App nötig', 'Nessuna app necessaria'),
    'Everything works with a button. My parents could use it.': (
        "Tout marche avec un bouton. Mes parents sauraient s'en servir.",
        'Alles funktioniert über einen Knopf. Meine Eltern könnten es bedienen.',
        'Tutto funziona con un pulsante. I miei genitori saprebbero usarlo.'),
    'Runs warm': ('Il chauffe', 'Wird warm', 'Si scalda'),
    'Works fine but gets warm under load. Give it some air.': (
        "Il fonctionne bien mais chauffe en charge. Laissez-lui de l'air.",
        'Läuft gut, wird aber unter Last warm. Lassen Sie ihm Luft.',
        'Funziona bene ma si scalda sotto carico. Lasciagli aria.'),
    'Quiet fan': ('Ventilateur silencieux', 'Leiser Lüfter', 'Ventola silenziosa'),
    'I forgot it was on. That is the highest praise for a fan.': (
        "J'ai oublié qu'il était allumé. C'est le plus beau compliment pour un ventilateur.",
        'Ich habe vergessen, dass er an war. Das ist das größte Lob für einen Lüfter.',
        'Mi ero dimenticato che era acceso. È il complimento più bello per una ventola.'),
    'Case is metal': ('Le boîtier est en métal', 'Das Gehäuse ist aus Metall', 'La scocca è in metallo'),
    'Real aluminium, not painted plastic. Feels like it will last.': (
        "Du vrai aluminium, pas du plastique peint. On sent que cela va durer.",
        'Echtes Aluminium, kein lackiertes Plastik. Man merkt, dass es hält.',
        'Vero alluminio, non plastica verniciata. Si sente che durerà.'),
    'Pairing was instant': ('Appairage immédiat', 'Kopplung war sofort da', 'Abbinamento immediato'),
    'Open the lid, tap once, done.': (
        "On ouvre le couvercle, on touche une fois, c'est fait.",
        'Deckel öffnen, einmal tippen, fertig.',
        'Apri il coperchio, tocchi una volta, fatto.'),
    'Wish it had USB-C': ('Dommage, pas de USB-C', 'Schade, kein USB-C', 'Peccato, niente USB-C'),
    'Everything else is right. The port is from another decade.': (
        "Tout le reste est juste. Le port vient d'une autre décennie.",
        'Alles andere stimmt. Der Anschluss stammt aus einem anderen Jahrzehnt.',
        "Tutto il resto va bene. La porta viene da un altro decennio."),
    'Great for calls': ('Parfait pour les appels', 'Super für Anrufe', 'Ottimo per le chiamate'),
    'Colleagues stopped asking me to repeat myself.': (
        'Mes collègues ne me demandent plus de répéter.',
        'Die Kollegen bitten mich nicht mehr, mich zu wiederholen.',
        'I colleghi non mi chiedono più di ripetere.'),
    'Speaker fills the room': ("L'enceinte remplit la pièce", 'Der Lautsprecher füllt den Raum', 'Lo speaker riempie la stanza'),
    'Small box, big sound. Party volume without distortion.': (
        "Petite boîte, grand son. Le volume d'une fête sans distorsion.",
        'Kleine Box, großer Klang. Partylautstärke ohne Verzerrung.',
        'Scatola piccola, suono grande. Volume da festa senza distorsione.'),
    'Manual is thin': ('Le manuel est maigre', 'Die Anleitung ist dünn', 'Il manuale è scarno'),
    'Works well, but I had to search online for the settings.': (
        "Il marche bien, mais j'ai dû chercher les réglages en ligne.",
        'Funktioniert gut, aber die Einstellungen musste ich online suchen.',
        'Funziona bene, ma ho dovuto cercare le impostazioni online.'),
    'Lens is sharp corner to corner': ("L'objectif est net d'un bord à l'autre", 'Das Objektiv ist bis in die Ecken scharf', "L'obiettivo è nitido da un angolo all'altro"),
    'Tested on a brick wall like a nerd. It passes.': (
        "Testé sur un mur de briques, comme un passionné. Il passe l'examen.",
        'Wie ein Nerd an einer Ziegelwand getestet. Es besteht.',
        'Provato su un muro di mattoni come un patito. Promosso.'),
    'Returned, wrong size': ('Retourné, mauvaise taille', 'Zurückgeschickt, falsche Größe', 'Reso, taglia sbagliata'),
    'My fault, the spec sheet was clear. Return was painless.': (
        'De ma faute, la fiche technique était claire. Le retour a été simple.',
        'Mein Fehler, das Datenblatt war klar. Die Rückgabe war problemlos.',
        'Colpa mia, la scheda era chiara. Il reso è stato semplice.'),
    'Charges the laptop too': ('Il charge aussi le portable', 'Lädt auch den Laptop', 'Carica anche il portatile'),
    'One cable for everything on the desk now.': (
        'Un seul câble pour tout ce qui est sur le bureau.',
        'Jetzt ein Kabel für alles auf dem Schreibtisch.',
        'Ora un solo cavo per tutto quello che sta sulla scrivania.'),
    'Slight hiss at idle': ('Un léger souffle au repos', 'Leichtes Rauschen im Leerlauf', 'Un leggero fruscio a riposo'),
    'Only with sensitive earphones and at full gain. Fine otherwise.': (
        'Seulement avec des écouteurs sensibles et à plein gain. Sinon, parfait.',
        'Nur mit empfindlichen Ohrhörern und bei voller Verstärkung. Sonst gut.',
        'Solo con auricolari sensibili e a guadagno massimo. Per il resto va bene.'),
    'Bought two': ('J\'en ai acheté deux', 'Zwei gekauft', 'Ne ho presi due'),
    'One for the office, one for home. No regrets.': (
        'Un pour le bureau, un pour la maison. Aucun regret.',
        'Einen fürs Büro, einen für zu Hause. Keine Reue.',
        'Uno per l\'ufficio, uno per casa. Nessun rimpianto.'),
    'Buttons feel cheap': ('Les boutons font bon marché', 'Die Knöpfe wirken billig', 'I pulsanti sembrano economici'),
    'Sound is great, the plastic buttons are not.': (
        'Le son est excellent, les boutons en plastique non.',
        'Der Klang ist super, die Plastikknöpfe nicht.',
        'Il suono è ottimo, i pulsanti di plastica no.'),
    'Setup took five minutes': ('Installation en cinq minutes', 'Einrichtung dauerte fünf Minuten', 'Configurazione in cinque minuti'),
    'Plugged in, updated, done before the coffee was ready.': (
        'Branché, mis à jour, terminé avant que le café soit prêt.',
        'Eingesteckt, aktualisiert, fertig, bevor der Kaffee durch war.',
        'Collegato, aggiornato, finito prima che il caffè fosse pronto.'),

    # Food
    'Tastes like the real thing': ('Le goût du vrai', 'Schmeckt nach dem Echten', 'Sa di vero'),
    'Bright, fresh and clearly made in small batches. Will reorder.': (
        'Vif, frais et clairement fait en petites quantités. Je recommanderai.',
        'Frisch, lebendig und klar in kleinen Mengen gemacht. Ich bestelle wieder.',
        'Vivo, fresco e chiaramente fatto in piccole quantità. Ordinerò ancora.'),
    'Good, a little pricey': ('Bon, un peu cher', 'Gut, etwas teuer', "Buono, un po' caro"),
    'Quality is there, but you pay for it. Worth it for a weekend.': (
        'La qualité est là, mais elle se paie. Cela vaut le coup pour un week-end.',
        'Die Qualität stimmt, aber man zahlt dafür. Für ein Wochenende lohnt es sich.',
        'La qualità c\'è, ma si paga. Ne vale la pena per un fine settimana.'),
    'Arrived cold and fast': ('Arrivé froid et vite', 'Kam kalt und schnell an', 'Arrivato freddo e in fretta'),
    'Packed with ice packs and a note. Everything was perfect.': (
        'Emballé avec des blocs de glace et un mot. Tout était parfait.',
        'Mit Kühlakkus und einer Notiz verpackt. Alles war perfekt.',
        'Imballato con siberini e un biglietto. Tutto perfetto.'),
    'Weekly staple now': ('Un incontournable de la semaine', 'Jetzt ein wöchentlicher Klassiker', 'Ormai un fisso della settimana'),
    'This has replaced the supermarket version in our house.': (
        'Cela a remplacé la version du supermarché chez nous.',
        'Das hat bei uns die Supermarktversion ersetzt.',
        'Ha sostituito la versione del supermercato a casa nostra.'),
    'Peppery finish': ('Une finale poivrée', 'Pfeffriger Abgang', 'Finale pepato'),
    'Green and grassy, with a proper pepper kick at the end.': (
        'Vert et herbacé, avec un vrai coup de poivre à la fin.',
        'Grün und grasig, mit einem echten Pfefferkick am Ende.',
        'Verde ed erbaceo, con una vera spinta di pepe alla fine.'),
    'Bread was still warm': ('Le pain était encore tiède', 'Das Brot war noch warm', 'Il pane era ancora caldo'),
    'Well, almost. Same-day delivery from the oven is a marvel.': (
        'Enfin, presque. La livraison le jour même depuis le four est une merveille.',
        'Naja, fast. Lieferung am selben Tag direkt aus dem Ofen ist ein Wunder.',
        'Beh, quasi. La consegna in giornata dal forno è una meraviglia.'),
    'Jar was half full': ('Le pot était à moitié plein', 'Das Glas war halb voll', 'Il vasetto era mezzo pieno'),
    'Tastes great, but the jar looked short. Check the weight, not the glass.': (
        "C'est très bon, mais le pot semblait peu rempli. Regardez le poids, pas le verre.",
        'Schmeckt super, aber das Glas wirkte knapp gefüllt. Achten Sie auf das Gewicht, nicht auf das Glas.',
        'Buonissimo, ma il vasetto sembrava poco pieno. Guarda il peso, non il vetro.'),
    'Kids ate the crusts': ('Les enfants ont mangé les croûtes', 'Die Kinder haben die Kruste gegessen', 'I bambini hanno mangiato le croste'),
    'That has never happened. Buying every week.': (
        "Cela n'était jamais arrivé. J'en achète toutes les semaines.",
        'Das ist noch nie passiert. Ich kaufe es jede Woche.',
        'Non era mai successo. Lo compro ogni settimana.'),
    'Strong coffee': ('Un café puissant', 'Starker Kaffee', 'Caffè forte'),
    'Dark and chocolatey. Not for people who like it light.': (
        "Foncé et chocolaté. Pas pour ceux qui l'aiment léger.",
        'Dunkel und schokoladig. Nichts für Leute, die es hell mögen.',
        'Scuro e cioccolatoso. Non per chi lo ama leggero.'),
    'Cheese needs a warning': ('Le fromage mérite un avertissement', 'Der Käse braucht eine Warnung', 'Il formaggio merita un avviso'),
    'It is glorious and it stinks out the fridge. Double wrap it.': (
        'Il est magnifique et il empeste le frigo. Emballez-le deux fois.',
        'Er ist herrlich und stinkt den Kühlschrank aus. Doppelt einpacken.',
        'È magnifico e appesta il frigo. Avvolgilo due volte.'),
    'Perfect crate': ('Un coffret parfait', 'Perfekte Kiste', 'Cassetta perfetta'),
    'Sent as a housewarming gift. They messaged me a photo.': (
        "Envoyé comme cadeau de pendaison de crémaillère. Ils m'ont envoyé une photo.",
        'Als Einweihungsgeschenk verschickt. Sie haben mir ein Foto geschickt.',
        'Mandata come regalo per la casa nuova. Mi hanno inviato una foto.'),
    'Too sweet for me': ('Trop sucré pour moi', 'Mir zu süß', 'Troppo dolce per me'),
    'Good quality soda but sweeter than I hoped.': (
        "Un soda de bonne qualité mais plus sucré que je l'espérais.",
        'Gute Limonade, aber süßer als erhofft.',
        'Bibita di buona qualità ma più dolce di quanto sperassi.'),
    'Pasta holds the sauce': ('Les pâtes accrochent la sauce', 'Die Pasta hält die Sauce', 'La pasta tiene il sugo'),
    'Bronze cut, rough surface. The difference is real.': (
        'Tréfilée au bronze, surface rugueuse. La différence est réelle.',
        'Bronzegezogen, raue Oberfläche. Der Unterschied ist echt.',
        'Trafilata al bronzo, superficie ruvida. La differenza è vera.'),
    'Delivery missed the slot': ('La livraison a manqué le créneau', 'Die Lieferung verpasste das Zeitfenster', 'La consegna ha mancato la fascia'),
    'Came a day late. Still cold, still good, but plan a day ahead.': (
        "Arrivé un jour en retard. Toujours froid, toujours bon, mais prévoyez un jour d'avance.",
        'Kam einen Tag zu spät. Immer noch kalt, immer noch gut, aber planen Sie einen Tag Puffer ein.',
        "Arrivato un giorno tardi. Ancora freddo, ancora buono, ma calcola un giorno in più."),
    'Honey is set, not runny': ('Le miel est crémeux, pas liquide', 'Der Honig ist fest, nicht flüssig', 'Il miele è cremoso, non liquido'),
    'Set honey with a floral taste. Spread it thick.': (
        'Un miel crémeux au goût floral. Étalez-le généreusement.',
        'Fester Honig mit blumigem Geschmack. Dick aufstreichen.',
        'Miele cremoso dal gusto floreale. Spalmalo abbondante.'),
    'Breakfast is sorted': ('Le petit-déjeuner est réglé', 'Das Frühstück ist geregelt', 'La colazione è risolta'),
    'Granola, jam and coffee in one order. Mornings are better.': (
        'Granola, confiture et café en une commande. Les matins sont meilleurs.',
        'Granola, Marmelade und Kaffee in einer Bestellung. Die Morgen sind besser.',
        'Granola, marmellata e caffè in un solo ordine. Le mattine sono migliori.'),
    'Cured ham sliced thin': ('Du jambon sec tranché fin', 'Dünn geschnittener Schinken', 'Prosciutto tagliato sottile'),
    'Paper thin and packed flat. Melted on warm bread.': (
        'Fin comme du papier et emballé à plat. Il a fondu sur du pain chaud.',
        'Hauchdünn und flach verpackt. Auf warmem Brot geschmolzen.',
        'Sottile come carta e confezionato piatto. Si è sciolto sul pane caldo.'),
    'Bitter chocolate': ('Un chocolat amer', 'Bittere Schokolade', 'Cioccolato amaro'),
    'Very dark. I like it, my partner does not.': (
        "Très noir. Je l'aime, mon conjoint non.",
        'Sehr dunkel. Mir gefällt sie, meinem Partner nicht.',
        'Molto fondente. A me piace, al mio partner no.'),
    'Great for a picnic': ('Parfait pour un pique-nique', 'Super für ein Picknick', 'Ottimo per un picnic'),
    'Everything travelled well in the crate and the ice lasted.': (
        'Tout a bien voyagé dans le coffret et la glace a tenu.',
        'Alles hat die Reise in der Kiste gut überstanden und das Eis hielt.',
        'Tutto ha viaggiato bene nella cassetta e il ghiaccio ha tenuto.'),
    'Tea is fragrant': ('Un thé parfumé', 'Der Tee duftet', 'Il tè è profumato'),
    'Loose leaf, big leaves, three steeps from one spoon.': (
        'En vrac, grandes feuilles, trois infusions avec une cuillère.',
        'Lose, große Blätter, drei Aufgüsse aus einem Löffel.',
        'Sfuso, foglie grandi, tre infusioni da un cucchiaio.'),
    'Wine surprised me': ("Le vin m'a surpris", 'Der Wein hat mich überrascht', 'Il vino mi ha sorpreso'),
    'Did not know the producer. Now I do.': (
        'Je ne connaissais pas le producteur. Maintenant si.',
        'Ich kannte den Erzeuger nicht. Jetzt schon.',
        'Non conoscevo il produttore. Ora sì.'),
    'Portion is small': ('La portion est petite', 'Die Portion ist klein', 'La porzione è piccola'),
    'Delicious, but two people finished it in one go.': (
        "Délicieux, mais à deux nous l'avons fini d'un coup.",
        'Köstlich, aber zu zweit war es in einem Zug weg.',
        'Delizioso, ma in due lo abbiamo finito in una volta.'),
    'Olive oil for cooking too': ("De l'huile d'olive pour la cuisson aussi", 'Olivenöl auch zum Kochen', "Olio d'oliva anche per cucinare"),
    'I bought the litre for the pan and the small bottle for salads.': (
        "J'ai pris le litre pour la poêle et la petite bouteille pour les salades.",
        'Ich habe den Liter für die Pfanne und die kleine Flasche für Salate gekauft.',
        'Ho preso il litro per la padella e la bottiglietta per le insalate.'),
    'Repeat order': ('Nouvelle commande', 'Nachbestellung', 'Riordino'),
    'Third crate. The team remembers the note about no nuts.': (
        "Troisième coffret. L'équipe se souvient de la note sans fruits à coque.",
        'Dritte Kiste. Das Team erinnert sich an die Notiz ohne Nüsse.',
        'Terza cassetta. Il team ricorda la nota senza frutta secca.'),

    # Books
    'Could not put it down': ('Impossible de le lâcher', 'Konnte es nicht weglegen', 'Non riuscivo a smettere'),
    'Finished it in two nights. The recommendation was spot on.': (
        'Fini en deux soirées. Le conseil était juste.',
        'In zwei Nächten durch. Die Empfehlung saß.',
        'Finito in due sere. Il consiglio era azzeccato.'),
    'Good, not great': ('Bien, sans plus', 'Gut, nicht großartig', 'Buono, non ottimo'),
    'Well written but slow in the middle. Lovely edition though.': (
        'Bien écrit mais lent au milieu. Belle édition cependant.',
        'Gut geschrieben, aber in der Mitte zäh. Schöne Ausgabe allerdings.',
        'Ben scritto ma lento a metà. Bella edizione però.'),
    'Beautiful edition': ('Une belle édition', 'Schöne Ausgabe', 'Bella edizione'),
    'Clothbound, good paper, lies flat. A pleasure to hold.': (
        "Relié toile, beau papier, il reste ouvert à plat. Un plaisir à tenir.",
        'Leineneinband, gutes Papier, liegt flach. Eine Freude in der Hand.',
        'Rilegato in tela, carta buona, resta aperto. Un piacere da tenere.'),
    'Perfect gift': ('Le cadeau parfait', 'Perfektes Geschenk', 'Regalo perfetto'),
    'Wrapped beautifully and arrived in two days.': (
        'Emballé avec soin et arrivé en deux jours.',
        'Schön verpackt und in zwei Tagen da.',
        'Confezionato con cura e arrivato in due giorni.'),
    'Ribbon marker': ('Le signet ruban', 'Das Lesebändchen', 'Il segnalibro in raso'),
    'Small thing, but the ribbon marker and the sewn binding made my week.': (
        'Un détail, mais le signet ruban et la reliure cousue ont fait ma semaine.',
        'Eine Kleinigkeit, aber das Lesebändchen und die Fadenbindung haben meine Woche gerettet.',
        'Un dettaglio, ma il segnalibro e la rilegatura cucita mi hanno fatto la settimana.'),
    'Print is small': ('Les caractères sont petits', 'Die Schrift ist klein', 'I caratteri sono piccoli'),
    'Fine story, but the type is small and the margins are tight.': (
        'Bonne histoire, mais les caractères sont petits et les marges serrées.',
        'Gute Geschichte, aber die Schrift ist klein und die Ränder sind eng.',
        'Bella storia, ma i caratteri sono piccoli e i margini stretti.'),
    'Read it twice': ('Lu deux fois', 'Zweimal gelesen', 'Letto due volte'),
    'The ending sent me back to page one. Rare.': (
        "La fin m'a renvoyé à la première page. C'est rare.",
        'Das Ende hat mich zurück auf Seite eins geschickt. Selten.',
        'Il finale mi ha rimandato a pagina uno. Raro.'),
    'Arrived with a dented corner': ('Arrivé avec un coin abîmé', 'Kam mit einer gestoßenen Ecke an', 'Arrivato con un angolo ammaccato'),
    'Packaging was thin. The book is fine, the corner is not.': (
        "L'emballage était léger. Le livre va bien, le coin non.",
        'Die Verpackung war dünn. Das Buch ist in Ordnung, die Ecke nicht.',
        "L'imballaggio era leggero. Il libro sta bene, l'angolo no."),
    'Great translation': ('Une excellente traduction', 'Großartige Übersetzung', 'Ottima traduzione'),
    'Reads like it was written in English. No awkward sentences.': (
        'On dirait un texte écrit en français. Aucune phrase bancale.',
        'Liest sich, als wäre es auf Deutsch geschrieben. Keine holprigen Sätze.',
        'Si legge come se fosse stato scritto in italiano. Nessuna frase storta.'),
    'Big for the shelf': ("Grand pour l'étagère", 'Groß für das Regal', 'Grande per lo scaffale'),
    'Larger format than expected. Check the dimensions.': (
        'Format plus grand que prévu. Vérifiez les dimensions.',
        'Größeres Format als erwartet. Prüfen Sie die Maße.',
        'Formato più grande del previsto. Controlla le dimensioni.'),
    'The maps alone': ('Rien que pour les cartes', 'Allein die Karten', 'Solo per le mappe'),
    'The endpaper maps are worth the price. The story is a bonus.': (
        "Les cartes des pages de garde valent le prix. L'histoire est un bonus.",
        'Die Karten auf dem Vorsatzpapier sind den Preis wert. Die Geschichte ist ein Bonus.',
        'Le mappe sui risguardi valgono il prezzo. La storia è un regalo in più.'),
    'Not for beginners': ('Pas pour débuter', 'Nichts für Anfänger', 'Non per principianti'),
    'Dense and rewarding, but start elsewhere if you are new to the subject.': (
        'Dense et gratifiant, mais commencez ailleurs si le sujet est nouveau pour vous.',
        'Dicht und lohnend, aber fangen Sie woanders an, wenn das Thema neu für Sie ist.',
        "Denso e appagante, ma inizia da altro se l'argomento è nuovo per te."),
    'Paperback is sturdy': ('Un broché solide', 'Das Taschenbuch ist stabil', 'La brossura è robusta'),
    'Flexible cover, opens flat, survived a beach week.': (
        "Couverture souple, il s'ouvre à plat, il a survécu à une semaine de plage.",
        'Flexibler Einband, öffnet flach, hat eine Strandwoche überstanden.',
        'Copertina flessibile, si apre piatto, ha resistito a una settimana in spiaggia.'),
    'Half the price elsewhere': ('Moitié prix ailleurs', 'Woanders halb so teuer', 'Metà prezzo altrove'),
    'Beautiful shop, but I found the same edition cheaper.': (
        "Belle boutique, mais j'ai trouvé la même édition moins chère.",
        'Schöner Laden, aber ich habe dieselbe Ausgabe günstiger gefunden.',
        'Bel negozio, ma ho trovato la stessa edizione a meno.'),
    'Signed copy': ('Un exemplaire signé', 'Signiertes Exemplar', 'Copia firmata'),
    'I did not expect the signature on the title page. Delighted.': (
        "Je ne m'attendais pas à la signature sur la page de titre. Ravi.",
        'Mit der Signatur auf der Titelseite hatte ich nicht gerechnet. Begeistert.',
        'Non mi aspettavo la firma sul frontespizio. Felicissimo.'),
    'Slow start, strong finish': ('Départ lent, belle fin', 'Langsamer Start, starkes Ende', 'Inizio lento, finale forte'),
    'Give it fifty pages. Then you will not stop.': (
        'Donnez-lui cinquante pages. Ensuite vous ne vous arrêterez plus.',
        'Geben Sie ihm fünfzig Seiten. Danach hören Sie nicht mehr auf.',
        'Dagli cinquanta pagine. Poi non ti fermi più.'),
    'Kids loved it': ('Les enfants ont adoré', 'Die Kinder liebten es', 'Ai bambini è piaciuto'),
    'Read aloud three nights running. The pictures hold up to a torch.': (
        'Lu à voix haute trois soirs de suite. Les images tiennent même à la lampe de poche.',
        'Drei Abende hintereinander vorgelesen. Die Bilder halten auch dem Taschenlampenlicht stand.',
        'Letto ad alta voce tre sere di fila. Le figure reggono anche alla torcia.'),
    'Index is excellent': ("L'index est excellent", 'Das Register ist ausgezeichnet', "L'indice è ottimo"),
    'For a reference book, the index is what matters, and this one is thorough.': (
        "Pour un ouvrage de référence, c'est l'index qui compte, et celui-ci est complet.",
        'Bei einem Nachschlagewerk zählt das Register, und dieses ist gründlich.',
        "In un'opera di consultazione conta l'indice, e questo è completo."),
    'Smells like a bookshop': ('Il sent la librairie', 'Riecht wie eine Buchhandlung', 'Profuma di libreria'),
    'Uncoated paper, sewn spine. Old fashioned in the best way.': (
        'Papier non couché, dos cousu. Vieille école, dans le bon sens.',
        'Ungestrichenes Papier, gehefteter Rücken. Altmodisch im besten Sinn.',
        "Carta non patinata, dorso cucito. All'antica, nel senso migliore."),
    'Too short': ('Trop court', 'Zu kurz', 'Troppo corto'),
    'Loved every page, wanted a hundred more.': (
        "J'ai aimé chaque page, j'en voulais cent de plus.",
        'Ich habe jede Seite geliebt und wollte hundert mehr.',
        'Ho amato ogni pagina, ne volevo cento in più.'),
    'Second volume please': ("Un deuxième tome, s'il vous plaît", 'Bitte einen zweiten Band', 'Un secondo volume, per favore'),
    'Ends on a cliff. Hoping the next one is on its way.': (
        "Il se termine en suspens. J'espère que la suite arrive.",
        'Endet an einer Klippe. Ich hoffe, der nächste ist unterwegs.',
        'Finisce in sospeso. Spero che il prossimo sia in arrivo.'),
    'Good notes': ('De bonnes notes', 'Gute Anmerkungen', 'Buone note'),
    'The introduction and notes add context without getting in the way.': (
        "L'introduction et les notes ajoutent du contexte sans gêner.",
        'Einleitung und Anmerkungen geben Kontext, ohne zu stören.',
        "L'introduzione e le note danno contesto senza disturbare."),

    # Jewelry
    'Delicate and well made': ('Délicat et bien fait', 'Zart und gut gemacht', 'Delicato e ben fatto'),
    'Finer than the photos suggest, in a good way. The finish is flawless.': (
        'Plus fin que sur les photos, dans le bon sens. La finition est impeccable.',
        'Feiner als die Fotos vermuten lassen, im positiven Sinn. Die Verarbeitung ist makellos.',
        'Più fine di quanto suggeriscano le foto, in senso buono. La finitura è impeccabile.'),
    'Lovely, a little small': ('Joli, un peu petit', 'Schön, etwas klein', "Bello, un po' piccolo"),
    'Beautiful piece. The pendant is smaller than I expected, so check the size.': (
        'Belle pièce. Le pendentif est plus petit que prévu, vérifiez la taille.',
        'Schönes Stück. Der Anhänger ist kleiner als erwartet, prüfen Sie die Größe.',
        'Bel pezzo. Il pendente è più piccolo del previsto, controlla la misura.'),
    'The box and the handwritten card made it. She cried.': (
        'La boîte et la carte écrite à la main ont tout fait. Elle a pleuré.',
        'Die Schachtel und die handgeschriebene Karte haben es ausgemacht. Sie hat geweint.',
        'La scatola e il biglietto scritto a mano hanno fatto tutto. Ha pianto.'),
    'Worn every day': ('Porté tous les jours', 'Jeden Tag getragen', 'Portato ogni giorno'),
    'Six months in, no tarnish, no loose stone.': (
        'Six mois plus tard, aucun ternissement, aucune pierre qui bouge.',
        'Nach sechs Monaten kein Anlaufen, kein loser Stein.',
        'Dopo sei mesi nessuna opacità, nessuna pietra allentata.'),
    'Clasp is secure': ('Le fermoir tient bien', 'Der Verschluss hält sicher', 'La chiusura tiene'),
    'Lobster clasp with a proper spring. Never opened by itself.': (
        "Fermoir mousqueton avec un vrai ressort. Il ne s'est jamais ouvert seul.",
        'Karabinerverschluss mit richtiger Feder. Er hat sich nie von selbst geöffnet.',
        'Chiusura a moschettone con una vera molla. Non si è mai aperta da sola.'),
    'Resized for free': ('Mis à la taille gratuitement', 'Kostenlos geweitet', 'Ridimensionato gratis'),
    'Half a size out. Sent back, resized, returned within a week.': (
        'Une demi-taille de trop. Renvoyé, ajusté, revenu en une semaine.',
        'Eine halbe Größe daneben. Zurückgeschickt, angepasst, in einer Woche wieder da.',
        'Mezza misura di troppo. Rispedito, ridimensionato, tornato in una settimana.'),
    'Catches the light': ('Il accroche la lumière', 'Fängt das Licht ein', 'Prende la luce'),
    'The stone sparkles under office lights. Colleagues noticed.': (
        "La pierre brille sous les néons du bureau. Mes collègues l'ont remarqué.",
        'Der Stein funkelt im Bürolicht. Die Kollegen haben es bemerkt.',
        "La pietra brilla sotto le luci dell'ufficio. I colleghi lo hanno notato."),
    'Chain is fine': ('La chaîne est fine', 'Die Kette ist fein', 'La catena è sottile'),
    'Beautiful but very fine. I take it off for the gym.': (
        "Belle mais très fine. Je l'enlève pour la salle.",
        'Schön, aber sehr fein. Fürs Studio nehme ich sie ab.',
        'Bella ma molto sottile. La tolgo per la palestra.'),
    'Stacks well': ("Elles s'empilent bien", 'Lässt sich gut stapeln', 'Si abbinano bene'),
    'Three thin rings, worn together. That was the plan and it works.': (
        "Trois anneaux fins, portés ensemble. C'était le plan et cela marche.",
        'Drei schmale Ringe, zusammen getragen. Das war der Plan und er geht auf.',
        'Tre anelli sottili, portati insieme. Era il piano e funziona.'),
    'Earring back is tiny': ('Le poussoir est minuscule', 'Der Verschluss ist winzig', 'Il fermaglio è minuscolo'),
    'Lovely hoops but the backs are small and easy to drop.': (
        'De jolies créoles mais les poussoirs sont petits et faciles à perdre.',
        'Schöne Creolen, aber die Verschlüsse sind klein und fallen leicht herunter.',
        'Bei cerchi ma i fermagli sono piccoli e cadono facilmente.'),
    'Solid gold, not plated': ("De l'or massif, pas du plaqué", 'Massives Gold, nicht vergoldet', 'Oro massiccio, non placcato'),
    'You can feel the weight. Worth every penny.': (
        'On sent le poids. Cela vaut chaque centime.',
        'Man spürt das Gewicht. Jeden Cent wert.',
        'Si sente il peso. Vale ogni centesimo.'),
    'Slight scratch on the band': ("Une légère rayure sur l'anneau", 'Leichter Kratzer am Ring', 'Un leggero graffio sulla fascia'),
    'Hairline mark out of the box. Polished it out myself.': (
        "Une marque fine à la sortie de la boîte. Je l'ai polie moi-même.",
        'Haarfeiner Kratzer direkt aus der Schachtel. Ich habe ihn selbst herauspoliert.',
        "Un segno sottilissimo appena tolto dalla scatola. L'ho lucidato da solo."),
    'Pearls are matched': ('Des perles assorties', 'Die Perlen sind abgestimmt', 'Perle abbinate'),
    'Same size, same lustre, well knotted between each.': (
        'Même taille, même éclat, bien nouées entre elles.',
        'Gleiche Größe, gleicher Glanz, sauber zwischen jeder geknotet.',
        'Stessa misura, stessa lucentezza, ben annodate una a una.'),
    'Fits the wrist': ('Il va bien au poignet', 'Passt ans Handgelenk', 'Sta bene al polso'),
    'Cuff opens just enough. Stays put all day.': (
        "Le jonc s'ouvre juste ce qu'il faut. Il tient toute la journée.",
        'Der Armreif öffnet sich gerade genug. Sitzt den ganzen Tag.',
        'Il bracciale si apre quanto basta. Resta al suo posto tutto il giorno.'),
    'Ring box is lovely': ("L'écrin est très beau", 'Die Ringschachtel ist schön', "La scatola dell'anello è bella"),
    'The linen box is a keepsake on its own.': (
        'La boîte en lin est un souvenir à elle seule.',
        'Die Leinenschachtel ist für sich schon ein Andenken.',
        'La scatola di lino è già di per sé un ricordo.'),
    'Wanted it bigger': ("Je l'aurais voulu plus grand", 'Hätte es größer gewollt', 'Lo volevo più grande'),
    'Beautiful stone, smaller than the photo led me to expect.': (
        'Belle pierre, plus petite que ce que la photo laissait croire.',
        'Schöner Stein, kleiner als das Foto erwarten ließ.',
        'Bella pietra, più piccola di quanto lasciasse pensare la foto.'),
    'No green finger': ('Pas de doigt vert', 'Kein grüner Finger', 'Nessun alone verde'),
    'A month of daily wear, no mark on the skin.': (
        'Un mois de port quotidien, aucune marque sur la peau.',
        'Einen Monat täglich getragen, keine Spur auf der Haut.',
        'Un mese di uso quotidiano, nessun segno sulla pelle.'),
    'Engraving is crisp': ('La gravure est nette', 'Die Gravur ist sauber', "L'incisione è netta"),
    'Two initials and a date, clean and even.': (
        'Deux initiales et une date, propres et régulières.',
        'Zwei Initialen und ein Datum, sauber und gleichmäßig.',
        'Due iniziali e una data, pulite e regolari.'),
    'Bought a second for my sister': ("J'en ai acheté un deuxième pour ma sœur", 'Ein zweites für meine Schwester gekauft', 'Ne ho preso un secondo per mia sorella'),
    'She saw mine and now we match.': (
        'Elle a vu le mien et maintenant nous sommes assorties.',
        'Sie hat meins gesehen und jetzt tragen wir dasselbe.',
        'Ha visto il mio e ora siamo uguali.'),
    'Post is short': ('La tige est courte', 'Der Stift ist kurz', 'Il perno è corto'),
    'Stud sits close to the ear, which I like. Bigger lobes may want longer posts.': (
        "La puce est près de l'oreille, ce que j'aime. Les lobes plus épais voudront des tiges plus longues.",
        'Der Stecker sitzt nah am Ohr, was mir gefällt. Größere Ohrläppchen brauchen längere Stifte.',
        "Il punto luce sta vicino all'orecchio, cosa che mi piace. Lobi più grandi vorranno perni più lunghi."),
    'Came with a cloth': ('Livré avec un chiffon', 'Kam mit einem Tuch', 'Arrivato con un panno'),
    'Polishing cloth and care notes in the box. Thoughtful.': (
        "Un chiffon de polissage et des conseils d'entretien dans la boîte. Bien pensé.",
        'Poliertuch und Pflegehinweise in der Schachtel. Aufmerksam.',
        'Panno per lucidare e istruzioni di cura nella scatola. Premuroso.'),

    # Beauty
    'Gentle and it works': ('Doux et efficace', 'Sanft und es wirkt', 'Delicato e funziona'),
    'No stinging, no fragrance, and my skin is calmer after two weeks.': (
        'Aucun picotement, aucun parfum, et ma peau est plus calme après deux semaines.',
        'Kein Brennen, kein Duft, und meine Haut ist nach zwei Wochen ruhiger.',
        'Nessun bruciore, nessun profumo, e la mia pelle è più calma dopo due settimane.'),
    'Nice but small': ('Bien mais petit', 'Schön, aber klein', 'Bello ma piccolo'),
    'Lovely texture. The jar is smaller than it looks, so watch the volume.': (
        "Belle texture. Le pot est plus petit qu'il n'y paraît, regardez le volume.",
        'Schöne Textur. Der Tiegel ist kleiner, als er aussieht, achten Sie auf die Menge.',
        'Bella texture. Il vasetto è più piccolo di quanto sembri, guarda il volume.'),
    'Refill is a great idea': ('La recharge est une bonne idée', 'Nachfüllen ist eine gute Idee', 'La ricarica è una bella idea'),
    'Bought the glass once, now I refill. Cheaper and less waste.': (
        "J'ai acheté le verre une fois, maintenant je recharge. Moins cher et moins de déchets.",
        'Das Glas einmal gekauft, jetzt fülle ich nach. Günstiger und weniger Müll.',
        'Ho comprato il vetro una volta, ora ricarico. Costa meno e si spreca meno.'),
    'My holy grail': ('Mon indispensable', 'Mein Must-have', 'Il mio irrinunciabile'),
    'Third jar. Nothing else has replaced it.': (
        "Troisième pot. Rien ne l'a remplacé.",
        'Dritter Tiegel. Nichts hat ihn ersetzt.',
        'Terzo vasetto. Niente lo ha sostituito.'),
    'Sinks in fast': ('Il pénètre vite', 'Zieht schnell ein', 'Si assorbe in fretta'),
    'No greasy film, makeup goes on top after a minute.': (
        'Aucun film gras, le maquillage passe par-dessus après une minute.',
        'Kein fettiger Film, Make-up kommt nach einer Minute darüber.',
        'Nessuna pellicola grassa, il trucco va sopra dopo un minuto.'),
    'Took a month to see it': ("Il a fallu un mois pour le voir", 'Es hat einen Monat gedauert', 'Ci è voluto un mese per vederlo'),
    'Patience needed. Around week four the texture of my skin changed.': (
        'Il faut de la patience. Vers la quatrième semaine, la texture de ma peau a changé.',
        'Geduld ist nötig. Etwa in Woche vier hat sich die Struktur meiner Haut verändert.',
        'Serve pazienza. Verso la quarta settimana la texture della mia pelle è cambiata.'),
    'Smells like nothing': ('Il ne sent rien', 'Riecht nach nichts', 'Non profuma di niente'),
    'Which is exactly what I wanted for reactive skin.': (
        "C'est exactement ce que je voulais pour une peau réactive.",
        'Genau das wollte ich für empfindliche Haut.',
        'Che è esattamente quello che volevo per una pelle reattiva.'),
    'Pump broke': ('La pompe a cassé', 'Die Pumpe ist kaputtgegangen', 'La pompetta si è rotta'),
    'The formula is great, the pump stopped after a month. Support sent a new one.': (
        "La formule est excellente, la pompe s'est arrêtée après un mois. Le service m'en a envoyé une neuve.",
        'Die Formel ist super, die Pumpe hat nach einem Monat aufgehört. Der Support hat eine neue geschickt.',
        "La formula è ottima, la pompetta si è fermata dopo un mese. L'assistenza me ne ha mandata una nuova."),
    'Good for oily skin': ('Bien pour les peaux grasses', 'Gut für fettige Haut', 'Buono per la pelle grassa'),
    'Matte finish without tightness. My afternoon shine is gone.': (
        "Fini mat sans tiraillement. Mes brillances de l'après-midi ont disparu.",
        'Mattes Finish ohne Spannen. Mein Glanz am Nachmittag ist weg.',
        'Finish opaco senza pelle tirata. La lucidità del pomeriggio è sparita.'),
    'Too rich for me': ('Trop riche pour moi', 'Mir zu reichhaltig', 'Troppo ricco per me'),
    'Beautiful for dry skin I am sure, too heavy for my combination skin.': (
        "Parfait pour une peau sèche j'en suis sûre, trop lourd pour ma peau mixte.",
        'Für trockene Haut sicher wunderbar, für meine Mischhaut zu schwer.',
        'Perfetto per la pelle secca ne sono certa, troppo pesante per la mia pelle mista.'),
    'Travel size please': ("Un format voyage, s'il vous plaît", 'Bitte eine Reisegröße', 'Un formato da viaggio, per favore'),
    'I love it but the bottle is too big for a carry-on.': (
        "Je l'adore mais le flacon est trop grand pour un bagage cabine.",
        'Ich liebe es, aber die Flasche ist zu groß fürs Handgepäck.',
        'Lo adoro ma il flacone è troppo grande per il bagaglio a mano.'),
    'Replaced three products': ('Il a remplacé trois produits', 'Hat drei Produkte ersetzt', 'Ha sostituito tre prodotti'),
    'Cleanser, toner and serum in one step. My shelf is empty now.': (
        'Nettoyant, lotion et sérum en une étape. Mon étagère est vide.',
        'Reinigung, Toner und Serum in einem Schritt. Mein Regal ist jetzt leer.',
        'Detergente, tonico e siero in un passaggio. Il mio scaffale ora è vuoto.'),
    'Glass feels premium': ('Le verre fait haut de gamme', 'Das Glas wirkt hochwertig', 'Il vetro sembra di pregio'),
    'Heavy frosted glass and a proper lid. Sits well on the sink.': (
        'Verre dépoli lourd et un vrai couvercle. Il tient bien sur le lavabo.',
        'Schweres Milchglas und ein richtiger Deckel. Steht gut am Waschbecken.',
        'Vetro satinato pesante e un vero coperchio. Sta bene sul lavandino.'),
    'Nice, not a miracle': ('Bien, sans miracle', 'Schön, kein Wunder', 'Bello, non un miracolo'),
    'Pleasant to use and my skin is fine, but the price promised more.': (
        'Agréable à utiliser et ma peau va bien, mais le prix promettait plus.',
        'Angenehm in der Anwendung und meine Haut ist gut, aber der Preis versprach mehr.',
        'Piacevole da usare e la mia pelle sta bene, ma il prezzo prometteva di più.'),
    'Calmed a flare up': ('Il a calmé une poussée', 'Hat einen Schub beruhigt', "Ha calmato un'irritazione"),
    'Used it on a red patch for three nights and it settled.': (
        "Utilisé sur une plaque rouge trois soirs et cela s'est calmé.",
        'Drei Nächte auf eine gerötete Stelle aufgetragen und es hat sich beruhigt.',
        'Usato su una zona rossa per tre sere e si è calmata.'),
    'A little goes far': ('Il en faut peu', 'Wenig reicht weit', 'Ne basta poco'),
    'Two pumps for the whole face. The bottle will last months.': (
        'Deux pressions pour tout le visage. Le flacon durera des mois.',
        'Zwei Pumpstöße fürs ganze Gesicht. Die Flasche hält Monate.',
        'Due dosi per tutto il viso. Il flacone durerà mesi.'),
    'Great under sunscreen': ('Parfait sous la crème solaire', 'Super unter Sonnencreme', 'Ottimo sotto la protezione solare'),
    'No pilling, which is rare. Sunscreen sits smoothly on top.': (
        "Aucun peluchage, ce qui est rare. La crème solaire s'étale bien par-dessus.",
        'Kein Pilling, was selten ist. Die Sonnencreme liegt glatt darüber.',
        'Niente pallini, cosa rara. La protezione solare si stende bene sopra.'),
    'Arrived leaking': ('Arrivé en fuite', 'Ausgelaufen angekommen', 'Arrivato che perdeva'),
    'The cap was loose and a third was gone. Replaced within a week.': (
        'Le bouchon était mal vissé et un tiers avait coulé. Remplacé en une semaine.',
        'Der Deckel war locker und ein Drittel war weg. Innerhalb einer Woche ersetzt.',
        'Il tappo era lento e un terzo era andato. Sostituito in una settimana.'),
    'Smooth after one use': ('Lisse dès la première fois', 'Nach einer Anwendung glatt', 'Liscia dopo un solo uso'),
    'The enzyme powder is gentle and my skin felt polished, not raw.': (
        'La poudre enzymatique est douce et ma peau était polie, pas agressée.',
        'Das Enzympulver ist sanft und meine Haut fühlte sich poliert an, nicht wund.',
        'La polvere enzimatica è delicata e la mia pelle è risultata levigata, non irritata.'),

    # Home
    'Solid and beautiful': ('Solide et beau', 'Solide und schön', 'Robusto e bello'),
    'Heavier and better made than expected. The oil finish is lovely.': (
        "Plus lourd et mieux fait que prévu. La finition à l'huile est superbe.",
        'Schwerer und besser verarbeitet als erwartet. Die Ölung ist wunderschön.',
        'Più pesante e meglio fatto del previsto. La finitura a olio è bellissima.'),
    'Good, delivery slow': ('Bien, livraison lente', 'Gut, Lieferung langsam', 'Buono, consegna lenta'),
    'Great piece, but it took six weeks. Worth the wait, just plan ahead.': (
        "Belle pièce, mais il a fallu six semaines. Cela vaut l'attente, prévoyez à l'avance.",
        'Tolles Stück, aber es dauerte sechs Wochen. Das Warten lohnt sich, planen Sie voraus.',
        "Bel pezzo, ma ci sono volute sei settimane. Vale l'attesa, ma organizzati prima."),
    'Room of choice delivery': ('Livraison dans la pièce de votre choix', 'Lieferung in den Wunschraum', 'Consegna nella stanza scelta'),
    'Two people carried it upstairs and took the packaging. Excellent.': (
        "Deux personnes l'ont monté et ont repris l'emballage. Excellent.",
        'Zwei Leute haben es hochgetragen und die Verpackung mitgenommen. Ausgezeichnet.',
        "Due persone l'hanno portato di sopra e hanno ripreso l'imballaggio. Ottimo."),
    'Cover replaced for free': ('Housse remplacée gratuitement', 'Bezug kostenlos ersetzt', 'Fodera sostituita gratis'),
    'A stain that would not come out. New cover, no charge.': (
        'Une tache impossible à enlever. Nouvelle housse, sans frais.',
        'Ein Fleck, der nicht rausging. Neuer Bezug, kostenlos.',
        'Una macchia che non veniva via. Fodera nuova, senza costi.'),
    'Linen softens fast': ("Le lin s'assouplit vite", 'Leinen wird schnell weich', 'Il lino si ammorbidisce in fretta'),
    'Crisp on day one, soft after three washes. Sleeping better.': (
        'Craquant le premier jour, doux après trois lavages. Je dors mieux.',
        'Am ersten Tag knackig, nach drei Wäschen weich. Ich schlafe besser.',
        'Croccante il primo giorno, morbido dopo tre lavaggi. Dormo meglio.'),
    'Colour is true': ('La couleur est fidèle', 'Die Farbe stimmt', 'Il colore è fedele'),
    'The oatmeal is the oatmeal in the photo. No surprises.': (
        "L'avoine est bien l'avoine de la photo. Aucune surprise.",
        'Das Haferbeige ist das Haferbeige vom Foto. Keine Überraschung.',
        "L'avena è proprio l'avena della foto. Nessuna sorpresa."),
    'Wobbles a little': ('Il bouge un peu', 'Wackelt ein wenig', "Balla un po'"),
    'One leg needed a shim on my old floor. Fine after that.': (
        "Un pied a eu besoin d'une cale sur mon vieux plancher. Parfait ensuite.",
        'Ein Bein brauchte auf meinem alten Boden eine Unterlage. Danach war es gut.',
        'Una gamba ha avuto bisogno di uno spessore sul mio vecchio pavimento. Poi tutto bene.'),
    'Guests ask where it is from': ("Les invités demandent d'où il vient", 'Gäste fragen, woher es ist', 'Gli ospiti chiedono da dove viene'),
    'Every time. The answer is always this shop.': (
        'À chaque fois. La réponse est toujours cette boutique.',
        'Jedes Mal. Die Antwort ist immer dieser Laden.',
        'Ogni volta. La risposta è sempre questo negozio.'),
    'Candle burns even': ('La bougie brûle régulièrement', 'Die Kerze brennt gleichmäßig', 'La candela brucia in modo uniforme'),
    'No tunnelling, no soot, forty hours as promised.': (
        'Aucun creusement, aucune suie, quarante heures comme promis.',
        'Kein Tunneln, kein Ruß, vierzig Stunden wie versprochen.',
        'Nessun tunnel, nessuna fuliggine, quaranta ore come promesso.'),
    'Too firm for me': ('Trop ferme pour moi', 'Mir zu fest', 'Troppo rigido per me'),
    'Well made sofa, but the seat is firmer than the showroom feel I wanted.': (
        "Canapé bien fait, mais l'assise est plus ferme que celle du magasin que je voulais.",
        'Gut gemachtes Sofa, aber die Sitzfläche ist fester als im Ausstellungsraum erhofft.',
        'Divano ben fatto, ma la seduta è più rigida di quella dello showroom che volevo.'),
    'Assembled in ten minutes': ('Monté en dix minutes', 'In zehn Minuten aufgebaut', 'Montato in dieci minuti'),
    'Four bolts and a key. Instructions with actual words.': (
        'Quatre boulons et une clé. Une notice avec de vrais mots.',
        'Vier Schrauben und ein Schlüssel. Eine Anleitung mit echten Wörtern.',
        'Quattro bulloni e una chiave. Istruzioni con parole vere.'),
    'Mug keeps coffee hot': ('La tasse garde le café chaud', 'Der Becher hält den Kaffee warm', 'La tazza tiene il caffè caldo'),
    'Thick stoneware. My coffee stays warm through a whole call.': (
        'Grès épais. Mon café reste chaud pendant tout un appel.',
        'Dickes Steinzeug. Mein Kaffee bleibt einen ganzen Anruf lang warm.',
        'Gres spesso. Il mio caffè resta caldo per tutta una chiamata.'),
    'Rug sheds at first': ('Le tapis perd ses fibres au début', 'Der Teppich haart anfangs', "Il tappeto perde pelo all'inizio"),
    'Wool fluff for two weeks, then it settled. Vacuum often at first.': (
        "Des peluches de laine pendant deux semaines, puis cela s'est calmé. Aspirez souvent au début.",
        'Zwei Wochen Wollflusen, dann war es vorbei. Anfangs oft saugen.',
        "Lanugine di lana per due settimane, poi si è calmato. All'inizio aspira spesso."),
    'Fits the alcove exactly': ("Il rentre pile dans l'alcôve", 'Passt genau in die Nische', 'Entra esatto nella nicchia'),
    'I measured twice and it fits to the centimetre.': (
        "J'ai mesuré deux fois et il rentre au centimètre près.",
        'Ich habe zweimal gemessen und es passt auf den Zentimeter.',
        'Ho misurato due volte ed entra al centimetro.'),
    'Throw is generous': ('Le plaid est grand', 'Die Decke ist großzügig', 'Il plaid è generoso'),
    'Big enough for two on the sofa. Fringe has not shed.': (
        "Assez grand pour deux sur le canapé. Les franges n'ont pas bougé.",
        'Groß genug für zwei auf dem Sofa. Die Fransen haben nicht gehaart.',
        'Abbastanza grande per due sul divano. La frangia non ha perso pelo.'),
    'Paint chipped on the edge': ('La peinture est écaillée sur le bord', 'Der Lack ist an der Kante abgeplatzt', 'La vernice è scheggiata sul bordo'),
    'Small chip on the frame from transit. Touch-up pot sent free.': (
        'Un petit éclat sur le cadre dû au transport. Un pot de retouche envoyé gratuitement.',
        'Kleiner Absplitterer am Rahmen vom Transport. Ausbesserungsfarbe kostenlos geschickt.',
        'Piccola scheggiatura sul telaio dal trasporto. Barattolo per ritocchi inviato gratis.'),
    'Table takes a beating': ('La table encaisse', 'Der Tisch hält was aus', 'Il tavolo regge tutto'),
    'Kids, homework, dinner. The oak just gets better.': (
        "Les enfants, les devoirs, le dîner. Le chêne ne fait que s'améliorer.",
        'Kinder, Hausaufgaben, Abendessen. Die Eiche wird nur schöner.',
        'Bambini, compiti, cena. Il rovere migliora soltanto.'),
    'Lamp gives a warm pool': ('La lampe donne une flaque de lumière chaude', 'Die Lampe gibt einen warmen Lichtkreis', 'La lampada dà un cerchio di luce calda'),
    'Perfect reading light. The switch on the cord is handy.': (
        "Une lumière de lecture parfaite. L'interrupteur sur le fil est pratique.",
        'Perfektes Leselicht. Der Schalter am Kabel ist praktisch.',
        "Luce da lettura perfetta. L'interruttore sul filo è comodo."),
    'Smells of wood': ('Il sent le bois', 'Riecht nach Holz', 'Profuma di legno'),
    'Opened the box and the workshop came with it.': (
        "J'ai ouvert la boîte et l'atelier est venu avec.",
        'Die Kiste geöffnet und die Werkstatt kam mit.',
        'Ho aperto la scatola e il laboratorio è venuto con lei.'),
    'Cushion lost its shape': ('Le coussin a perdu sa forme', 'Das Kissen hat die Form verloren', 'Il cuscino ha perso la forma'),
    'Feather filling flattens. Plump it daily or choose foam.': (
        "Le garnissage en plumes s'aplatit. Retapez-le chaque jour ou choisissez la mousse.",
        'Federfüllung flacht ab. Täglich aufschütteln oder Schaum wählen.',
        "L'imbottitura in piuma si appiattisce. Sprimaccialo ogni giorno o scegli la gomma."),
    'Vase is heavy': ('Le vase est lourd', 'Die Vase ist schwer', 'Il vaso è pesante'),
    'Stoneware with real weight. Tulips do not tip it.': (
        'Du grès avec un vrai poids. Les tulipes ne le renversent pas.',
        'Steinzeug mit echtem Gewicht. Tulpen kippen sie nicht um.',
        'Gres con un peso vero. I tulipani non lo rovesciano.'),
    'Worth the wait': ("Cela valait l'attente", 'Das Warten hat sich gelohnt', "Ne è valsa l'attesa"),
    'Eight weeks, made to order, and it shows in every joint.': (
        'Huit semaines, fait sur commande, et cela se voit dans chaque assemblage.',
        'Acht Wochen, auf Bestellung gefertigt, und man sieht es an jeder Verbindung.',
        'Otto settimane, fatto su ordinazione, e si vede in ogni giunzione.'),
    'Storage inside the bench': ('Du rangement dans le banc', 'Stauraum in der Bank', 'Contenitore dentro la panca'),
    'I did not notice the lid lifts. Winter blankets live there now.': (
        "Je n'avais pas vu que le couvercle se soulève. Les couvertures d'hiver y vivent maintenant.",
        'Ich hatte nicht gemerkt, dass sich der Deckel hebt. Die Winterdecken wohnen jetzt dort.',
        'Non avevo notato che il coperchio si alza. Ora ci stanno le coperte invernali.'),
    'Sheets fit a deep mattress': ('Les draps vont sur un matelas épais', 'Die Laken passen auf eine dicke Matratze', 'Le lenzuola stanno su un materasso alto'),
    'Finally a fitted sheet that stays on the corners.': (
        'Enfin un drap housse qui tient aux coins.',
        'Endlich ein Spannbettlaken, das an den Ecken hält.',
        'Finalmente un lenzuolo con angoli che tiene.'),

    # Sports
    'Fits as described': ('Conforme à la description', 'Passt wie beschrieben', 'Veste come descritto'),
    'The fitting notes were accurate. No blisters on a 30 km run.': (
        'Les conseils de taille étaient justes. Aucune ampoule sur 30 km.',
        'Die Größenhinweise stimmten. Keine Blasen auf 30 km.',
        'Le note sulla vestibilità erano giuste. Nessuna vescica su 30 km.'),
    'Good, sizing runs small': ('Bien, taille petit', 'Gut, fällt klein aus', 'Buono, veste stretto'),
    'Quality is great. Go half a size up.': (
        'La qualité est excellente. Prenez une demi-taille au-dessus.',
        'Die Qualität ist super. Eine halbe Nummer größer nehmen.',
        'La qualità è ottima. Prendi mezza taglia in più.'),
    'Survived a season': ('Il a passé la saison', 'Hat eine Saison überstanden', 'Ha superato una stagione'),
    'Rain, mud, a hundred washes. Still going.': (
        'Pluie, boue, cent lavages. Toujours là.',
        'Regen, Schlamm, hundert Wäschen. Läuft immer noch.',
        'Pioggia, fango, cento lavaggi. Ancora qui.'),
    'Returned, no questions': ('Retourné sans discussion', 'Zurückgegeben, ohne Fragen', 'Reso senza domande'),
    'Did not suit my stride. Return was easy and fast.': (
        "Cela ne convenait pas à ma foulée. Le retour a été simple et rapide.",
        'Passte nicht zu meinem Laufstil. Die Rückgabe war einfach und schnell.',
        'Non andava con la mia falcata. Il reso è stato facile e veloce.'),
    'Grip in the wet': ("De l'accroche sur le mouillé", 'Grip bei Nässe', 'Aderenza sul bagnato'),
    'Ran a rainy trail and never slipped.': (
        "J'ai couru un sentier sous la pluie sans jamais glisser.",
        'Bin einen nassen Trail gelaufen und nie gerutscht.',
        'Ho corso un sentiero sotto la pioggia senza mai scivolare.'),
    'Bottle does not leak': ('La gourde ne fuit pas', 'Die Flasche läuft nicht aus', 'La borraccia non perde'),
    'Upside down in the bag all day. Dry bag.': (
        "À l'envers dans le sac toute la journée. Sac sec.",
        'Den ganzen Tag kopfüber in der Tasche. Trockene Tasche.',
        'A testa in giù nella borsa tutto il giorno. Borsa asciutta.'),
    'Light and warm': ('Léger et chaud', 'Leicht und warm', 'Leggera e calda'),
    'Packs into its own pocket and still cuts the wind.': (
        'Elle se range dans sa propre poche et coupe encore le vent.',
        'Lässt sich in die eigene Tasche packen und hält trotzdem den Wind ab.',
        'Si ripiega nella sua tasca e taglia comunque il vento.'),
    'Seams rubbed': ('Les coutures ont frotté', 'Die Nähte haben gescheuert', 'Le cuciture hanno sfregato'),
    'Great shorts but a seam rubbed on long rides. Fine under 40 km.': (
        'Très bon cuissard mais une couture a frotté sur les longues sorties. Parfait sous 40 km.',
        'Tolle Hose, aber eine Naht hat bei langen Fahrten gescheuert. Unter 40 km gut.',
        'Ottimi pantaloncini ma una cucitura ha sfregato nelle uscite lunghe. Sotto i 40 km vanno bene.'),
    'Mat stays put': ('Le tapis ne glisse pas', 'Die Matte bleibt liegen', 'Il tappetino non scivola'),
    'No sliding on a wooden floor, even in a sweaty class.': (
        'Aucun glissement sur un parquet, même pendant un cours transpirant.',
        'Kein Rutschen auf Holzboden, auch nicht in einer verschwitzten Stunde.',
        'Non scivola sul parquet, nemmeno in una lezione sudata.'),
    'Zips froze': ('Les fermetures ont gelé', 'Die Reißverschlüsse froren ein', 'Le cerniere si sono bloccate'),
    'Fine jacket, but the zip pulls are small with gloves on.': (
        'Bonne veste, mais les tirettes sont petites avec des gants.',
        'Gute Jacke, aber die Zipper sind mit Handschuhen zu klein.',
        'Bella giacca, ma i cursori sono piccoli con i guanti.'),
    'Race day shoe': ('La chaussure des jours de course', 'Der Wettkampfschuh', 'La scarpa da gara'),
    'Saved it for the marathon. Personal best.': (
        "Je l'ai gardée pour le marathon. Record personnel.",
        'Für den Marathon aufgehoben. Persönliche Bestzeit.',
        "L'ho tenuta per la maratona. Record personale."),
    'Straps dig in': ('Les bretelles rentrent', 'Die Gurte schneiden ein', 'Gli spallacci segnano'),
    'Backpack carries well when full, straps dig when empty.': (
        "Le sac porte bien quand il est plein, les bretelles rentrent quand il est vide.",
        'Der Rucksack trägt sich voll gut, leer schneiden die Gurte ein.',
        'Lo zaino porta bene quando è pieno, gli spallacci segnano quando è vuoto.'),
    'Socks that stay up': ('Des chaussettes qui tiennent', 'Socken, die halten', 'Calze che stanno su'),
    'Finally. No slipping into the shoe at km ten.': (
        'Enfin. Elles ne glissent plus dans la chaussure au dixième kilomètre.',
        'Endlich. Kein Rutschen in den Schuh bei Kilometer zehn.',
        'Finalmente. Non scivolano nella scarpa al decimo chilometro.'),
    'Heavier than listed': ("Plus lourd qu'annoncé", 'Schwerer als angegeben', 'Più pesante di quanto indicato'),
    'Good bag, but 200 g over the stated weight on my scale.': (
        'Bon sac, mais 200 g de plus que le poids annoncé sur ma balance.',
        'Gute Tasche, aber 200 g über dem angegebenen Gewicht auf meiner Waage.',
        'Buona borsa, ma 200 g oltre il peso dichiarato sulla mia bilancia.'),
    'Bright enough for night': ('Assez visible la nuit', 'Hell genug für die Nacht', 'Abbastanza visibile di notte'),
    'The reflective panels light up like a sign.': (
        "Les bandes réfléchissantes s'allument comme un panneau.",
        'Die Reflexstreifen leuchten wie ein Schild.',
        'Le bande riflettenti si accendono come un cartello.'),
    'Wore through at the toe': ('Usé au bout', 'An der Zehe durchgelaufen', 'Consumata sulla punta'),
    'Six hundred kilometres, which is fair. Buying again.': (
        "Six cents kilomètres, c'est honnête. Je rachète.",
        'Sechshundert Kilometer, das ist fair. Ich kaufe wieder.',
        'Seicento chilometri, che è onesto. La ricompro.'),
    'Great for cold mornings': ('Parfait pour les matins froids', 'Super für kalte Morgen', 'Ottimo per le mattine fredde'),
    'Thermal layer under a shell and I was warm at zero degrees.': (
        "Une couche thermique sous une coupe-vent et j'avais chaud à zéro degré.",
        'Thermoschicht unter einer Hülle und mir war bei null Grad warm.',
        'Strato termico sotto un guscio e stavo al caldo a zero gradi.'),
    'Ball holds pressure': ('Le ballon garde la pression', 'Der Ball hält den Druck', 'Il pallone tiene la pressione'),
    'Pumped it in March, still firm in May.': (
        'Gonflé en mars, encore ferme en mai.',
        'Im März aufgepumpt, im Mai noch prall.',
        'Gonfiato a marzo, ancora duro a maggio.'),
    'Laces too long': ('Lacets trop longs', 'Schnürsenkel zu lang', 'Lacci troppo lunghi'),
    'Double knot needed. Otherwise a great shoe.': (
        'Il faut un double nœud. Sinon une très bonne chaussure.',
        'Doppelter Knoten nötig. Sonst ein toller Schuh.',
        'Serve un doppio nodo. Per il resto una gran scarpa.'),
    'Kids team loves them': ("L'équipe des enfants les adore", 'Die Kindermannschaft liebt sie', 'La squadra dei bambini le adora'),
    'Ordered twelve. All fit, all survived the season.': (
        "J'en ai commandé douze. Toutes à la bonne taille, toutes ont passé la saison.",
        'Zwölf bestellt. Alle passten, alle haben die Saison überstanden.',
        'Ne ho ordinate dodici. Tutte giuste, tutte hanno superato la stagione.'),
    'Watch strap is comfy': ('Le bracelet est confortable', 'Das Armband ist bequem', 'Il cinturino è comodo'),
    'Soft silicone, no sweat rash, easy to swap.': (
        'Silicone souple, aucune irritation, facile à changer.',
        'Weiches Silikon, kein Schweißausschlag, leicht zu wechseln.',
        'Silicone morbido, nessuna irritazione, facile da cambiare.'),
    'Pockets in the right place': ('Des poches bien placées', 'Taschen an der richtigen Stelle', 'Tasche al posto giusto'),
    'Phone, key, gel. Nothing bounces.': (
        'Téléphone, clé, gel. Rien ne bouge.',
        'Handy, Schlüssel, Gel. Nichts hüpft.',
        'Telefono, chiave, gel. Niente rimbalza.'),
    'Faded after a summer': ('Délavé après un été', 'Nach einem Sommer verblasst', "Sbiadito dopo un'estate"),
    'Colour went from navy to blue. Still works.': (
        'La couleur est passée du marine au bleu. Cela fonctionne encore.',
        'Die Farbe ging von Marine zu Blau. Funktioniert trotzdem.',
        'Il colore è passato dal blu navy al blu. Funziona ancora.'),
    'Delivered before the race': ('Livré avant la course', 'Vor dem Rennen geliefert', 'Consegnato prima della gara'),
    'Ordered Tuesday, raced Saturday. Thank you.': (
        'Commandé mardi, couru samedi. Merci.',
        'Dienstag bestellt, Samstag gelaufen. Danke.',
        'Ordinato martedì, gara sabato. Grazie.'),

    # Kids
    'Beautifully made': ('Magnifiquement fait', 'Wunderschön gemacht', 'Fatto benissimo'),
    'Smooth wood, no splinters, non-toxic paint. Loved by a two year old.': (
        "Bois lisse, aucune écharde, peinture sans toxique. Adoré par un enfant de deux ans.",
        'Glattes Holz, keine Splitter, ungiftige Farbe. Von einem Zweijährigen geliebt.',
        'Legno liscio, nessuna scheggia, vernice atossica. Amato da un bimbo di due anni.'),
    'Good, a bit small': ('Bien, un peu petit', 'Gut, etwas klein', "Buono, un po' stretto"),
    'Lovely quality but sizes run small. Go up one.': (
        'Belle qualité mais les tailles sont petites. Prenez une taille au-dessus.',
        'Schöne Qualität, aber die Größen fallen klein aus. Eine Nummer größer nehmen.',
        'Bella qualità ma le taglie vestono strette. Prendi una taglia in più.'),
    'Survived everything': ('Il a tout survécu', 'Hat alles überstanden', 'Ha resistito a tutto'),
    'Washed fifty times, still soft and the colour has held.': (
        'Lavé cinquante fois, toujours doux et la couleur a tenu.',
        'Fünfzigmal gewaschen, immer noch weich und die Farbe hält.',
        'Lavato cinquanta volte, ancora morbido e il colore ha tenuto.'),
    'Perfect present': ('Un cadeau parfait', 'Perfektes Präsent', 'Un regalo perfetto'),
    'Wrapped, carded and delivered in two days.': (
        'Emballé, avec une carte, livré en deux jours.',
        'Verpackt, mit Karte, in zwei Tagen geliefert.',
        'Confezionato, con biglietto, consegnato in due giorni.'),
    'Chewed and fine': ('Mâchouillé et intact', 'Bekaut und heil', 'Masticato e intatto'),
    'Teething baby, three months of chewing, still no chips.': (
        'Bébé qui fait ses dents, trois mois de mâchouillage, aucun éclat.',
        'Zahnendes Baby, drei Monate Kauen, noch keine Absplitterung.',
        'Bimbo che mette i denti, tre mesi di morsi, ancora nessuna scheggiatura.'),
    'Poppers instead of buttons': ('Des pressions plutôt que des boutons', 'Druckknöpfe statt Knöpfe', 'Bottoni a pressione invece dei bottoni'),
    'Night changes are faster. Small thing, huge difference.': (
        'Les changes de nuit sont plus rapides. Un détail, une énorme différence.',
        'Das Wickeln in der Nacht geht schneller. Kleinigkeit, riesiger Unterschied.',
        'I cambi notturni sono più rapidi. Piccola cosa, enorme differenza.'),
    'Nap time favourite': ('Le préféré de la sieste', 'Der Liebling zur Schlafenszeit', 'Il preferito del riposino'),
    'Will not sleep without the rabbit. We bought a spare.': (
        "Il ne dort pas sans le lapin. Nous en avons acheté un deuxième.",
        'Ohne den Hasen schläft er nicht. Wir haben einen Ersatz gekauft.',
        'Non dorme senza il coniglio. Ne abbiamo comprato uno di scorta.'),
    'Wheels fell off': ('Les roues sont tombées', 'Die Räder fielen ab', 'Le ruote si sono staccate'),
    'One wheel came loose after a week. Glued and fine, but still.': (
        "Une roue s'est détachée après une semaine. Recollée et c'est bon, mais quand même.",
        'Ein Rad löste sich nach einer Woche. Geklebt und gut, aber trotzdem.',
        'Una ruota si è staccata dopo una settimana. Incollata e va bene, ma comunque.'),
    'Grew with her': ('Il a grandi avec elle', 'Ist mitgewachsen', 'È cresciuto con lei'),
    'Adjustable straps meant it fit from three months to a year.': (
        "Les bretelles réglables lui ont permis d'aller de trois mois à un an.",
        'Verstellbare Gurte, also passte es von drei Monaten bis zu einem Jahr.',
        'Le bretelle regolabili gli hanno fatto andare bene da tre mesi a un anno.'),
    'Colours are soft': ('Des couleurs douces', 'Die Farben sind sanft', 'I colori sono tenui'),
    'Muted tones that do not shout. Matches the nursery.': (
        'Des tons discrets qui ne crient pas. Assortis à la chambre.',
        'Gedeckte Töne, die nicht schreien. Passt zum Kinderzimmer.',
        'Toni smorzati che non urlano. Si abbinano alla cameretta.'),
    'Puzzle is a hit': ('Le puzzle a du succès', 'Das Puzzle kommt an', 'Il puzzle è un successo'),
    'Ten pieces, thick wood, and the pictures make sense.': (
        "Dix pièces, bois épais, et les images ont du sens.",
        'Zehn Teile, dickes Holz, und die Bilder ergeben Sinn.',
        'Dieci pezzi, legno spesso, e le figure hanno senso.'),
    'Zip is tricky': ('La fermeture est difficile', 'Der Reißverschluss ist knifflig', 'La cerniera è difficile'),
    'Great coat but a stiff zip for small hands.': (
        'Très beau manteau mais une fermeture dure pour de petites mains.',
        'Toller Mantel, aber ein strammer Reißverschluss für kleine Hände.',
        'Bel cappotto ma una cerniera dura per mani piccole.'),
    'Wooden blocks clack nicely': ('Les cubes en bois font un joli bruit', 'Die Holzklötze klackern schön', 'I cubi di legno fanno un bel rumore'),
    'The sound is half the fun apparently.': (
        'Le bruit fait la moitié du plaisir, apparemment.',
        'Der Klang ist offenbar der halbe Spaß.',
        'Il suono è metà del divertimento, a quanto pare.'),
    'Hand-me-down ready': ('Prêt pour le suivant', 'Bereit zum Weitergeben', 'Pronto per il fratellino'),
    'Second child wearing it now and it still looks new.': (
        "Le deuxième enfant le porte maintenant et il a l'air neuf.",
        'Das zweite Kind trägt es jetzt und es sieht noch neu aus.',
        'Ora lo indossa il secondo figlio e sembra ancora nuovo.'),
    'Instructions were clear': ('La notice était claire', 'Die Anleitung war klar', 'Le istruzioni erano chiare'),
    'Built the kitchen in twenty minutes with a toddler helping.': (
        "J'ai monté la cuisine en vingt minutes avec un petit qui aidait.",
        'Die Küche in zwanzig Minuten aufgebaut, mit einem Kleinkind als Helfer.',
        'Ho montato la cucina in venti minuti con un bimbo che aiutava.'),
    'Too warm for spring': ('Trop chaud pour le printemps', 'Zu warm für den Frühling', 'Troppo caldo per la primavera'),
    'Beautiful knit but heavy. A winter piece.': (
        "Belle maille mais lourde. Une pièce d'hiver.",
        'Schöner Strick, aber schwer. Ein Winterstück.',
        'Bella maglia ma pesante. Un capo invernale.'),
    'Bath toy has no holes': ("Le jouet de bain n'a pas de trous", 'Das Badespielzeug hat keine Löcher', 'Il gioco da bagno non ha buchi'),
    'No mould inside. Someone thought about this.': (
        "Aucune moisissure à l'intérieur. Quelqu'un y a pensé.",
        'Kein Schimmel innen. Da hat jemand mitgedacht.',
        'Niente muffa dentro. Qualcuno ci ha pensato.'),
    'Print faded a bit': ("L'imprimé a un peu passé", 'Der Druck ist etwas verblasst', "La stampa è un po' sbiadita"),
    'Still soft, but the print lost some colour after many washes.': (
        "Toujours doux, mais l'imprimé a perdu de la couleur après de nombreux lavages.",
        'Immer noch weich, aber der Druck hat nach vielen Wäschen Farbe verloren.',
        'Ancora morbido, ma la stampa ha perso colore dopo molti lavaggi.'),
    'Stacks and knocks down': ('On empile et on renverse', 'Stapeln und umwerfen', 'Impila e butta giù'),
    'Thirty times a day. Never gets old.': (
        "Trente fois par jour. On ne s'en lasse pas.",
        'Dreißigmal am Tag. Wird nie langweilig.',
        'Trenta volte al giorno. Non stanca mai.'),
    'Sizing chart was right': ('Le guide des tailles était juste', 'Die Größentabelle stimmte', 'La tabella taglie era giusta'),
    'Measured, ordered, fit. Thank you for the chart.': (
        'Mesuré, commandé, à la bonne taille. Merci pour le guide.',
        'Gemessen, bestellt, es passt. Danke für die Tabelle.',
        'Misurato, ordinato, calzato. Grazie per la tabella.'),
    'Muslin is huge': ('Le lange est immense', 'Das Mulltuch ist riesig', 'La mussola è enorme'),
    'Big enough to swaddle and later a picnic blanket.': (
        "Assez grand pour emmailloter et plus tard servir de nappe de pique-nique.",
        'Groß genug zum Pucken und später als Picknickdecke.',
        'Abbastanza grande per fasciare e poi come telo da picnic.'),
    'Grandparents approved': ('Approuvé par les grands-parents', 'Von den Großeltern gebilligt', 'Approvato dai nonni'),
    'They said it looks like the toys they had. High praise.': (
        "Ils ont dit que cela ressemble aux jouets qu'ils avaient. Un beau compliment.",
        'Sie sagten, es sehe aus wie ihr eigenes Spielzeug von damals. Großes Lob.',
        'Hanno detto che sembra i giochi che avevano loro. Gran complimento.'),
    'Bib catches everything': ('Le bavoir attrape tout', 'Das Lätzchen fängt alles auf', 'Il bavaglino prende tutto'),
    'Deep pocket, wipes clean, no more laundry after lunch.': (
        "Poche profonde, il s'essuie, plus de lessive après le déjeuner.",
        'Tiefe Tasche, abwischbar, keine Wäsche mehr nach dem Mittagessen.',
        'Tasca profonda, si pulisce, niente più bucato dopo pranzo.'),
    'Bell is loud': ('La clochette est forte', 'Die Glocke ist laut', 'Il campanello è forte'),
    'Lovely rattle, but the bell is louder than I expected.': (
        'Joli hochet, mais la clochette est plus forte que prévu.',
        'Schöne Rassel, aber die Glocke ist lauter als erwartet.',
        'Bel sonaglio, ma il campanello è più forte del previsto.'),

    # Garden
    'Healthy and well packed': ('Sain et bien emballé', 'Gesund und gut verpackt', 'Sana e ben imballata'),
    'Arrived upright with damp compost and no broken leaves.': (
        'Arrivé droit avec du terreau humide et aucune feuille cassée.',
        'Kam aufrecht an, mit feuchter Erde und ohne gebrochene Blätter.',
        'Arrivata dritta con terriccio umido e nessuna foglia rotta.'),
    'Smaller than expected': ('Plus petit que prévu', 'Kleiner als erwartet', 'Più piccola del previsto'),
    'Healthy plant but a smaller pot than I thought. Check the pot size.': (
        'Plante saine mais un pot plus petit que je ne pensais. Vérifiez la taille du pot.',
        'Gesunde Pflanze, aber ein kleinerer Topf als gedacht. Prüfen Sie die Topfgröße.',
        'Pianta sana ma un vaso più piccolo di quanto pensassi. Controlla la misura del vaso.'),
    'Sharp and solid': ('Affûté et solide', 'Scharf und solide', 'Affilato e robusto'),
    'The tool is heavy in a good way and came sharp.': (
        "L'outil est lourd dans le bon sens et est arrivé affûté.",
        'Das Werkzeug ist angenehm schwer und kam scharf an.',
        "L'attrezzo è pesante nel senso buono ed è arrivato affilato."),
    'Replaced without fuss': ('Remplacé sans histoires', 'Ohne Umstände ersetzt', 'Sostituita senza problemi'),
    'One plant failed. Photo sent, new one in three days.': (
        "Une plante n'a pas pris. Photo envoyée, une nouvelle en trois jours.",
        'Eine Pflanze ging ein. Foto geschickt, eine neue in drei Tagen.',
        'Una pianta non ha attecchito. Foto inviata, una nuova in tre giorni.'),
    'Flowered in three weeks': ('Fleuri en trois semaines', 'Blühte nach drei Wochen', 'Ha fiorito in tre settimane'),
    'Planted it on a Sunday, first bud by month end.': (
        'Planté un dimanche, premier bouton à la fin du mois.',
        'An einem Sonntag gepflanzt, erste Knospe zum Monatsende.',
        'Piantata di domenica, primo bocciolo a fine mese.'),
    'Terracotta is thick': ('La terre cuite est épaisse', 'Die Terrakotta ist dick', 'La terracotta è spessa'),
    'Proper fired clay, not the thin stuff. Survived a frost.': (
        "De la vraie argile cuite, pas la version fine. Elle a passé une gelée.",
        'Echter gebrannter Ton, nicht die dünne Ware. Hat einen Frost überstanden.',
        'Vera argilla cotta, non quella sottile. Ha superato una gelata.'),
    'Seeds all came up': ('Toutes les graines ont levé', 'Alle Samen sind aufgegangen', 'Tutti i semi sono nati'),
    'Twenty sown, nineteen seedlings. Cannot ask for more.': (
        "Vingt semées, dix-neuf plants. On ne peut pas demander mieux.",
        'Zwanzig gesät, neunzehn Sämlinge. Mehr kann man nicht verlangen.',
        'Venti seminati, diciannove piantine. Non si può chiedere di più.'),
    'Soil was dry on arrival': ("La terre était sèche à l'arrivée", 'Die Erde war bei Ankunft trocken', "La terra era secca all'arrivo"),
    'Plant bounced back after a soak, but the box sat somewhere warm.': (
        'La plante est repartie après un bon arrosage, mais le colis est resté au chaud.',
        'Die Pflanze erholte sich nach einem Tauchbad, aber der Karton stand irgendwo warm.',
        'La pianta si è ripresa dopo una bella bagnata, ma la scatola è rimasta al caldo.'),
    'Handle fits the hand': ('Le manche tient bien en main', 'Der Griff liegt gut in der Hand', 'Il manico sta bene in mano'),
    'Ash handle, no blisters after an afternoon of digging.': (
        'Manche en frêne, aucune ampoule après un après-midi à bêcher.',
        'Eschengriff, keine Blasen nach einem Nachmittag Graben.',
        'Manico in frassino, nessuna vescica dopo un pomeriggio a scavare.'),
    'Bees love it': ("Les abeilles l'adorent", 'Die Bienen lieben sie', 'Le api la adorano'),
    'Covered in bees within a week of planting.': (
        "Couverte d'abeilles une semaine après la plantation.",
        'Eine Woche nach dem Pflanzen voller Bienen.',
        'Coperta di api una settimana dopo la messa a dimora.'),
    'Wrong colour': ('Mauvaise couleur', 'Falsche Farbe', 'Colore sbagliato'),
    'Ordered white, got pink. Beautiful, but not what I ordered. Refund given.': (
        "J'ai commandé du blanc, j'ai reçu du rose. C'est beau, mais ce n'est pas ma commande. Remboursement accordé.",
        'Weiß bestellt, Rosa bekommen. Schön, aber nicht das Bestellte. Erstattung erhalten.',
        'Ordinato bianco, arrivato rosa. Bello, ma non quello che avevo ordinato. Rimborso concesso.'),
    'Hardy as promised': ('Rustique comme promis', 'Winterhart wie versprochen', 'Rustica come promesso'),
    'Left out all winter in a pot and it came back.': (
        "Laissée dehors tout l'hiver en pot et elle est repartie.",
        'Den ganzen Winter im Topf draußen gelassen und sie kam zurück.',
        "Lasciata fuori tutto l'inverno in vaso ed è ripartita."),
    'Good starter set': ('Un bon kit pour débuter', 'Gutes Einsteigerset', 'Buon kit per iniziare'),
    'Everything a first garden needs and nothing it does not.': (
        "Tout ce qu'un premier jardin demande et rien de plus.",
        'Alles, was ein erster Garten braucht, und nichts darüber hinaus.',
        'Tutto quello che serve a un primo giardino e niente di più.'),
    'Watering can pours well': ("L'arrosoir verse bien", 'Die Gießkanne gießt gut', "L'annaffiatoio versa bene"),
    'Long spout, fine rose, no dribble down the side.': (
        'Long bec, pomme fine, aucune coulure sur le côté.',
        'Langer Auslauf, feine Brause, kein Tropfen an der Seite.',
        'Becco lungo, cipolla fine, nessuna goccia sul lato.'),
    'Delivery was gentle': ('Une livraison en douceur', 'Die Lieferung war behutsam', 'La consegna è stata delicata'),
    'The courier carried it upright. The driver deserves the credit.': (
        "Le livreur l'a porté droit. Le mérite lui revient.",
        'Der Kurier hat sie aufrecht getragen. Das Lob gebührt dem Fahrer.',
        "Il corriere l'ha portata dritta. Il merito è dell'autista."),
    'Herbs on the sill': ('Des herbes sur le rebord', 'Kräuter auf der Fensterbank', 'Erbe sul davanzale'),
    'Six pots on the kitchen sill and I have not bought parsley since.': (
        "Six pots sur le rebord de la cuisine et je n'ai plus acheté de persil.",
        'Sechs Töpfe auf der Küchenfensterbank und ich habe seitdem keine Petersilie mehr gekauft.',
        'Sei vasi sul davanzale della cucina e non compro più prezzemolo.'),
    'Compost smells right': ('Le terreau sent bon', 'Der Kompost riecht richtig', 'Il compost ha il profumo giusto'),
    'Dark and crumbly. My tomatoes doubled in a month.': (
        'Foncé et friable. Mes tomates ont doublé en un mois.',
        'Dunkel und krümelig. Meine Tomaten haben sich in einem Monat verdoppelt.',
        'Scuro e friabile. I miei pomodori sono raddoppiati in un mese.'),
    'Pot has no drainage hole': ("Le pot n'a pas de trou de drainage", 'Der Topf hat kein Abzugsloch', 'Il vaso non ha il foro di drenaggio'),
    'Lovely glaze but no hole. Drill it or use it indoors with gravel.': (
        "Un bel émail mais pas de trou. Percez-le ou utilisez-le à l'intérieur avec des graviers.",
        'Schöne Glasur, aber kein Loch. Bohren Sie es oder nutzen Sie ihn drinnen mit Kies.',
        'Bello smalto ma niente foro. Fallo tu o usalo in casa con la ghiaia.'),
    'Pruners cut clean': ('Le sécateur coupe net', 'Die Schere schneidet sauber', 'Le cesoie tagliano netto'),
    'Bypass blades, no crushing. Roses thanked me.': (
        "Lames franches, aucun écrasement. Les rosiers m'ont remercié.",
        'Bypass-Klingen, kein Quetschen. Die Rosen haben es mir gedankt.',
        'Lame bypass, nessuno schiacciamento. Le rose mi hanno ringraziato.'),
    'Bigger than the photo': ('Plus grande que sur la photo', 'Größer als auf dem Foto', 'Più grande della foto'),
    'A three year old plant, not a plug. Delighted.': (
        'Une plante de trois ans, pas un godet. Ravi.',
        'Eine dreijährige Pflanze, kein Steckling. Begeistert.',
        'Una pianta di tre anni, non una piantina. Felicissimo.'),
    'Label was helpful': ("L'étiquette a été utile", 'Das Etikett war hilfreich', "L'etichetta è stata utile"),
    'Planting depth, spacing and sun on the tag. Saved a search.': (
        "Profondeur de plantation, espacement et exposition sur l'étiquette. Cela m'a évité une recherche.",
        'Pflanztiefe, Abstand und Sonne auf dem Schild. Hat mir eine Suche erspart.',
        'Profondità, distanza e sole sul cartellino. Mi ha risparmiato una ricerca.'),
    'Gloves are tough': ('Les gants sont résistants', 'Die Handschuhe sind robust', 'I guanti sono resistenti'),
    'Thorns did not get through. Fit is snug.': (
        'Les épines ne sont pas passées. La coupe est ajustée.',
        'Dornen kamen nicht durch. Die Passform ist eng.',
        'Le spine non sono passate. La vestibilità è aderente.'),
    'Slow to establish': ("Longue à s'installer", 'Braucht lange zum Anwachsen', 'Lenta ad attecchire'),
    'Took a full season to settle. Now it is the best thing in the border.': (
        "Il a fallu une saison entière pour qu'elle s'installe. C'est maintenant la plus belle du massif.",
        'Sie brauchte eine ganze Saison. Jetzt ist sie das Beste im Beet.',
        "Ci è voluta una stagione intera. Ora è la cosa più bella dell'aiuola."),
    'Bulbs came in paper': ('Les bulbes sont livrés dans du papier', 'Die Zwiebeln kamen in Papier', 'I bulbi sono arrivati nella carta'),
    'No plastic in the box at all. Every bulb sprouted.': (
        'Aucun plastique dans le colis. Chaque bulbe a germé.',
        'Überhaupt kein Plastik im Karton. Jede Zwiebel ist ausgetrieben.',
        'Nessuna plastica nella scatola. Ogni bulbo è germogliato.'),
    'Trellis went up in an hour': ('Le treillis a été posé en une heure', 'Das Spalier stand in einer Stunde', "Il traliccio è salito in un'ora"),
    'Cedar, pre-drilled, and the screws were in the box.': (
        'Cèdre, pré-percé, et les vis étaient dans la boîte.',
        'Zeder, vorgebohrt, und die Schrauben lagen in der Box.',
        'Cedro, pre-forato, e le viti erano nella scatola.'),
}

# Product names and descriptions. Filled pack by pack.
PRODUCTS = {}

# Every table is keyed the same way, so the builder reads one merged map per language.
LANGUAGES = ('fr', 'de', 'it')


def table(language):
    """English string to translation, for one store view code."""
    index = LANGUAGES.index(language)
    merged = {}
    for source in (CATEGORIES, REVIEWS, PRODUCTS):
        for english, values in source.items():
            merged[english] = values[index]
    return merged
