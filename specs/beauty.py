CODE = 'beauty'; ROOT = 'Beauty'; STORE_NAME = 'Glow Atelier'; ATTRIBUTE_SET = 'Beauty'; WEIGHT = 0.2
ATTRIBUTE_COLUMNS = ['skin_type', 'volume', 'scent', 'color']
ATTRIBUTES = [
    dict(code='skin_type', label='Skin type', input='multiselect', scope='global', filterable=1, filterable_in_search=1, visible_on_front=1, sets='Beauty', group='General', sort_order=50),
    dict(code='volume', label='Volume', input='select', scope='global', filterable=1, visible_on_front=1, comparable=1, is_configurable=1, sets='Beauty', group='General', sort_order=60),
    dict(code='scent', label='Scent', input='select', scope='global', filterable=1, visible_on_front=1, is_configurable=1, sets='Beauty', group='General', sort_order=70),
]
OPTIONS = {'skin_type': ['All skin', 'Dry', 'Oily', 'Combination', 'Sensitive'], 'volume': ['30 ml', '50 ml', '100 ml', '200 ml', '250 ml'], 'scent': ['Unscented', 'Neroli', 'Fig', 'Cedar', 'Rose', 'Citrus']}
ROOT_DESCRIPTION = 'Skincare, body care and fragrance made in small batches with short ingredient lists.'
META_DESCRIPTION = 'Glow Atelier: cleansers, serums, moisturisers, body care and fragrance with short ingredient lists, made in small batches.'
PRODUCT_STYLE = 'Studio product photograph of a single cosmetic bottle or jar on a plain white seamless background, frosted glass and matte caps, plain label without text, soft even light, no text, no lettering, no logos, no watermark, centered with margin around it.'
SCENE_STYLE = 'Soft editorial beauty photograph, pale marble and linen surfaces, morning light, a sprig of eucalyptus or a citrus slice, shallow depth of field, no text, no lettering, no logos, no watermark.'
SCENES = {
    'hero-main': 'Frosted glass skincare bottles and a ceramic dish with a sprig of eucalyptus on pale marble, soft morning light, water droplets.',
    'hero-side': 'A close up of a hand holding a small glass dropper bottle with golden serum against a soft pink background.',
    'editorial': 'A person in a white apron blending cream in a small lab with glass beakers and dried botanicals.',
    'about': 'A small bright workshop with shelves of amber glass bottles and drying herbs.',
}
CATEGORIES = [
    dict(path='cleansers', name='Cleansers', description='Balms, gels and oils that take the day off gently.', landing_title='Take the day off', landing_text='Cleansing balms, gels and oils that remove everything and strip nothing.', scene='A frosted glass bottle of cleanser and a folded white face cloth on marble with a citrus slice.'),
    dict(path='serums', name='Serums', description='Concentrated actives, one at a time.', landing_title='One active, done well', landing_text='Vitamin C, hyaluronic acid, retinal and niacinamide. One thing per bottle, at a dose that works.', scene='Three small glass dropper bottles with pale gold serum on a pale pink surface.'),
    dict(path='moisturisers', name='Moisturisers', description='Creams and lotions for every skin and season.', landing_title='Comfort, all day', landing_text='Light lotions for summer, rich creams for winter, and a balm for the weeks in between.', scene='A frosted glass jar of white cream with the lid beside it on linen.'),
    dict(path='body', name='Body', description='Washes, oils and hand care.', landing_title='Below the neck', landing_text='Body washes, dry oils and hand creams in the same short-list formulas as the face range.', scene='A bottle of body oil and a bar of soap on a wooden bath tray with a linen towel.'),
    dict(path='fragrance', name='Fragrance', description='Small-batch scents in five notes or fewer.', landing_title='Five notes, no more', landing_text='Eau de parfum and solid scents built on five notes or fewer, so you can name what you smell.', scene='A small glass perfume bottle with a wooden cap on marble beside dried flowers.'),
    dict(path='sets', name='Sets', description='Routines and travel kits, boxed.', landing_title='The routine, boxed', landing_text='Morning and evening routines and a travel kit, packed in a linen pouch.', scene='A linen pouch with small travel size bottles spilling out on a pale surface.'),
]
HERO = dict(badge='New batch', title='Short lists, long results', text='Every formula fits on the front of the bottle. Made in batches of two hundred, dated by hand.')
FEATURES = [('leaf', 'Short ingredient lists', 'Ten or fewer, on the front'), ('flask', 'Small batches', 'Dated and numbered'), ('arrow-back-up', 'Return if it stings', 'Even opened, thirty days'), ('recycle', 'Refills', 'Glass back, refill cheaper')]
STORY = dict(title='Made in a room you could visit', text1='Glow Atelier started with one cream and a list of ten ingredients. Everything since has kept the rule: if it does not fit on the front, it does not go in.', text2='Batches are two hundred at a time, dated by hand, and shipped within the month.')
PROMO = dict(badge='Refill', title='Bring the glass back', text='Every bottle and jar has a refill at a lower price. Post the empty back, or drop it in the atelier.', path='moisturisers', button='See the refills', list_title='Refillable favourites')
TESTIMONIALS = [('The vitamin C serum is the first that did not sting. My skin looks awake.', 'Elena R.', 'Amsterdam'), ('Ten ingredients on the front. I can finally read a label.', 'Marcus T.', 'Leeds'), ('The fig perfume gets more compliments than anything I have owned.', 'Priya S.', 'Toronto')]
NEWSLETTER = dict(title='Batch notes', text='A note when a new batch lands: what changed, what did not, and a sample offer.')
ABOUT = dict(title='One cream and a rule', paragraphs=['Glow Atelier began with a single moisturiser made for skin that reacted to everything. Ten ingredients, all on the front of the jar.', 'Every product since has kept that rule. Batches are small, dated by hand, and we tell you the batch number when you order.', 'The atelier has a door on the street. Come in, smell things, bring your empties back.'])
REVIEWS = [
    ('Gentle and it works', 'No stinging, no fragrance, and my skin is calmer after two weeks.', 5),
    ('Nice but small', 'Lovely texture. The jar is smaller than it looks, so watch the volume.', 4),
    ('Refill is a great idea', 'Bought the glass once, now I refill. Cheaper and less waste.', 5),
    ('My holy grail', 'Third jar. Nothing else has replaced it.', 5),
    ('Sinks in fast', 'No greasy film, makeup goes on top after a minute.', 5),
    ('Took a month to see it', 'Patience needed. Around week four the texture of my skin changed.', 4),
    ('Smells like nothing', 'Which is exactly what I wanted for reactive skin.', 5),
    ('Pump broke', 'The formula is great, the pump stopped after a month. Support sent a new one.', 3),
    ('Good for oily skin', 'Matte finish without tightness. My afternoon shine is gone.', 5),
    ('Too rich for me', 'Beautiful for dry skin I am sure, too heavy for my combination skin.', 3),
    ('Travel size please', 'I love it but the bottle is too big for a carry-on.', 4),
    ('Replaced three products', 'Cleanser, toner and serum in one step. My shelf is empty now.', 5),
    ('Glass feels premium', 'Heavy frosted glass and a proper lid. Sits well on the sink.', 5),
    ('Nice, not a miracle', 'Pleasant to use and my skin is fine, but the price promised more.', 3),
    ('Calmed a flare up', 'Used it on a red patch for three nights and it settled.', 5),
    ('A little goes far', 'Two pumps for the whole face. The bottle will last months.', 5),
    ('Great under sunscreen', 'No pilling, which is rare. Sunscreen sits smoothly on top.', 5),
    ('Arrived leaking', 'The cap was loose and a third was gone. Replaced within a week.', 3),
    ('Smooth after one use', 'The enzyme powder is gentle and my skin felt polished, not raw.', 5),
    ('Best sleep mask', 'Wake up with plumper skin. Wash the pillowcase though.', 5),
    ('Worth the price', 'Twice what I paid before and twice as good. Fair.', 5),
    ('Cloths are soft', 'Softer after each wash and they dry fast. Bought a second set.', 5),
    ('Dropper is fiddly', 'Good serum, but the dropper pulls up half a dose. Squeeze twice.', 4),
    ('Kept the routine simple', 'Three products, morning and night, and my skin is the best it has been.', 5),
]
def P(sku, name, cats, price, desc, prompt, **kw):
    d = dict(sku=sku, name=name, categories=cats, price=price, description=desc, prompt=prompt); d.update(kw); return d
PRODUCTS = [
    P('G-CLEANSE-BALM', 'Cleansing balm', ['cleansers'], 28, 'A shea and jojoba balm that melts makeup and sunscreen, then rinses clean with a cloth.', 'a frosted glass jar of pale yellow cleansing balm with a matte white lid', axis='volume', values=['50 ml', '100 ml'], attributes=dict(skin_type='All skin|Dry', scent='Unscented')),
    P('G-GEL-CLEANSER', 'Gel cleanser', ['cleansers'], 22, 'A low-foam gel with glycerin and oat, for morning and after the balm.', 'a frosted glass pump bottle of clear gel cleanser', axis='volume', values=['100 ml', '200 ml'], attributes=dict(skin_type='Oily|Combination', scent='Unscented')),
    P('G-CLEANSE-OIL', 'Cleansing oil', ['cleansers'], 26, 'Sunflower and squalane, emulsifies with water and leaves no film.', 'a clear glass pump bottle of golden cleansing oil', attributes=dict(skin_type='All skin|Dry', scent='Neroli', volume='100 ml')),
    P('G-MICELLAR', 'Micellar water', ['cleansers'], 16, 'A no-rinse water for the evenings when the sink is too far.', 'a clear glass bottle of micellar water with a flip cap', attributes=dict(skin_type='All skin|Sensitive', scent='Unscented', volume='200 ml')),
    P('G-EXFOLIANT', 'Enzyme exfoliant', ['cleansers'], 30, 'Papaya enzymes and rice powder, once a week, no grains.', 'a small frosted glass jar of fine pale powder', attributes=dict(skin_type='All skin|Combination', scent='Unscented', volume='50 ml')),
    P('G-FACE-CLOTH', 'Muslin face cloths', ['cleansers', 'sets'], 12, 'Three organic muslin cloths, softer with every wash.', 'three folded white muslin face cloths stacked', attributes=dict(skin_type='All skin', scent='Unscented', volume='')),
    P('G-VIT-C', 'Vitamin C serum', ['serums'], 42, 'Ten percent stabilised vitamin C with ferulic acid, in a dark glass dropper.', 'a dark amber glass dropper bottle with a white label', axis='volume', values=['30 ml', '50 ml'], attributes=dict(skin_type='All skin|Combination', scent='Unscented')),
    P('G-HA-SERUM', 'Hyaluronic serum', ['serums'], 32, 'Three weights of hyaluronic acid for water that stays.', 'a clear glass dropper bottle with a clear gel serum', axis='volume', values=['30 ml', '50 ml'], attributes=dict(skin_type='All skin|Dry', scent='Unscented')),
    P('G-RETINAL', 'Retinal night serum', ['serums'], 48, 'Point one percent retinaldehyde in squalane, for evenings, twice a week to start.', 'a dark blue glass dropper bottle', attributes=dict(skin_type='All skin|Combination', scent='Unscented', volume='30 ml')),
    P('G-NIACINAMIDE', 'Niacinamide serum', ['serums'], 26, 'Five percent niacinamide with zinc, for pores and shine.', 'a frosted glass dropper bottle with a light milky serum', attributes=dict(skin_type='Oily|Combination', scent='Unscented', volume='30 ml')),
    P('G-PEPTIDE', 'Peptide serum', ['serums'], 52, 'A peptide blend for firmness, in a light lotion base.', 'a white glass pump bottle with a slim silver cap', attributes=dict(skin_type='All skin|Dry', scent='Unscented', volume='30 ml')),
    P('G-EYE-SERUM', 'Eye serum', ['serums'], 36, 'Caffeine and peptides with a cool steel tip.', 'a small glass tube with a steel rollerball applicator', attributes=dict(skin_type='All skin', scent='Unscented', volume='30 ml')),
    P('G-DAY-CREAM', 'Day cream SPF 30', ['moisturisers'], 34, 'A light mineral sunscreen cream with no white cast.', 'a frosted glass jar of light white cream with a bamboo lid', axis='volume', values=['50 ml', '100 ml'], attributes=dict(skin_type='All skin|Combination', scent='Unscented')),
    P('G-NIGHT-CREAM', 'Night cream', ['moisturisers'], 38, 'Shea, ceramides and oat. The original ten-ingredient jar.', 'a frosted glass jar of rich white cream', axis='volume', values=['50 ml', '100 ml'], attributes=dict(skin_type='Dry|Sensitive', scent='Unscented')),
    P('G-LIGHT-LOTION', 'Light lotion', ['moisturisers'], 28, 'A gel-cream for summer and oily skin, absorbs in seconds.', 'a frosted glass pump bottle of light lotion', attributes=dict(skin_type='Oily|Combination', scent='Unscented', volume='100 ml')),
    P('G-BALM', 'Repair balm', ['moisturisers', 'body'], 18, 'A thick balm for lips, cuticles, elbows and windburn.', 'a small aluminium tin of pale balm with the lid off', attributes=dict(skin_type='All skin|Dry', scent='Unscented', volume='30 ml')),
    P('G-FACE-OIL', 'Face oil', ['moisturisers'], 40, 'Rosehip, squalane and a drop of neroli, for the last step.', 'a small amber glass dropper bottle of golden face oil', axis='scent', values=['Unscented', 'Neroli'], attributes=dict(skin_type='Dry|Sensitive', volume='30 ml')),
    P('G-FACE-MIST', 'Hydrating mist', ['moisturisers'], 20, 'Rose water and glycerin, for planes and afternoons.', 'a frosted glass spray bottle', attributes=dict(skin_type='All skin', scent='Rose', volume='100 ml')),
    P('G-BODY-WASH', 'Body wash', ['body'], 22, 'A creamy wash with oat and glycerin in a refillable bottle.', 'a frosted glass pump bottle of body wash', axis='scent', values=['Unscented', 'Fig', 'Cedar'], attributes=dict(skin_type='All skin', volume='250 ml')),
    P('G-BODY-OIL', 'Dry body oil', ['body'], 30, 'A fast-absorbing oil for after the shower, no residue.', 'a clear glass bottle of body oil with a wooden cap', axis='scent', values=['Neroli', 'Fig'], attributes=dict(skin_type='All skin|Dry', volume='100 ml')),
    P('G-HAND-CREAM', 'Hand cream', ['body', 'sets'], 14, 'A non-greasy hand cream in an aluminium tube.', 'an aluminium tube of hand cream with a white cap', axis='scent', values=['Unscented', 'Rose', 'Citrus'], attributes=dict(skin_type='All skin', volume='50 ml')),
    P('G-BODY-CREAM', 'Body cream', ['body'], 26, 'Shea and oat for winter skin, in a wide jar.', 'a wide frosted glass jar of white body cream', attributes=dict(skin_type='Dry|Sensitive', scent='Unscented', volume='200 ml')),
    P('G-SOAP-BAR', 'Cold-process soap', ['body'], 9, 'Olive and coconut oil soap, cured six weeks.', 'a bar of pale handmade soap with a rough edge', axis='scent', values=['Unscented', 'Cedar', 'Citrus'], attributes=dict(skin_type='All skin', volume='')),
    P('G-DEODORANT', 'Cream deodorant', ['body'], 15, 'A baking-soda-free cream deodorant in a glass jar.', 'a small glass jar of white cream deodorant with a bamboo lid', axis='scent', values=['Unscented', 'Cedar'], attributes=dict(skin_type='All skin|Sensitive', volume='50 ml')),
    P('G-LIP-BALM', 'Lip balm', ['body', 'sets'], 8, 'Beeswax and shea in a paper tube.', 'a small paper tube lip balm', attributes=dict(skin_type='All skin', scent='Unscented', volume='')),
    P('G-EDP-FIG', 'Fig eau de parfum', ['fragrance'], 68, 'Green fig, milk and cedar. Five notes.', 'a small square glass perfume bottle with a wooden cap', axis='volume', values=['30 ml', '50 ml'], attributes=dict(skin_type='', scent='Fig')),
    P('G-EDP-NEROLI', 'Neroli eau de parfum', ['fragrance'], 68, 'Orange blossom, petitgrain and a little musk.', 'a small round glass perfume bottle with a white cap', axis='volume', values=['30 ml', '50 ml'], attributes=dict(skin_type='', scent='Neroli')),
    P('G-EDP-CEDAR', 'Cedar eau de parfum', ['fragrance'], 68, 'Cedar, vetiver and black pepper. Warm and dry.', 'a tall dark glass perfume bottle with a black cap', axis='volume', values=['30 ml', '50 ml'], attributes=dict(skin_type='', scent='Cedar')),
    P('G-SOLID-SCENT', 'Solid perfume', ['fragrance'], 24, 'The same five notes in a beeswax base, in a pocket tin.', 'a small brass tin of solid perfume with the lid open', axis='scent', values=['Fig', 'Neroli', 'Cedar', 'Rose'], attributes=dict(skin_type='', volume='')),
    P('G-ROOM-MIST', 'Linen mist', ['fragrance'], 22, 'A light mist for sheets and towels.', 'a frosted glass spray bottle with a wooden cap', axis='scent', values=['Fig', 'Citrus'], attributes=dict(skin_type='', volume='100 ml')),
    P('G-CANDLE', 'Soy candle', ['fragrance'], 32, 'A forty-hour soy candle in a reusable glass.', 'a soy candle in a frosted glass with a wooden lid', axis='scent', values=['Fig', 'Cedar', 'Rose'], attributes=dict(skin_type='', volume='')),
    P('G-DISCOVERY', 'Fragrance discovery set', ['fragrance', 'sets'], 20, 'Three 2 ml vials of the eau de parfums, credited against a full bottle.', 'three small glass sample vials in a slim box', attributes=dict(skin_type='', scent='', volume='')),
    P('G-AM-ROUTINE', 'Morning routine', ['sets'], 90, 'Gel cleanser, vitamin C and day cream, at a saving.', 'three frosted glass skincare products arranged in a row on white', grouped=['G-GEL-CLEANSER-100-ML', 'G-VIT-C-30-ML', 'G-DAY-CREAM-50-ML'], attributes=dict(skin_type='All skin', scent='Unscented', volume='')),
    P('G-PM-ROUTINE', 'Evening routine', ['sets'], 100, 'Cleansing balm, retinal serum and night cream.', 'a jar, a dropper bottle and a cream jar arranged on white', grouped=['G-CLEANSE-BALM-50-ML', 'G-RETINAL', 'G-NIGHT-CREAM-50-ML'], attributes=dict(skin_type='All skin', scent='Unscented', volume='')),
    P('G-TRAVEL-KIT', 'Travel kit', ['sets'], 34, 'Five 30 ml bottles in a linen pouch, cabin approved.', 'five small frosted travel bottles in an open linen pouch', attributes=dict(skin_type='All skin', scent='Unscented', volume='30 ml')),
    P('G-HAND-SET', 'Hand care set', ['sets', 'body'], 28, 'Hand cream, repair balm and a nail oil in a small box.', 'a hand cream tube, a small tin and a nail oil bottle in an open box', grouped=['G-HAND-CREAM-UNSCENTED', 'G-BALM', 'G-LIP-BALM'], attributes=dict(skin_type='All skin', scent='Unscented', volume='')),
    P('G-HEADBAND', 'Spa headband', ['sets'], 10, 'A soft cotton terry headband for cleansing.', 'a white cotton terry spa headband', attributes=dict(skin_type='', scent='', volume='')),
    P('G-GUA-SHA', 'Jade gua sha', ['sets'], 18, 'A jade tool for the face oil step.', 'a green jade gua sha stone', attributes=dict(skin_type='', scent='', volume='')),
    P('G-GIFT-CARD', 'Glow gift card', ['sets'], 50, 'A gift card by email, for a routine they choose.', 'a pale pink gift card with a gold edge', type='virtual', attributes=dict(skin_type='', scent='', volume='')),
]
POSTS = [
    ('The order of a routine', '<p>Thin to thick. Cleanser, then water-based serums, then oil, then cream. Sunscreen last in the morning, and nothing after retinal at night.</p><p>One new product at a time, two weeks apart. If something stings, stop, and tell us.</p>', 'Skincare bottles lined up in order of use on a marble shelf in soft light.'),
    ('Why ten ingredients', '<p>Fewer ingredients means fewer things to react to and a label you can read. It also means each one has to earn its place, at a dose that does something.</p><p>Our longest list is nine. The shortest is three.</p>', 'A hand holding a frosted glass jar with a short handwritten style ingredient label, blurred background.'),
    ('How to refill', '<p>Rinse the glass, post it back in the box it came in, and we send a refill at the lower price. Or bring it to the atelier and fill it at the counter.</p><p>Every refill saves a jar. Last year that was four thousand of them.</p>', 'Empty frosted glass jars in a wooden crate on a workshop counter.'),
]
MORE = {
    'G-CLEANSE-BALM': 'Massage it on dry skin for a minute, add warm water, then wipe. One jar lasts about three months of evenings.',
    'G-GEL-CLEANSER': 'It rinses clean without the tight feeling. The pump gives one dose for the whole face.',
    'G-CLEANSE-OIL': 'Two pumps in dry hands, a slow massage, then water turns it milky. Waterproof mascara comes off too.',
    'G-MICELLAR': 'Soak a cotton pad, press for five seconds, wipe once. Follow with a cleanser when you have the energy.',
    'G-EXFOLIANT': 'Mix a small spoon with water in the palm until it foams. Sunday evening is the right night for it.',
    'G-FACE-CLOTH': 'Use one per evening and wash them together at sixty degrees. They dry on the rail by morning.',
    'G-VIT-C': 'Four drops on clean skin in the morning, before sunscreen. The dark glass keeps the formula fresh for three months after opening.',
    'G-HA-SERUM': 'Press it on damp skin so the acids have water to hold. It sits well under any cream.',
    'G-RETINAL': 'Start with two nights a week and add a night every fortnight. Always wear sunscreen the next day.',
    'G-NIACINAMIDE': 'A pea-sized amount for the T zone, morning or evening. Results show around week six.',
    'G-PEPTIDE': 'The lotion base makes it a serum and a light moisturiser in one step. Good for the neck as well.',
    'G-EYE-SERUM': 'Keep it in the fridge and roll the tip from the inner corner outward. Two seconds per eye is enough.',
    'G-DAY-CREAM': 'Zinc oxide only, tinted just enough to disappear on most skin tones. Reapply after swimming.',
    'G-NIGHT-CREAM': 'A thick cream that softens into the skin overnight. Ten ingredients on the label, nothing hidden behind a fragrance.',
    'G-LIGHT-LOTION': 'It gives water without oil, so makeup sits well over it. The tube fits a gym bag.',
    'G-BALM': 'A little on the fingertip goes a long way. Keep one in the coat pocket from October to March.',
    'G-FACE-OIL': 'Two drops pressed over the night cream, or mixed into it. The neroli fades in a minute.',
    'G-FACE-MIST': 'A fine spray from thirty centimetres, eyes closed. It sets makeup and revives it at four in the afternoon.',
    'G-BODY-WASH': 'The glass bottle comes once and the refill pouches come after. The oat leaves the skin soft, not slippery.',
    'G-BODY-OIL': 'Spray on damp skin after the shower and get dressed straight away. It sinks in before the towel is folded.',
    'G-HAND-CREAM': 'It absorbs before you touch the keyboard. The tube survives a handbag for a year.',
    'G-BODY-CREAM': 'Rich enough for shins in January and elbows all year. The wide jar makes it easy to reach the last spoon.',
    'G-SOAP-BAR': 'The bar keeps its shape in the shower if it rests on a slatted dish. Unscented, so it suits the whole family.',
    'G-DEODORANT': 'A pea-sized amount warmed between the fingers is enough for a day. It does not stain shirts.',
    'G-LIP-BALM': 'The paper tube pushes up from the bottom and goes in the compost when it is done. Faintly sweet from the beeswax.',
    'G-EDP-FIG': 'It opens green and settles into milk and cedar after an hour. Lasts a working day on skin.',
    'G-EDP-NEROLI': 'Bright in the morning, soft by lunch. Made for warm weather and white shirts.',
    'G-EDP-CEDAR': 'A dry, quiet scent that stays close to the skin. The pepper fades first and the cedar stays until evening.',
    'G-SOLID-SCENT': 'Warm it with a fingertip and press on the wrists. The tin fits a pocket and never spills.',
    'G-ROOM-MIST': 'Two sprays on the pillow before bed, or on towels fresh from the line. It dries without marks.',
    'G-CANDLE': 'Trim the wick to five millimetres before each burn. Once the wax is gone, the glass holds pens.',
    'G-DISCOVERY': 'Try each vial for a day before deciding. The price comes off the full bottle you choose afterwards.',
    'G-AM-ROUTINE': 'Three steps in the order they are listed, five minutes in total. The set costs less than the three bought apart.',
    'G-PM-ROUTINE': 'Balm first, serum on dry skin, cream last. Start the serum slowly, the leaflet explains how.',
    'G-TRAVEL-KIT': 'Cleanser, serum, day cream, night cream and body wash in bottles that pass security. The pouch washes at forty degrees.',
    'G-HAND-SET': 'Everything for hands that garden, type and wash too often. The box is ready to give.',
    'G-HEADBAND': 'It keeps hair off the face while the balm does its work. Machine washable.',
    'G-GUA-SHA': 'Cool stone, slow strokes from the centre of the face outward. A minute each side, after the face oil.',
    'G-GIFT-CARD': 'Delivered by email within the hour, with a message of your own. Valid for a year on everything in the store.',
}
