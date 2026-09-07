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

# Product names and descriptions. A variant is named after its parent plus an option value, and the
# short description is the first sentence of the description, so only the base copy lives here.
# The invented brand names (Ashford, Meridian, Voltline, ...) never translate.
PRODUCTS = {
    # Fashion
    'Ashford linen shirt': ('Chemise en lin Ashford', 'Ashford Leinenhemd', 'Camicia di lino Ashford'),
    'A relaxed linen shirt with a soft collar and mother-of-pearl buttons. Packs flat, dries fast, gets better with every wash. Cut from midweight European linen with a curved hem that works tucked or out. Wash cold and hang to dry.': (
        "Une chemise en lin décontractée, col souple et boutons de nacre. Elle se plie à plat, sèche vite et s'améliore à chaque lavage. Coupée dans un lin européen de poids moyen, avec un bas arrondi qui se porte rentré ou sorti. Lavage à froid, séchage sur cintre.",
        'Ein lockeres Leinenhemd mit weichem Kragen und Perlmuttknöpfen. Es packt flach, trocknet schnell und wird mit jeder Wäsche besser. Aus mittelschwerem europäischem Leinen, mit rundem Saum zum Reinstecken oder Offentragen. Kalt waschen und hängend trocknen.',
        'Una camicia di lino dal taglio morbido, con collo soft e bottoni in madreperla. Si piega piatta, asciuga in fretta e migliora a ogni lavaggio. Tagliata in lino europeo di peso medio, con fondo arrotondato che sta bene dentro o fuori. Lavare a freddo e asciugare appesa.'),
    'Meridian silk blouse': ('Blouse en soie Meridian', 'Meridian Seidenbluse', 'Blusa di seta Meridian'),
    'A fluid silk blouse with a concealed placket and a slightly dropped shoulder. Wear it tucked or loose. Sandwashed mulberry silk that falls close without clinging. Dry clean, or hand wash cold and lay flat.': (
        "Une blouse en soie fluide, patte de boutonnage cachée et épaule légèrement tombante. À porter rentrée ou libre. Soie de mûrier sablée qui tombe près du corps sans coller. Nettoyage à sec, ou lavage à la main à froid et séchage à plat.",
        'Eine fließende Seidenbluse mit verdeckter Knopfleiste und leicht abfallender Schulter. Ob eingesteckt oder locker getragen. Sandgewaschene Maulbeerseide, die nah fällt, ohne zu kleben. Chemisch reinigen oder kalt von Hand waschen und liegend trocknen.',
        "Una blusa di seta fluida, con cannoncino nascosto e spalla leggermente scesa. Da portare dentro o fuori. Seta di gelso lavata alla sabbia che cade vicino al corpo senza appiccicarsi. Lavaggio a secco, oppure a mano in acqua fredda e ad asciugare in piano."),
    'Nordlys ribbed tank': ('Débardeur côtelé Nordlys', 'Nordlys Ripptop', 'Canotta a coste Nordlys'),
    'A ribbed cotton tank with a square neck. The layering piece that works alone on warm days. A dense rib in organic cotton that holds its shape all day. Machine wash, no tumble.': (
        "Un débardeur en coton côtelé à encolure carrée. La pièce à superposer qui se suffit aussi quand il fait chaud. Une côte dense en coton biologique qui garde sa forme toute la journée. Lavage en machine, pas de sèche-linge.",
        'Ein geripptes Baumwolltop mit eckigem Ausschnitt. Das Lagen-Teil, das an warmen Tagen auch allein funktioniert. Ein dichter Rippstrick aus Biobaumwolle, der den ganzen Tag in Form bleibt. Maschinenwäsche, nicht in den Trockner.',
        'Una canotta di cotone a coste con scollo quadrato. Il capo da sovrapporre che nei giorni caldi sta bene anche da solo. Una costa fitta in cotone biologico che tiene la forma tutto il giorno. Lavaggio in lavatrice, no asciugatrice.'),
    'Bruma Sol wrap top': ('Top portefeuille Bruma Sol', 'Bruma Sol Wickeltop', 'Top a portafoglio Bruma Sol'),
    'A wrap top in crinkled cotton that ties at the side. No ironing, ever. The crinkle is set in the fabric, so it comes out of the suitcase ready. Machine wash cold.': (
        "Un top portefeuille en coton froissé qui se noue sur le côté. Jamais de repassage. Le froissé est fixé dans le tissu, il sort donc de la valise prêt à porter. Lavage en machine à froid.",
        'Ein Wickeltop aus Krinkelbaumwolle, das an der Seite gebunden wird. Nie wieder bügeln. Der Krinkel steckt im Stoff, also kommt es tragefertig aus dem Koffer. Kalt in der Maschine waschen.',
        'Un top a portafoglio in cotone crinkle che si annoda sul fianco. Mai più ferro da stiro. Il crinkle è fissato nel tessuto, quindi esce dalla valigia già pronto. Lavaggio in lavatrice a freddo.'),
    'Harbour stripe tee': ('T-shirt rayé Harbour', 'Harbour Streifenshirt', 'T-shirt a righe Harbour'),
    'A heavyweight striped tee with a boat neck, cut from organic cotton. A 220 g jersey with a wide neck and a straight hem. It shrinks a touch on the first wash, then stays put.': (
        "Un t-shirt rayé épais à encolure bateau, en coton biologique. Un jersey de 220 g avec une large encolure et un bas droit. Il rétrécit un peu au premier lavage, puis ne bouge plus.",
        'Ein schweres Streifenshirt mit U-Boot-Ausschnitt aus Biobaumwolle. Ein 220-g-Jersey mit weitem Ausschnitt und geradem Saum. Es geht bei der ersten Wäsche etwas ein und bleibt danach so.',
        'Una t-shirt a righe pesante con scollo a barca, in cotone biologico. Una jersey da 220 g con scollo largo e fondo dritto. Si ritira un poco al primo lavaggio, poi resta così.'),
    'Sand wide-leg trousers': ('Pantalon large Sand', 'Sand Marlenehose', 'Pantaloni a gamba larga Sand'),
    'High-waisted wide-leg trousers in a linen and viscose blend that falls straight and cool. A fitted waist, a flat front and a leg that ends at the ankle. Machine wash cold and hang to dry.': (
        "Un pantalon large taille haute, en mélange lin et viscose, qui tombe droit et reste frais. Une taille ajustée, un devant plat et une jambe qui s'arrête à la cheville. Lavage en machine à froid, séchage sur cintre.",
        'Eine weite Hose mit hohem Bund aus Leinen-Viskose-Mix, die gerade fällt und kühl bleibt. Ein anliegender Bund, eine flache Front und ein Bein, das am Knöchel endet. Kalt waschen und hängend trocknen.',
        'Pantaloni a gamba larga a vita alta, in misto lino e viscosa, che cadono dritti e restano freschi. Vita aderente, davanti liscio e gamba che finisce alla caviglia. Lavaggio a freddo e asciugatura appesi.'),
    'Fjordline straight jeans': ('Jean droit Fjordline', 'Fjordline Straight Jeans', 'Jeans dritti Fjordline'),
    'A straight-leg jean in rigid organic denim with a high rise. Breaks in to fit you. Rigid 13 oz denim from an Italian mill, with a button fly. Wash rarely and cold.': (
        "Un jean droit en denim brut biologique, taille haute. Il se façonne à votre silhouette. Un denim rigide de 13 oz d'une filature italienne, braguette à boutons. Lavez-le rarement et à froid.",
        'Eine gerade Jeans aus festem Bio-Denim mit hoher Leibhöhe. Sie arbeitet sich in deine Form ein. Fester 13-oz-Denim aus einer italienischen Weberei, mit Knopfleiste. Selten und kalt waschen.',
        "Un jeans dritto in denim rigido biologico a vita alta. Si adatta a te con l'uso. Denim rigido da 13 oz di una filatura italiana, con patta a bottoni. Lavare di rado e a freddo."),
    'Coast cropped chinos': ('Chino court Coast', 'Coast Chino, verkürzt', 'Chino corti Coast'),
    'Cropped chinos in garment-dyed cotton twill, with a clean front and a slim ankle. Garment dyed, so the colour is soft and a little uneven. A touch of stretch in the twill.': (
        "Un chino court en sergé de coton teint en pièce, devant net et cheville fine. Teint après confection, la couleur est douce et un peu irrégulière. Le sergé contient une pointe d'élasthanne.",
        'Ein verkürzter Chino aus stückgefärbtem Baumwolltwill, mit glatter Front und schmalem Knöchel. Stückgefärbt, daher ist die Farbe weich und leicht ungleichmäßig. Etwas Stretch im Twill.',
        "Chino corti in twill di cotone tinto in capo, con davanti pulito e caviglia stretta. Tinti in capo, quindi il colore è morbido e un po' irregolare. Un pizzico di elastico nel twill."),
    'Salt denim shorts': ('Short en jean Salt', 'Salt Jeansshorts', 'Shorts di jeans Salt'),
    'Relaxed denim shorts with a raw hem and a high waist, in a light wash. Cut from 12 oz denim with a four-inch inseam. The hem frays a little more with every wash.': (
        "Un short en jean décontracté, bas brut et taille haute, dans un lavage clair. Coupé dans un denim de 12 oz avec une entrejambe de dix centimètres. Le bas s'effiloche un peu plus à chaque lavage.",
        'Lockere Jeansshorts mit offenem Saum und hohem Bund, in heller Waschung. Aus 12-oz-Denim mit zehn Zentimetern Innenbeinlänge. Der Saum franst mit jeder Wäsche ein wenig mehr aus.',
        'Shorts di jeans dal taglio morbido, con fondo vivo e vita alta, in lavaggio chiaro. Tagliati in denim da 12 oz con cavallo di dieci centimetri. Il fondo si sfrangia un poco a ogni lavaggio.'),
    'Ashford linen midi dress': ('Robe midi en lin Ashford', 'Ashford Midikleid aus Leinen', 'Abito midi di lino Ashford'),
    'A sleeveless linen midi dress with a square neck and pockets. The one you pack first. The skirt falls to mid calf with a slit at the back. Wash cold and hang to dry.': (
        "Une robe midi en lin sans manches, encolure carrée et poches. Celle que vous mettez en premier dans la valise. La jupe tombe à mi-mollet avec une fente au dos. Lavage à froid, séchage sur cintre.",
        'Ein ärmelloses Midikleid aus Leinen mit eckigem Ausschnitt und Taschen. Das Kleid, das zuerst in den Koffer kommt. Der Rock fällt bis zur halben Wade, mit Schlitz hinten. Kalt waschen und hängend trocknen.',
        "Un abito midi di lino senza maniche, con scollo quadrato e tasche. Quello che metti in valigia per primo. La gonna arriva a metà polpaccio con uno spacco dietro. Lavare a freddo e asciugare appeso."),
    'Meridian slip dress': ('Robe nuisette Meridian', 'Meridian Slipdress', 'Abito sottoveste Meridian'),
    'A bias-cut silk slip dress that skims rather than clings. Dinner, then dancing. Adjustable straps, a low back and a hem below the knee. Dry clean, or hand wash cold.': (
        "Une robe nuisette en soie coupée dans le biais, qui effleure sans coller. Le dîner, puis la piste. Bretelles réglables, dos échancré et ourlet sous le genou. Nettoyage à sec, ou lavage à la main à froid.",
        'Ein schräg geschnittenes Seiden-Slipdress, das streift statt zu kleben. Erst Essen, dann Tanzen. Verstellbare Träger, tiefer Rücken und ein Saum unter dem Knie. Chemisch reinigen oder kalt von Hand waschen.',
        "Un abito sottoveste di seta tagliato in sbieco, che sfiora invece di fasciare. Prima la cena, poi il ballo. Spalline regolabili, schiena scoperta e orlo sotto il ginocchio. Lavaggio a secco o a mano in acqua fredda."),
    'Harbour shirt dress': ('Robe chemise Harbour', 'Harbour Hemdblusenkleid', 'Abito camicia Harbour'),
    'A cotton poplin shirt dress with a belted waist and a full skirt. Crisp poplin with a self belt and side pockets. Machine wash cold.': (
        "Une robe chemise en popeline de coton, ceinture à la taille et jupe ample. Une popeline nette, avec une ceinture assortie et des poches sur les côtés. Lavage en machine à froid.",
        'Ein Hemdblusenkleid aus Baumwollpopeline mit Gürtel und weitem Rock. Knackige Popeline mit Stoffgürtel und Seitentaschen. Kalt in der Maschine waschen.',
        'Un abito camicia in popeline di cotone, con cintura in vita e gonna ampia. Popeline compatto, cintura in tinta e tasche laterali. Lavaggio in lavatrice a freddo.'),
    'Sable pleated skirt': ('Jupe plissée Sable', 'Sable Plisseerock', 'Gonna plissé Sable'),
    'A knife-pleated midi skirt in recycled satin, with an elastic waistband. The pleats are heat set and survive the wash. The hem sits below the knee.': (
        "Une jupe midi à plis couchés en satin recyclé, avec une taille élastique. Les plis sont thermofixés et résistent au lavage. L'ourlet tombe sous le genou.",
        'Ein Midirock mit Kellerfalten aus recyceltem Satin, mit Gummibund. Die Falten sind thermofixiert und überstehen die Wäsche. Der Saum sitzt unter dem Knie.',
        'Una gonna midi a pieghe piatte in raso riciclato, con elastico in vita. Le pieghe sono fissate a caldo e resistono al lavaggio. Lorlo cade sotto il ginocchio.'),
    'Salt denim skirt': ('Jupe en jean Salt', 'Salt Jeansrock', 'Gonna di jeans Salt'),
    'An A-line denim mini skirt with patch pockets, in a mid wash. Rigid denim with a front button fly and a raw hem. It sits at the natural waist.': (
        "Une mini-jupe en jean trapèze avec des poches plaquées, dans un lavage moyen. Un denim rigide avec une braguette à boutons et un bas brut. Elle se porte à la taille naturelle.",
        'Ein Jeans-Minirock in A-Linie mit aufgesetzten Taschen, in mittlerer Waschung. Fester Denim mit Knopfleiste vorn und offenem Saum. Er sitzt in der natürlichen Taille.',
        'Una minigonna di jeans a trapezio con tasche applicate, in lavaggio medio. Denim rigido con patta a bottoni davanti e fondo vivo. Sta in vita naturale.'),
    'Ashford linen camp shirt': ('Chemise camp en lin Ashford', 'Ashford Leinen-Campshirt', 'Camicia camp di lino Ashford'),
    'A washed linen shirt with a one-piece collar. Roll the sleeves, forget the iron. Garment washed for softness, with a chest pocket and a straight hem. Machine wash cold.': (
        "Une chemise en lin lavé, col une pièce. Remontez les manches, oubliez le fer. Lavée après confection pour la souplesse, avec une poche poitrine et un bas droit. Lavage en machine à froid.",
        'Ein gewaschenes Leinenhemd mit einteiligem Kragen. Ärmel hochkrempeln, Bügeleisen vergessen. Stückgewaschen für Weichheit, mit Brusttasche und geradem Saum. Kalt in der Maschine waschen.',
        'Una camicia di lino lavato, con collo in un pezzo. Arrotola le maniche e dimentica il ferro. Lavata in capo per la morbidezza, con taschino e fondo dritto. Lavaggio in lavatrice a freddo.'),
    'Halden oxford shirt': ('Chemise oxford Halden', 'Halden Oxfordhemd', 'Camicia oxford Halden'),
    'A button-down oxford in brushed organic cotton, cut slim through the body. A 150 g oxford cloth with a soft roll collar and a locker loop. Machine wash warm.': (
        "Une chemise oxford à col boutonné, en coton biologique gratté, ajustée au corps. Un tissu oxford de 150 g avec un col souple qui roule et une patte au dos. Lavage en machine à chaud.",
        'Ein Button-down-Oxford aus gebürsteter Biobaumwolle, schmal geschnitten. Ein 150-g-Oxfordstoff mit weichem Rollkragen und Aufhängeschlaufe. Warm in der Maschine waschen.',
        'Una camicia oxford con collo button-down, in cotone biologico spazzolato, tagliata aderente. Un tessuto oxford da 150 g con collo morbido che si arrotola e asola sul retro. Lavaggio in lavatrice a caldo.'),
    'Bruma Sol camp shirt': ('Chemise camp Bruma Sol', 'Bruma Sol Campshirt', 'Camicia camp Bruma Sol'),
    'A short-sleeved camp collar shirt in a woven cotton, with a straight hem. A loose fit in a light woven cotton with a single chest pocket. Machine wash cold.': (
        "Une chemise à col camp et manches courtes, en coton tissé, avec un bas droit. Une coupe ample dans un coton tissé léger, avec une seule poche poitrine. Lavage en machine à froid.",
        'Ein kurzärmeliges Hemd mit Campkragen aus gewebter Baumwolle und geradem Saum. Eine lockere Passform in leichter Webbaumwolle mit einer Brusttasche. Kalt in der Maschine waschen.',
        'Una camicia a maniche corte con collo camp, in cotone tessuto e fondo dritto. Vestibilità ampia in un cotone leggero, con un solo taschino. Lavaggio in lavatrice a freddo.'),
    'Fjordline flannel shirt': ('Chemise en flanelle Fjordline', 'Fjordline Flanellhemd', 'Camicia di flanella Fjordline'),
    'A brushed flannel overshirt in a muted check, with two chest pockets. Heavy brushed cotton with a rounded hem, cut to wear open over a tee. Machine wash cold.': (
        "Une surchemise en flanelle grattée à carreaux discrets, avec deux poches poitrine. Un coton gratté épais au bas arrondi, coupé pour se porter ouvert sur un t-shirt. Lavage en machine à froid.",
        'Ein Overshirt aus gebürstetem Flanell in gedecktem Karo, mit zwei Brusttaschen. Schwere gebürstete Baumwolle mit rundem Saum, zum offenen Tragen über einem Shirt. Kalt in der Maschine waschen.',
        'Una sovracamicia di flanella spazzolata a quadri discreti, con due taschini. Cotone spazzolato pesante con fondo arrotondato, pensata per stare aperta su una t-shirt. Lavaggio in lavatrice a freddo.'),
    'Harbour crew tee': ('T-shirt col rond Harbour', 'Harbour Rundhalsshirt', 'T-shirt girocollo Harbour'),
    'A heavyweight organic cotton tee with a ribbed crew neck. Buy two. A 220 g jersey with a rib neck that keeps its shape. It shrinks a touch on the first wash, then stays put.': (
        "Un t-shirt épais en coton biologique, col rond côtelé. Prenez-en deux. Un jersey de 220 g dont l'encolure côtelée garde sa forme. Il rétrécit un peu au premier lavage, puis ne bouge plus.",
        'Ein schweres Shirt aus Biobaumwolle mit geripptem Rundhals. Kauf zwei davon. Ein 220-g-Jersey, dessen Rippkragen die Form hält. Es geht bei der ersten Wäsche etwas ein und bleibt danach so.',
        'Una t-shirt pesante in cotone biologico con girocollo a coste. Prendine due. Una jersey da 220 g con collo a coste che tiene la forma. Si ritira un poco al primo lavaggio, poi resta così.'),
    'Meridian pique polo': ('Polo piqué Meridian', 'Meridian Piqué-Polo', 'Polo in piqué Meridian'),
    'A pique polo with a two-button placket, cut from long-staple cotton. A fine pique that breathes, with a rib collar and a straight hem. Machine wash cold.': (
        "Un polo en piqué à patte deux boutons, coupé dans un coton à fibres longues. Un piqué fin qui respire, avec un col côtelé et un bas droit. Lavage en machine à froid.",
        'Ein Piqué-Polo mit Zweiknopfleiste aus langstapeliger Baumwolle. Ein feines Piqué, das atmet, mit Rippkragen und geradem Saum. Kalt in der Maschine waschen.',
        'Una polo in piqué con cannoncino a due bottoni, in cotone a fibra lunga. Un piqué fine che respira, con collo a coste e fondo dritto. Lavaggio in lavatrice a freddo.'),
    'Nordlys merino crew': ('Pull col rond mérinos Nordlys', 'Nordlys Merino-Rundhals', 'Maglia girocollo in merino Nordlys'),
    'A fine-gauge merino crew neck that layers under a jacket without bulk. Extra fine merino at 19 microns, so it does not itch. Hand wash or wool cycle.': (
        "Un pull col rond en mérinos fin qui se porte sous une veste sans épaisseur. Un mérinos extra-fin de 19 microns, qui ne gratte pas. Lavage à la main ou cycle laine.",
        'Ein feiner Merino-Rundhalspullover, der unter der Jacke nicht aufträgt. Extrafeines Merino mit 19 Mikron, das nicht kratzt. Handwäsche oder Wollprogramm.',
        'Una maglia girocollo in merino fine che sta sotto una giacca senza fare volume. Merino extrafine da 19 micron, quindi non punge. Lavaggio a mano o programma lana.'),
    'Nordlys shawl cardigan': ('Cardigan col châle Nordlys', 'Nordlys Schalkragenjacke', 'Cardigan con collo a scialle Nordlys'),
    'A chunky shawl-collar cardigan in a wool and alpaca blend, with horn buttons. A heavy five-gauge knit with a shawl collar and two patch pockets. Hand wash or wool cycle.': (
        "Un gros cardigan à col châle en mélange laine et alpaga, avec des boutons en corne. Une maille lourde de jauge cinq, col châle et deux poches plaquées. Lavage à la main ou cycle laine.",
        'Eine dicke Strickjacke mit Schalkragen aus Wolle und Alpaka, mit Hornknöpfen. Ein schwerer Strick in Feinheit fünf, mit Schalkragen und zwei aufgesetzten Taschen. Handwäsche oder Wollprogramm.',
        'Un cardigan pesante con collo a scialle in misto lana e alpaca, con bottoni in corno. Una maglia grossa di finezza cinque, collo a scialle e due tasche applicate. Lavaggio a mano o programma lana.'),
    'Coast waffle henley': ('Henley nid-abeille Coast', 'Coast Waffel-Henley', 'Henley a nido dape Coast'),
    'A long-sleeved waffle knit henley with a three-button placket. Thermal waffle cotton that traps warmth without weight. Machine wash warm.': (
        "Un henley à manches longues en maille nid-d'abeille, patte à trois boutons. Un coton gaufré thermique qui retient la chaleur sans peser. Lavage en machine à chaud.",
        'Ein langärmeliger Henley aus Waffelstrick mit Dreiknopfleiste. Thermische Waffelbaumwolle, die Wärme hält, ohne aufzutragen. Warm in der Maschine waschen.',
        "Una henley a maniche lunghe in maglia a nido d'ape, con cannoncino a tre bottoni. Cotone waffle termico che trattiene il calore senza pesare. Lavaggio in lavatrice a caldo."),
    'Coast chinos': ('Chino Coast', 'Coast Chino', 'Chino Coast'),
    'Garment-dyed cotton twill chinos with a tapered leg and a touch of stretch. A 280 g twill, garment dyed and washed for a soft hand. Machine wash cold.': (
        "Un chino en sergé de coton teint en pièce, jambe fuselée et une pointe d'élasthanne. Un sergé de 280 g, teint et lavé après confection pour un toucher doux. Lavage en machine à froid.",
        'Ein Chino aus stückgefärbtem Baumwolltwill mit schmal zulaufendem Bein und etwas Stretch. Ein 280-g-Twill, stückgefärbt und gewaschen für einen weichen Griff. Kalt in der Maschine waschen.',
        'Un chino in twill di cotone tinto in capo, con gamba affusolata e un pizzico di elastico. Un twill da 280 g, tinto e lavato in capo per una mano morbida. Lavaggio in lavatrice a freddo.'),
    'Fjordline selvedge jeans': ('Jean selvedge Fjordline', 'Fjordline Selvedge Jeans', 'Jeans selvedge Fjordline'),
    'Raw selvedge denim with a regular fit and a straight leg. Wear them in. A 14 oz Japanese selvedge with a button fly and a red line on the outseam. Wash rarely and cold.': (
        "Un denim selvedge brut, coupe droite et jambe droite. À vous de le façonner. Un selvedge japonais de 14 oz, braguette à boutons et liseré rouge sur la couture extérieure. Lavez-le rarement et à froid.",
        'Roher Selvedge-Denim in normaler Passform mit geradem Bein. Trag ihn ein. Ein japanischer 14-oz-Selvedge mit Knopfleiste und roter Linie an der Außennaht. Selten und kalt waschen.',
        "Denim selvedge grezzo, vestibilità regolare e gamba dritta. Falli tuoi con l'uso. Un selvedge giapponese da 14 oz con patta a bottoni e cimosa rossa sulla cucitura esterna. Lavare di rado e a freddo."),
    'Sand linen trousers': ('Pantalon en lin Sand', 'Sand Leinenhose', 'Pantaloni di lino Sand'),
    'Drawstring linen trousers with a relaxed leg. Airport to beach without a change. An elastic and drawstring waist with a relaxed leg and a cropped hem. Machine wash cold.': (
        "Un pantalon en lin à cordon de serrage, jambe décontractée. De l'aéroport à la plage sans se changer. Une taille élastique à cordon, une jambe ample et un bas raccourci. Lavage en machine à froid.",
        'Eine Leinenhose mit Kordelzug und lockerem Bein. Vom Flughafen an den Strand ohne Umziehen. Ein Gummibund mit Kordel, ein lockeres Bein und ein verkürzter Saum. Kalt in der Maschine waschen.',
        "Pantaloni di lino con coulisse e gamba morbida. Dall'aeroporto alla spiaggia senza cambiarsi. Vita elastica con coulisse, gamba comoda e fondo accorciato. Lavaggio in lavatrice a freddo."),
    'Harbour cargo shorts': ('Short cargo Harbour', 'Harbour Cargoshorts', 'Shorts cargo Harbour'),
    'Ripstop cotton cargo shorts with bellows pockets and a nine-inch inseam. A 200 g ripstop with two front pockets, two bellows pockets and a rear pocket. Machine wash cold.': (
        "Un short cargo en coton ripstop, poches à soufflet et entrejambe de vingt-trois centimètres. Un ripstop de 200 g avec deux poches devant, deux poches à soufflet et une poche arrière. Lavage en machine à froid.",
        'Cargoshorts aus Ripstop-Baumwolle mit Balgtaschen und 23 Zentimetern Innenbeinlänge. Ein 200-g-Ripstop mit zwei Vordertaschen, zwei Balgtaschen und einer Gesäßtasche. Kalt in der Maschine waschen.',
        'Shorts cargo in cotone ripstop, con tasche a soffietto e cavallo di ventitré centimetri. Un ripstop da 200 g con due tasche davanti, due a soffietto e una dietro. Lavaggio in lavatrice a freddo.'),
    'Ashford linen blazer': ('Veste en lin Ashford', 'Ashford Leinenblazer', 'Giacca di lino Ashford'),
    'An unstructured linen blazer with patch pockets and a half lining. Creases are part of the look. No shoulder pads, a single vent and a half lining in cotton. Dry clean or steam.': (
        "Une veste en lin déstructurée, poches plaquées et demi-doublure. Les plis font partie du style. Sans épaulettes, une fente au dos et une demi-doublure en coton. Nettoyage à sec ou vapeur.",
        'Ein unkonstruierter Leinenblazer mit aufgesetzten Taschen und Halbfutter. Knitter gehören dazu. Ohne Schulterpolster, mit einem Rückenschlitz und Halbfutter aus Baumwolle. Chemisch reinigen oder dämpfen.',
        'Una giacca di lino destrutturata, con tasche applicate e mezza fodera. Le pieghe fanno parte del look. Senza spalline, con uno spacco dietro e mezza fodera in cotone. Lavaggio a secco o vapore.'),
    'Nordlys knit blazer': ('Veste en maille Nordlys', 'Nordlys Strickblazer', 'Giacca in maglia Nordlys'),
    'A jersey knit blazer in merino wool that moves like a cardigan and looks like a jacket. A milano-stitch merino with patch pockets and no lining. Hand wash or wool cycle.': (
        "Une veste en maille de mérinos qui bouge comme un cardigan et se porte comme une veste. Un mérinos point milano, poches plaquées et sans doublure. Lavage à la main ou cycle laine.",
        'Ein Strickblazer aus Merinowolle, der sich wie eine Strickjacke bewegt und wie ein Sakko aussieht. Ein Merino im Milanostich mit aufgesetzten Taschen und ohne Futter. Handwäsche oder Wollprogramm.',
        'Una giacca in maglia di merino che si muove come un cardigan e sembra una giacca. Un merino a punto milano con tasche applicate e senza fodera. Lavaggio a mano o programma lana.'),
    'Halden field jacket': ('Veste de terrain Halden', 'Halden Fieldjacket', 'Giacca field Halden'),
    'A four-pocket field jacket in waxed cotton with a corduroy collar. Waxed cotton that sheds rain and darkens with age. Re-wax it once a year and it lasts decades.': (
        "Une veste de terrain à quatre poches en coton huilé, col en velours côtelé. Un coton huilé qui repousse la pluie et fonce avec le temps. Réhuilez-la une fois par an et elle dure des décennies.",
        'Eine Fieldjacket mit vier Taschen aus gewachster Baumwolle und Cordkragen. Gewachste Baumwolle, die Regen abweist und mit den Jahren nachdunkelt. Einmal im Jahr nachwachsen und sie hält Jahrzehnte.',
        'Una giacca field a quattro tasche in cotone cerato, con collo in velluto a coste. Cotone cerato che respinge la pioggia e si scurisce con gli anni. Ricera una volta lanno e dura decenni.'),
    'Ottavia round sunglasses': ('Lunettes de soleil rondes Ottavia', 'Ottavia Sonnenbrille, rund', 'Occhiali da sole tondi Ottavia'),
    'Round acetate sunglasses with polarised lenses and a keyhole bridge. Hand-polished acetate with five-barrel hinges and category three lenses. A hard case and a cloth are included.': (
        "Des lunettes de soleil rondes en acétate, verres polarisés et pont en trou de serrure. Un acétate poli à la main, charnières à cinq tenons et verres de catégorie trois. Un étui rigide et un chiffon sont inclus.",
        'Eine runde Sonnenbrille aus Acetat mit polarisierten Gläsern und Keyhole-Steg. Handpoliertes Acetat mit Fünfnietscharnieren und Gläsern der Kategorie drei. Hartschalenetui und Tuch liegen bei.',
        'Occhiali da sole tondi in acetato, con lenti polarizzate e ponte a goccia. Acetato lucidato a mano, cerniere a cinque perni e lenti di categoria tre. Custodia rigida e panno inclusi.'),
    'Ottavia aviator sunglasses': ('Lunettes de soleil aviateur Ottavia', 'Ottavia Pilotenbrille', 'Occhiali da sole aviator Ottavia'),
    'Slim steel aviators with green glass lenses and a double bridge. Steel frames with adjustable nose pads and mineral glass lenses. A hard case and a cloth are included.': (
        "Des lunettes aviateur fines en acier, verres minéraux verts et double pont. Une monture en acier avec plaquettes réglables et verres en verre minéral. Un étui rigide et un chiffon sont inclus.",
        'Eine schmale Pilotenbrille aus Stahl mit grünen Glasgläsern und Doppelsteg. Stahlfassung mit verstellbaren Nasenpads und mineralischen Gläsern. Hartschalenetui und Tuch liegen bei.',
        'Occhiali aviator sottili in acciaio, con lenti in vetro verde e doppio ponte. Montatura in acciaio con naselli regolabili e lenti minerali. Custodia rigida e panno inclusi.'),
    'Ottavia square sunglasses': ('Lunettes de soleil carrées Ottavia', 'Ottavia Sonnenbrille, eckig', 'Occhiali da sole quadrati Ottavia'),
    'Bold square sunglasses in polished acetate with grey gradient lenses. Thick acetate frames with a keyhole bridge and category three lenses. A hard case and a cloth are included.': (
        "Des lunettes de soleil carrées affirmées en acétate poli, verres gris dégradés. Une monture épaisse en acétate avec un pont en trou de serrure et des verres de catégorie trois. Un étui rigide et un chiffon sont inclus.",
        'Eine markante eckige Sonnenbrille aus poliertem Acetat mit grauen Verlaufsgläsern. Dicke Acetatfassung mit Keyhole-Steg und Gläsern der Kategorie drei. Hartschalenetui und Tuch liegen bei.',
        'Occhiali da sole quadrati e decisi in acetato lucido, con lenti grigie sfumate. Montatura spessa in acetato con ponte a goccia e lenti di categoria tre. Custodia rigida e panno inclusi.'),
    'Ottavia reading glasses': ('Lunettes de lecture Ottavia', 'Ottavia Lesebrille', 'Occhiali da lettura Ottavia'),
    'Lightweight reading glasses in a panto shape, with a cloth case. Available from +1.0 to +3.0 in half steps. The lenses are scratch coated.': (
        "Des lunettes de lecture légères de forme panto, avec un étui en tissu. Disponibles de +1,0 à +3,0 par demi-degrés. Les verres reçoivent un traitement anti-rayures.",
        'Eine leichte Lesebrille in Panto-Form, mit Stoffetui. Erhältlich von +1,0 bis +3,0 in halben Schritten. Die Gläser sind kratzfest beschichtet.',
        'Occhiali da lettura leggeri di forma panto, con custodia in tessuto. Disponibili da +1,0 a +3,0 a mezzi passi. Le lenti hanno un trattamento antigraffio.'),
    'Meridian curb chain': ('Chaîne gourmette Meridian', 'Meridian Panzerkette', 'Catena grumette Meridian'),
    'A slim curb chain in gold-plated sterling silver, 45 cm. A 3 mm curb link with a lobster clasp, plated in 18 karat gold. Wear it alone or under a shirt.': (
        "Une fine chaîne gourmette en argent massif plaqué or, 45 cm. Une maille gourmette de 3 mm avec un fermoir mousqueton, plaquée or 18 carats. À porter seule ou sous une chemise.",
        'Eine schmale Panzerkette aus vergoldetem Sterlingsilber, 45 cm. Ein 3-mm-Panzerglied mit Karabinerverschluss, vergoldet mit 18 Karat. Allein oder unter dem Hemd zu tragen.',
        'Una catena grumette sottile in argento sterling dorato, 45 cm. Maglia grumette da 3 mm con chiusura a moschettone, placcata in oro 18 carati. Da portare da sola o sotto la camicia.'),
    'Halden signet ring': ('Chevalière Halden', 'Halden Siegelring', 'Anello chevalier Halden'),
    'A square signet ring in solid sterling silver, plain face for engraving. A 12 mm square face, polished, on a solid band. Engraving is free and takes three days.': (
        "Une chevalière carrée en argent massif, plateau lisse à graver. Un plateau carré de 12 mm, poli, sur un anneau plein. La gravure est offerte et prend trois jours.",
        'Ein eckiger Siegelring aus massivem Sterlingsilber, mit glatter Platte zum Gravieren. Eine 12-mm-Quadratplatte, poliert, auf einem massiven Ring. Die Gravur ist kostenlos und dauert drei Tage.',
        "Un anello chevalier quadrato in argento sterling massiccio, con piano liscio da incidere. Piano quadrato da 12 mm, lucido, su una fascia piena. L'incisione è gratuita e richiede tre giorni."),
    'Bruma Sol hoops': ('Créoles Bruma Sol', 'Bruma Sol Creolen', 'Cerchi Bruma Sol'),
    'Medium hammered hoop earrings in gold-plated brass. Thirty millimetre hoops with a hinged closure, plated in 18 karat gold. Sold as a pair.': (
        "Des créoles moyennes martelées en laiton plaqué or. Des anneaux de trente millimètres à fermeture à charnière, plaqués or 18 carats. Vendues par paire.",
        'Mittelgroße gehämmerte Creolen aus vergoldetem Messing. Dreißig Millimeter Durchmesser, mit Scharnierverschluss, vergoldet mit 18 Karat. Als Paar verkauft.',
        'Cerchi medi martellati in ottone dorato. Cerchi da trenta millimetri con chiusura a cerniera, placcati in oro 18 carati. Venduti in coppia.'),
    'Coast rope bracelet': ('Bracelet corde Coast', 'Coast Segeltau-Armband', 'Bracciale in corda Coast'),
    'A braided nylon rope bracelet with a stainless steel shackle clasp. Nylon rope from a sailmaker, with a shackle that opens with a coin. One size, adjusts with the knot.': (
        "Un bracelet en corde de nylon tressée avec une manille en acier inoxydable. Une corde de nylon de voilier, avec une manille qui s'ouvre avec une pièce. Taille unique, réglable par le nœud.",
        'Ein Armband aus geflochtenem Nylonseil mit Schäkelverschluss aus Edelstahl. Nylonseil vom Segelmacher, mit einem Schäkel, der sich mit einer Münze öffnet. Eine Größe, über den Knoten verstellbar.',
        'Un bracciale in corda di nylon intrecciata con grillo in acciaio inossidabile. Corda di nylon da velaio, con un grillo che si apre con una moneta. Taglia unica, si regola con il nodo.'),
    'Halden leather sandals': ('Sandales en cuir Halden', 'Halden Ledersandalen', 'Sandali di pelle Halden'),
    'Flat leather sandals with two straps and a moulded footbed. Vegetable-tanned leather uppers on a cork footbed with a rubber sole. They mould to the foot in a week.': (
        "Des sandales plates en cuir à deux brides, avec une semelle moulée. Une tige en cuir à tannage végétal sur un lit de liège et une semelle en caoutchouc. Elles épousent le pied en une semaine.",
        'Flache Ledersandalen mit zwei Riemen und geformtem Fußbett. Pflanzlich gegerbtes Obermaterial auf einem Korkfußbett mit Gummisohle. Sie passen sich in einer Woche dem Fuß an.',
        'Sandali bassi in pelle a due fasce, con plantare sagomato. Tomaia in pelle conciata al vegetale su plantare di sughero e suola in gomma. Si adattano al piede in una settimana.'),
    'Harbour canvas sneakers': ('Baskets en toile Harbour', 'Harbour Canvas-Sneaker', 'Sneaker di tela Harbour'),
    'Low canvas sneakers with a natural rubber sole and cotton laces. Heavy cotton canvas on a vulcanised natural rubber sole. Wipe clean, or machine wash cold in a bag.': (
        "Des baskets basses en toile, semelle en caoutchouc naturel et lacets en coton. Une toile de coton épaisse sur une semelle vulcanisée en caoutchouc naturel. Un coup de chiffon, ou lavage en machine à froid dans un filet.",
        'Niedrige Canvas-Sneaker mit Naturkautschuksohle und Baumwollschnürsenkeln. Schweres Baumwollcanvas auf einer vulkanisierten Naturkautschuksohle. Abwischen oder kalt im Beutel in der Maschine waschen.',
        'Sneaker basse di tela, con suola in caucciù naturale e lacci di cotone. Tela di cotone pesante su una suola vulcanizzata in caucciù naturale. Si puliscono con un panno, oppure in lavatrice a freddo dentro un sacchetto.'),
    'Halden penny loafers': ('Mocassins Halden', 'Halden Pennyloafer', 'Mocassini Halden'),
    'Penny loafers in full-grain leather with a stacked heel. Full-grain leather, a leather sole with a rubber insert and a stacked leather heel. Made in Portugal.': (
        "Des mocassins en cuir pleine fleur avec un talon empilé. Cuir pleine fleur, semelle en cuir avec insert en caoutchouc et talon en cuir empilé. Fabriqués au Portugal.",
        'Pennyloafer aus Vollnarbenleder mit gestapeltem Absatz. Vollnarbenleder, eine Ledersohle mit Gummieinsatz und ein gestapelter Lederabsatz. In Portugal gefertigt.',
        'Mocassini in pelle pieno fiore con tacco accatastato. Pelle pieno fiore, suola in cuoio con inserto in gomma e tacco in cuoio accatastato. Prodotti in Portogallo.'),
    'Bruma Sol espadrilles': ('Espadrilles Bruma Sol', 'Bruma Sol Espadrilles', 'Espadrillas Bruma Sol'),
    'Canvas espadrilles with a jute sole, made in Spain. Cotton canvas stitched by hand to a jute sole with a thin rubber tread. Buy them snug, they stretch.': (
        "Des espadrilles en toile à semelle de jute, fabriquées en Espagne. Une toile de coton cousue à la main sur une semelle de jute avec une fine bande de caoutchouc. Prenez-les serrées, elles se détendent.",
        'Espadrilles aus Canvas mit Jutesohle, in Spanien gefertigt. Baumwollcanvas, von Hand auf eine Jutesohle mit dünner Gummilaufsohle genäht. Eng kaufen, sie weiten sich.',
        'Espadrillas di tela con suola in juta, prodotte in Spagna. Tela di cotone cucita a mano su una suola di juta con sottile battistrada in gomma. Prendile strette, si allargano.'),
    'Fjordline chelsea boots': ('Bottines chelsea Fjordline', 'Fjordline Chelsea Boots', 'Stivaletti chelsea Fjordline'),
    'Suede chelsea boots with a crepe sole and elastic side panels. Suede uppers on a crepe sole that softens every step. Spray them before the first wear.': (
        "Des bottines chelsea en daim, semelle en crêpe et soufflets élastiques. Une tige en daim sur une semelle de crêpe qui adoucit chaque pas. Imperméabilisez-les avant le premier port.",
        'Chelsea Boots aus Veloursleder mit Kreppsohle und elastischen Seiteneinsätzen. Velours-Obermaterial auf einer Kreppsohle, die jeden Schritt weicher macht. Vor dem ersten Tragen imprägnieren.',
        'Stivaletti chelsea in camoscio, con suola in crepe ed elastici laterali. Tomaia in camoscio su una suola in crepe che ammorbidisce ogni passo. Trattali con lo spray prima di indossarli.'),
    'Halden leather weekender': ('Sac week-end en cuir Halden', 'Halden Leder-Reisetasche', 'Borsone di pelle Halden'),
    'A full-grain leather weekender with a brass zip and a detachable strap. Fits under the seat. Fifty centimetres wide with a cotton lining and an inside zip pocket. The leather scuffs and darkens with age.': (
        "Un sac week-end en cuir pleine fleur, fermeture en laiton et bandoulière amovible. Il passe sous le siège. Cinquante centimètres de large, doublure en coton et poche zippée intérieure. Le cuir se patine et fonce avec le temps.",
        'Eine Reisetasche aus Vollnarbenleder mit Messingreißverschluss und abnehmbarem Gurt. Passt unter den Sitz. Fünfzig Zentimeter breit, mit Baumwollfutter und Innenreißverschlusstasche. Das Leder bekommt Spuren und dunkelt nach.',
        'Un borsone in pelle pieno fiore, con zip in ottone e tracolla staccabile. Entra sotto il sedile. Cinquanta centimetri di larghezza, fodera in cotone e tasca interna con zip. La pelle si segna e si scurisce con gli anni.'),
    'Meridian crossbody bag': ('Sac bandoulière Meridian', 'Meridian Umhängetasche', 'Borsa a tracolla Meridian'),
    'A compact leather crossbody bag with a flap and an adjustable strap. Full-grain leather with a magnetic flap and a card slot inside. The strap adjusts from 100 to 130 cm.': (
        "Un petit sac bandoulière en cuir avec un rabat et une sangle réglable. Cuir pleine fleur, rabat aimanté et un porte-carte à l'intérieur. La sangle se règle de 100 à 130 cm.",
        'Eine kompakte Umhängetasche aus Leder mit Überschlag und verstellbarem Gurt. Vollnarbenleder mit Magnetlasche und einem Kartenfach innen. Der Gurt lässt sich von 100 auf 130 cm einstellen.',
        "Una piccola borsa a tracolla in pelle, con patta e tracolla regolabile. Pelle pieno fiore, patta magnetica e uno scomparto per le carte all'interno. La tracolla si regola da 100 a 130 cm."),
    'Harbour canvas tote': ('Tote bag en toile Harbour', 'Harbour Canvas-Shopper', 'Shopper di tela Harbour'),
    'A heavy canvas tote with leather handles and an inside pocket. A 20 oz canvas that stands on its own, with a magnetic closure. Machine wash cold, the leather handles included.': (
        "Un tote bag en toile épaisse avec des anses en cuir et une poche intérieure. Une toile de 20 oz qui tient debout toute seule, avec une fermeture aimantée. Lavage en machine à froid, anses en cuir comprises.",
        'Ein schwerer Canvas-Shopper mit Ledergriffen und Innentasche. Ein 20-oz-Canvas, das von allein steht, mit Magnetverschluss. Kalt in der Maschine waschen, samt Ledergriffen.',
        'Uno shopper in tela pesante con manici di pelle e tasca interna. Una tela da 20 oz che sta in piedi da sola, con chiusura magnetica. Lavaggio in lavatrice a freddo, manici di pelle compresi.'),
    'Fjordline cabin case': ('Valise cabine Fjordline', 'Fjordline Kabinenkoffer', 'Trolley da cabina Fjordline'),
    'A hard-shell cabin case in recycled polycarbonate with silent wheels and a TSA lock. Fifty-five by thirty-five by twenty centimetres, 2.8 kg, with four double wheels. The shell dents and pops back.': (
        "Une valise cabine rigide en polycarbonate recyclé, roues silencieuses et serrure TSA. Cinquante-cinq sur trente-cinq sur vingt centimètres, 2,8 kg, avec quatre roues doubles. La coque se creuse puis reprend sa forme.",
        'Ein Hartschalen-Kabinenkoffer aus recyceltem Polycarbonat mit leisen Rollen und TSA-Schloss. Fünfundfünfzig mal fünfunddreißig mal zwanzig Zentimeter, 2,8 kg, mit vier Doppelrollen. Die Schale gibt nach und springt zurück.',
        'Un trolley da cabina rigido in policarbonato riciclato, con ruote silenziose e serratura TSA. Cinquantacinque per trentacinque per venti centimetri, 2,8 kg, con quattro ruote doppie. Il guscio si ammacca e torna come prima.'),
    'Coast daypack': ('Sac à dos Coast', 'Coast Tagesrucksack', 'Zaino da giorno Coast'),
    'A 20-litre daypack in recycled nylon with a padded laptop sleeve. A padded back, a fifteen-inch laptop sleeve and a water bottle pocket. The fabric is made from recycled bottles.': (
        "Un sac à dos de 20 litres en nylon recyclé, avec un compartiment matelassé pour ordinateur. Un dos matelassé, une housse pour portable de quinze pouces et une poche pour gourde. Le tissu est fait de bouteilles recyclées.",
        'Ein 20-Liter-Tagesrucksack aus recyceltem Nylon mit gepolstertem Laptopfach. Ein gepolsterter Rücken, ein Fach für fünfzehn Zoll und eine Flaschentasche. Der Stoff besteht aus recycelten Flaschen.',
        'Uno zaino da 20 litri in nylon riciclato, con scomparto imbottito per il portatile. Schienale imbottito, tasca per portatili da quindici pollici e porta borraccia. Il tessuto è fatto di bottiglie riciclate.'),

    # Electronics
    'Kestrel K2 noise-cancelling headphones': ('Casque à réduction de bruit Kestrel K2', 'Kestrel K2 Kopfhörer mit Geräuschunterdrückung', 'Cuffie con cancellazione del rumore Kestrel K2'),
    'Over-ear headphones with adaptive noise cancelling, forty hours of battery and a flat tuning. Fold flat into a hard case, charge by USB-C, and the cancelling adapts to a plane or a train. The tuning is flat, so what you hear is the recording.': (
        "Un casque circum-auriculaire à réduction de bruit adaptative, quarante heures d'autonomie et un réglage neutre. Il se plie à plat dans un étui rigide, se charge en USB-C, et la réduction s'adapte à l'avion ou au train. Le réglage est neutre, vous entendez donc l'enregistrement.",
        'Ein Over-Ear-Kopfhörer mit adaptiver Geräuschunterdrückung, vierzig Stunden Akku und neutraler Abstimmung. Er faltet flach ins Hartschalenetui, lädt über USB-C, und die Unterdrückung passt sich Flugzeug oder Zug an. Die Abstimmung ist neutral, du hörst also die Aufnahme.',
        "Cuffie circumaurali con cancellazione adattiva del rumore, quaranta ore di autonomia e una taratura neutra. Si piegano piatte nella custodia rigida, si caricano via USB-C e la cancellazione si adatta all'aereo o al treno. La taratura è neutra, quindi senti la registrazione."),
    'Kestrel Buds': ('Écouteurs Kestrel Buds', 'Kestrel Buds', 'Auricolari Kestrel Buds'),
    'True wireless earbuds with a six-hour charge and a case that adds three more. The buds seal well and the microphones handle a windy call. The case charges wirelessly or by USB-C.': (
        "Des écouteurs sans fil de six heures d'autonomie, avec un boîtier qui en ajoute trois. Ils isolent bien et les micros tiennent un appel dans le vent. Le boîtier se recharge sans fil ou en USB-C.",
        'Kabellose Ohrhörer mit sechs Stunden Laufzeit und einem Etui, das drei weitere gibt. Sie dichten gut ab und die Mikrofone halten ein Gespräch im Wind aus. Das Etui lädt kabellos oder über USB-C.',
        "Auricolari true wireless con sei ore di carica e una custodia che ne aggiunge altre tre. Isolano bene e i microfoni reggono una chiamata con il vento. La custodia si carica senza fili o via USB-C."),
    'Kestrel Studio in-ear monitors': ('Moniteurs intra-auriculaires Kestrel Studio', 'Kestrel Studio In-Ear-Monitore', 'Monitor in-ear Kestrel Studio'),
    'Wired in-ear monitors with a single dynamic driver and a detachable cable. A single driver keeps the sound coherent from bass to treble. The cable unclips, so a broken cable is not a broken pair.': (
        "Des moniteurs intra-auriculaires filaires à transducteur dynamique unique et câble détachable. Un seul transducteur garde un son cohérent des graves aux aigus. Le câble se déclipse, un câble cassé ne signifie donc pas une paire perdue.",
        'Kabelgebundene In-Ear-Monitore mit einem einzigen dynamischen Treiber und abnehmbarem Kabel. Ein einziger Treiber hält den Klang von Bass bis Höhen stimmig. Das Kabel klickt ab, ein Kabelbruch ist also kein Totalschaden.',
        'Monitor in-ear con cavo, driver dinamico singolo e cavo staccabile. Un solo driver mantiene il suono coerente dai bassi agli acuti. Il cavo si sgancia, quindi un cavo rotto non è un paio rotto.'),
    'Nimbus Go speaker': ('Enceinte Nimbus Go', 'Nimbus Go Lautsprecher', 'Speaker Nimbus Go'),
    'A pocket speaker with a real passive radiator, twelve hours of play and an IP67 rating. It survives a pool and a beach, and pairs with a second unit for stereo. Twelve hours at normal volume.': (
        "Une enceinte de poche avec un vrai radiateur passif, douze heures de lecture et un indice IP67. Elle survit à la piscine et à la plage, et s'apparie avec une deuxième pour la stéréo. Douze heures à volume normal.",
        'Ein Taschenlautsprecher mit echtem Passivradiator, zwölf Stunden Spielzeit und IP67. Er übersteht Pool und Strand und lässt sich mit einem zweiten zu Stereo koppeln. Zwölf Stunden bei normaler Lautstärke.',
        "Uno speaker tascabile con un vero radiatore passivo, dodici ore di riproduzione e grado IP67. Sopravvive alla piscina e alla spiaggia, e si abbina a un secondo per lo stereo. Dodici ore a volume normale."),
    'Nimbus Shelf active speakers': ('Enceintes actives Nimbus Shelf', 'Nimbus Shelf Aktivlautsprecher', 'Diffusori attivi Nimbus Shelf'),
    'A pair of powered bookshelf speakers with a built-in DAC and Bluetooth. Plug in the turntable, the television or a laptop, or stream from a phone. No separate amplifier needed.': (
        "Une paire d'enceintes de bibliothèque amplifiées, avec un DAC intégré et le Bluetooth. Branchez la platine, la télévision ou un ordinateur, ou diffusez depuis un téléphone. Aucun amplificateur séparé n'est nécessaire.",
        'Ein Paar aktive Regallautsprecher mit eingebautem DAC und Bluetooth. Plattenspieler, Fernseher oder Laptop anschließen oder vom Handy streamen. Ein separater Verstärker ist nicht nötig.',
        'Una coppia di diffusori da scaffale amplificati, con DAC integrato e Bluetooth. Collega il giradischi, il televisore o un portatile, oppure trasmetti dal telefono. Non serve un amplificatore a parte.'),
    'Nimbus Spin turntable': ('Platine Nimbus Spin', 'Nimbus Spin Plattenspieler', 'Giradischi Nimbus Spin'),
    'A belt-drive turntable with a carbon tonearm and a built-in phono stage. The phono stage switches off for people who own one already. Set up in ten minutes with the included gauge.': (
        "Une platine à entraînement par courroie, bras en carbone et préampli phono intégré. Le préampli se désactive pour ceux qui en ont déjà un. Réglage en dix minutes avec le gabarit fourni.",
        'Ein riemengetriebener Plattenspieler mit Carbon-Tonarm und eingebauter Phonovorstufe. Die Vorstufe lässt sich abschalten, wenn schon eine da ist. In zehn Minuten eingerichtet, mit der beiliegenden Schablone.',
        'Un giradischi a cinghia con braccio in carbonio e stadio phono integrato. Lo stadio phono si spegne per chi ne ha già uno. Si mette a punto in dieci minuti con la dima inclusa.'),
    'Kestrel Pocket DAC': ('DAC de poche Kestrel', 'Kestrel Pocket DAC', 'DAC tascabile Kestrel'),
    'A USB-C headphone amplifier the size of a lighter, with a balanced output. It powers demanding headphones from a phone or a laptop and adds no noise of its own. The case is machined aluminium.': (
        "Un amplificateur casque USB-C de la taille d'un briquet, avec une sortie symétrique. Il alimente des casques exigeants depuis un téléphone ou un ordinateur et n'ajoute aucun bruit. Le boîtier est en aluminium usiné.",
        'Ein USB-C-Kopfhörerverstärker in Feuerzeuggröße, mit symmetrischem Ausgang. Er treibt anspruchsvolle Kopfhörer an Handy oder Laptop und fügt kein eigenes Rauschen hinzu. Das Gehäuse ist gefrästes Aluminium.',
        'Un amplificatore per cuffie USB-C grande come un accendino, con uscita bilanciata. Pilota cuffie esigenti da telefono o portatile e non aggiunge rumore suo. La scocca è in alluminio lavorato.'),
    'Nimbus Bar soundbar': ('Barre de son Nimbus Bar', 'Nimbus Bar Soundbar', 'Soundbar Nimbus Bar'),
    'A compact soundbar with a wireless subwoofer and HDMI eARC. One cable to the television and the subwoofer finds the bar by itself. Dialogue mode makes voices clear at low volume.': (
        "Une barre de son compacte avec un caisson sans fil et une prise HDMI eARC. Un seul câble vers la télévision, et le caisson trouve la barre tout seul. Le mode dialogue rend les voix claires à faible volume.",
        'Eine kompakte Soundbar mit kabellosem Subwoofer und HDMI eARC. Ein Kabel zum Fernseher, und der Subwoofer findet die Bar von allein. Der Dialogmodus macht Stimmen auch leise verständlich.',
        'Una soundbar compatta con subwoofer senza fili e HDMI eARC. Un solo cavo al televisore e il subwoofer trova la barra da solo. La modalità dialoghi rende chiare le voci a volume basso.'),
    'Voltline Air 14 laptop': ('Ordinateur portable Voltline Air 14', 'Voltline Air 14 Notebook', 'Portatile Voltline Air 14'),
    'A fourteen-inch laptop with a matte display, eighteen hours of battery and a keyboard people write on. Sixteen gigabytes of memory, a fast SSD and a case that opens with one hand. It charges from any USB-C charger.': (
        "Un portable de quatorze pouces à écran mat, dix-huit heures d'autonomie et un clavier sur lequel on écrit vraiment. Seize gigaoctets de mémoire, un SSD rapide et un châssis qui s'ouvre d'une main. Il se recharge avec n'importe quel chargeur USB-C.",
        'Ein Vierzehn-Zoll-Notebook mit mattem Display, achtzehn Stunden Akku und einer Tastatur, auf der man wirklich schreibt. Sechzehn Gigabyte Speicher, eine schnelle SSD und ein Gehäuse, das sich mit einer Hand öffnet. Es lädt an jedem USB-C-Netzteil.',
        "Un portatile da quattordici pollici con schermo opaco, diciotto ore di autonomia e una tastiera su cui si scrive davvero. Sedici gigabyte di memoria, un SSD veloce e una scocca che si apre con una mano. Si carica con qualsiasi caricatore USB-C."),
    'Voltline Pro 16 laptop': ('Ordinateur portable Voltline Pro 16', 'Voltline Pro 16 Notebook', 'Portatile Voltline Pro 16'),
    'A sixteen-inch workstation with a 120 Hz display and quiet fans. Built for people who compile, render and edit. The fans stay quiet until the work gets heavy.': (
        "Une station de travail de seize pouces avec un écran 120 Hz et des ventilateurs discrets. Conçue pour ceux qui compilent, rendent et montent. Les ventilateurs restent silencieux tant que la charge reste raisonnable.",
        'Eine Sechzehn-Zoll-Workstation mit 120-Hz-Display und leisen Lüftern. Gebaut für Menschen, die kompilieren, rendern und schneiden. Die Lüfter bleiben leise, bis die Arbeit schwer wird.',
        'Una workstation da sedici pollici con schermo a 120 Hz e ventole silenziose. Pensata per chi compila, renderizza e monta. Le ventole restano silenziose finché il lavoro non si fa pesante.'),
    'Tessera 27 inch 4K monitor': ('Écran 4K 27 pouces Tessera', 'Tessera 27 Zoll 4K Monitor', 'Monitor 4K da 27 pollici Tessera'),
    'A 27-inch 4K IPS display with USB-C power delivery and a matte coating. One USB-C cable carries video, data and 90 W of power to a laptop. The stand tilts, swivels and rises.': (
        "Un écran IPS 4K de 27 pouces avec alimentation USB-C et traitement mat. Un seul câble USB-C transporte la vidéo, les données et 90 W vers un portable. Le pied s'incline, pivote et monte.",
        'Ein 27-Zoll-4K-IPS-Display mit USB-C Power Delivery und matter Beschichtung. Ein USB-C-Kabel überträgt Bild, Daten und 90 W an ein Notebook. Der Fuß neigt, dreht und hebt sich.',
        'Uno schermo IPS 4K da 27 pollici con alimentazione USB-C e trattamento opaco. Un solo cavo USB-C porta video, dati e 90 W al portatile. Il piedistallo si inclina, ruota e si alza.'),
    'Tessera 34 inch ultrawide monitor': ('Écran ultra-large 34 pouces Tessera', 'Tessera 34 Zoll Ultrawide Monitor', 'Monitor ultrawide da 34 pollici Tessera'),
    'A curved ultrawide with a 144 Hz panel and a KVM switch. Two computers, one keyboard and mouse, switched with a button. The curve keeps the corners at the same distance as the centre.': (
        "Un écran ultra-large incurvé, dalle 144 Hz et commutateur KVM. Deux ordinateurs, un clavier et une souris, échangés d'un bouton. La courbure garde les coins à la même distance que le centre.",
        'Ein gebogener Ultrawide mit 144-Hz-Panel und KVM-Schalter. Zwei Rechner, eine Tastatur und Maus, per Knopfdruck gewechselt. Die Krümmung hält die Ecken so weit entfernt wie die Mitte.',
        'Un ultrawide curvo con pannello a 144 Hz e switch KVM. Due computer, una tastiera e un mouse, si cambia con un pulsante. La curvatura tiene gli angoli alla stessa distanza del centro.'),
    'Orbit Labs 75 mechanical keyboard': ('Clavier mécanique Orbit Labs 75', 'Orbit Labs 75 mechanische Tastatur', 'Tastiera meccanica Orbit Labs 75'),
    'A 75 percent mechanical keyboard with hot-swap switches and a gasket mount. The switches pull out without soldering, and the gasket mount softens every keystroke. Wired or Bluetooth.': (
        "Un clavier mécanique au format 75 pour cent, switches hot-swap et montage sur joint. Les switches s'extraient sans soudure, et le montage sur joint adoucit chaque frappe. Filaire ou Bluetooth.",
        'Eine mechanische Tastatur im 75-Prozent-Format mit Hot-Swap-Schaltern und Gasket-Mount. Die Schalter lassen sich ohne Löten ziehen, und der Gasket-Mount dämpft jeden Anschlag. Kabel oder Bluetooth.',
        'Una tastiera meccanica in formato 75 per cento, con switch hot-swap e montaggio gasket. Gli switch si estraggono senza saldature e il gasket ammorbidisce ogni battuta. Con cavo o Bluetooth.'),
    'Orbit Labs Glide mouse': ('Souris Orbit Labs Glide', 'Orbit Labs Glide Maus', 'Mouse Orbit Labs Glide'),
    'A lightweight wireless mouse with a 4000 Hz polling rate and PTFE feet. Fifty-eight grams, a week of battery, and feet that glide on any mat. The receiver lives inside the mouse when not in use.': (
        "Une souris sans fil légère, taux d'interrogation de 4000 Hz et patins en PTFE. Cinquante-huit grammes, une semaine d'autonomie et des patins qui glissent sur tous les tapis. Le récepteur se range dans la souris.",
        'Eine leichte kabellose Maus mit 4000 Hz Abtastrate und PTFE-Gleitfüßen. Achtundfünfzig Gramm, eine Woche Akku und Füße, die auf jedem Pad gleiten. Der Empfänger wohnt in der Maus, wenn er nicht steckt.',
        "Un mouse wireless leggero, con polling a 4000 Hz e piedini in PTFE. Cinquantotto grammi, una settimana di autonomia e piedini che scivolano su qualsiasi tappetino. Il ricevitore si ripone dentro il mouse."),
    'Voltline Thunderbolt dock': ('Station Thunderbolt Voltline', 'Voltline Thunderbolt Dock', 'Dock Thunderbolt Voltline'),
    'A Thunderbolt dock with two displays, ten ports and 96 W of charging. One cable from the laptop to the dock, and the desk is ready. Two 4K displays at 60 Hz.': (
        "Une station Thunderbolt pour deux écrans, dix ports et 96 W de charge. Un câble du portable à la station, et le bureau est prêt. Deux écrans 4K à 60 Hz.",
        'Ein Thunderbolt-Dock für zwei Displays, mit zehn Anschlüssen und 96 W Ladeleistung. Ein Kabel vom Notebook zum Dock, und der Schreibtisch ist bereit. Zwei 4K-Displays mit 60 Hz.',
        'Un dock Thunderbolt per due schermi, con dieci porte e 96 W di ricarica. Un cavo dal portatile al dock e la scrivania è pronta. Due schermi 4K a 60 Hz.'),
    'Voltline portable SSD': ('SSD portable Voltline', 'Voltline portable SSD', 'SSD portatile Voltline'),
    'A rugged USB-C SSD with 2000 MB/s reads, in a rubber sleeve. Two terabytes in a case that survives a drop from two metres. The USB-C cable is in the box.': (
        "Un SSD USB-C robuste, 2000 Mo/s en lecture, dans une gaine en caoutchouc. Deux téraoctets dans un boîtier qui survit à une chute de deux mètres. Le câble USB-C est dans la boîte.",
        'Eine robuste USB-C-SSD mit 2000 MB/s Lesegeschwindigkeit, in einer Gummihülle. Zwei Terabyte in einem Gehäuse, das einen Sturz aus zwei Metern übersteht. Das USB-C-Kabel liegt bei.',
        'Un SSD USB-C robusto, 2000 MB/s in lettura, in una guaina di gomma. Due terabyte in una scocca che resiste a una caduta da due metri. Il cavo USB-C è nella scatola.'),
    'Tessera 4K webcam': ('Webcam 4K Tessera', 'Tessera 4K Webcam', 'Webcam 4K Tessera'),
    'A 4K webcam with a large sensor and a privacy shutter. The sensor handles a dark room without grain. Slide the shutter shut and it is a lens cap, not a promise.': (
        "Une webcam 4K à grand capteur, avec un volet de confidentialité. Le capteur tient une pièce sombre sans bruit. Fermez le volet et c'est un cache d'objectif, pas une promesse.",
        'Eine 4K-Webcam mit großem Sensor und Sichtschutzblende. Der Sensor kommt mit einem dunklen Raum ohne Rauschen zurecht. Blende zu heißt Objektivdeckel, nicht Versprechen.',
        "Una webcam 4K con sensore grande e otturatore per la privacy. Il sensore regge una stanza buia senza grana. Chiudi l'otturatore ed è un coperchio, non una promessa."),
    'Halide M1 mirrorless camera': ('Appareil hybride Halide M1', 'Halide M1 spiegellose Kamera', 'Fotocamera mirrorless Halide M1'),
    'A full-frame mirrorless body with in-body stabilisation and a quiet shutter. Twenty-four megapixels, dual card slots and a viewfinder that does not lag. The body is sealed against rain.': (
        "Un boîtier hybride plein format avec stabilisation intégrée et obturateur silencieux. Vingt-quatre mégapixels, deux emplacements de carte et un viseur sans latence. Le boîtier est étanche à la pluie.",
        'Ein spiegelloses Vollformatgehäuse mit Bildstabilisierung im Body und leisem Verschluss. Vierundzwanzig Megapixel, zwei Kartenfächer und ein Sucher ohne Verzögerung. Das Gehäuse ist gegen Regen abgedichtet.',
        "Un corpo mirrorless full frame con stabilizzazione integrata e otturatore silenzioso. Ventiquattro megapixel, doppio slot per schede e un mirino senza ritardo. Il corpo è sigillato contro la pioggia."),
    'Halide 35 mm f/1.8 lens': ('Objectif Halide 35 mm f/1,8', 'Halide 35 mm f/1,8 Objektiv', 'Obiettivo Halide 35 mm f/1,8'),
    'A compact 35 mm prime with fast, silent focus. The one-lens travel kit. Sharp wide open, close focusing to 25 cm, and small enough for a jacket pocket. Weather sealed at the mount.': (
        "Une focale fixe 35 mm compacte, mise au point rapide et silencieuse. Le kit de voyage à un seul objectif. Piqué dès la pleine ouverture, mise au point à 25 cm et assez petit pour une poche de veste. Joint d'étanchéité à la monture.",
        'Eine kompakte 35-mm-Festbrennweite mit schnellem, leisem Fokus. Das Reisekit mit einem einzigen Objektiv. Schon offen scharf, Nahgrenze 25 cm und klein genug für die Jackentasche. Am Bajonett abgedichtet.',
        'Un 35 mm fisso compatto, con messa a fuoco rapida e silenziosa. Il kit da viaggio con un solo obiettivo. Nitido già a tutta apertura, mette a fuoco a 25 cm ed è piccolo da stare in tasca. Guarnizione sulla baionetta.'),
    'Halide 85 mm f/1.4 lens': ('Objectif Halide 85 mm f/1,4', 'Halide 85 mm f/1,4 Objektiv', 'Obiettivo Halide 85 mm f/1,4'),
    'A portrait prime with creamy bokeh and weather sealing. Wide open it separates a face from a busy background. Focus is fast enough for children and dogs.': (
        "Une focale fixe à portrait au bokeh crémeux et aux joints d'étanchéité. À pleine ouverture, elle détache un visage d'un fond chargé. La mise au point suffit pour les enfants et les chiens.",
        'Eine Porträt-Festbrennweite mit cremigem Bokeh und Wetterschutz. Offen trennt sie ein Gesicht von einem unruhigen Hintergrund. Der Fokus ist schnell genug für Kinder und Hunde.',
        'Un fisso da ritratto con bokeh cremoso e guarnizioni contro le intemperie. A tutta apertura stacca un volto da uno sfondo affollato. La messa a fuoco basta per bambini e cani.'),
    'Halide 24-70 mm f/2.8 lens': ('Objectif Halide 24-70 mm f/2,8', 'Halide 24-70 mm f/2,8 Objektiv', 'Obiettivo Halide 24-70 mm f/2,8'),
    'The standard zoom, sharp at every stop. Weddings, landscapes and everything between. Weather sealed, with a lock switch for the zoom ring.': (
        "Le zoom standard, piqué à toutes les ouvertures. Mariages, paysages et tout ce qui se trouve entre les deux. Joints d'étanchéité et verrou pour la bague de zoom.",
        'Das Standardzoom, bei jeder Blende scharf. Hochzeiten, Landschaften und alles dazwischen. Abgedichtet, mit Sperre für den Zoomring.',
        'Lo zoom standard, nitido a ogni diaframma. Matrimoni, paesaggi e tutto quello che sta in mezzo. Guarnizioni contro le intemperie e blocco per la ghiera dello zoom.'),
    'Halide Pocket compact camera': ('Appareil compact Halide Pocket', 'Halide Pocket Kompaktkamera', 'Fotocamera compatta Halide Pocket'),
    'A pocket camera with a one-inch sensor and a fast lens. Better than your phone, fits the same pocket. A real zoom, a real flash and a battery that lasts a day out. Raw files, if you want them.': (
        "Un appareil de poche à capteur d'un pouce et objectif lumineux. Mieux que votre téléphone, dans la même poche. Un vrai zoom, un vrai flash et une batterie qui tient une journée. Des fichiers raw, si vous en voulez.",
        'Eine Taschenkamera mit Ein-Zoll-Sensor und lichtstarkem Objektiv. Besser als das Handy, passt in dieselbe Tasche. Ein echtes Zoom, ein echter Blitz und ein Akku für einen Tag draußen. Raw-Dateien, wenn du willst.',
        'Una compatta da tasca con sensore da un pollice e obiettivo luminoso. Meglio del telefono, sta nella stessa tasca. Uno zoom vero, un flash vero e una batteria che dura una giornata fuori. File raw, se li vuoi.'),
    'Halide Go action camera': ('Caméra daction Halide Go', 'Halide Go Actionkamera', 'Action cam Halide Go'),
    'A waterproof action camera with 5K video and horizon lock. Waterproof to ten metres without a case. Horizon lock keeps the video level on a bike or a board.': (
        "Une caméra d'action étanche, vidéo 5K et verrouillage d'horizon. Étanche à dix mètres sans caisson. Le verrouillage d'horizon garde l'image droite sur un vélo ou une planche.",
        'Eine wasserdichte Actionkamera mit 5K-Video und Horizontstabilisierung. Wasserdicht bis zehn Meter ohne Gehäuse. Die Horizontstabilisierung hält das Bild auf Rad oder Board gerade.',
        "Una action cam impermeabile, con video 5K e blocco dell'orizzonte. Impermeabile fino a dieci metri senza custodia. Il blocco dell'orizzonte tiene dritto il video in bici o sulla tavola."),
    'Halide carbon travel tripod': ('Trépied de voyage en carbone Halide', 'Halide Carbon-Reisestativ', 'Treppiede da viaggio in carbonio Halide'),
    'A carbon fibre tripod that folds to 40 cm and holds 10 kg. The legs fold back over the head to fit a daypack. The centre column reverses for low shots.': (
        "Un trépied en fibre de carbone qui se plie à 40 cm et porte 10 kg. Les jambes se replient sur la rotule pour tenir dans un sac à dos. La colonne centrale s'inverse pour les prises au ras du sol.",
        'Ein Carbonstativ, das auf 40 cm zusammenfaltet und 10 kg trägt. Die Beine klappen über den Kopf, damit es in den Tagesrucksack passt. Die Mittelsäule lässt sich für bodennahe Aufnahmen umdrehen.',
        'Un treppiede in fibra di carbonio che si chiude a 40 cm e regge 10 kg. Le gambe si ripiegano sopra la testa per stare in uno zaino. La colonna centrale si inverte per gli scatti bassi.'),
    'Halide sling bag': ('Sacoche Halide', 'Halide Slingtasche', 'Marsupio Halide'),
    'A six-litre sling for a body and two lenses, with a weather flap. The camera comes out with one hand, and the flap keeps rain out. The strap swaps sides for left-handers.': (
        "Une sacoche de six litres pour un boîtier et deux objectifs, avec un rabat anti-intempéries. L'appareil sort d'une main, et le rabat arrête la pluie. La sangle se change de côté pour les gauchers.",
        'Eine Sechs-Liter-Slingtasche für ein Gehäuse und zwei Objektive, mit Wetterlasche. Die Kamera kommt mit einer Hand heraus, und die Lasche hält Regen ab. Der Gurt lässt sich für Linkshänder umsetzen.',
        "Un marsupio da sei litri per un corpo e due obiettivi, con patta antipioggia. La macchina esce con una mano e la patta tiene fuori la pioggia. La tracolla si sposta di lato per i mancini."),
    'Voltline SD card': ('Carte SD Voltline', 'Voltline SD-Karte', 'Scheda SD Voltline'),
    'A V90 SD card for 8K video and fast bursts. Two hundred and fifty-six gigabytes with sustained writes for 8K video. Rated for ten thousand insertions.': (
        "Une carte SD V90 pour la vidéo 8K et les rafales rapides. Deux cent cinquante-six gigaoctets avec un débit d'écriture soutenu pour la 8K. Prévue pour dix mille insertions.",
        'Eine V90-SD-Karte für 8K-Video und schnelle Serien. Zweihundertsechsundfünfzig Gigabyte mit anhaltender Schreibrate für 8K. Für zehntausend Steckzyklen ausgelegt.',
        'Una scheda SD V90 per video 8K e raffiche veloci. Duecentocinquantasei gigabyte con scrittura sostenuta per l8K. Prevista per diecimila inserimenti.'),
    'Orbit Labs smart bulb': ('Ampoule connectée Orbit Labs', 'Orbit Labs Smart-Leuchtmittel', 'Lampadina smart Orbit Labs'),
    'A colour smart bulb that works over your local network. No account. Set the colour and the schedule from the hub, with no cloud and no account. Works with a normal switch too.': (
        "Une ampoule connectée en couleur qui fonctionne sur votre réseau local. Sans compte. Réglez la couleur et les horaires depuis le hub, sans nuage et sans compte. Elle marche aussi avec un interrupteur normal.",
        'Ein farbiges Smart-Leuchtmittel, das über das lokale Netz läuft. Ohne Konto. Farbe und Zeitplan stellst du am Hub ein, ohne Cloud und ohne Konto. Es funktioniert auch mit einem normalen Schalter.',
        'Una lampadina smart a colori che funziona sulla rete locale. Senza account. Imposti colore e orari dallhub, senza cloud e senza account. Va anche con un interruttore normale.'),
    'Orbit Labs smart plug': ('Prise connectée Orbit Labs', 'Orbit Labs Smart-Steckdose', 'Presa smart Orbit Labs'),
    'A compact plug with energy metering and a physical button. It reports watts and kilowatt hours, and the button works when the network is down. Rated for a heater.': (
        "Une prise compacte avec mesure de consommation et bouton physique. Elle indique les watts et les kilowattheures, et le bouton fonctionne même réseau coupé. Prévue pour un radiateur.",
        'Eine kompakte Steckdose mit Energiemessung und physischem Knopf. Sie meldet Watt und Kilowattstunden, und der Knopf funktioniert auch ohne Netz. Für einen Heizlüfter ausgelegt.',
        'Una presa compatta con misura dei consumi e pulsante fisico. Indica watt e chilowattora, e il pulsante funziona anche con la rete giù. Adatta a una stufa.'),
    'Nimbus Home speaker': ('Enceinte Nimbus Home', 'Nimbus Home Lautsprecher', 'Speaker Nimbus Home'),
    'A room-filling speaker with local voice control and a mute switch that cuts power to the mics. Voice commands are processed in the room, not on a server. The mute switch is a physical cut, not a request.': (
        "Une enceinte qui remplit la pièce, avec commande vocale locale et un interrupteur qui coupe l'alimentation des micros. Les commandes vocales sont traitées dans la pièce, pas sur un serveur. L'interrupteur coupe vraiment, ce n'est pas une demande.",
        'Ein raumfüllender Lautsprecher mit lokaler Sprachsteuerung und einem Schalter, der die Mikrofone vom Strom trennt. Sprachbefehle werden im Raum verarbeitet, nicht auf einem Server. Der Schalter trennt wirklich, er bittet nicht darum.',
        "Uno speaker che riempie la stanza, con comandi vocali locali e un interruttore che toglie corrente ai microfoni. I comandi vocali si elaborano nella stanza, non su un server. L'interruttore stacca davvero, non è una richiesta."),
    'Orbit Labs video doorbell': ('Sonnette vidéo Orbit Labs', 'Orbit Labs Video-Türklingel', 'Videocitofono Orbit Labs'),
    'A wired doorbell camera that records to a card in your home, not a cloud. Wired to the existing chime, recording to a card behind the unit. Notifications come from your own hub.': (
        "Une sonnette caméra filaire qui enregistre sur une carte chez vous, pas dans un nuage. Raccordée au carillon existant, elle enregistre sur une carte placée derrière l'appareil. Les notifications viennent de votre propre hub.",
        'Eine kabelgebundene Türklingelkamera, die auf eine Karte bei dir zu Hause aufzeichnet, nicht in eine Cloud. An den vorhandenen Gong angeschlossen, mit Aufzeichnung auf eine Karte hinter dem Gerät. Die Benachrichtigungen kommen von deinem eigenen Hub.',
        "Un videocitofono cablato che registra su una scheda in casa tua, non su un cloud. Collegato al campanello esistente, registra su una scheda dietro l'unità. Le notifiche arrivano dal tuo hub."),
    'Orbit Labs thermostat': ('Thermostat Orbit Labs', 'Orbit Labs Thermostat', 'Termostato Orbit Labs'),
    'A learning thermostat with a rotary dial and an e-paper display. Turn the dial to set the temperature and it learns the rest. Runs on the hub, no cloud.': (
        "Un thermostat qui apprend, avec une molette et un écran e-paper. Tournez la molette pour régler la température, il apprend le reste. Il tourne sur le hub, sans nuage.",
        'Ein lernendes Thermostat mit Drehrad und E-Paper-Display. Am Rad die Temperatur einstellen, den Rest lernt es. Es läuft am Hub, ohne Cloud.',
        'Un termostato che impara, con manopola e display e-paper. Giri la manopola per impostare la temperatura e il resto lo impara. Gira sullhub, senza cloud.'),
    'Orbit Labs sensor kit': ('Kit de capteurs Orbit Labs', 'Orbit Labs Sensor-Set', 'Kit sensori Orbit Labs'),
    'Four door sensors and two motion sensors, batteries included. Stick the sensors on doors and shelves, pair them with the hub, and the batteries last two years.': (
        "Quatre capteurs d'ouverture et deux détecteurs de mouvement, piles comprises. Collez les capteurs sur les portes et les étagères, appairez-les au hub, et les piles durent deux ans.",
        'Vier Türsensoren und zwei Bewegungsmelder, Batterien inklusive. Die Sensoren an Türen und Regale kleben, mit dem Hub koppeln, und die Batterien halten zwei Jahre.',
        "Quattro sensori per le porte e due di movimento, batterie incluse. Attacchi i sensori a porte e scaffali, li abbini all'hub e le batterie durano due anni."),
    'Orbit Labs home hub': ('Hub domestique Orbit Labs', 'Orbit Labs Home Hub', 'Hub domestico Orbit Labs'),
    'The hub that runs your home on your own network, with Zigbee and Thread. It speaks Zigbee, Thread and Wi-Fi, stores its data on the device, and updates when you say so.': (
        "Le hub qui pilote votre maison sur votre propre réseau, en Zigbee et Thread. Il parle Zigbee, Thread et Wi-Fi, garde ses données sur l'appareil et se met à jour quand vous le décidez.",
        'Der Hub, der dein Zuhause im eigenen Netz steuert, mit Zigbee und Thread. Er spricht Zigbee, Thread und WLAN, speichert seine Daten auf dem Gerät und aktualisiert, wenn du es sagst.',
        "L'hub che gestisce la casa sulla tua rete, con Zigbee e Thread. Parla Zigbee, Thread e Wi-Fi, tiene i dati sul dispositivo e si aggiorna quando lo dici tu."),
    'Voltline Watch': ('Montre Voltline', 'Voltline Watch', 'Orologio Voltline'),
    'A smart watch with a sapphire glass face, a week of battery and offline maps. Heart rate, sleep, GPS routes and offline maps, on a battery that lasts seven days. The face is sapphire.': (
        "Une montre connectée à verre saphir, une semaine d'autonomie et des cartes hors ligne. Fréquence cardiaque, sommeil, traces GPS et cartes hors ligne, sur une batterie qui tient sept jours. Le verre est en saphir.",
        'Eine Smartwatch mit Saphirglas, einer Woche Akku und Offline-Karten. Puls, Schlaf, GPS-Routen und Offline-Karten, auf einem Akku, der sieben Tage hält. Das Glas ist Saphir.',
        "Uno smartwatch con vetro zaffiro, una settimana di autonomia e mappe offline. Battito, sonno, tracce GPS e mappe offline, su una batteria che dura sette giorni. Il vetro è zaffiro."),
    'Voltline Band': ('Bracelet Voltline', 'Voltline Band', 'Braccialetto Voltline'),
    'A slim tracker with sleep, heart rate and two weeks of battery. It weighs fourteen grams and tracks sleep, steps and heart rate for two weeks between charges. The strap comes in three colours.': (
        "Un traceur fin qui suit le sommeil, la fréquence cardiaque, avec deux semaines d'autonomie. Il pèse quatorze grammes et suit le sommeil, les pas et le rythme cardiaque pendant deux semaines entre deux charges. Le bracelet existe en trois couleurs.",
        'Ein schmaler Tracker für Schlaf, Puls und zwei Wochen Akku. Er wiegt vierzehn Gramm und zeichnet Schlaf, Schritte und Puls zwei Wochen lang auf. Das Armband gibt es in drei Farben.',
        'Un tracker sottile che segue sonno e battito, con due settimane di autonomia. Pesa quattordici grammi e registra sonno, passi e battito per due settimane tra una carica e l altra. Il cinturino è in tre colori.'),
    'Voltline Ring': ('Bague Voltline', 'Voltline Ring', 'Anello Voltline'),
    'A titanium sleep ring that lasts a week, no subscription. Sleep stages, resting heart rate and temperature from a ring you forget. Charge once a week.': (
        "Une bague de sommeil en titane qui tient une semaine, sans abonnement. Phases de sommeil, fréquence cardiaque au repos et température, depuis une bague qu'on oublie. Une charge par semaine.",
        'Ein Schlafring aus Titan, der eine Woche hält, ohne Abo. Schlafphasen, Ruhepuls und Temperatur von einem Ring, den man vergisst. Einmal pro Woche laden.',
        'Un anello per il sonno in titanio che dura una settimana, senza abbonamento. Fasi del sonno, battito a riposo e temperatura da un anello che dimentichi. Si carica una volta a settimana.'),
    'Voltline leather watch strap': ('Bracelet de montre en cuir Voltline', 'Voltline Leder-Uhrenarmband', 'Cinturino di pelle Voltline'),
    'A vegetable-tanned leather strap with a quick-release pin. Full-grain leather that softens in a week. The quick-release pin swaps it in seconds.': (
        "Un bracelet en cuir à tannage végétal avec une barrette à ressort rapide. Un cuir pleine fleur qui s'assouplit en une semaine. La barrette rapide le change en quelques secondes.",
        'Ein pflanzlich gegerbtes Lederarmband mit Schnellwechselsteg. Vollnarbenleder, das in einer Woche weich wird. Der Schnellwechselsteg tauscht es in Sekunden.',
        'Un cinturino in pelle conciata al vegetale con barretta a sgancio rapido. Pelle pieno fiore che si ammorbidisce in una settimana. La barretta lo cambia in pochi secondi.'),
    'Voltline 65 W charger': ('Chargeur Voltline 65 W', 'Voltline 65-W-Ladegerät', 'Caricatore Voltline 65 W'),
    'A GaN charger with two USB-C ports, small enough to lose. Charges a laptop and a phone at once, from a plug the size of a matchbox. Foldable prongs.': (
        "Un chargeur GaN à deux ports USB-C, assez petit pour se perdre. Il charge un portable et un téléphone en même temps, depuis une prise de la taille d'une boîte d'allumettes. Broches pliables.",
        'Ein GaN-Ladegerät mit zwei USB-C-Anschlüssen, klein genug zum Verlieren. Es lädt Notebook und Handy gleichzeitig, aus einem Stecker in Streichholzschachtelgröße. Klappbare Stifte.',
        "Un caricatore GaN con due porte USB-C, piccolo abbastanza da perdersi. Carica insieme un portatile e un telefono, da una spina grande come una scatola di fiammiferi. Spinotti pieghevoli."),
    'Voltline braided USB-C cable': ('Câble USB-C tressé Voltline', 'Voltline USB-C-Kabel, geflochten', 'Cavo USB-C intrecciato Voltline'),
    'A 2 m braided cable for 240 W charging and 40 Gbps data. Two metres of braided nylon, rated for the fastest laptops and displays. The connectors are aluminium.': (
        "Un câble tressé de 2 m pour une charge de 240 W et 40 Gbit/s de données. Deux mètres de nylon tressé, prévus pour les portables et les écrans les plus rapides. Les connecteurs sont en aluminium.",
        'Ein 2-m-Geflechtkabel für 240 W Ladeleistung und 40 Gbit/s Daten. Zwei Meter geflochtenes Nylon, ausgelegt für die schnellsten Notebooks und Displays. Die Stecker sind aus Aluminium.',
        'Un cavo intrecciato da 2 m per ricarica a 240 W e dati a 40 Gbps. Due metri di nylon intrecciato, adatti ai portatili e agli schermi più veloci. I connettori sono in alluminio.'),
    'Voltline 20000 power bank': ('Batterie externe Voltline 20000', 'Voltline 20000 Powerbank', 'Power bank Voltline 20000'),
    'A 20000 mAh power bank with 65 W output and a display. Enough for a laptop and two phone charges. The display shows the percentage, not a row of dots.': (
        "Une batterie externe de 20000 mAh, sortie 65 W et écran. De quoi charger un portable et deux téléphones. L'écran affiche le pourcentage, pas une rangée de points.",
        'Eine 20000-mAh-Powerbank mit 65 W Ausgang und Display. Genug für ein Notebook und zwei Handyladungen. Das Display zeigt Prozent, keine Punktreihe.',
        'Un power bank da 20000 mAh, uscita da 65 W e display. Basta per un portatile e due ricariche del telefono. Il display mostra la percentuale, non una fila di puntini.'),
    'Tessera laptop stand': ('Support pour portable Tessera', 'Tessera Laptopständer', 'Supporto per portatile Tessera'),
    'An aluminium stand that raises the screen to eye height and folds flat. It lifts the screen to eye height for a straight neck and folds flat for a bag. Fits laptops up to 16 inches.': (
        "Un support en aluminium qui met l'écran à hauteur des yeux et se plie à plat. Il relève l'écran pour garder la nuque droite et se range à plat dans un sac. Il accepte les portables jusqu'à 16 pouces.",
        'Ein Aluminiumständer, der den Bildschirm auf Augenhöhe hebt und flach zusammenklappt. Er hebt das Display auf Augenhöhe für einen geraden Nacken und passt flach in die Tasche. Für Notebooks bis 16 Zoll.',
        "Un supporto in alluminio che porta lo schermo all'altezza degli occhi e si chiude piatto. Alza lo schermo per tenere il collo dritto e si ripiega per la borsa. Adatto a portatili fino a 16 pollici."),
    'Orbit Labs desk mat': ('Sous-main Orbit Labs', 'Orbit Labs Schreibtischunterlage', 'Tappetino da scrivania Orbit Labs'),
    'A felt and cork desk mat, 90 by 40 cm. Wool felt on top, cork underneath, no slipping. The keyboard and the mouse both fit with room to spare.': (
        "Un sous-main en feutre et liège, 90 sur 40 cm. Feutre de laine dessus, liège dessous, aucun glissement. Le clavier et la souris tiennent tous les deux avec de la marge.",
        'Eine Schreibtischunterlage aus Filz und Kork, 90 mal 40 cm. Wollfilz oben, Kork unten, kein Verrutschen. Tastatur und Maus passen beide mit Platz drumherum.',
        'Un tappetino da scrivania in feltro e sughero, 90 per 40 cm. Feltro di lana sopra, sughero sotto, non scivola. Tastiera e mouse ci stanno entrambi con spazio in più.'),
    'Tessera phone case': ('Coque de téléphone Tessera', 'Tessera Handyhülle', 'Cover per telefono Tessera'),
    'A slim case in recycled polymer with a microfibre lining. Slim enough to keep the phone slim, grippy enough to survive a wet hand. Buttons stay clicky.': (
        "Une coque fine en polymère recyclé, doublée de microfibre. Assez fine pour garder le téléphone fin, assez adhérente pour résister à une main mouillée. Les boutons restent francs.",
        'Eine schmale Hülle aus recyceltem Polymer mit Mikrofaserfutter. Schmal genug, damit das Handy schmal bleibt, griffig genug für eine nasse Hand. Die Tasten bleiben knackig.',
        'Una cover sottile in polimero riciclato, foderata in microfibra. Sottile quanto basta per non ingrossare il telefono, ruvida quanto basta per una mano bagnata. I tasti restano precisi.'),
    'Tessera screen cleaning kit': ('Kit de nettoyage écran Tessera', 'Tessera Bildschirm-Reinigungsset', 'Kit per pulire gli schermi Tessera'),
    'A spray, two cloths and a brush, for screens and lenses. Alcohol free, safe for coatings and lenses. One bottle cleans a year of screens.': (
        "Un spray, deux chiffons et une brosse, pour les écrans et les objectifs. Sans alcool, sans danger pour les traitements et les lentilles. Un flacon nettoie une année d'écrans.",
        'Ein Spray, zwei Tücher und ein Pinsel, für Bildschirme und Objektive. Alkoholfrei, unbedenklich für Beschichtungen und Linsen. Eine Flasche reinigt ein Jahr lang Bildschirme.',
        'Uno spray, due panni e un pennello, per schermi e obiettivi. Senza alcol, sicuro su trattamenti e lenti. Un flacone pulisce un anno di schermi.'),
    'Home office kit': ('Kit bureau à domicile', 'Homeoffice-Set', 'Kit per ufficio in casa'),
    'Keyboard, mouse, laptop stand and desk mat in one order. Everything for a clean desk in one box, at a saving. Keyboard, mouse, stand and mat.': (
        "Clavier, souris, support pour portable et sous-main en une commande. Tout pour un bureau net dans une seule boîte, à prix réduit. Clavier, souris, support et sous-main.",
        'Tastatur, Maus, Laptopständer und Schreibtischunterlage in einer Bestellung. Alles für einen aufgeräumten Schreibtisch in einer Box, mit Ersparnis. Tastatur, Maus, Ständer und Unterlage.',
        'Tastiera, mouse, supporto per portatile e tappetino in un solo ordine. Tutto per una scrivania in ordine in una scatola, con un risparmio. Tastiera, mouse, supporto e tappetino.'),
    'Travel charging kit': ('Kit de charge pour le voyage', 'Reise-Ladeset', 'Kit di ricarica da viaggio'),
    'Charger, cable and power bank, packed in a zip pouch. Charger, cable and power bank in a pouch that fits a jacket pocket. Enough for a week away.': (
        "Chargeur, câble et batterie externe, dans une pochette zippée. Chargeur, câble et batterie dans une pochette qui tient dans une poche de veste. De quoi tenir une semaine.",
        'Ladegerät, Kabel und Powerbank in einer Reißverschlusstasche. Ladegerät, Kabel und Powerbank in einer Tasche, die in die Jackentasche passt. Genug für eine Woche unterwegs.',
        'Caricatore, cavo e power bank in una pochette con zip. Caricatore, cavo e power bank in una custodia che sta in tasca. Bastano per una settimana fuori.'),

    # Food
    'Puglia extra virgin olive oil': ("Huile d'olive vierge extra des Pouilles", 'Natives Olivenöl extra aus Apulien', "Olio extravergine di oliva pugliese"),
    'Cold-pressed from Coratina olives within hours of picking. Peppery, green and best raw on bread and greens. Pressed in November and bottled dark to keep the flavour. Use the small bottle for salads and the litre for the pan.': (
        "Pressée à froid à partir d'olives Coratina quelques heures après la récolte. Poivrée, verte et meilleure crue, sur du pain et des légumes. Pressée en novembre et mise en bouteille sombre pour garder le goût. La petite bouteille pour les salades, le litre pour la poêle.",
        'Kalt gepresst aus Coratina-Oliven, wenige Stunden nach der Ernte. Pfeffrig, grün und roh am besten, auf Brot und Gemüse. Im November gepresst und dunkel abgefüllt, damit der Geschmack bleibt. Die kleine Flasche für Salate, den Liter für die Pfanne.',
        "Spremuto a freddo da olive Coratina poche ore dopo la raccolta. Pepato, verde e al meglio a crudo, su pane e verdure. Spremuto a novembre e imbottigliato scuro per tenere il sapore. La bottiglietta per le insalate, il litro per la padella."),
    'Bronze-cut rigatoni': ('Rigatoni tréfilés au bronze', 'Bronzegezogene Rigatoni', 'Rigatoni trafilati al bronzo'),
    'Slow-dried durum wheat pasta cut through bronze dies, so the sauce clings. Dried for two days at a low temperature, which keeps the wheat flavour. Ten minutes in salted water.': (
        "Des pâtes de blé dur séchées lentement et tréfilées au bronze, pour que la sauce accroche. Séchées deux jours à basse température, ce qui garde le goût du blé. Dix minutes dans l'eau salée.",
        'Hartweizenpasta, langsam getrocknet und durch Bronzematrizen gezogen, damit die Sauce haftet. Zwei Tage bei niedriger Temperatur getrocknet, das erhält den Weizengeschmack. Zehn Minuten in Salzwasser.',
        'Pasta di grano duro essiccata lentamente e trafilata al bronzo, così il sugo si attacca. Essiccata due giorni a bassa temperatura, che tiene il sapore del grano. Dieci minuti in acqua salata.'),
    'Gragnano spaghetti': ('Spaghetti de Gragnano', 'Gragnano Spaghetti', 'Spaghetti di Gragnano'),
    'Long, slow-dried spaghetti from Gragnano, with the bite to hold a carbonara. Made from Italian durum wheat and mountain water. Eleven minutes for al dente.': (
        "Des spaghetti longs de Gragnano, séchés lentement, avec la tenue qu'il faut pour une carbonara. Faits de blé dur italien et d'eau de montagne. Onze minutes pour l'al dente.",
        'Lange, langsam getrocknete Spaghetti aus Gragnano, mit dem Biss für eine Carbonara. Aus italienischem Hartweizen und Bergwasser. Elf Minuten für al dente.',
        'Spaghetti lunghi di Gragnano, essiccati lentamente, con la tenuta giusta per una carbonara. Fatti con grano duro italiano e acqua di montagna. Undici minuti per l al dente.'),
    'Apricot jam': ("Confiture d'abricot", 'Aprikosenmarmelade', 'Marmellata di albicocche'),
    'Whole apricots cooked in copper with cane sugar and nothing else. Sixty percent fruit, set softly, with pieces of apricot in every spoon. Keep in the fridge once open.': (
        "Des abricots entiers cuits au chaudron de cuivre avec du sucre de canne, et rien d'autre. Soixante pour cent de fruits, une prise souple, des morceaux d'abricot dans chaque cuillère. À garder au frais une fois ouverte.",
        'Ganze Aprikosen im Kupferkessel mit Rohrzucker gekocht, sonst nichts. Sechzig Prozent Frucht, weich geliert, mit Aprikosenstücken in jedem Löffel. Nach dem Öffnen kühl lagern.',
        "Albicocche intere cotte in rame con zucchero di canna e niente altro. Sessanta per cento di frutta, presa morbida, con pezzi di albicocca in ogni cucchiaio. Dopo l apertura tenere in frigo."),
    'Black fig jam': ('Confiture de figues noires', 'Schwarze Feigenmarmelade', 'Marmellata di fichi neri'),
    'Late-summer black figs with a squeeze of lemon. Made for cheese. Dark, sticky and not too sweet. A spoon beside a hard cheese or on warm toast.': (
        "Des figues noires de fin d'été avec un trait de citron. Faite pour le fromage. Sombre, collante et pas trop sucrée. Une cuillère à côté d'un fromage à pâte dure ou sur un toast chaud.",
        'Schwarze Feigen vom Spätsommer mit einem Spritzer Zitrone. Für Käse gemacht. Dunkel, klebrig und nicht zu süß. Ein Löffel neben einem Hartkäse oder auf warmem Toast.',
        "Fichi neri di fine estate con una spruzzata di limone. Fatta per il formaggio. Scura, appiccicosa e non troppo dolce. Un cucchiaio accanto a un formaggio stagionato o su un crostino caldo."),
    'Wildflower honey': ('Miel de fleurs sauvages', 'Wildblütenhonig', 'Miele di fiori di campo'),
    'Raw honey from hives on a hillside of thyme and heather. Unfiltered, crystallises with time. Never heated above hive temperature, so it sets over the winter. Warm the jar in water to bring it back.': (
        "Un miel cru de ruches posées sur une colline de thym et de bruyère. Non filtré, il cristallise avec le temps. Jamais chauffé au-delà de la température de la ruche, il se fige donc en hiver. Réchauffez le pot au bain-marie pour le rendre liquide.",
        'Roher Honig aus Bienenstöcken an einem Hang voller Thymian und Heide. Ungefiltert, kristallisiert mit der Zeit. Nie über Stocktemperatur erhitzt, deshalb wird er im Winter fest. Das Glas im Wasserbad erwärmen, dann wird er wieder flüssig.',
        "Miele crudo da arnie su una collina di timo ed erica. Non filtrato, cristallizza con il tempo. Mai scaldato oltre la temperatura dell'arnia, quindi d'inverno si rapprende. Scalda il vasetto a bagnomaria per riportarlo liquido."),
    'San Marzano passata': ('Passata de San Marzano', 'San-Marzano-Passata', 'Passata di San Marzano'),
    'Sieved San Marzano tomatoes in a glass bottle, picked ripe and nothing added. Bottled the day the tomatoes are picked, with a leaf of basil. Enough for two pans of sauce.': (
        "Des tomates San Marzano tamisées en bouteille de verre, cueillies mûres et sans rien ajouté. Mises en bouteille le jour de la récolte, avec une feuille de basilic. De quoi faire deux casseroles de sauce.",
        'Passierte San-Marzano-Tomaten in der Glasflasche, reif gepflückt und ohne Zusätze. Am Erntetag abgefüllt, mit einem Basilikumblatt. Genug für zwei Töpfe Sauce.',
        'Pomodori San Marzano passati in bottiglia di vetro, raccolti maturi e senza aggiunte. Imbottigliati il giorno della raccolta, con una foglia di basilico. Bastano per due pentole di sugo.'),
    'Flaky sea salt': ('Sel de mer en flocons', 'Meersalzflocken', 'Sale marino in fiocchi'),
    'Pyramid flakes harvested from Atlantic salt pans. Finishing salt, not for the pot. The flakes crush between the fingers over a finished dish. A tub lasts a year in most kitchens.': (
        "Des flocons en pyramide récoltés dans des marais salants de l'Atlantique. Un sel de finition, pas un sel de cuisson. Les flocons s'écrasent entre les doigts sur un plat terminé. Une boîte dure un an dans la plupart des cuisines.",
        'Pyramidenflocken aus atlantischen Salzgärten. Ein Finishing-Salz, nichts für den Topf. Die Flocken zerdrückt man zwischen den Fingern über dem fertigen Gericht. Eine Dose hält in den meisten Küchen ein Jahr.',
        "Fiocchi a piramide raccolti nelle saline dell'Atlantico. Un sale da finitura, non da pentola. I fiocchi si sbriciolano tra le dita sul piatto finito. Una confezione dura un anno nella maggior parte delle cucine."),
    'Country sourdough': ('Pain au levain de campagne', 'Bauernbrot mit Sauerteig', 'Pane di campagna a lievito madre'),
    'A 48-hour sourdough with a dark crust and an open crumb. Wheat, water, salt and time. Baked before dawn, packed warm, delivered the same day. It keeps for four days in a cloth.': (
        "Un pain au levain de 48 heures, croûte foncée et mie alvéolée. Farine, eau, sel et temps. Cuit avant l'aube, emballé tiède, livré le jour même. Il se garde quatre jours dans un linge.",
        'Ein 48-Stunden-Sauerteigbrot mit dunkler Kruste und offener Krume. Weizen, Wasser, Salz und Zeit. Vor Sonnenaufgang gebacken, warm verpackt, am selben Tag geliefert. In einem Tuch hält es vier Tage.',
        "Un pane a lievito madre di 48 ore, con crosta scura e mollica alveolata. Farina, acqua, sale e tempo. Cotto prima dell'alba, confezionato caldo, consegnato in giornata. Si conserva quattro giorni in un canovaccio."),
    'Baguette tradition': ('Baguette de tradition', 'Baguette Tradition', 'Baguette tradizionale'),
    'A long-fermented baguette with a thin crust that shatters. Made with a poolish left overnight, so the crumb is creamy. Best eaten the day it arrives.': (
        "Une baguette à longue fermentation, avec une croûte fine qui éclate. Faite avec une poolish laissée toute la nuit, la mie est donc crémeuse. À manger le jour de la livraison.",
        'Eine lang geführte Baguette mit dünner Kruste, die splittert. Mit einem über Nacht geführten Poolish gemacht, deshalb ist die Krume cremig. Am besten am Liefertag essen.',
        'Una baguette a lunga fermentazione, con crosta sottile che si sbriciola. Fatta con una poolish lasciata tutta la notte, così la mollica è cremosa. Da mangiare il giorno che arriva.'),
    'Butter croissants': ('Croissants au beurre', 'Buttercroissants', 'Croissant al burro'),
    'Six croissants laminated with cultured butter. Best warmed for five minutes. Twenty-seven layers of butter and dough, proved overnight. They freeze well and bake from frozen.': (
        "Six croissants feuilletés au beurre de baratte. Meilleurs réchauffés cinq minutes. Vingt-sept couches de beurre et de pâte, pointées toute la nuit. Ils se congèlent bien et se cuisent surgelés.",
        'Sechs Croissants, touriert mit Sauerrahmbutter. Am besten fünf Minuten aufgewärmt. Siebenundzwanzig Schichten Butter und Teig, über Nacht geführt. Sie lassen sich gut einfrieren und tiefgefroren backen.',
        'Sei croissant sfogliati con burro di panna acida. Al meglio scaldati cinque minuti. Ventisette strati di burro e impasto, lievitati tutta la notte. Si congelano bene e si cuociono da surgelati.'),
    'Seeded rye loaf': ('Pain de seigle aux graines', 'Roggenbrot mit Saaten', 'Pane di segale ai semi'),
    'Dense rye with sunflower and pumpkin seeds. Keeps for a week. A dense loaf that slices thin and toasts well. Good with butter, better with cheese.': (
        "Un seigle dense aux graines de tournesol et de courge. Il se garde une semaine. Un pain dense qui se coupe fin et se grille bien. Bon avec du beurre, meilleur avec du fromage.",
        'Ein dichtes Roggenbrot mit Sonnenblumen- und Kürbiskernen. Es hält eine Woche. Ein dichter Laib, der sich dünn schneiden und gut toasten lässt. Gut mit Butter, besser mit Käse.',
        'Una segale densa con semi di girasole e zucca. Si conserva una settimana. Un pane compatto che si taglia sottile e si tosta bene. Buono con il burro, meglio con il formaggio.'),
    'Gluten-free seed loaf': ('Pain aux graines sans gluten', 'Glutenfreies Saatenbrot', 'Pane ai semi senza glutine'),
    'A buckwheat and seed loaf with no gluten and no compromise on crust. Baked in a separate kitchen, so it is safe for coeliacs. Toast it and the crust comes alive.': (
        "Un pain de sarrasin et de graines, sans gluten et sans compromis sur la croûte. Cuit dans une cuisine séparée, il convient donc aux cœliaques. Grillez-le et la croûte se réveille.",
        'Ein Brot aus Buchweizen und Saaten, ohne Gluten und ohne Kompromiss bei der Kruste. In einer eigenen Küche gebacken, also sicher für Zöliakiebetroffene. Getoastet erwacht die Kruste.',
        'Un pane di grano saraceno e semi, senza glutine e senza rinunce sulla crosta. Cotto in una cucina separata, quindi sicuro per i celiaci. Tostalo e la crosta si risveglia.'),
    'Cardamom buns': ('Brioches à la cardamome', 'Kardamomschnecken', 'Girelle al cardamomo'),
    'Six twisted buns with cardamom sugar and a pearl sugar top. Freshly ground cardamom in the dough and the sugar. Warm them for three minutes before serving.': (
        "Six brioches torsadées au sucre de cardamome, avec du sucre perlé dessus. De la cardamome fraîchement moulue dans la pâte et dans le sucre. Réchauffez-les trois minutes avant de servir.",
        'Sechs gedrehte Schnecken mit Kardamomzucker und Hagelzucker obenauf. Frisch gemahlener Kardamom im Teig und im Zucker. Vor dem Servieren drei Minuten aufwärmen.',
        'Sei girelle intrecciate con zucchero al cardamomo e granella sopra. Cardamomo macinato fresco nell impasto e nello zucchero. Scaldale tre minuti prima di servirle.'),
    'Cave-aged cheddar': ('Cheddar affiné en cave', 'Höhlengereifter Cheddar', 'Cheddar affinato in grotta'),
    'Clothbound cheddar aged eighteen months in a stone cave. Crumbly, sharp, sweet at the end. Made from the milk of one herd and turned by hand in the cave. Cut to order, about 250 g.': (
        "Un cheddar sous toile affiné dix-huit mois dans une cave de pierre. Friable, puissant, sucré en fin de bouche. Fait du lait d'un seul troupeau et retourné à la main dans la cave. Coupé à la commande, environ 250 g.",
        'Ein in Tuch gereifter Cheddar, achtzehn Monate in einer Steinhöhle. Bröckelig, kräftig, am Ende süß. Aus der Milch einer einzigen Herde, in der Höhle von Hand gewendet. Auf Bestellung geschnitten, etwa 250 g.',
        "Un cheddar fasciato nella tela e affinato diciotto mesi in una grotta di pietra. Friabile, deciso, dolce sul finale. Fatto con il latte di una sola mandria e rivoltato a mano nella grotta. Tagliato su ordinazione, circa 250 g."),
    'Manchego 12 months': ('Manchego 12 mois', 'Manchego, 12 Monate', 'Manchego 12 mesi'),
    'Sheep milk cheese aged a year. Nutty and firm, for slicing with quince. From the raw milk of Manchega sheep, with a natural rind. Slice thin and serve at room temperature.': (
        "Un fromage de brebis affiné un an. Fruit sec et ferme, à trancher avec de la pâte de coing. Au lait cru de brebis manchega, avec une croûte naturelle. Tranchez-le fin et servez-le à température ambiante.",
        'Ein Schafskäse, ein Jahr gereift. Nussig und fest, in Scheiben mit Quittenbrot. Aus der Rohmilch von Manchega-Schafen, mit Naturrinde. Dünn schneiden und bei Raumtemperatur servieren.',
        'Un formaggio di pecora stagionato un anno. Di nocciola e compatto, da affettare con la cotognata. Dal latte crudo di pecore manchega, con crosta naturale. Affettalo sottile e servilo a temperatura ambiente.'),
    'Farmhouse brie': ('Brie fermier', 'Bauernhof-Brie', 'Brie di fattoria'),
    'A soft, bloomy-rind brie from raw milk. Ripe at the edges, chalky in the middle. About 400 g, sold ripe. Leave it out for an hour before serving and the middle softens.': (
        "Un brie au lait cru à croûte fleurie. Fait sur les bords, encore crayeux au cœur. Environ 400 g, vendu à point. Sortez-le une heure avant de servir et le cœur s'assouplit.",
        'Ein Brie aus Rohmilch mit Weißschimmelrinde. Am Rand reif, in der Mitte kreidig. Etwa 400 g, reif verkauft. Eine Stunde vor dem Servieren herausnehmen, dann wird die Mitte weich.',
        'Un brie a latte crudo con crosta fiorita. Maturo sui bordi, ancora gessoso al centro. Circa 400 g, venduto a punto. Tiralo fuori un ora prima di servirlo e il cuore si ammorbidisce.'),
    'Pecorino romano': ('Pecorino romano', 'Pecorino Romano', 'Pecorino romano'),
    'Salty sheep milk cheese for grating over pasta. Aged ten months, hard and salty. Grate it over pasta or shave it over broad beans.': (
        "Un fromage de brebis salé à râper sur les pâtes. Affiné dix mois, dur et salé. Râpez-le sur des pâtes ou taillez-le en copeaux sur des fèves.",
        'Ein salziger Schafskäse zum Reiben über Pasta. Zehn Monate gereift, hart und salzig. Über Pasta reiben oder über Saubohnen hobeln.',
        'Un formaggio di pecora sapido da grattugiare sulla pasta. Stagionato dieci mesi, duro e salato. Grattugialo sulla pasta o taglialo a scaglie sulle fave.'),
    'Iberico ham, sliced': ('Jambon ibérique, tranché', 'Iberico-Schinken, geschnitten', 'Prosciutto iberico, affettato'),
    'Acorn-fed Iberico ham, hand sliced and vacuum packed. Cured for thirty-six months in the mountain air. Eighty grams, sliced by hand the day it ships.': (
        "Un jambon ibérique nourri au gland, tranché à la main et emballé sous vide. Affiné trente-six mois à l'air de la montagne. Quatre-vingts grammes, tranchés à la main le jour de l'expédition.",
        'Iberico-Schinken von eichelgefütterten Schweinen, von Hand geschnitten und vakuumiert. Sechsunddreißig Monate in der Bergluft gereift. Achtzig Gramm, am Versandtag von Hand geschnitten.',
        "Prosciutto iberico da maiali nutriti con ghiande, affettato a mano e confezionato sottovuoto. Stagionato trentasei mesi nell'aria di montagna. Ottanta grammi, affettati a mano il giorno della spedizione."),
    'Fennel salami': ('Saucisson au fenouil', 'Fenchelsalami', 'Salame al finocchio'),
    'A coarse pork salami with wild fennel seed, air dried for eight weeks. One whole salami of about 300 g. Peel the casing and slice thick.': (
        "Un saucisson de porc à grain épais, aux graines de fenouil sauvage, séché à l'air pendant huit semaines. Un saucisson entier d'environ 300 g. Retirez la peau et coupez épais.",
        'Eine grobe Schweinesalami mit wildem Fenchelsamen, acht Wochen luftgetrocknet. Eine ganze Salami von etwa 300 g. Die Pelle abziehen und dick schneiden.',
        'Un salame di maiale a grana grossa con semi di finocchietto selvatico, essiccato all aria per otto settimane. Un salame intero di circa 300 g. Togli il budello e taglia spesso.'),
    'Cured chorizo': ('Chorizo sec', 'Luftgetrockneter Chorizo', 'Chorizo stagionato'),
    'Smoked paprika chorizo, cured whole. Slice thin or cook in chunks. About 250 g, mild smoke, a little heat. Fry it in chunks and use the red oil for eggs.': (
        "Un chorizo au paprika fumé, séché entier. À trancher fin ou à cuire en morceaux. Environ 250 g, fumé doux, un peu relevé. Faites-le revenir en morceaux et servez-vous de l'huile rouge pour les œufs.",
        'Ein Chorizo mit geräuchertem Paprika, im Ganzen gereift. Dünn schneiden oder in Stücken braten. Etwa 250 g, milder Rauch, etwas Schärfe. In Stücken anbraten und das rote Öl für Eier nutzen.',
        "Un chorizo al paprika affumicato, stagionato intero. Da affettare sottile o da cuocere a pezzi. Circa 250 g, affumicatura dolce, un po' piccante. Rosolalo a pezzi e usa l'olio rosso per le uova."),
    'Marinated olives': ('Olives marinées', 'Marinierte Oliven', 'Olive marinate'),
    'Green and black olives in oil with lemon peel and thyme. A 300 g jar of mixed olives, with stones. Drain and warm them for a minute before serving.': (
        "Des olives vertes et noires à l'huile, avec du zeste de citron et du thym. Un bocal de 300 g d'olives mélangées, avec noyaux. Égouttez-les et réchauffez-les une minute avant de servir.",
        'Grüne und schwarze Oliven in Öl mit Zitronenschale und Thymian. Ein 300-g-Glas gemischte Oliven, mit Kern. Abtropfen lassen und vor dem Servieren eine Minute erwärmen.',
        'Olive verdi e nere sott olio, con scorza di limone e timo. Un vasetto da 300 g di olive miste, con il nocciolo. Scolale e scaldale un minuto prima di servirle.'),
    'Espresso blend': ('Mélange espresso', 'Espressomischung', 'Miscela espresso'),
    'Brazil and Ethiopia, roasted dark enough for milk and bright enough without. Roasted on Mondays and shipped in the same week. Whole bean or ground for espresso, moka or filter.': (
        "Brésil et Éthiopie, torréfiés assez foncés pour le lait et assez vifs sans. Torréfiés le lundi et expédiés dans la semaine. En grains ou moulus pour l'espresso, la moka ou le filtre.",
        'Brasilien und Äthiopien, dunkel genug für Milch und hell genug ohne. Montags geröstet und in derselben Woche versandt. Ganze Bohne oder gemahlen für Espresso, Moka oder Filter.',
        'Brasile ed Etiopia, tostati abbastanza scuri per il latte e abbastanza vivi senza. Tostati il lunedì e spediti nella stessa settimana. In grani o macinati per espresso, moka o filtro.'),
    'Ethiopia single origin': ('Éthiopie pure origine', 'Äthiopien Single Origin', 'Etiopia monorigine'),
    'Washed Yirgacheffe with jasmine and citrus. Roasted light for filter. Grown at two thousand metres and washed at the mill. Brew at fifteen to one for filter.': (
        "Un Yirgacheffe lavé, aux notes de jasmin et d'agrumes. Torréfaction claire pour le filtre. Cultivé à deux mille mètres et lavé à la station. Dosez à quinze pour un en filtre.",
        'Ein gewaschener Yirgacheffe mit Jasmin und Zitrus. Hell geröstet für Filter. Auf zweitausend Metern angebaut und in der Aufbereitungsanlage gewaschen. Für Filter fünfzehn zu eins dosieren.',
        'Uno Yirgacheffe lavato, con note di gelsomino e agrumi. Tostatura chiara per il filtro. Coltivato a duemila metri e lavato alla stazione. Dosa quindici a uno per il filtro.'),
    'Swiss water decaf': ('Décaféiné à l eau', 'Entkoffeiniert mit Wasser', 'Decaffeinato ad acqua'),
    'A Colombian decaffeinated with water only. Chocolate and red fruit. The caffeine is removed with water alone, so the flavour stays. Nobody notices it is decaf.': (
        "Un colombien décaféiné à l'eau seule. Chocolat et fruits rouges. La caféine est retirée à l'eau, le goût reste donc. Personne ne remarque que c'est un décaféiné.",
        'Ein Kolumbianer, nur mit Wasser entkoffeiniert. Schokolade und rote Früchte. Das Koffein wird allein mit Wasser entzogen, der Geschmack bleibt. Niemand merkt, dass es entkoffeiniert ist.',
        'Un colombiano decaffeinato solo con acqua. Cioccolato e frutti rossi. La caffeina si toglie con la sola acqua, quindi il sapore resta. Nessuno si accorge che è decaffeinato.'),
    'Earl Grey loose leaf': ('Earl Grey en vrac', 'Earl Grey, lose', 'Earl Grey sfuso'),
    'Ceylon black tea with cold-pressed bergamot oil. Big leaves and real bergamot, not flavouring. Three minutes at ninety-five degrees.': (
        "Un thé noir de Ceylan à l'huile de bergamote pressée à froid. De grandes feuilles et de la vraie bergamote, pas un arôme. Trois minutes à quatre-vingt-quinze degrés.",
        'Ein Ceylon-Schwarztee mit kaltgepresstem Bergamottöl. Große Blätter und echte Bergamotte, kein Aroma. Drei Minuten bei fünfundneunzig Grad.',
        'Un tè nero di Ceylon con olio di bergamotto spremuto a freddo. Foglie grandi e bergamotto vero, non aroma. Tre minuti a novantacinque gradi.'),
    'Sencha green tea': ('Thé vert sencha', 'Sencha Grüntee', 'Tè verde sencha'),
    'First-flush sencha, grassy and sweet. Brew at 70 degrees. Steamed and rolled leaves from the spring harvest. Sixty seconds for the first cup, longer for the second.': (
        "Un sencha de première récolte, herbacé et doux. Infusez à 70 degrés. Des feuilles étuvées et roulées de la récolte de printemps. Soixante secondes pour la première tasse, plus longtemps pour la seconde.",
        'Ein Sencha der ersten Ernte, grasig und süß. Bei 70 Grad aufgießen. Gedämpfte und gerollte Blätter der Frühjahrsernte. Sechzig Sekunden für die erste Tasse, länger für die zweite.',
        'Un sencha di primo raccolto, erbaceo e dolce. Infusione a 70 gradi. Foglie cotte al vapore e arrotolate dal raccolto di primavera. Sessanta secondi per la prima tazza, di più per la seconda.'),
    'Chamomile flowers': ('Fleurs de camomille', 'Kamillenblüten', 'Fiori di camomilla'),
    'Whole dried chamomile flowers for a calm evening cup. Whole flowers, not dust, from a farm in the hills. Five minutes covered in a pot.': (
        "Des fleurs de camomille entières séchées, pour une tasse du soir apaisante. Des fleurs entières, pas de la poussière, d'une ferme des collines. Cinq minutes à couvert dans une théière.",
        'Ganze getrocknete Kamillenblüten für eine ruhige Tasse am Abend. Ganze Blüten, kein Staub, von einem Hof in den Hügeln. Fünf Minuten zugedeckt in der Kanne.',
        'Fiori di camomilla interi essiccati, per una tazza serale che calma. Fiori interi, non polvere, da una fattoria di collina. Cinque minuti coperti in teiera.'),
    'Drinking chocolate flakes': ('Copeaux de chocolat chaud', 'Trinkschokoladen-Flocken', 'Scaglie di cioccolata da bere'),
    'Seventy percent dark chocolate flakes for the pan, not the kettle. Two spoons per cup, heated slowly with milk. Made from a single-estate cacao.': (
        "Des copeaux de chocolat noir à soixante-dix pour cent, pour la casserole et non la bouilloire. Deux cuillères par tasse, chauffées doucement avec du lait. Faits d'un cacao d'un seul domaine.",
        'Siebzigprozentige Zartbitterflocken für den Topf, nicht für den Wasserkocher. Zwei Löffel pro Tasse, langsam mit Milch erhitzt. Aus dem Kakao eines einzigen Guts.',
        'Scaglie di cioccolato fondente al settanta per cento, per il pentolino e non per il bollitore. Due cucchiai a tazza, scaldati piano con il latte. Fatte con cacao di una sola tenuta.'),
    'Cloudy apple juice': ('Jus de pomme trouble', 'Naturtrüber Apfelsaft', 'Succo di mela torbido'),
    'Pressed from orchard apples, unfiltered and pasteurised gently. Pressed in the autumn from six old varieties. Cloudy because nothing is filtered out.': (
        "Pressé à partir de pommes de verger, non filtré et pasteurisé en douceur. Pressé à l'automne à partir de six variétés anciennes. Il est trouble parce que rien n'est filtré.",
        'Aus Streuobstäpfeln gepresst, ungefiltert und schonend pasteurisiert. Im Herbst aus sechs alten Sorten gepresst. Naturtrüb, weil nichts herausgefiltert wird.',
        'Spremuto da mele di frutteto, non filtrato e pastorizzato con delicatezza. Spremuto in autunno da sei varietà antiche. È torbido perché non si filtra niente.'),
    'Sicilian lemonade': ('Limonade sicilienne', 'Sizilianische Limonade', 'Limonata siciliana'),
    'Sparkling lemonade with Sicilian lemons and cane sugar, not too sweet. Real lemon juice, cane sugar and water, carbonated in the bottle. Serve very cold.': (
        "Une limonade pétillante aux citrons de Sicile et au sucre de canne, pas trop sucrée. Du vrai jus de citron, du sucre de canne et de l'eau, gazéifiés en bouteille. À servir très frais.",
        'Eine prickelnde Limonade mit sizilianischen Zitronen und Rohrzucker, nicht zu süß. Echter Zitronensaft, Rohrzucker und Wasser, in der Flasche karbonisiert. Sehr kalt servieren.',
        "Una limonata frizzante con limoni di Sicilia e zucchero di canna, non troppo dolce. Succo di limone vero, zucchero di canna e acqua, carbonata in bottiglia. Da servire molto fredda."),
    'Fiery ginger beer': ('Bière de gingembre relevée', 'Feuriges Ingwerbier', 'Ginger beer piccante'),
    'Fermented ginger beer with a real kick. Fresh root ginger, fermented for three days. Drink it alone or with a dark rum.': (
        "Une bière de gingembre fermentée qui a du répondant. Du gingembre frais, fermenté trois jours. À boire seule ou avec un rhum ambré.",
        'Ein fermentiertes Ingwerbier mit echtem Biss. Frische Ingwerwurzel, drei Tage fermentiert. Pur trinken oder mit einem dunklen Rum.',
        'Una ginger beer fermentata che pizzica davvero. Zenzero fresco, fermentato tre giorni. Da bere da sola o con un rum scuro.'),
    'Hibiscus kombucha': ('Kombucha à l hibiscus', 'Hibiskus-Kombucha', 'Kombucha allibisco'),
    'Live kombucha with hibiscus and lime. Keep it cold. A live drink with a light fizz and a sour finish. Store it cold and open it slowly.': (
        "Un kombucha vivant à l'hibiscus et au citron vert. À garder au froid. Une boisson vivante, légèrement pétillante, à la finale acidulée. Conservez-la au froid et ouvrez-la doucement.",
        'Ein lebendiger Kombucha mit Hibiskus und Limette. Kalt halten. Ein lebendiges Getränk mit leichter Kohlensäure und säuerlichem Abgang. Kalt lagern und langsam öffnen.',
        "Un kombucha vivo con ibisco e lime. Da tenere al freddo. Una bevanda viva con una leggera effervescenza e un finale acidulo. Conservala al freddo e aprila piano."),
    'Douro red': ('Rouge du Douro', 'Douro Rotwein', 'Rosso del Douro'),
    'A field blend from old vines in the Douro. Dark fruit, soft tannin, open an hour early. Touriga and friends from vines older than the winemaker. Decant it and drink it with grilled meat.': (
        "Un assemblage de vieilles vignes du Douro. Fruits noirs, tanins souples, à ouvrir une heure avant. Touriga et compagnie, de vignes plus vieilles que le vigneron. Carafez-le et buvez-le avec une viande grillée.",
        'Ein Gemischter Satz von alten Reben im Douro. Dunkle Frucht, weiches Tannin, eine Stunde vorher öffnen. Touriga und Freunde von Reben, die älter sind als der Winzer. Dekantieren und zu Gegrilltem trinken.',
        'Un uvaggio di vecchie vigne del Douro. Frutta scura, tannino morbido, da aprire un ora prima. Touriga e compagni da viti più vecchie del produttore. Decantalo e bevilo con la carne alla griglia.'),
    'Vinho verde': ('Vinho verde', 'Vinho Verde', 'Vinho verde'),
    'Light, dry and faintly sparkling. The summer bottle. Low in alcohol, high in freshness, with a slight prickle. Serve ice cold with fish.': (
        "Léger, sec et légèrement perlant. La bouteille de l'été. Peu d'alcool, beaucoup de fraîcheur, avec un petit picotement. À servir glacé avec du poisson.",
        'Leicht, trocken und leicht prickelnd. Die Sommerflasche. Wenig Alkohol, viel Frische, mit einem kleinen Kribbeln. Eiskalt zu Fisch servieren.',
        'Leggero, secco e appena frizzante. La bottiglia dell estate. Poco alcol, molta freschezza, con un piccolo pizzicore. Servilo ghiacciato con il pesce.'),
    'Rosso vermouth': ('Vermouth rouge', 'Roter Wermut', 'Vermouth rosso'),
    'A bittersweet vermouth with wormwood and orange peel. Serve on ice with a twist. Made on a white wine base with twenty botanicals. Keep it in the fridge once open.': (
        "Un vermouth doux-amer à l'absinthe et au zeste d'orange. À servir sur glace avec un zeste. Élaboré sur une base de vin blanc avec vingt plantes. À garder au frais une fois ouvert.",
        'Ein bittersüßer Wermut mit Wermutkraut und Orangenschale. Auf Eis mit einer Zeste servieren. Auf Weißweinbasis mit zwanzig Botanicals gemacht. Nach dem Öffnen im Kühlschrank aufbewahren.',
        "Un vermouth agrodolce con assenzio e scorza d'arancia. Da servire con ghiaccio e una scorza. Fatto su base di vino bianco con venti botaniche. Dopo l'apertura tienilo in frigo."),
    'Oil and vinegar set': ('Coffret huile et vinaigre', 'Öl-und-Essig-Set', 'Set olio e aceto'),
    'Our Puglia oil with a twelve-year balsamic, boxed together. The two bottles our kitchen reaches for most, in a wooden box. A gift that gets used.': (
        "Notre huile des Pouilles avec un balsamique de douze ans, réunis dans un coffret. Les deux bouteilles que notre cuisine attrape le plus souvent, dans une boîte en bois. Un cadeau qui sert.",
        'Unser apulisches Öl mit einem zwölfjährigen Balsamico, zusammen in einer Kiste. Die zwei Flaschen, nach denen unsere Küche am häufigsten greift, in einer Holzkiste. Ein Geschenk, das benutzt wird.',
        "Il nostro olio pugliese con un balsamico di dodici anni, insieme in una cassetta. Le due bottiglie che la nostra cucina usa di più, in una cassetta di legno. Un regalo che si usa."),
    'Balsamic vinegar 12 years': ('Vinaigre balsamique 12 ans', 'Balsamico, 12 Jahre', 'Aceto balsamico 12 anni'),
    'Aged in a series of wooden casks. Thick, sweet, a few drops at a time. Aged in oak, chestnut and cherry casks. Use it drop by drop on cheese, strawberries or a steak.': (
        "Vieilli dans une batterie de fûts de bois. Épais, sucré, quelques gouttes à la fois. Vieilli en fûts de chêne, de châtaignier et de cerisier. Utilisez-le goutte à goutte sur un fromage, des fraises ou une pièce de viande.",
        'In einer Reihe von Holzfässern gereift. Dickflüssig, süß, ein paar Tropfen auf einmal. In Eichen-, Kastanien- und Kirschfässern gereift. Tropfenweise über Käse, Erdbeeren oder ein Steak.',
        'Invecchiato in una batteria di botti di legno. Denso, dolce, poche gocce alla volta. Invecchiato in botti di rovere, castagno e ciliegio. Usalo goccia a goccia su formaggio, fragole o una bistecca.'),
    'Breakfast crate': ('Coffret petit-déjeuner', 'Frühstückskiste', 'Cassetta colazione'),
    'Croissants, honey, apricot jam and a bag of espresso in a wooden crate. Everything for a slow Sunday morning, packed the night before it ships. The crate is a nice thing to keep.': (
        "Croissants, miel, confiture d'abricot et un paquet d'espresso dans une caisse en bois. Tout pour un dimanche matin sans hâte, préparé la veille de l'expédition. La caisse est agréable à garder.",
        'Croissants, Honig, Aprikosenmarmelade und ein Beutel Espresso in einer Holzkiste. Alles für einen langsamen Sonntagmorgen, am Abend vor dem Versand gepackt. Die Kiste behält man gern.',
        'Croissant, miele, marmellata di albicocche e un pacchetto di espresso in una cassetta di legno. Tutto per una domenica mattina senza fretta, preparata la sera prima della spedizione. La cassetta è bella da tenere.'),
    'Cheese board crate': ('Coffret plateau de fromages', 'Käsebrett-Kiste', 'Cassetta tagliere di formaggi'),
    'Cheddar, manchego, brie and fig jam, cut and packed cold. Four cheeses and a jam that suits them all, with tasting notes. Serves six as a course.': (
        "Cheddar, manchego, brie et confiture de figues, coupés et emballés au froid. Quatre fromages et une confiture qui va avec tous, avec des notes de dégustation. Pour six personnes en plateau.",
        'Cheddar, Manchego, Brie und Feigenmarmelade, geschnitten und kalt verpackt. Vier Käse und eine Marmelade, die zu allen passt, mit Verkostungsnotizen. Reicht für sechs als Gang.',
        'Cheddar, manchego, brie e marmellata di fichi, tagliati e confezionati al freddo. Quattro formaggi e una marmellata che sta bene con tutti, con note di degustazione. Per sei persone come portata.'),
    'Aperitivo crate': ('Coffret apéritif', 'Aperitivo-Kiste', 'Cassetta aperitivo'),
    'Vermouth, olives, fennel salami and a bag of taralli. The hour before dinner, in a box. Serve the vermouth on ice with an orange peel.': (
        "Vermouth, olives, saucisson au fenouil et un paquet de taralli. L'heure d'avant le dîner, dans une boîte. Servez le vermouth sur glace avec un zeste d'orange.",
        'Wermut, Oliven, Fenchelsalami und ein Beutel Taralli. Die Stunde vor dem Abendessen, in einer Kiste. Den Wermut auf Eis mit einer Orangenschale servieren.',
        "Vermouth, olive, salame al finocchio e un pacchetto di taralli. L'ora prima di cena, in una cassetta. Servi il vermouth con ghiaccio e una scorza d'arancia."),
    'Fennel taralli': ('Taralli au fenouil', 'Fenchel-Taralli', 'Taralli al finocchio'),
    'Crunchy ring biscuits with fennel seed and olive oil, for the aperitivo hour. Baked twice, so they stay crunchy for weeks. A 250 g bag.': (
        "De petits anneaux croquants aux graines de fenouil et à l'huile d'olive, pour l'apéritif. Cuits deux fois, ils restent croquants des semaines. Un sachet de 250 g.",
        'Knusprige Ringe mit Fenchelsamen und Olivenöl, für die Aperitivo-Stunde. Zweimal gebacken, deshalb bleiben sie wochenlang knusprig. Ein 250-g-Beutel.',
        "Anelli croccanti con semi di finocchio e olio d'oliva, per l'ora dell'aperitivo. Cotti due volte, così restano croccanti per settimane. Un sacchetto da 250 g."),
    'Marcona almonds': ('Amandes Marcona', 'Marcona-Mandeln', 'Mandorle Marcona'),
    'Fried in olive oil and salted. The bar snack. Flat, sweet almonds from Spain, fried and salted lightly. A 200 g bag.': (
        "Frites à l'huile d'olive et salées. Le grignotage de comptoir. Des amandes plates et douces d'Espagne, frites et légèrement salées. Un sachet de 200 g.",
        'In Olivenöl frittiert und gesalzen. Der Snack an der Bar. Flache, süße Mandeln aus Spanien, frittiert und leicht gesalzen. Ein 200-g-Beutel.',
        "Fritte nell'olio d'oliva e salate. Lo snack da bancone. Mandorle piatte e dolci dalla Spagna, fritte e salate appena. Un sacchetto da 200 g."),
    'Dark chocolate bar 72%': ('Tablette de chocolat noir 72 %', 'Zartbitterschokolade 72 %', 'Tavoletta fondente 72%'),
    'Single-estate cacao, stone ground, seventy-two percent. A 70 g bar with a clean snap and a long finish. Stone ground, so the texture is slightly rough.': (
        "Un cacao d'un seul domaine, broyé à la meule de pierre, à soixante-douze pour cent. Une tablette de 70 g à la cassure nette et à la longue finale. Broyée à la pierre, la texture est légèrement râpeuse.",
        'Kakao von einem einzigen Gut, auf Stein gemahlen, zweiundsiebzig Prozent. Eine 70-g-Tafel mit sauberem Bruch und langem Abgang. Auf Stein gemahlen, daher ist die Textur leicht rau.',
        'Cacao di una sola tenuta, macinato a pietra, settantadue per cento. Una tavoletta da 70 g con uno spacco netto e un finale lungo. Macinata a pietra, quindi la texture è leggermente ruvida.'),
    'Maple pecan granola': ('Granola érable et noix de pécan', 'Ahorn-Pekan-Granola', 'Granola acero e pecan'),
    'Oats, pecans and maple, baked in small trays until the clusters hold. A 500 g bag with real clusters and not too much sugar. Pecans in every handful.': (
        "Avoine, noix de pécan et sirop d'érable, cuits en petites plaques jusqu'à ce que les grappes tiennent. Un sachet de 500 g avec de vraies grappes et peu de sucre. Des noix de pécan dans chaque poignée.",
        'Hafer, Pekannüsse und Ahornsirup, in kleinen Blechen gebacken, bis die Cluster halten. Ein 500-g-Beutel mit echten Clustern und nicht zu viel Zucker. Pekannüsse in jeder Handvoll.',
        "Avena, noci pecan e sciroppo d'acero, cotti in piccole teglie finché i grumi tengono. Un sacchetto da 500 g con grumi veri e poco zucchero. Pecan in ogni manciata."),

    # Books. The titles are invented, so each store view gets the title of its own edition.
    'The Salt Houses': ('Les maisons de sel', 'Die Salzhäuser', 'Le case di sale'),
    'Three sisters return to a fishing village to sell the family house and find the tide has other plans. A novel about what we keep. Three hundred and twenty pages, clothbound with a ribbon marker. The first novel of the year to make our staff argue.': (
        "Trois sœurs reviennent dans un village de pêcheurs pour vendre la maison de famille, et la marée en décide autrement. Un roman sur ce que l'on garde. Trois cent vingt pages, relié toile avec un signet ruban. Le premier roman de l'année à faire débattre notre équipe.",
        'Drei Schwestern kehren in ein Fischerdorf zurück, um das Elternhaus zu verkaufen, und die Flut hat andere Pläne. Ein Roman darüber, was wir behalten. Dreihundertzwanzig Seiten, Leineneinband mit Lesebändchen. Der erste Roman des Jahres, über den unser Team streitet.',
        "Tre sorelle tornano in un villaggio di pescatori per vendere la casa di famiglia e scoprono che la marea ha altri piani. Un romanzo su ciò che teniamo. Trecentoventi pagine, rilegato in tela con segnalibro. Il primo romanzo dell'anno che ha fatto discutere il nostro staff."),
    'The Last Orchard': ('Le dernier verger', 'Der letzte Obstgarten', "L'ultimo frutteto"),
    'A widower plants a hundred trees he will not live to see fruit. His neighbours have opinions. A short, warm book about time and stubbornness. Read it in an afternoon and think about it for a week.': (
        "Un veuf plante cent arbres dont il ne verra jamais les fruits. Ses voisins ont un avis. Un livre court et chaleureux sur le temps et l'obstination. Lisez-le en un après-midi, il vous suivra une semaine.",
        'Ein Witwer pflanzt hundert Bäume, deren Früchte er nicht mehr erleben wird. Seine Nachbarn haben eine Meinung dazu. Ein kurzes, warmes Buch über Zeit und Sturheit. An einem Nachmittag gelesen, eine Woche im Kopf.',
        'Un vedovo pianta cento alberi di cui non vedrà i frutti. I vicini hanno la loro opinione. Un libro breve e caldo sul tempo e sulla testardaggine. Si legge in un pomeriggio e resta in testa una settimana.'),
    'Quiet Rooms': ('Chambres silencieuses', 'Stille Zimmer', 'Stanze silenziose'),
    'Linked short stories set in one apartment building over forty years. Twelve stories, each in a different flat, each a different decade. Readers of quiet fiction will feel at home.': (
        "Des nouvelles liées, situées dans un même immeuble sur quarante ans. Douze histoires, chacune dans un appartement différent, chacune dans une décennie différente. Les amateurs de récits discrets seront chez eux.",
        'Verbundene Erzählungen in einem einzigen Wohnhaus über vierzig Jahre. Zwölf Geschichten, jede in einer anderen Wohnung, jede in einem anderen Jahrzehnt. Wer leise Literatur mag, ist hier zu Hause.',
        'Racconti legati tra loro, ambientati in un solo condominio nell arco di quarant anni. Dodici storie, ognuna in un appartamento diverso, ognuna in un decennio diverso. Chi ama la narrativa sommessa si sentirà a casa.'),
    'North Light': ('Lumière du nord', 'Nordlicht', 'Luce del nord'),
    'A painter moves to the far north to escape a scandal and finds the light does not care. Long winters, long sentences and a slow thaw. A novel for a fireside and a blanket.': (
        "Un peintre part vers le grand nord pour fuir un scandale et découvre que la lumière s'en moque. De longs hivers, de longues phrases et un dégel lent. Un roman pour le coin du feu et une couverture.",
        'Ein Maler zieht in den hohen Norden, um einem Skandal zu entkommen, und stellt fest, dass das Licht sich nicht darum schert. Lange Winter, lange Sätze und ein langsames Tauwetter. Ein Roman für Kamin und Decke.',
        'Un pittore si trasferisce nel profondo nord per sfuggire a uno scandalo e scopre che alla luce non importa. Inverni lunghi, frasi lunghe e un disgelo lento. Un romanzo da camino e coperta.'),
    'Paper Birds': ('Oiseaux de papier', 'Papiervögel', 'Uccelli di carta'),
    'A translator falls for the author she cannot meet. Quiet and devastating. Told in letters and margin notes. Two hundred pages, best read in one sitting.': (
        "Une traductrice s'éprend de l'auteur qu'elle ne peut pas rencontrer. Discret et dévastateur. Raconté par lettres et notes en marge. Deux cents pages, à lire d'une traite.",
        'Eine Übersetzerin verliebt sich in den Autor, den sie nicht treffen kann. Leise und niederschmetternd. Erzählt in Briefen und Randnotizen. Zweihundert Seiten, am besten in einem Zug.',
        "Una traduttrice si innamora dell'autore che non può incontrare. Sommesso e devastante. Raccontato per lettere e note a margine. Duecento pagine, meglio in una sola seduta."),
    'The Summer House': ("La maison d'été", 'Das Sommerhaus', 'La casa destate'),
    'Six friends, one house by the lake, and a promise nobody kept. A holiday novel with teeth. Every chapter is a different summer, and the last one changes the rest.': (
        "Six amis, une maison au bord du lac et une promesse que personne n'a tenue. Un roman de vacances qui mord. Chaque chapitre est un été différent, et le dernier change tous les autres.",
        'Sechs Freunde, ein Haus am See und ein Versprechen, das niemand gehalten hat. Ein Ferienroman mit Zähnen. Jedes Kapitel ist ein anderer Sommer, und der letzte verändert alle davor.',
        "Sei amici, una casa sul lago e una promessa che nessuno ha mantenuto. Un romanzo estivo che morde. Ogni capitolo è un'estate diversa, e l'ultimo cambia tutti gli altri."),
    'Cold Harbour': ('Port froid', 'Kalter Hafen', 'Porto freddo'),
    'A body in the harbour, a town that lies in unison, and a detective who grew up there. The first Ruth Mallory novel. A slow, cold crime story with a detective who knows every face in the pub.': (
        "Un corps dans le port, une ville qui ment d'une seule voix et une enquêtrice qui a grandi là. Le premier roman de Ruth Mallory. Un polar lent et froid, avec une enquêtrice qui connaît tous les visages du bar.",
        'Eine Leiche im Hafen, eine Stadt, die im Chor lügt, und eine Ermittlerin, die dort aufgewachsen ist. Der erste Ruth-Mallory-Roman. Ein langsamer, kalter Krimi mit einer Ermittlerin, die jedes Gesicht in der Kneipe kennt.',
        'Un corpo nel porto, una città che mente all unisono e una detective che è cresciuta lì. Il primo romanzo di Ruth Mallory. Un giallo lento e freddo con una detective che conosce ogni faccia del pub.'),
    'The Long Tide': ('La longue marée', 'Die lange Flut', 'La lunga marea'),
    'Mallory returns. So does the past. The second Mallory novel picks up ten years later. Read Cold Harbour first, though it stands alone.': (
        "Mallory revient. Le passé aussi. Le deuxième roman reprend dix ans plus tard. Lisez Port froid d'abord, même s'il se tient seul.",
        'Mallory kehrt zurück. Die Vergangenheit auch. Der zweite Mallory-Roman setzt zehn Jahre später ein. Lies Kalter Hafen zuerst, auch wenn er für sich steht.',
        'Mallory torna. E torna anche il passato. Il secondo romanzo riprende dieci anni dopo. Leggi prima Porto freddo, anche se questo si regge da solo.'),
    'Clean Break': ('Coupure nette', 'Sauberer Schnitt', 'Taglio netto'),
    'A heist planned by a locksmith who has never broken a law. Until now. Fast, funny and precise about locks. The plan goes wrong on page forty and keeps going wrong.': (
        "Un casse préparé par un serrurier qui n'a jamais enfreint la loi. Jusqu'ici. Rapide, drôle et très précis sur les serrures. Le plan déraille page quarante et continue de dérailler.",
        'Ein Coup, geplant von einem Schlosser, der nie ein Gesetz gebrochen hat. Bis jetzt. Schnell, komisch und genau, was Schlösser angeht. Der Plan geht auf Seite vierzig schief und danach immer weiter.',
        'Un colpo pianificato da un fabbro che non ha mai infranto una legge. Fino a ora. Veloce, divertente e preciso sulle serrature. Il piano va storto a pagina quaranta e continua ad andare storto.'),
    'The Midnight Train': ('Le train de minuit', 'Der Mitternachtszug', 'Il treno di mezzanotte'),
    'A cosy mystery on the overnight sleeper to the coast. No blood, plenty of tea, and a puzzle that plays fair. The first of a series.': (
        "Une enquête douce à bord du train de nuit vers la côte. Pas de sang, beaucoup de thé et une énigme qui joue franc jeu. Le premier d'une série.",
        'Ein gemütlicher Krimi im Nachtzug an die Küste. Kein Blut, viel Tee und ein Rätsel, das fair spielt. Der erste einer Reihe.',
        'Un giallo gentile sul treno notturno verso la costa. Niente sangue, molto tè e un enigma che gioca pulito. Il primo di una serie.'),
    'The Witness Room': ('La salle des témoins', 'Der Zeugenraum', 'La stanza dei testimoni'),
    'A courtroom thriller told by the one person who cannot speak. A thriller built on a single trick, and the trick holds. Best not to read the last page first.': (
        "Un thriller judiciaire raconté par la seule personne qui ne peut pas parler. Un thriller bâti sur une seule idée, et l'idée tient. Mieux vaut ne pas lire la dernière page en premier.",
        'Ein Gerichtsthriller, erzählt von der einzigen Person, die nicht sprechen kann. Ein Thriller, der auf einem einzigen Kniff steht, und der Kniff trägt. Lies besser nicht zuerst die letzte Seite.',
        "Un thriller giudiziario raccontato dall'unica persona che non può parlare. Un thriller costruito su un solo trucco, e il trucco regge. Meglio non leggere prima l'ultima pagina."),
    'Small Things Everywhere': ('De petites choses partout', 'Kleine Dinge überall', 'Piccole cose ovunque'),
    'Microbiology for the curious, from your kitchen sponge to the deep sea. Short chapters, clear drawings, no equations. Written for adults who remember liking science once.': (
        "La microbiologie pour les curieux, de l'éponge de cuisine aux grands fonds. Des chapitres courts, des dessins clairs, aucune équation. Écrit pour les adultes qui se souviennent d'avoir aimé les sciences.",
        'Mikrobiologie für Neugierige, vom Küchenschwamm bis in die Tiefsee. Kurze Kapitel, klare Zeichnungen, keine Gleichungen. Für Erwachsene, die sich erinnern, dass sie Naturwissenschaft mal mochten.',
        'La microbiologia per i curiosi, dalla spugna della cucina agli abissi. Capitoli brevi, disegni chiari, nessuna equazione. Scritto per adulti che ricordano di aver amato la scienza.'),
    'Deep Time': ('Le temps profond', 'Tiefenzeit', 'Il tempo profondo'),
    'The story of the Earth in twelve rocks. Each chapter starts with one rock and ends with a continent. Full-page colour plates throughout.': (
        "L'histoire de la Terre en douze roches. Chaque chapitre part d'une roche et finit sur un continent. Des planches en couleur pleine page tout du long.",
        'Die Geschichte der Erde in zwölf Gesteinen. Jedes Kapitel beginnt mit einem Stein und endet mit einem Kontinent. Durchgehend ganzseitige Farbtafeln.',
        'La storia della Terra in dodici rocce. Ogni capitolo parte da una roccia e finisce con un continente. Tavole a colori a piena pagina in tutto il volume.'),
    'The Pocket Bird Guide': ('Le guide des oiseaux de poche', 'Der Vogelführer für die Tasche', 'La guida tascabile agli uccelli'),
    'Two hundred birds, one pocket. Waterproof cover. Two hundred species with a painting, a map and the call in words. It fits a coat pocket and survives rain.': (
        "Deux cents oiseaux, une poche. Couverture imperméable. Deux cents espèces avec une planche, une carte et le chant décrit en mots. Il tient dans une poche de manteau et survit à la pluie.",
        'Zweihundert Vögel, eine Tasche. Wasserfester Einband. Zweihundert Arten mit Zeichnung, Karte und dem Ruf in Worten. Er passt in die Manteltasche und übersteht Regen.',
        'Duecento uccelli, una tasca. Copertina impermeabile. Duecento specie con una tavola, una mappa e il canto descritto a parole. Sta in tasca al cappotto e resiste alla pioggia.'),
    'The Night Sky, Month by Month': ('Le ciel nocturne, mois par mois', 'Der Nachthimmel, Monat für Monat', 'Il cielo notturno, mese per mese'),
    'A year of stargazing with a torch and this book. Twelve chapters, one per month, with charts drawn for the naked eye. A red torch is all the equipment you need.': (
        "Une année d'observation avec une lampe et ce livre. Douze chapitres, un par mois, avec des cartes dessinées pour l'œil nu. Une lampe rouge est tout l'équipement nécessaire.",
        'Ein Jahr Sternegucken mit einer Lampe und diesem Buch. Zwölf Kapitel, eines pro Monat, mit Karten für das bloße Auge. Eine rote Lampe ist die ganze Ausrüstung.',
        "Un anno di osservazione con una torcia e questo libro. Dodici capitoli, uno al mese, con carte disegnate per l'occhio nudo. Una torcia rossa è tutta l'attrezzatura che serve."),
    'Trees of the Old World': ("Les arbres de l'Ancien Monde", 'Bäume der Alten Welt', 'Alberi del Vecchio Mondo'),
    'A large-format guide to five hundred trees, with leaf and bark plates. A coffee-table book that is also a real reference. The plates show leaf, bark, flower and winter twig.': (
        "Un guide grand format de cinq cents arbres, avec des planches de feuilles et d'écorces. Un beau livre qui est aussi une vraie référence. Les planches montrent la feuille, l'écorce, la fleur et le rameau d'hiver.",
        'Ein großformatiger Führer zu fünfhundert Bäumen, mit Blatt- und Rindentafeln. Ein Bildband, der zugleich ein echtes Nachschlagewerk ist. Die Tafeln zeigen Blatt, Rinde, Blüte und Winterzweig.',
        'Una guida di grande formato a cinquecento alberi, con tavole di foglie e cortecce. Un libro da tavolo che è anche una vera opera di consultazione. Le tavole mostrano foglia, corteccia, fiore e ramo invernale.'),
    'A Short History of Weather': ('Une brève histoire du temps quil fait', 'Eine kurze Geschichte des Wetters', 'Breve storia del tempo atmosferico'),
    'Clouds, storms and the people who learned to read them. From shepherds to satellites in three hundred pages. Written with a lightness that suits the subject.': (
        "Les nuages, les tempêtes et ceux qui ont appris à les lire. Des bergers aux satellites en trois cents pages. Écrit avec une légèreté qui convient au sujet.",
        'Wolken, Stürme und die Menschen, die sie lesen lernten. Von Hirten zu Satelliten in dreihundert Seiten. Mit einer Leichtigkeit geschrieben, die zum Thema passt.',
        'Nuvole, tempeste e le persone che hanno imparato a leggerle. Dai pastori ai satelliti in trecento pagine. Scritto con una leggerezza che si addice al tema.'),
    'Roads of Silk': ('Les routes de la soie', 'Straßen aus Seide', 'Strade di seta'),
    'A journey along the old trade routes, then and now. Part travel diary, part history. The author walks and takes the bus, and both make good chapters.': (
        "Un voyage le long des anciennes routes commerciales, hier et aujourd'hui. Moitié carnet de route, moitié histoire. L'auteur marche et prend le bus, et les deux donnent de bons chapitres.",
        'Eine Reise entlang der alten Handelswege, damals und heute. Halb Reisetagebuch, halb Geschichte. Der Autor geht zu Fuß und nimmt den Bus, und beides ergibt gute Kapitel.',
        "Un viaggio lungo le antiche vie commerciali, ieri e oggi. Metà diario di viaggio, metà storia. L'autore cammina e prende l'autobus, e da entrambi nascono buoni capitoli."),
    'The City of Water': ('La ville deau', 'Die Stadt aus Wasser', "La città d'acqua"),
    'Venice from lagoon to biennale, in twenty buildings. Twenty buildings, twenty short essays, one plan of the city. Take it with you or read it at home.': (
        "Venise de la lagune à la biennale, en vingt bâtiments. Vingt bâtiments, vingt courts essais, un plan de la ville. À emporter ou à lire chez soi.",
        'Venedig von der Lagune bis zur Biennale, in zwanzig Bauten. Zwanzig Bauten, zwanzig kurze Essays, ein Stadtplan. Zum Mitnehmen oder zum Lesen zu Hause.',
        'Venezia dalla laguna alla biennale, in venti edifici. Venti edifici, venti brevi saggi, una pianta della città. Da portare con sé o da leggere a casa.'),
    'Letters from the Front': ('Lettres du front', 'Briefe von der Front', 'Lettere dal fronte'),
    'Sixty letters, sixty lives. A war told from the kitchen table. The letters are printed whole, with a page of context before each one. Hard to read quickly.': (
        "Soixante lettres, soixante vies. Une guerre racontée depuis la table de la cuisine. Les lettres sont imprimées en entier, avec une page de contexte avant chacune. Difficile à lire vite.",
        'Sechzig Briefe, sechzig Leben. Ein Krieg, erzählt vom Küchentisch aus. Die Briefe sind vollständig abgedruckt, mit einer Seite Kontext vor jedem. Schwer schnell zu lesen.',
        'Sessanta lettere, sessanta vite. Una guerra raccontata dal tavolo di cucina. Le lettere sono stampate per intero, con una pagina di contesto prima di ognuna. Difficile leggerlo in fretta.'),
    'An Empire of Tea': ('Un empire du thé', 'Ein Imperium aus Tee', 'Un impero di tè'),
    'How a leaf built fortunes and broke nations. Trade, taste and politics in one leaf. The author has a gift for the telling detail.': (
        "Comment une feuille a bâti des fortunes et brisé des nations. Commerce, goût et politique dans une seule feuille. L'auteur a le don du détail qui parle.",
        'Wie ein Blatt Vermögen schuf und Nationen zerbrach. Handel, Geschmack und Politik in einem einzigen Blatt. Der Autor hat ein Gespür für das sprechende Detail.',
        "Come una foglia ha costruito fortune e spezzato nazioni. Commercio, gusto e politica in una sola foglia. L'autore ha il dono del dettaglio che dice tutto."),
    'The Plague Year': ('Lannée de la peste', 'Das Pestjahr', 'Lanno della peste'),
    'One city, one year, one doctor keeping a diary. A diary edited into a story, with the gaps left in. The doctor never says what he feels, and you feel it anyway.': (
        "Une ville, une année, un médecin qui tient un journal. Un journal transformé en récit, avec les silences conservés. Le médecin ne dit jamais ce qu'il ressent, et on le ressent quand même.",
        'Eine Stadt, ein Jahr, ein Arzt, der Tagebuch führt. Ein Tagebuch, zu einer Erzählung geordnet, mit den Lücken darin. Der Arzt sagt nie, was er fühlt, und man fühlt es trotzdem.',
        'Una città, un anno, un medico che tiene un diario. Un diario montato in racconto, con i vuoti lasciati dentro. Il medico non dice mai quello che prova, e tu lo senti lo stesso.'),
    'Weeknight': ('En semaine', 'Unter der Woche', 'Feriali'),
    'Sixty dinners in under forty minutes, with a shopping list that fits one hand. Every recipe on one page, with a photo and a timeline. Sixty dinners, no special equipment.': (
        "Soixante dîners en moins de quarante minutes, avec une liste de courses qui tient dans une main. Chaque recette sur une page, avec une photo et un déroulé. Soixante dîners, sans matériel particulier.",
        'Sechzig Abendessen in unter vierzig Minuten, mit einer Einkaufsliste, die in eine Hand passt. Jedes Rezept auf einer Seite, mit Foto und Zeitplan. Sechzig Abendessen, ohne Spezialgerät.',
        'Sessanta cene in meno di quaranta minuti, con una lista della spesa che sta in una mano. Ogni ricetta su una pagina, con foto e tempi. Sessanta cene, senza attrezzatura speciale.'),
    'The Bread Book': ('Le livre du pain', 'Das Brotbuch', 'Il libro del pane'),
    'Sourdough, flatbreads and buns, with step photographs and no mystique. Twenty base recipes with variations, and photographs of every fold. The starter chapter alone is worth the price.': (
        "Pain au levain, galettes et brioches, avec des photos d'étapes et sans mystère. Vingt recettes de base avec des variantes, et une photo de chaque rabat. Le chapitre sur le levain vaut à lui seul le prix.",
        'Sauerteig, Fladenbrote und Brötchen, mit Schrittfotos und ohne Geheimniskrämerei. Zwanzig Grundrezepte mit Varianten und Fotos von jeder Faltung. Allein das Kapitel zum Anstellgut ist den Preis wert.',
        'Lievito madre, focacce e panini, con foto passo passo e senza misteri. Venti ricette base con varianti e la foto di ogni piega. Il capitolo sul lievito vale da solo il prezzo.'),
    'Vegetables First': ("Les légumes d'abord", 'Gemüse zuerst', 'Prima le verdure'),
    'A hundred recipes that start with what is in season. Organised by season, then by vegetable. Most recipes feed four in under an hour.': (
        "Cent recettes qui partent de ce qui est de saison. Classées par saison, puis par légume. La plupart nourrissent quatre personnes en moins d'une heure.",
        'Hundert Rezepte, die bei dem beginnen, was Saison hat. Nach Jahreszeit geordnet, dann nach Gemüse. Die meisten sättigen vier Personen in unter einer Stunde.',
        "Cento ricette che partono da quello che è di stagione. Ordinate per stagione, poi per verdura. Quasi tutte sfamano quattro persone in meno di un'ora."),
    'Jars': ('Bocaux', 'Gläser', 'Barattoli'),
    'Jams, pickles and ferments for a small kitchen. Small batches, ordinary jars, a chapter on what went wrong and why. Good for a first ferment.': (
        "Confitures, conserves au vinaigre et ferments pour une petite cuisine. Petites quantités, bocaux ordinaires, un chapitre sur ce qui a raté et pourquoi. Parfait pour une première fermentation.",
        'Marmeladen, Eingelegtes und Fermente für eine kleine Küche. Kleine Mengen, gewöhnliche Gläser, ein Kapitel darüber, was schiefging und warum. Gut für die erste Fermentation.',
        'Marmellate, sottaceti e fermentati per una cucina piccola. Piccole quantità, barattoli comuni, un capitolo su cosa è andato storto e perché. Ottimo per una prima fermentazione.'),
    'Coffee at Home': ('Le café à la maison', 'Kaffee zu Hause', 'Il caffè a casa'),
    'Beans, water, grind, time. Everything else is detail. Filter, espresso, cold brew, in that order of difficulty. Each method has a ratio and a timing chart.': (
        "Le grain, l'eau, la mouture, le temps. Tout le reste est du détail. Filtre, espresso, extraction à froid, dans cet ordre de difficulté. Chaque méthode a son ratio et son tableau de temps.",
        'Bohne, Wasser, Mahlgrad, Zeit. Alles andere ist Detail. Filter, Espresso, Cold Brew, in dieser Reihenfolge der Schwierigkeit. Jede Methode hat ein Verhältnis und eine Zeittabelle.',
        "Chicco, acqua, macinatura, tempo. Tutto il resto è dettaglio. Filtro, espresso, cold brew, in quest'ordine di difficoltà. Ogni metodo ha un rapporto e una tabella dei tempi."),
    'Goodnight, Little Fox': ('Bonne nuit, petit renard', 'Gute Nacht, kleiner Fuchs', 'Buonanotte, piccola volpe'),
    'A picture book for the last five minutes of the day. Twenty-four pages, soft colours, one sentence a page. Ages one to four.': (
        "Un album pour les cinq dernières minutes de la journée. Vingt-quatre pages, des couleurs douces, une phrase par page. De un à quatre ans.",
        'Ein Bilderbuch für die letzten fünf Minuten des Tages. Vierundzwanzig Seiten, weiche Farben, ein Satz pro Seite. Von eins bis vier Jahren.',
        'Un albo illustrato per gli ultimi cinque minuti della giornata. Ventiquattro pagine, colori tenui, una frase per pagina. Da uno a quattro anni.'),
    'The Big Dig': ('Le grand chantier', 'Die große Baustelle', 'Il grande scavo'),
    'Diggers, dumpers and a very deep hole. Big machines, big sounds, and a hole that gets deeper every page. Ages two to five.': (
        "Des pelleteuses, des tombereaux et un trou très profond. De grosses machines, de gros bruits, et un trou qui se creuse à chaque page. De deux à cinq ans.",
        'Bagger, Kipper und ein sehr tiefes Loch. Große Maschinen, große Geräusche und ein Loch, das mit jeder Seite tiefer wird. Von zwei bis fünf Jahren.',
        'Scavatrici, dumper e una buca molto profonda. Macchine grandi, rumori grandi e una buca che si fa più profonda a ogni pagina. Da due a cinque anni.'),
    'Milo and the Sea': ('Milo et la mer', 'Milo und das Meer', 'Milo e il mare'),
    'A first chapter book about a boy, a boat and a very patient seagull. Ten short chapters with a picture on every spread. For readers of six to eight.': (
        "Un premier roman illustré sur un garçon, un bateau et une mouette très patiente. Dix courts chapitres avec une image sur chaque double page. Pour les lecteurs de six à huit ans.",
        'Ein erstes Kapitelbuch über einen Jungen, ein Boot und eine sehr geduldige Möwe. Zehn kurze Kapitel mit einem Bild auf jeder Doppelseite. Für Leser von sechs bis acht.',
        'Un primo libro a capitoli su un bambino, una barca e un gabbiano molto paziente. Dieci capitoli brevi con una figura su ogni doppia pagina. Per lettori dai sei agli otto anni.'),
    'Dragon School': ('Lécole des dragons', 'Drachenschule', 'La scuola dei draghi'),
    'Where dragons learn to fly and one of them would rather read. A funny school story with a quiet hero. Ages seven to ten, and the adult reading aloud.': (
        "Là où les dragons apprennent à voler, et où l'un d'eux préfère lire. Une histoire d'école drôle avec un héros discret. De sept à dix ans, et l'adulte qui lit à voix haute.",
        'Wo Drachen fliegen lernen und einer von ihnen lieber liest. Eine lustige Schulgeschichte mit einem leisen Helden. Von sieben bis zehn Jahren, und für den Erwachsenen, der vorliest.',
        "Dove i draghi imparano a volare e uno di loro preferisce leggere. Una storia di scuola divertente con un eroe sommesso. Dai sette ai dieci anni, e per l'adulto che legge ad alta voce."),
    'A is for Anteater': ('A comme fourmilier', 'A wie Ameisenbär', 'A come formichiere'),
    'An alphabet of unusual animals, painted in gouache. Every letter gets an animal nobody expects and a painting to match. Ages three to six.': (
        "Un alphabet d'animaux inattendus, peints à la gouache. Chaque lettre reçoit un animal auquel personne ne pense et une peinture assortie. De trois à six ans.",
        'Ein Alphabet ungewöhnlicher Tiere, in Gouache gemalt. Jeder Buchstabe bekommt ein Tier, mit dem niemand rechnet, und ein passendes Bild. Von drei bis sechs Jahren.',
        'Un alfabeto di animali insoliti, dipinti a guazzo. Ogni lettera riceve un animale a cui nessuno pensa e un dipinto che gli somiglia. Dai tre ai sei anni.'),
    'Ask an Astronaut': ('Demande à une astronaute', 'Frag eine Astronautin', 'Chiedi a unastronauta'),
    'Fifty questions from children, answered from orbit. Real questions from real children, answered with patience and photographs. Ages eight and up.': (
        "Cinquante questions d'enfants, auxquelles on répond depuis l'orbite. De vraies questions de vrais enfants, des réponses patientes et des photographies. À partir de huit ans.",
        'Fünfzig Fragen von Kindern, aus dem Orbit beantwortet. Echte Fragen echter Kinder, geduldig beantwortet und mit Fotos. Ab acht Jahren.',
        "Cinquanta domande dei bambini, con risposta dall'orbita. Domande vere di bambini veri, risposte pazienti e fotografie. Dagli otto anni in su."),
    'Poems of the Sea': ('Poèmes de la mer', 'Gedichte vom Meer', 'Poesie del mare'),
    'Two hundred years of poems about water, in a pocket edition. Two hundred poems in a cloth pocket edition with a ribbon. The kind of book that lives in a coat.': (
        "Deux cents ans de poèmes sur l'eau, en édition de poche. Deux cents poèmes dans une édition de poche reliée toile, avec un signet. Le genre de livre qui vit dans un manteau.",
        'Zweihundert Jahre Gedichte über Wasser, in einer Taschenausgabe. Zweihundert Gedichte in einer Leinen-Taschenausgabe mit Lesebändchen. Ein Buch, das im Mantel wohnt.',
        'Duecento anni di poesie sull acqua, in edizione tascabile. Duecento poesie in un tascabile rilegato in tela con segnalibro. Il tipo di libro che vive in un cappotto.'),
    'An Atlas of Walks': ('Un atlas de promenades', 'Ein Atlas der Wanderungen', 'Un atlante di camminate'),
    'Fifty walks with hand-drawn maps, from a morning to a week. Every walk has a hand-drawn map, a distance, a pub and a train home. Fifty reasons to leave the house.': (
        "Cinquante promenades avec des cartes dessinées à la main, d'une matinée à une semaine. Chaque promenade a sa carte dessinée, sa distance, son café et son train de retour. Cinquante raisons de sortir.",
        'Fünfzig Wanderungen mit handgezeichneten Karten, von einem Morgen bis zu einer Woche. Jede Wanderung hat eine gezeichnete Karte, eine Distanz, ein Gasthaus und einen Zug nach Hause. Fünfzig Gründe, das Haus zu verlassen.',
        'Cinquanta camminate con mappe disegnate a mano, da una mattina a una settimana. Ogni camminata ha la sua mappa disegnata, la distanza, un locale e un treno per tornare. Cinquanta motivi per uscire di casa.'),
    'The Book of Colour': ('Le livre de la couleur', 'Das Buch der Farbe', 'Il libro del colore'),
    'Fifty pigments and the stories of the people who found them. Fifty short chapters, one pigment each, with a swatch printed on the page. A book to open anywhere.': (
        "Cinquante pigments et l'histoire de ceux qui les ont trouvés. Cinquante courts chapitres, un pigment chacun, avec un échantillon imprimé sur la page. Un livre à ouvrir n'importe où.",
        'Fünfzig Pigmente und die Geschichten der Menschen, die sie fanden. Fünfzig kurze Kapitel, je ein Pigment, mit einem auf die Seite gedruckten Farbfeld. Ein Buch, das man überall aufschlägt.',
        'Cinquanta pigmenti e le storie di chi li ha trovati. Cinquanta capitoli brevi, uno per pigmento, con un campione stampato sulla pagina. Un libro da aprire ovunque.'),
    'The Ruth Mallory set': ('Le coffret Ruth Mallory', 'Das Ruth-Mallory-Set', 'Il cofanetto Ruth Mallory'),
    'Both Mallory novels, boxed, at a saving. Cold Harbour and The Long Tide in matching clothbound editions, in a slipcase. Cheaper than the two apart.': (
        "Les deux romans Mallory, en coffret, à prix réduit. Port froid et La longue marée en éditions reliées toile assorties, dans un étui. Moins cher que les deux séparés.",
        'Beide Mallory-Romane, im Schuber, mit Ersparnis. Kalter Hafen und Die lange Flut in passenden Leinenausgaben, im Schuber. Günstiger als beide einzeln.',
        'Entrambi i romanzi di Mallory, in cofanetto, con un risparmio. Porto freddo e La lunga marea in edizioni in tela coordinate, dentro un astuccio. Costa meno dei due separati.'),
    'The kitchen shelf': ('Létagère de la cuisine', 'Das Küchenregal', 'Lo scaffale della cucina'),
    'Weeknight, The Bread Book and Vegetables First, together. The three cookbooks our staff use most, in one order. Enough dinners for a year.': (
        "En semaine, Le livre du pain et Les légumes d'abord, réunis. Les trois livres de cuisine que notre équipe utilise le plus, en une commande. De quoi dîner un an.",
        'Unter der Woche, Das Brotbuch und Gemüse zuerst, zusammen. Die drei Kochbücher, die unser Team am meisten nutzt, in einer Bestellung. Abendessen für ein Jahr.',
        'Feriali, Il libro del pane e Prima le verdure, insieme. I tre libri di cucina che il nostro staff usa di più, in un solo ordine. Cene per un anno.'),
    'The bedtime shelf': ('Létagère du soir', 'Das Gutenachtregal', 'Lo scaffale della buonanotte'),
    'Three picture books for the last five minutes of the day. Goodnight Little Fox, The Big Dig and A is for Anteater, packed together. Wrapped on request.': (
        "Trois albums pour les cinq dernières minutes de la journée. Bonne nuit petit renard, Le grand chantier et A comme fourmilier, réunis. Emballage cadeau sur demande.",
        'Drei Bilderbücher für die letzten fünf Minuten des Tages. Gute Nacht kleiner Fuchs, Die große Baustelle und A wie Ameisenbär, zusammen verpackt. Auf Wunsch als Geschenk.',
        'Tre albi illustrati per gli ultimi cinque minuti della giornata. Buonanotte piccola volpe, Il grande scavo e A come formichiere, insieme. Su richiesta con confezione regalo.'),
    'Folio canvas tote': ('Tote bag en toile Folio', 'Folio Canvas-Shopper', 'Shopper di tela Folio'),
    'A heavy canvas tote big enough for a hardback and a loaf. Heavy natural canvas with long handles and a flat bottom. Big enough for a week of reading.': (
        "Un tote bag en toile épaisse, assez grand pour un livre relié et une miche. Une toile naturelle épaisse, de longues anses et un fond plat. Assez grand pour une semaine de lecture.",
        'Ein schwerer Canvas-Shopper, groß genug für ein gebundenes Buch und ein Brot. Schweres Naturcanvas mit langen Henkeln und flachem Boden. Groß genug für eine Woche Lesestoff.',
        'Uno shopper in tela pesante, grande abbastanza per un libro rilegato e una pagnotta. Tela naturale pesante, manici lunghi e fondo piatto. Grande abbastanza per una settimana di letture.'),
    'Brass bookmark set': ('Lot de marque-pages en laiton', 'Messing-Lesezeichen-Set', 'Set di segnalibri in ottone'),
    'Three brass bookmarks with a folded tab. They do not fall out. Three brass tabs that hook over the page edge. They stay put in a bag and never mark the paper.': (
        "Trois marque-pages en laiton à languette pliée. Ils ne tombent pas. Trois languettes de laiton qui s'accrochent au bord de la page. Ils restent en place dans un sac et ne marquent jamais le papier.",
        'Drei Lesezeichen aus Messing mit gefalteter Lasche. Sie fallen nicht heraus. Drei Messinglaschen, die sich über die Seitenkante haken. Sie bleiben in der Tasche sitzen und markieren das Papier nie.',
        'Tre segnalibri in ottone con linguetta piegata. Non cadono. Tre linguette di ottone che si agganciano al bordo della pagina. Restano al loro posto in borsa e non segnano mai la carta.'),
    'Clip reading light': ('Lampe de lecture à pince', 'Klemm-Leseleuchte', 'Luce da lettura a clip'),
    'A warm rechargeable clip light for reading beside someone asleep. Warm light, three levels, a clip that fits a paperback or a hardback. Charges by USB-C in an hour.': (
        "Une lampe à pince rechargeable à lumière chaude, pour lire à côté de quelqu'un qui dort. Lumière chaude, trois niveaux, une pince qui tient sur un broché comme sur un relié. Recharge en USB-C en une heure.",
        'Eine warme, aufladbare Klemmleuchte zum Lesen neben jemandem, der schläft. Warmes Licht, drei Stufen, eine Klemme für Taschenbuch oder gebundenes Buch. Lädt in einer Stunde über USB-C.',
        'Una luce a clip ricaricabile con luce calda, per leggere accanto a chi dorme. Luce calda, tre livelli, una clip che sta su una brossura o su un rilegato. Si carica via USB-C in un ora.'),
    'Folio gift card': ('Carte cadeau Folio', 'Folio Geschenkkarte', 'Carta regalo Folio'),
    'A paper gift card in an envelope, for people who choose their own. A paper card in a linen envelope, posted the same day. Any amount, valid for a year.': (
        "Une carte cadeau en papier dans une enveloppe, pour ceux qui choisissent eux-mêmes. Une carte en papier dans une enveloppe de lin, postée le jour même. N'importe quel montant, valable un an.",
        'Eine Geschenkkarte aus Papier im Umschlag, für Menschen, die selbst wählen. Eine Papierkarte in einem Leinenumschlag, am selben Tag verschickt. Jeder Betrag, ein Jahr gültig.',
        'Una carta regalo di carta in una busta, per chi sceglie da sé. Una carta di carta in una busta di lino, spedita in giornata. Qualsiasi importo, valida un anno.'),
}

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
