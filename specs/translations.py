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
    'Sleeves a touch long': ('Manches un peu longues', 'Ärmel etwas zu lang', 'Maniche un po lunghe'),
    'Good shirt, but the sleeves are long on me. A cuff roll fixes it.': (
        'Bonne chemise, mais les manches sont longues pour moi. Un revers règle le problème.',
        'Gutes Hemd, aber die Ärmel sind mir zu lang. Einmal umschlagen löst das.',
        'Bella camicia, ma le maniche sono lunghe per me. Un risvolto risolve.'),
    'Solid basics': ('Des basiques solides', 'Solide Basics', 'Basici solidi'),
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
    'Cheap and cheerful': ('Simple et efficace', 'Günstig und gut', 'Economico e allegro'),
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
    'Solid, a bit pricey': ('Solide, un peu cher', 'Solide, etwas teuer', 'Solido, un po caro'),
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
        'Interruzioni allinizio. Un aggiornamento dopo, stabilissimo.'),
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
        'Tout marche avec un bouton. Mes parents sauraient sen servir.',
        'Alles funktioniert über einen Knopf. Meine Eltern könnten es bedienen.',
        'Tutto funziona con un pulsante. I miei genitori saprebbero usarlo.'),
    'Runs warm': ('Il chauffe', 'Wird warm', 'Si scalda'),
    'Works fine but gets warm under load. Give it some air.': (
        'Il fonctionne bien mais chauffe en charge. Laissez-lui de lair.',
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
    'Pairing was instant': ('Appairage immédiat', 'Kopplung war sofort da', "L'accoppiamento è stato immediato"),
    'Open the lid, tap once, done.': (
        'On ouvre le couvercle, on touche une fois, cest fait.',
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
    'Speaker fills the room': ('Lenceinte remplit la pièce', 'Der Lautsprecher füllt den Raum', 'Lo speaker riempie la stanza'),
    'Small box, big sound. Party volume without distortion.': (
        'Petite boîte, grand son. Le volume dune fête sans distorsion.',
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
    'Good, a little pricey': ('Bon, un peu cher', 'Gut, etwas teuer', 'Buono, un po caro'),
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
        'Foncé et chocolaté. Pas pour ceux qui laiment léger.',
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
