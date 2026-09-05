CODE = 'books'; ROOT = 'Books'; STORE_NAME = 'Folio'; ATTRIBUTE_SET = 'Books'; WEIGHT = 0.4
ATTRIBUTE_COLUMNS = ['format', 'genre', 'author', 'pages']
ATTRIBUTES = [
    dict(code='format', label='Format', input='select', scope='global', filterable=1, visible_on_front=1, comparable=1, is_configurable=1, sets='Books', group='General', sort_order=50),
    dict(code='genre', label='Genre', input='multiselect', scope='global', filterable=1, filterable_in_search=1, visible_on_front=1, sets='Books', group='General', sort_order=60),
    dict(code='author', label='Author', input='text', scope='global', searchable=1, visible_on_front=1, used_in_product_listing=1, sets='Books', group='General', sort_order=70),
    dict(code='pages', label='Pages', input='text', scope='global', visible_on_front=1, comparable=1, sets='Books', group='General', sort_order=80),
]
OPTIONS = {'format': ['Hardcover', 'Paperback', 'Audiobook', 'E-book'], 'genre': ['Fiction', 'Crime', 'Science', 'History', 'Cooking', 'Poetry', 'Children', 'Travel', 'Art']}
ROOT_DESCRIPTION = 'An independent bookshop with a short shelf and long opinions.'
META_DESCRIPTION = 'Folio: new fiction, crime, science, history, cookbooks and childrens books, chosen one at a time by booksellers.'
PRODUCT_STYLE = 'Studio product photograph of a single book standing upright on a plain white seamless background, soft light, the cover shows only an abstract or illustrated design with no readable text, no lettering, no logos, no watermark, centered with margin around it.'
SCENE_STYLE = 'Warm editorial photograph of a small independent bookshop, wooden shelves, brass lamps, soft afternoon light, shallow depth of field, no readable text, no lettering, no logos, no watermark.'
SCENES = {
    'hero-main': 'A reading nook with a leather armchair, a stack of clothbound books on a side table and a tall window with rain outside.',
    'hero-side': 'A close up of a hand holding an open book with a cup of tea beside it on a wooden table.',
    'editorial': 'A bookseller on a ladder placing a book on a high wooden shelf in a narrow shop.',
    'about': 'The front of a small bookshop with a bay window full of books and a bicycle leaning outside.',
}
CATEGORIES = [
    dict(path='fiction', name='Fiction', description='Novels and short stories, new and worth rereading.', landing_title='Stories we argue about', landing_text='Every novel on this shelf was read by two of us. If we disagreed, it stayed. Those are the good ones.', scene='A table of novels with colourful abstract covers, fanned out under a brass reading lamp.'),
    dict(path='crime', name='Crime & Thrillers', description='Detectives, heists and the people who get away with it.', landing_title='Read after dark', landing_text='Police procedurals, cosy mysteries and the kind of thriller that costs you a night of sleep.', scene='A dark wooden desk with a stack of paperbacks, a magnifying glass and a green banker lamp.'),
    dict(path='science', name='Science & Nature', description='How things work, from cells to galaxies.', landing_title='Curiosity, bound', landing_text='Popular science that respects the reader, field guides you can carry, and the occasional big idea.', scene='A desk with an open illustrated book about birds, a pair of binoculars and a fern in a pot.'),
    dict(path='history', name='History', description='The long view, told well.', landing_title='What happened, and why', landing_text='Narrative history, biography and the odd primary source. No textbooks.', scene='An old map spread on a wooden table with a stack of clothbound history books and a brass compass.'),
    dict(path='cooking', name='Cooking', description='Cookbooks that get splashed.', landing_title='Books for the counter', landing_text='Cookbooks we cook from, with pages that lie flat and recipes that work on a Tuesday.', scene='An open cookbook on a kitchen counter with a bowl of lemons and a wooden spoon.'),
    dict(path='children', name='Children', description='Picture books and first chapter books.', landing_title='First favourites', landing_text='Picture books for the bedtime rota and chapter books for readers who just took off.', scene='A low shelf of colourful picture books with a small wooden stool and a stuffed rabbit.'),
]
HERO = dict(badge='Staff picks', title='Read something we would defend', text='A short shelf, chosen one book at a time by people who read all day and still read at night.')
FEATURES = [('truck', 'Free delivery over 25', 'Or collect in the shop'), ('book', 'Signed copies', 'When the author visits'), ('arrow-back-up', 'Easy returns', 'Fourteen days, unread'), ('gift', 'Gift wrap', 'Brown paper and string')]
STORY = dict(title='A short shelf, on purpose', text1='Folio opened with four hundred books and a rule: nothing goes on the shelf that one of us would not press into your hands.', text2='We are still small. We still read everything. That is the point.')
PROMO = dict(badge='Book of the month', title='The subscription', text='One book a month, chosen for you after a short conversation about what you love and what you avoid.', path='fiction', button='Start with fiction', list_title='This month on the table')
TESTIMONIALS = [('They asked me three questions and sent the best novel I read all year.', 'Elena R.', 'Edinburgh'), ('The gift wrap is worth it alone. Brown paper, string, a card in real handwriting.', 'Marcus T.', 'Leeds'), ('My kids fight over the picture books. That is a compliment.', 'Priya S.', 'Cork')]
NEWSLETTER = dict(title='The shelf letter', text='A short note every other week: what we read, what we argued about, and what is coming in.')
ABOUT = dict(title='Four hundred books and a rule', paragraphs=['Folio started in a former barber shop with four hundred books and one rule: nothing goes on the shelf that a bookseller here would not press into your hands.', 'We read everything we sell. When two of us disagree about a book, it stays, because those are usually the interesting ones.', 'The shop is still small. The website is the same shelf, with the same people behind it.'])
REVIEWS = [
    ('Could not put it down', 'Finished it in two nights. The recommendation was spot on.', 5),
    ('Good, not great', 'Well written but slow in the middle. Lovely edition though.', 3),
    ('Beautiful edition', 'Clothbound, good paper, lies flat. A pleasure to hold.', 5),
    ('Perfect gift', 'Wrapped beautifully and arrived in two days.', 5),
    ('Ribbon marker', 'Small thing, but the ribbon marker and the sewn binding made my week.', 5),
    ('Print is small', 'Fine story, but the type is small and the margins are tight.', 3),
    ('Read it twice', 'The ending sent me back to page one. Rare.', 5),
    ('Arrived with a dented corner', 'Packaging was thin. The book is fine, the corner is not.', 3),
    ('Great translation', 'Reads like it was written in English. No awkward sentences.', 5),
    ('Big for the shelf', 'Larger format than expected. Check the dimensions.', 4),
    ('The maps alone', 'The endpaper maps are worth the price. The story is a bonus.', 5),
    ('Not for beginners', 'Dense and rewarding, but start elsewhere if you are new to the subject.', 4),
    ('Paperback is sturdy', 'Flexible cover, opens flat, survived a beach week.', 5),
    ('Half the price elsewhere', 'Beautiful shop, but I found the same edition cheaper.', 3),
    ('Signed copy', 'I did not expect the signature on the title page. Delighted.', 5),
    ('Slow start, strong finish', 'Give it fifty pages. Then you will not stop.', 4),
    ('Kids loved it', 'Read aloud three nights running. The pictures hold up to a torch.', 5),
    ('Index is excellent', 'For a reference book, the index is what matters, and this one is thorough.', 5),
    ('Smells like a bookshop', 'Uncoated paper, sewn spine. Old fashioned in the best way.', 5),
    ('Too short', 'Loved every page, wanted a hundred more.', 4),
    ('Second volume please', 'Ends on a cliff. Hoping the next one is on its way.', 4),
    ('Good notes', 'The introduction and notes add context without getting in the way.', 5),
    ('Fast delivery', 'Ordered Thursday, read it Saturday.', 5),
    ('Cover scratches easily', 'Matte cover shows every mark. Get a sleeve.', 3),
]
def P(sku, name, cats, price, desc, prompt, **kw):
    d = dict(sku=sku, name=name, categories=cats, price=price, description=desc, prompt=prompt); d.update(kw); return d
def book(sku, title, author, cats, price, pages, genre, desc, cover, formats=None, **kw):
    a = dict(author=author, pages=pages, genre=genre)
    if formats:
        return P(sku, title, cats, price, desc, cover, axis='format', values=formats, attributes=a, **kw)
    a['format'] = kw.pop('format', 'Paperback')
    return P(sku, title, cats, price, desc, cover, attributes=a, **kw)
PRODUCTS = [
    book('B-SALT-HOUSES', 'The Salt Houses', 'Mara Lindqvist', ['fiction'], 18, 336, 'Fiction', 'Three sisters return to a fishing village to sell the family house and find the tide has other plans. A novel about what we keep.', 'a book with an abstract cover of blue and white waves', formats=['Hardcover', 'Paperback', 'E-book']),
    book('B-LAST-ORCHARD', 'The Last Orchard', 'Tomas Reyes', ['fiction'], 16, 288, 'Fiction', 'A widower plants a hundred trees he will not live to see fruit. His neighbours have opinions.', 'a book with an illustrated cover of an apple tree in autumn colours', formats=['Hardcover', 'Paperback']),
    book('B-QUIET-ROOMS', 'Quiet Rooms', 'Ines Halloran', ['fiction'], 14, 240, 'Fiction', 'Linked short stories set in one apartment building over forty years.', 'a book with a minimal cover of a single window in warm yellow'),
    book('B-NORTH-LIGHT', 'North Light', 'Anders Vik', ['fiction'], 17, 352, 'Fiction', 'A painter moves to the far north to escape a scandal and finds the light does not care.', 'a book with a cover of pale northern light over a fjord', formats=['Hardcover', 'Paperback']),
    book('B-PAPER-BIRDS', 'Paper Birds', 'Yuki Aoyama', ['fiction'], 15, 272, 'Fiction', 'A translator falls for the author she cannot meet. Quiet and devastating.', 'a book with a cover of origami birds in red and cream'),
    book('B-SUMMER-HOUSE', 'The Summer House', 'Clara Vance', ['fiction', 'crime'], 16, 320, 'Fiction|Crime', 'Six friends, one house by the lake, and a promise nobody kept.', 'a book with a cover of a lake house at dusk in dark blues'),
    book('B-COLD-HARBOUR', 'Cold Harbour', 'Detective Ruth Mallory 1', ['crime'], 15, 384, 'Crime', 'A body in the harbour, a town that lies in unison, and a detective who grew up there.', 'a book with a dark cover of a harbour at night with one lit window', formats=['Paperback', 'Audiobook', 'E-book']),
    book('B-LONG-TIDE', 'The Long Tide', 'Detective Ruth Mallory 2', ['crime'], 15, 400, 'Crime', 'Mallory returns. So does the past.', 'a book with a dark cover of a tide line on a grey beach', formats=['Paperback', 'Audiobook']),
    book('B-CLEAN-BREAK', 'Clean Break', 'Sol Ferrante', ['crime'], 16, 352, 'Crime', 'A heist planned by a locksmith who has never broken a law. Until now.', 'a book with a graphic cover of a keyhole in black and gold'),
    book('B-MIDNIGHT-TRAIN', 'The Midnight Train', 'Agnes Brook', ['crime'], 13, 296, 'Crime', 'A cosy mystery on the overnight sleeper to the coast.', 'a book with an illustrated cover of a train in the moonlight'),
    book('B-WITNESS', 'The Witness Room', 'Sol Ferrante', ['crime'], 17, 368, 'Crime', 'A courtroom thriller told by the one person who cannot speak.', 'a book with a stark red and black cover of an empty chair'),
    book('B-SMALL-THINGS', 'Small Things Everywhere', 'Dr. Lena Ostrowski', ['science'], 19, 312, 'Science', 'Microbiology for the curious, from your kitchen sponge to the deep sea.', 'a book with a cover of colourful microscopic cells', formats=['Hardcover', 'Paperback', 'E-book']),
    book('B-DEEP-TIME', 'Deep Time', 'Hal Berger', ['science', 'history'], 22, 416, 'Science|History', 'The story of the Earth in twelve rocks.', 'a book with a cover of layered rock strata in ochre and grey', formats=['Hardcover', 'Paperback']),
    book('B-BIRD-GUIDE', 'The Pocket Bird Guide', 'Folio Field Guides', ['science'], 14, 224, 'Science|Nature', 'Two hundred birds, one pocket. Waterproof cover.', 'a small field guide with an illustrated cover of a robin on a branch', format='Paperback'),
    book('B-NIGHT-SKY', 'The Night Sky, Month by Month', 'Priya Nair', ['science'], 18, 256, 'Science', 'A year of stargazing with a torch and this book.', 'a book with a cover of a deep blue star field', formats=['Hardcover', 'Paperback']),
    book('B-TREE-BOOK', 'Trees of the Old World', 'Folio Field Guides', ['science'], 24, 320, 'Science|Nature', 'A large-format guide to five hundred trees, with leaf and bark plates.', 'a large book with a cover of a green leaf pattern', format='Hardcover'),
    book('B-WEATHER', 'A Short History of Weather', 'Hal Berger', ['science'], 12, 208, 'Science', 'Clouds, storms and the people who learned to read them.', 'a book with a cover of cumulus clouds on a pale sky'),
    book('B-SILK-ROAD', 'Roads of Silk', 'Aisha Rahman', ['history'], 24, 480, 'History|Travel', 'A journey along the old trade routes, then and now.', 'a book with a cover of a desert caravan in warm tones', formats=['Hardcover', 'Paperback', 'Audiobook']),
    book('B-CITY-WATER', 'The City of Water', 'Marco Bellini', ['history'], 20, 400, 'History', 'Venice from lagoon to biennale, in twenty buildings.', 'a book with a cover of a canal and gondola in muted colours', formats=['Hardcover', 'Paperback']),
    book('B-LETTERS', 'Letters from the Front', 'Edited by Ruth Adler', ['history'], 18, 336, 'History', 'Sixty letters, sixty lives. A war told from the kitchen table.', 'a book with a cover of old handwritten envelopes in sepia'),
    book('B-EMPIRE-TEA', 'An Empire of Tea', 'Aisha Rahman', ['history', 'cooking'], 19, 368, 'History|Cooking', 'How a leaf built fortunes and broke nations.', 'a book with a cover of a porcelain teacup on a dark green ground'),
    book('B-PLAGUE-YEAR', 'The Plague Year', 'Marco Bellini', ['history'], 17, 320, 'History', 'One city, one year, one doctor keeping a diary.', 'a book with a cover of a medieval city woodcut in black and red'),
    book('B-WEEKNIGHT', 'Weeknight', 'Sam Okafor', ['cooking'], 26, 288, 'Cooking', 'Sixty dinners in under forty minutes, with a shopping list that fits one hand.', 'a cookbook with a cover of a bowl of pasta from above', formats=['Hardcover', 'E-book']),
    book('B-BREAD-BOOK', 'The Bread Book', 'Elin Sorensen', ['cooking'], 28, 320, 'Cooking', 'Sourdough, flatbreads and buns, with step photographs and no mystique.', 'a cookbook with a cover of a sliced sourdough loaf', format='Hardcover'),
    book('B-VEG-FIRST', 'Vegetables First', 'Sam Okafor', ['cooking'], 25, 304, 'Cooking', 'A hundred recipes that start with what is in season.', 'a cookbook with a cover of bright vegetables on a wooden board', formats=['Hardcover', 'Paperback']),
    book('B-PRESERVES', 'Jars', 'Elin Sorensen', ['cooking'], 22, 240, 'Cooking', 'Jams, pickles and ferments for a small kitchen.', 'a cookbook with a cover of glass jars of colourful preserves', format='Hardcover'),
    book('B-COFFEE-BOOK', 'Coffee at Home', 'Nico Valdez', ['cooking'], 20, 224, 'Cooking', 'Beans, water, grind, time. Everything else is detail.', 'a book with a cover of a pour over coffee cone in matte black', format='Hardcover'),
    book('B-GOODNIGHT-FOX', 'Goodnight, Little Fox', 'Illustrated by Ada Wren', ['children'], 12, 32, 'Children', 'A picture book for the last five minutes of the day.', 'a picture book with an illustrated cover of a sleepy fox under the moon', format='Hardcover'),
    book('B-BIG-DIG', 'The Big Dig', 'Illustrated by Ada Wren', ['children'], 12, 32, 'Children', 'Diggers, dumpers and a very deep hole.', 'a picture book with an illustrated cover of a yellow digger', format='Hardcover'),
    book('B-SEA-ADVENTURE', 'Milo and the Sea', 'Ben Harker', ['children'], 9, 160, 'Children', 'A first chapter book about a boy, a boat and a very patient seagull.', 'a chapter book with an illustrated cover of a small boat on a green sea', formats=['Paperback', 'Audiobook']),
    book('B-DRAGON-SCHOOL', 'Dragon School', 'Ben Harker', ['children'], 9, 176, 'Children', 'Where dragons learn to fly and one of them would rather read.', 'a chapter book with an illustrated cover of a small purple dragon reading', formats=['Paperback', 'Audiobook']),
    book('B-ABC-ANIMALS', 'A is for Anteater', 'Illustrated by Ada Wren', ['children'], 14, 56, 'Children', 'An alphabet of unusual animals, painted in gouache.', 'a large picture book with an illustrated cover of an anteater in bright gouache', format='Hardcover'),
    book('B-SPACE-KIDS', 'Ask an Astronaut', 'Priya Nair', ['children', 'science'], 15, 96, 'Children|Science', 'Fifty questions from children, answered from orbit.', 'a book with a cover of a cartoon astronaut floating above Earth', format='Hardcover'),
    book('B-POEMS-SEA', 'Poems of the Sea', 'Edited by Ines Halloran', ['fiction'], 14, 192, 'Poetry', 'Two hundred years of poems about water, in a pocket edition.', 'a small clothbound book with a cover of a deep teal wave pattern', format='Hardcover'),
    book('B-ATLAS-WALKS', 'An Atlas of Walks', 'Folio Field Guides', ['science', 'history'], 30, 352, 'Travel|Nature', 'Fifty walks with hand-drawn maps, from a morning to a week.', 'a large book with a cover of a hand drawn map with a red route line', format='Hardcover'),
    book('B-ART-COLOUR', 'The Book of Colour', 'Nadia Ferro', ['history'], 32, 288, 'Art|History', 'Fifty pigments and the stories of the people who found them.', 'a large book with a cover of colour swatches in a grid', format='Hardcover'),
    P('B-CRIME-SET', 'The Ruth Mallory set', ['crime'], 27, 'Both Mallory novels, boxed, at a saving.', 'two dark paperback crime novels in a slipcase', grouped=['B-COLD-HARBOUR-PAPERBACK', 'B-LONG-TIDE-PAPERBACK'], attributes=dict(author='Detective Ruth Mallory', genre='Crime', format='Paperback')),
    P('B-COOK-SET', 'The kitchen shelf', ['cooking'], 70, 'Weeknight, The Bread Book and Vegetables First, together.', 'three hardcover cookbooks stacked with colourful spines', grouped=['B-WEEKNIGHT-HARDCOVER', 'B-BREAD-BOOK', 'B-VEG-FIRST-HARDCOVER'], attributes=dict(author='Various', genre='Cooking', format='Hardcover')),
    P('B-BEDTIME-SET', 'The bedtime shelf', ['children'], 30, 'Three picture books for the last five minutes of the day.', 'three illustrated picture books fanned on a pale blanket', grouped=['B-GOODNIGHT-FOX', 'B-BIG-DIG', 'B-ABC-ANIMALS'], attributes=dict(author='Ada Wren', genre='Children', format='Hardcover')),
    P('B-TOTE', 'Folio canvas tote', ['fiction'], 12, 'A heavy canvas tote big enough for a hardback and a loaf.', 'a natural canvas tote bag with a small embroidered fox', attributes=dict(author='', genre='', format='')),
    P('B-BOOKMARKS', 'Brass bookmark set', ['fiction'], 9, 'Three brass bookmarks with a folded tab. They do not fall out.', 'three slim brass bookmarks on white', attributes=dict(author='', genre='', format='')),
    P('B-READING-LIGHT', 'Clip reading light', ['fiction'], 16, 'A warm rechargeable clip light for reading beside someone asleep.', 'a small warm clip on reading light', attributes=dict(author='', genre='', format='')),
    P('B-GIFT-CARD', 'Folio gift card', ['fiction'], 25, 'A paper gift card in an envelope, for people who choose their own.', 'a plain cream gift card in a kraft envelope', type='virtual', attributes=dict(author='', genre='', format='')),
]
POSTS = [
    ('How we choose the shelf', '<p>Every book in the shop was read by at least one of us before it was ordered. Not the blurb, not the reviews, the book. If two of us disagree, it stays, because those tend to be the books people remember.</p><p>The shelf is short on purpose. A short shelf you can trust beats a long one you have to search.</p>', 'A bookseller reading at a wooden counter with a stack of books and a pencil.'),
    ('Reading aloud, past the picture books', '<p>Chapter books are the bridge. A child who is read to at seven will read alone at eight, and the trick is to stop at the exciting bit. Every night.</p><p>Start with something funny. Nobody ever fell in love with reading through a worthy book.</p>', 'A parent and child reading a chapter book together under a blanket in warm lamp light.'),
    ('The case for the hardback', '<p>A hardback lies flat, survives a bath and a beach, and will be on your shelf in thirty years. A paperback is cheaper. Both are right.</p><p>We stock both when we can. When we cannot, we tell you which one to wait for.</p>', 'A clothbound hardback book lying open on a wooden table with a pair of reading glasses.'),
]
MORE = {
    'B-SALT-HOUSES': 'Three hundred and twenty pages, clothbound with a ribbon marker. The first novel of the year to make our staff argue.',
    'B-LAST-ORCHARD': 'A short, warm book about time and stubbornness. Read it in an afternoon and think about it for a week.',
    'B-QUIET-ROOMS': 'Twelve stories, each in a different flat, each a different decade. Readers of quiet fiction will feel at home.',
    'B-NORTH-LIGHT': 'Long winters, long sentences and a slow thaw. A novel for a fireside and a blanket.',
    'B-PAPER-BIRDS': 'Told in letters and margin notes. Two hundred pages, best read in one sitting.',
    'B-SUMMER-HOUSE': 'A holiday novel with teeth. Every chapter is a different summer, and the last one changes the rest.',
    'B-COLD-HARBOUR': 'The first Ruth Mallory novel. A slow, cold crime story with a detective who knows every face in the pub.',
    'B-LONG-TIDE': 'The second Mallory novel picks up ten years later. Read Cold Harbour first, though it stands alone.',
    'B-CLEAN-BREAK': 'Fast, funny and precise about locks. The plan goes wrong on page forty and keeps going wrong.',
    'B-MIDNIGHT-TRAIN': 'No blood, plenty of tea, and a puzzle that plays fair. The first of a series.',
    'B-WITNESS': 'A thriller built on a single trick, and the trick holds. Best not to read the last page first.',
    'B-SMALL-THINGS': 'Short chapters, clear drawings, no equations. Written for adults who remember liking science once.',
    'B-DEEP-TIME': 'Each chapter starts with one rock and ends with a continent. Full-page colour plates throughout.',
    'B-BIRD-GUIDE': 'Two hundred species with a painting, a map and the call in words. It fits a coat pocket and survives rain.',
    'B-NIGHT-SKY': 'Twelve chapters, one per month, with charts drawn for the naked eye. A red torch is all the equipment you need.',
    'B-TREE-BOOK': 'A coffee-table book that is also a real reference. The plates show leaf, bark, flower and winter twig.',
    'B-WEATHER': 'From shepherds to satellites in three hundred pages. Written with a lightness that suits the subject.',
    'B-SILK-ROAD': 'Part travel diary, part history. The author walks and takes the bus, and both make good chapters.',
    'B-CITY-WATER': 'Twenty buildings, twenty short essays, one plan of the city. Take it with you or read it at home.',
    'B-LETTERS': 'The letters are printed whole, with a page of context before each one. Hard to read quickly.',
    'B-EMPIRE-TEA': 'Trade, taste and politics in one leaf. The author has a gift for the telling detail.',
    'B-PLAGUE-YEAR': 'A diary edited into a story, with the gaps left in. The doctor never says what he feels, and you feel it anyway.',
    'B-WEEKNIGHT': 'Every recipe on one page, with a photo and a timeline. Sixty dinners, no special equipment.',
    'B-BREAD-BOOK': 'Twenty base recipes with variations, and photographs of every fold. The starter chapter alone is worth the price.',
    'B-VEG-FIRST': 'Organised by season, then by vegetable. Most recipes feed four in under an hour.',
    'B-PRESERVES': 'Small batches, ordinary jars, a chapter on what went wrong and why. Good for a first ferment.',
    'B-COFFEE-BOOK': 'Filter, espresso, cold brew, in that order of difficulty. Each method has a ratio and a timing chart.',
    'B-GOODNIGHT-FOX': 'Twenty-four pages, soft colours, one sentence a page. Ages one to four.',
    'B-BIG-DIG': 'Big machines, big sounds, and a hole that gets deeper every page. Ages two to five.',
    'B-SEA-ADVENTURE': 'Ten short chapters with a picture on every spread. For readers of six to eight.',
    'B-DRAGON-SCHOOL': 'A funny school story with a quiet hero. Ages seven to ten, and the adult reading aloud.',
    'B-ABC-ANIMALS': 'Every letter gets an animal nobody expects and a painting to match. Ages three to six.',
    'B-SPACE-KIDS': 'Real questions from real children, answered with patience and photographs. Ages eight and up.',
    'B-POEMS-SEA': 'Two hundred poems in a cloth pocket edition with a ribbon. The kind of book that lives in a coat.',
    'B-ATLAS-WALKS': 'Every walk has a hand-drawn map, a distance, a pub and a train home. Fifty reasons to leave the house.',
    'B-ART-COLOUR': 'Fifty short chapters, one pigment each, with a swatch printed on the page. A book to open anywhere.',
    'B-CRIME-SET': 'Cold Harbour and The Long Tide in matching clothbound editions, in a slipcase. Cheaper than the two apart.',
    'B-COOK-SET': 'The three cookbooks our staff use most, in one order. Enough dinners for a year.',
    'B-BEDTIME-SET': 'Goodnight Little Fox, The Big Dig and A is for Anteater, packed together. Wrapped on request.',
    'B-TOTE': 'Heavy natural canvas with long handles and a flat bottom. Big enough for a week of reading.',
    'B-BOOKMARKS': 'Three brass tabs that hook over the page edge. They stay put in a bag and never mark the paper.',
    'B-READING-LIGHT': 'Warm light, three levels, a clip that fits a paperback or a hardback. Charges by USB-C in an hour.',
    'B-GIFT-CARD': 'A paper card in a linen envelope, posted the same day. Any amount, valid for a year.',
}
GALLERY = [('A reading nook with a leather armchair, a floor lamp and a window seat full of books', 'fiction'), ('A stack of clothbound novels with a cup of tea on a wooden table', 'fiction'), ('A tall shot of a narrow bookshop aisle with shelves to the ceiling and a rolling ladder', 'history'), ('An open cookbook on a kitchen counter with flour, eggs and a wooden spoon', 'cooking'), ('A child reading a picture book on a rug with a dog asleep beside them, afternoon light', 'children')]
BRANDS = [('Folio', 'PRESS'), ('Larkspur', 'BOOKS'), ('Meridian', 'CLASSICS'), ('Quill & Ash', 'PUBLISHING'), ('Harbour', 'CRIME'), ('Northlight', 'SCIENCE'), ('Hearth', 'COOKBOOKS'), ('Little Owl', 'CHILDREN'), ('Atlas', 'HISTORY'), ('Ink & Vellum', 'EDITIONS')]
GALLERY_TITLE = 'Between the shelves'
