CODE = 'kids'; ROOT = 'Kids'; STORE_NAME = 'Little Lark'; ATTRIBUTE_SET = 'Kids'; WEIGHT = 0.5
ATTRIBUTE_COLUMNS = ['age_range', 'size', 'color', 'material']
ATTRIBUTES = [
    dict(code='age_range', label='Age', input='select', scope='global', filterable=1, filterable_in_search=1, visible_on_front=1, used_in_product_listing=1, sets='Kids', group='General', sort_order=50),
]
OPTIONS = {'age_range': ['0 to 1', '1 to 3', '3 to 5', '5 to 8', '8 and up'], 'size': ['62', '68', '74', '80', '86', '92', '98', '104', '110', '116', '122', '128']}
ROOT_DESCRIPTION = 'Toys, clothes and things for small rooms, chosen to last more than one child.'
META_DESCRIPTION = 'Little Lark: wooden toys, organic cotton clothes, books, nursery furniture and outdoor gear for children from birth to eight.'
PRODUCT_STYLE = 'Studio product photograph of a single childrens product on a plain white seamless background, bright soft light, cheerful colours, no people, no text, no lettering, no logos, no watermark, centered with margin around it.'
SCENE_STYLE = 'Warm editorial photograph of a childrens room or garden, pale wood, soft pastel textiles, morning light, no faces visible, no readable text, no lettering, no logos, no watermark.'
SCENES = {
    'hero-main': 'A bright playroom with a wooden play kitchen, a pile of soft toys and a striped rug, a small child seen from behind.',
    'hero-side': 'A close up of a wooden stacking toy with rainbow rings on a pale pink blanket.',
    'editorial': 'A toymaker sanding a wooden toy car at a bench full of small painted parts.',
    'about': 'A small shop with wooden toys on low shelves and a rocking horse in the window.',
}
CATEGORIES = [
    dict(path='toys', name='Toys', description='Wooden and soft toys, from rattles to construction sets.', landing_title='Toys that get handed down', landing_text='Beech, maple and organic cotton. Toys that survive a second child and a third.', scene='Wooden toys, a stacking tower, a train and a felt rabbit on a pale wooden floor.'),
    dict(path='clothing', name='Clothing', description='Organic cotton basics in sizes 62 to 128.', landing_title='Soft, washable, again', landing_text='Organic cotton that survives the wash, with room to grow and snaps where it matters.', scene='Small folded organic cotton clothes in pastel colours on a wooden shelf.'),
    dict(path='books', name='Books', description='Board books, picture books and first readers.', landing_title='Read it again', landing_text='Books that stand up to being read a hundred times and chewed twice.', scene='A low shelf of picture books with a small chair and a soft toy.'),
    dict(path='nursery', name='Nursery', description='Cots, changing tables and storage in solid wood.', landing_title='A room that grows', landing_text='Cots that become beds, changing tables that become desks, and storage that stays.', scene='A calm nursery with a wooden cot, a mobile and a rocking chair in soft light.'),
    dict(path='outdoor', name='Outdoor', description='Balance bikes, scooters and rain gear.', landing_title='Outside, in any weather', landing_text='Balance bikes, scooters, wellies and the rain suit that makes puddles a plan.', scene='A small wooden balance bike and yellow wellies by a garden gate after rain.'),
    dict(path='gifts', name='Gifts', description='Boxed sets for new babies and birthdays.', landing_title='Ready to give', landing_text='Newborn boxes, birthday sets and the toys grandparents ask about.', scene='A wrapped gift box with a wooden rattle and a small knitted toy beside it.'),
]
HERO = dict(badge='New arrivals', title='Made to be handed down', text='Wooden toys, organic cotton and furniture that grows. Nothing here is for one season.')
FEATURES = [('truck', 'Free delivery over 40', 'Two to three days'), ('shield-check', 'Safety tested', 'Every toy, every batch'), ('arrow-back-up', 'Easy returns', 'Thirty days, unworn'), ('gift', 'Gift wrap', 'Free, with a card')]
STORY = dict(title='Toys that last three children', text1='Little Lark began when two parents could not find a toy that outlived a birthday. We found a toymaker in the hills, and then a mill for the cotton.', text2='Everything here is tested for safety, and then tested by our own children, which is harder.')
PROMO = dict(badge='Newborn', title='The newborn box', text='A rattle, a muslin set, a bodysuit and a board book, in a box that becomes a keepsake.', path='gifts', button='See the boxes', list_title='Gift boxes')
TESTIMONIALS = [('The wooden train has survived two boys and a dog. Still perfect.', 'Elena R.', 'Utrecht'), ('The rain suit means we go out every day now. Puddles are the plan.', 'Marcus T.', 'Leeds'), ('Bodysuits that did not shrink or twist. Rare.', 'Priya S.', 'Toronto')]
NEWSLETTER = dict(title='Small news', text='A note every month: new toys, sizes back in stock, and things we learned from our own kids.')
ABOUT = dict(title='Two parents and a toymaker', paragraphs=['Little Lark started at a kitchen table with a broken plastic toy and a question: why does nothing last?', 'We found a toymaker who works in beech and maple, and a mill that weaves organic cotton. Everything since has come from people we have met.', 'Every toy is safety tested, then tested by our own children. The second test is harder.'])
REVIEWS = [
    ('Beautifully made', 'Smooth wood, no splinters, non-toxic paint. Loved by a two year old.', 5),
    ('Good, a bit small', 'Lovely quality but sizes run small. Go up one.', 4),
    ('Survived everything', 'Washed fifty times, still soft and the colour has held.', 5),
    ('Perfect present', 'Wrapped, carded and delivered in two days.', 5),
    ('Chewed and fine', 'Teething baby, three months of chewing, still no chips.', 5),
    ('Poppers instead of buttons', 'Night changes are faster. Small thing, huge difference.', 5),
    ('Nap time favourite', 'Will not sleep without the rabbit. We bought a spare.', 5),
    ('Wheels fell off', 'One wheel came loose after a week. Glued and fine, but still.', 3),
    ('Grew with her', 'Adjustable straps meant it fit from three months to a year.', 5),
    ('Colours are soft', 'Muted tones that do not shout. Matches the nursery.', 5),
    ('Puzzle is a hit', 'Ten pieces, thick wood, and the pictures make sense.', 5),
    ('Zip is tricky', 'Great coat but a stiff zip for small hands.', 4),
    ('Wooden blocks clack nicely', 'The sound is half the fun apparently.', 5),
    ('Hand-me-down ready', 'Second child wearing it now and it still looks new.', 5),
    ('Instructions were clear', 'Built the kitchen in twenty minutes with a toddler helping.', 5),
    ('Too warm for spring', 'Beautiful knit but heavy. A winter piece.', 4),
    ('Bath toy has no holes', 'No mould inside. Someone thought about this.', 5),
    ('Print faded a bit', 'Still soft, but the print lost some colour after many washes.', 3),
    ('Stacks and knocks down', 'Thirty times a day. Never gets old.', 5),
    ('Sizing chart was right', 'Measured, ordered, fit. Thank you for the chart.', 5),
    ('Muslin is huge', 'Big enough to swaddle and later a picnic blanket.', 5),
    ('Grandparents approved', 'They said it looks like the toys they had. High praise.', 5),
    ('Bib catches everything', 'Deep pocket, wipes clean, no more laundry after lunch.', 5),
    ('Bell is loud', 'Lovely rattle, but the bell is louder than I expected.', 4),
]
def P(sku, name, cats, price, desc, prompt, **kw):
    d = dict(sku=sku, name=name, categories=cats, price=price, description=desc, prompt=prompt); d.update(kw); return d
BABY = ['62', '68', '74', '80']
TODDLER = ['86', '92', '98', '104']
KID = ['110', '116', '122', '128']
PRODUCTS = [
    P('K-STACKER', 'Rainbow stacker', ['toys', 'gifts'], 28, 'Seven beech rings on a peg, painted with water-based colour.', 'a wooden rainbow ring stacking toy', attributes=dict(age_range='1 to 3', material='Oak', color='Red', size='')),
    P('K-TRAIN', 'Wooden train set', ['toys'], 65, 'A 30-piece beech track with a three-car train and a bridge.', 'a wooden train set with curved tracks and a small engine', attributes=dict(age_range='3 to 5', material='Oak', color='Brown', size='')),
    P('K-BLOCKS', 'Building blocks, 50 pieces', ['toys'], 45, 'Fifty maple blocks in a cotton bag.', 'a pile of natural wooden building blocks', attributes=dict(age_range='1 to 3', material='Oak', color='Oatmeal', size='')),
    P('K-RABBIT', 'Felt rabbit', ['toys', 'gifts'], 24, 'A hand-sewn wool felt rabbit, 25 cm, with a linen dress.', 'a small {value} felt rabbit soft toy', axis='color', values=['Grey', 'Pink', 'Oatmeal'], picture_per_value=True, attributes=dict(age_range='0 to 1', material='Wool', size='')),
    P('K-PLAY-KITCHEN', 'Play kitchen', ['toys', 'nursery'], 180, 'A birch play kitchen with a working tap sound and a chalkboard.', 'a small wooden childrens play kitchen', attributes=dict(age_range='3 to 5', material='Oak', color='White', size='')),
    P('K-PUZZLE', 'Animal puzzle', ['toys'], 18, 'A nine-piece chunky wooden puzzle of farm animals.', 'a chunky wooden puzzle with painted farm animals', attributes=dict(age_range='1 to 3', material='Oak', color='Green', size='')),
    P('K-RATTLE', 'Beech rattle', ['toys', 'gifts'], 12, 'A ring rattle in oiled beech with a bell inside.', 'a wooden ring rattle with small beads', attributes=dict(age_range='0 to 1', material='Oak', color='Oatmeal', size='')),
    P('K-DOLL', 'Cotton doll', ['toys'], 34, 'A 35 cm soft doll in organic cotton with a removable dress.', 'a soft cotton doll with yarn hair and a striped dress', attributes=dict(age_range='1 to 3', material='Cotton', color='Pink', size='')),
    P('K-CAR-SET', 'Wooden cars, set of 3', ['toys'], 22, 'Three small cars in maple with rubber wheels.', 'three small painted wooden toy cars', attributes=dict(age_range='1 to 3', material='Oak', color='Blue', size='')),
    P('K-MARBLE-RUN', 'Marble run', ['toys'], 55, 'A 40-piece wooden marble run with glass marbles.', 'a wooden marble run tower with glass marbles', attributes=dict(age_range='5 to 8', material='Oak', color='Oatmeal', size='')),
    P('K-CRAFT-KIT', 'Craft box', ['toys'], 26, 'Paper, wool, glue and thirty ideas.', 'an open craft box with coloured paper, wool and scissors', attributes=dict(age_range='5 to 8', material='Cotton', color='Yellow', size='')),
    P('K-BOARD-GAME', 'Forest board game', ['toys'], 30, 'A cooperative game for ages five and up, twenty minutes a round.', 'a colourful illustrated board game box with wooden pieces', attributes=dict(age_range='5 to 8', material='Oak', color='Green', size='')),
    P('K-BODYSUIT', 'Bodysuits, 3 pack', ['clothing'], 28, 'Three long-sleeve bodysuits in organic cotton with envelope necks.', 'three folded {value} baby bodysuits', axis='color', values=['White', 'Oatmeal', 'Pink'], picture_per_value=True, attributes=dict(age_range='0 to 1', material='Cotton', size='')),
    P('K-SLEEPSUIT', 'Sleepsuit', ['clothing'], 22, 'A footed sleepsuit with a two-way zip.', 'a folded striped baby sleepsuit', axis='size', values=BABY, attributes=dict(age_range='0 to 1', material='Cotton', color='Blue Light')),
    P('K-LEGGINGS', 'Leggings, 2 pack', ['clothing'], 20, 'Two pairs of soft leggings with a wide waistband.', 'two folded pairs of {value} childrens leggings', axis='color', values=['Grey', 'Green', 'Salmon'], picture_per_value=True, attributes=dict(age_range='1 to 3', material='Cotton', size='')),
    P('K-TEE', 'Striped tee', ['clothing'], 15, 'A breton stripe tee in organic cotton.', 'a folded {value} and white striped childrens t-shirt', axis='color', values=['Blue', 'Red', 'Green'], picture_per_value=True, attributes=dict(age_range='3 to 5', material='Cotton', size='')),
    P('K-DUNGAREES', 'Cord dungarees', ['clothing'], 38, 'Corduroy dungarees with adjustable straps and knee patches.', 'a pair of {value} corduroy childrens dungarees laid flat', axis='color', values=['Brown', 'Green', 'Blue Dark'], picture_per_value=True, attributes=dict(age_range='1 to 3', material='Cotton', size='')),
    P('K-CARDIGAN', 'Knit cardigan', ['clothing'], 34, 'A merino cardigan with wooden buttons.', 'a small {value} knitted childrens cardigan laid flat', axis='color', values=['Oatmeal', 'Green', 'Pink'], picture_per_value=True, attributes=dict(age_range='1 to 3', material='Wool', size='')),
    P('K-DRESS', 'Cotton dress', ['clothing'], 30, 'A pinafore dress in printed organic cotton.', 'a childrens pinafore dress with a small floral print laid flat', axis='size', values=TODDLER, attributes=dict(age_range='3 to 5', material='Cotton', color='Yellow')),
    P('K-HOODIE', 'Hoodie', ['clothing'], 32, 'A brushed cotton hoodie with a kangaroo pocket.', 'a {value} childrens hoodie laid flat', axis='color', values=['Grey', 'Blue Dark', 'Orange'], picture_per_value=True, attributes=dict(age_range='5 to 8', material='Cotton', size='')),
    P('K-JEANS', 'Soft jeans', ['clothing'], 28, 'Stretch denim with an elastic waist and no scratchy seams.', 'a pair of childrens soft blue jeans laid flat', axis='size', values=KID, attributes=dict(age_range='5 to 8', material='Denim', color='Blue Jean')),
    P('K-SOCKS', 'Socks, 5 pack', ['clothing'], 14, 'Five pairs in soft cotton with a grip sole.', 'five pairs of small colourful childrens socks', axis='size', values=['19', '23', '27', '31'], attributes=dict(age_range='1 to 3', material='Cotton', color='Blue')),
    P('K-HAT', 'Sun hat', ['clothing', 'outdoor'], 16, 'A wide-brim cotton sun hat with a chin strap.', 'a {value} childrens wide brim sun hat', axis='color', values=['Oatmeal', 'Blue', 'Yellow'], picture_per_value=True, attributes=dict(age_range='1 to 3', material='Cotton', size='')),
    P('K-BOARD-BOOK', 'Board book set', ['books', 'gifts'], 24, 'Four board books about colours, animals, food and bedtime.', 'four small colourful board books fanned out', attributes=dict(age_range='0 to 1', material='', color='Yellow', size='')),
    P('K-PICTURE-BOOK', 'The Lark Who Lost Her Song', ['books'], 14, 'A picture book about a bird, a storm and the neighbour who helped.', 'a picture book with an illustrated cover of a small bird on a branch', attributes=dict(age_range='3 to 5', material='', color='Blue Light', size='')),
    P('K-BEDTIME-BOOK', 'One Hundred Goodnights', ['books'], 14, 'A hundred one-line goodnights, one page each.', 'a picture book with an illustrated cover of a moon over rooftops', attributes=dict(age_range='1 to 3', material='', color='Blue Dark', size='')),
    P('K-FIRST-READER', 'Otto and the Big Puddle', ['books'], 9, 'A first reader with short words and long puddles.', 'a slim childrens book with an illustrated cover of a boy in wellies', attributes=dict(age_range='5 to 8', material='', color='Yellow', size='')),
    P('K-ATLAS', 'My First Atlas', ['books'], 22, 'A large illustrated atlas with animals on every page.', 'a large illustrated childrens atlas with a colourful map cover', attributes=dict(age_range='5 to 8', material='', color='Green', size='')),
    P('K-COT', 'Convertible cot', ['nursery'], 390, 'A beech cot that becomes a toddler bed, with three mattress heights.', 'a wooden convertible baby cot', attributes=dict(age_range='0 to 1', material='Oak', color='Oatmeal', size='')),
    P('K-CHANGING-TABLE', 'Changing table', ['nursery'], 290, 'A changing table with two shelves that becomes a desk.', 'a wooden changing table with two shelves', attributes=dict(age_range='0 to 1', material='Oak', color='White', size='')),
    P('K-ROCKER', 'Rocking chair', ['nursery'], 340, 'A nursing chair in boucle on ash rockers.', 'an oatmeal boucle rocking chair on wooden rockers', attributes=dict(age_range='0 to 1', material='Wool', color='Oatmeal', size='')),
    P('K-MOBILE', 'Felt mobile', ['nursery', 'gifts'], 36, 'Clouds, a moon and three birds in wool felt.', 'a felt baby mobile with clouds, a moon and small birds', attributes=dict(age_range='0 to 1', material='Wool', color='White', size='')),
    P('K-SHELF', 'Picture book shelf', ['nursery', 'books'], 90, 'A front-facing shelf so covers show.', 'a low wooden front facing bookshelf for children', attributes=dict(age_range='1 to 3', material='Oak', color='Oatmeal', size='')),
    P('K-STORAGE', 'Toy storage boxes, set of 3', ['nursery'], 48, 'Three felt boxes with wooden handles.', 'three grey felt storage boxes with wooden handles', attributes=dict(age_range='1 to 3', material='Wool', color='Grey', size='')),
    P('K-NIGHT-LIGHT', 'Rabbit night light', ['nursery'], 32, 'A silicone rabbit that glows warm and dims with a tap.', 'a small white silicone rabbit night light glowing softly', attributes=dict(age_range='0 to 1', material='Rubber', color='White', size='')),
    P('K-MUSLINS', 'Muslin squares, 3 pack', ['nursery', 'gifts'], 22, 'Three large organic muslins, for everything.', 'three folded {value} organic muslin squares', axis='color', values=['White', 'Oatmeal', 'Green'], picture_per_value=True, attributes=dict(age_range='0 to 1', material='Cotton', size='')),
    P('K-BALANCE-BIKE', 'Balance bike', ['outdoor'], 120, 'A birch balance bike with a padded seat and 12 inch tyres.', 'a small {value} wooden balance bike', axis='color', values=['Red', 'Green', 'Blue'], picture_per_value=True, attributes=dict(age_range='1 to 3', material='Oak', size='')),
    P('K-SCOOTER', 'Three-wheel scooter', ['outdoor'], 85, 'A lean-to-steer scooter with a light-up deck.', 'a small {value} three wheel childrens scooter', axis='color', values=['Blue', 'Pink', 'Green'], picture_per_value=True, attributes=dict(age_range='3 to 5', material='Nylon', size='')),
    P('K-RAIN-SUIT', 'Rain suit', ['outdoor', 'clothing'], 45, 'A one-piece rain suit with taped seams and welded feet loops.', 'a {value} childrens one piece rain suit laid flat', axis='color', values=['Yellow', 'Blue Dark'], picture_per_value=True, attributes=dict(age_range='1 to 3', material='Recycled polyester', size='')),
    P('K-WELLIES', 'Wellies', ['outdoor'], 28, 'Natural rubber wellies with a pull loop.', 'a pair of {value} childrens rubber wellington boots', axis='color', values=['Yellow', 'Green', 'Red'], picture_per_value=True, attributes=dict(age_range='1 to 3', material='Rubber', size='')),
    P('K-HELMET', 'Kids helmet', ['outdoor'], 40, 'A light helmet with a dial fit and a rear light.', 'a {value} childrens bike helmet', axis='color', values=['Blue', 'Pink', 'Green'], picture_per_value=True, attributes=dict(age_range='3 to 5', material='Recycled polyester', size='')),
    P('K-SAND-SET', 'Sand play set', ['outdoor'], 18, 'A bucket, a spade, a rake and two moulds in recycled plastic.', 'a colourful childrens sand bucket and spade set', attributes=dict(age_range='1 to 3', material='Recycled polyester', color='Yellow', size='')),
    P('K-KITE', 'Bird kite', ['outdoor'], 22, 'A single-line kite shaped like a lark, easy to launch.', 'a colourful bird shaped kite', attributes=dict(age_range='5 to 8', material='Nylon', color='Orange', size='')),
    P('K-NEWBORN-BOX', 'Newborn box', ['gifts'], 70, 'A rattle, three muslins, a bodysuit pack and the board books, boxed.', 'an open gift box with a wooden rattle, muslins, bodysuits and board books', grouped=['K-RATTLE', 'K-MUSLINS-WHITE', 'K-BODYSUIT-WHITE', 'K-BOARD-BOOK'], attributes=dict(age_range='0 to 1', material='', color='', size='')),
    P('K-BIRTHDAY-BOX', 'Birthday box, age 3', ['gifts'], 95, 'A puzzle, the car set, a picture book and a sun hat.', 'an open gift box with a wooden puzzle, toy cars, a picture book and a sun hat', grouped=['K-PUZZLE', 'K-CAR-SET', 'K-PICTURE-BOOK', 'K-HAT-OATMEAL'], attributes=dict(age_range='3 to 5', material='', color='', size='')),
    P('K-GIFT-CARD', 'Little Lark gift card', ['gifts'], 30, 'A gift card by email.', 'a pale yellow gift card with a small bird illustration', type='virtual', attributes=dict(age_range='', material='', color='', size='')),
]
POSTS = [
    ('Toys by age, without the noise', '<p>Under one: things to hold, shake and chew. One to three: things to stack, push and pour. Three to five: things to pretend with. Five and up: things to build and break.</p><p>Fewer, better, and out of sight in rotation. A toy that comes back after a month is new again.</p>', 'A low shelf with a few wooden toys arranged with space between them in a bright room.'),
    ('How to size a child', '<p>Our sizes are heights in centimetres. Measure against a wall, add four for growing room, and pick the nearest size up. Trousers with an adjustable waist buy you a season.</p><p>Wash cold, dry flat, and they will fit the next child too.</p>', 'A child measured against a wall with pencil marks, seen from behind.'),
    ('Puddles are the plan', '<p>A rain suit, wellies and a warm layer underneath turn a wet day into the best day. Twenty minutes outside beats an hour of television, for everyone.</p><p>Hang the suit to dry, rinse the boots, and go again tomorrow.</p>', 'Yellow wellies jumping in a puddle on a garden path, low angle.'),
]
MORE = {
    'K-STACKER': 'The rings are large enough for small hands and the peg is rounded. From twelve months.',
    'K-TRAIN': 'The track fits the pieces of other wooden sets. From three years.',
    'K-BLOCKS': 'Cubes, arches, triangles and planks, sanded smooth and left unpainted. From eighteen months.',
    'K-RABBIT': 'Filled with wool, so it is soft and light. Hand wash and it keeps its shape.',
    'K-PLAY-KITCHEN': 'Solid birch with two hobs, an oven door and a shelf for pans. Assembly takes twenty minutes.',
    'K-PUZZLE': 'Thick pieces with a knob for small fingers. From eighteen months.',
    'K-RATTLE': 'Oiled beech with no paint and a bell that cannot come out. From birth.',
    'K-DOLL': 'Washable at thirty degrees, hair and all. The dress comes off and goes back on.',
    'K-CAR-SET': 'Small enough for a pocket, quiet enough for a wooden floor. From eighteen months.',
    'K-MARBLE-RUN': 'The pieces stack in any order, so every run is different. From four years.',
    'K-CRAFT-KIT': 'Enough material for thirty afternoons, with the ideas on cards. From four years.',
    'K-BOARD-GAME': 'Players work together to get the animals home before nightfall. Two to four players.',
    'K-BODYSUIT': 'Poppers at the crotch, an envelope neck for easy changes. From newborn to twenty-four months.',
    'K-SLEEPSUIT': 'The zip runs from the foot, so a night change does not wake the top half. From newborn to two years.',
    'K-LEGGINGS': 'Soft organic cotton with a little stretch and no labels inside. From six months to six years.',
    'K-TEE': 'A boat neck that goes over the head without a fight. From six months to eight years.',
    'K-DUNGAREES': 'Poppers at the legs for the first year, buttons on the straps later. From six months to five years.',
    'K-CARDIGAN': 'Soft merino that washes at thirty degrees. From newborn to six years.',
    'K-DRESS': 'A pinafore that layers over a tee in winter and stands alone in summer. From one to eight years.',
    'K-HOODIE': 'Brushed inside, with a hood that stays up. From two to ten years.',
    'K-JEANS': 'Stretchy enough to climb in, soft enough to sleep in. From two to ten years.',
    'K-SOCKS': 'A grip sole for wooden floors and a cuff that stays up. From six months to six years.',
    'K-HAT': 'The brim shades the neck and the strap keeps the wind from taking it. From six months to six years.',
    'K-BOARD-BOOK': 'Thick pages, rounded corners and colours that hold up to chewing. From six months.',
    'K-PICTURE-BOOK': 'Thirty-two pages with a picture on every spread. From three years.',
    'K-BEDTIME-BOOK': 'One line per page, so the reading stops when the eyes close. From one year.',
    'K-FIRST-READER': 'Short chapters, big type and a joke on every page. From five years.',
    'K-ATLAS': 'Every continent on a double spread, with the animals that live there. From four years.',
    'K-COT': 'Solid beech with a mattress base at three heights. It converts with the parts in the box.',
    'K-CHANGING-TABLE': 'The top lifts off and it becomes a desk when the nappies are done. Solid birch.',
    'K-ROCKER': 'Deep seat, high arms and a quiet rock. The boucle cover is removable.',
    'K-MOBILE': 'Wool felt shapes on a wooden arm that clips to a cot. It turns in a draught.',
    'K-SHELF': 'Three shallow shelves show the covers, so a child can choose. Fixings for the wall are included.',
    'K-STORAGE': 'Felt boxes that fold flat and stand firm. Each one holds a season of toys.',
    'K-NIGHT-LIGHT': 'Tap once for warm light, twice for dim, and it turns itself off after an hour. Charges by USB-C.',
    'K-MUSLINS': 'Large squares of double-layer organic cotton, 120 by 120 cm. Swaddle, burp cloth, sun shade.',
    'K-BALANCE-BIKE': 'Air tyres, a low frame and a seat that rises with the child. From two years.',
    'K-SCOOTER': 'Lean to steer, so it is easy to learn. The deck lights up when it rolls. From three years.',
    'K-RAIN-SUIT': 'Waterproof to 10 000 mm with taped seams and elastic cuffs. From one to six years.',
    'K-WELLIES': 'Natural rubber with a cotton lining and a loop for pulling. Sizes from 20 to 34.',
    'K-HELMET': 'Adjust the dial and the helmet fits for two years of growing. From two years.',
    'K-SAND-SET': 'Thick recycled plastic that survives a summer. The mould shapes are a fish and a star.',
    'K-KITE': 'A single line and a tail, ready to fly from the bag. From four years.',
    'K-NEWBORN-BOX': 'The four things every new baby needs, in a box with a card. Wrapped on request.',
    'K-BIRTHDAY-BOX': 'Four presents for a third birthday, chosen to be played with together. Wrapped on request.',
    'K-GIFT-CARD': 'Delivered by email within the hour, with a message of your own. Valid for a year in the store.',
}
