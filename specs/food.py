CODE = 'food'; ROOT = 'Food'; STORE_NAME = 'Harvest & Hearth'; ATTRIBUTE_SET = 'Food'; WEIGHT = 0.5
ATTRIBUTE_COLUMNS = ['diet', 'origin', 'pack_size']
ATTRIBUTES = [
    dict(code='diet', label='Diet', input='multiselect', scope='global', filterable=1, filterable_in_search=1, visible_on_front=1, sets='Food', group='General', sort_order=50),
    dict(code='origin', label='Origin', input='select', scope='global', filterable=1, visible_on_front=1, comparable=1, sets='Food', group='General', sort_order=60),
    dict(code='pack_size', label='Pack size', input='select', scope='global', filterable=1, visible_on_front=1, is_configurable=1, sets='Food', group='General', sort_order=70),
]
OPTIONS = {'diet': ['Vegan', 'Vegetarian', 'Gluten free', 'Organic'], 'origin': ['Italy', 'Spain', 'France', 'Greece', 'Portugal', 'Local farms'], 'pack_size': ['100 g', '250 g', '500 g', '1 kg', '6 pack']}
ROOT_DESCRIPTION = 'Small-batch food from farms and makers we know by name.'
META_DESCRIPTION = 'Harvest & Hearth: olive oil, pasta, cheese, coffee and drinks from small producers, delivered fresh.'
PRODUCT_STYLE = 'Studio product photograph of a single food item on a plain white seamless background, soft natural light, no text, no lettering, no logos, no watermark, centered with margin around it. Labels are plain kraft paper without writing.'
SCENE_STYLE = 'Warm editorial food photograph, rustic wooden surfaces, natural window light, shallow depth of field, no text, no lettering, no logos, no watermark.'
SCENES = {
    'hero-main': 'A long farmhouse table laid with sourdough loaves, a wedge of aged cheese, tomatoes on the vine and a bottle of olive oil, morning light through a barn door.',
    'hero-side': 'A ceramic bowl of fresh pasta dusted with flour beside a small pile of eggs on a wooden board.',
    'editorial': 'A farmer holding a crate of vegetables at the edge of a field at sunrise, seen from the side.',
    'about': 'A small stone kitchen with copper pots, a wood-fired oven and a table of jars of preserves.',
}
CATEGORIES = [
    dict(path='pantry', name='Pantry', description='Olive oil, pasta, grains and preserves for every day.', landing_title='The shelf that feeds the week', landing_text='Cold-pressed oils, bronze-cut pasta and jams cooked in copper. Everything on this shelf lasts, and everything gets used.', scene='A pantry shelf with bottles of olive oil, jars of jam and bags of pasta in soft light.'),
    dict(path='bakery', name='Bakery', description='Bread and pastries baked before dawn, shipped the same day.', landing_title='Baked before you wake', landing_text='Sourdough, focaccia and pastries from our own oven. Order before midnight and they leave the bakery the next morning.', scene='A wooden counter with sourdough loaves, croissants and a focaccia fresh from a stone oven.'),
    dict(path='cheese-charcuterie', name='Cheese & Charcuterie', description='Aged cheeses and cured meats from small dairies and farms.', landing_title='Aged with patience', landing_text='Cave-aged cheese and cured meats from farms that name their animals. Cut to order and packed cold.', scene='A slate board with wedges of aged cheese, sliced cured ham and a bunch of grapes.'),
    dict(path='coffee-tea', name='Coffee & Tea', description='Single-origin coffee and loose leaf tea, roasted and packed weekly.', landing_title='Roasted this week', landing_text='Small-lot coffee roasted on Mondays and loose leaf teas from two estates. Ground to order or whole bean.', scene='A pour-over coffee setup with a bag of beans and a tin of loose tea on a wooden counter.'),
    dict(path='drinks', name='Drinks', description='Craft sodas, juices, wine and spirits from small producers.', landing_title='Bottled by hand', landing_text='Pressed juices, small-batch sodas and a short list of wines we drink ourselves.', scene='Glass bottles of juice and craft soda on a marble counter with sliced citrus, backlit by a window.'),
    dict(path='gift-boxes', name='Gift Boxes', description='Curated boxes for tables, birthdays and thank-yous.', landing_title='A box that says it', landing_text='Our own selections, packed in a wooden crate with straw and a handwritten card.', scene='An open wooden gift crate filled with jars, a bottle of oil, cheese and a loaf, tied with twine.'),
]
HERO = dict(badge='New harvest', title='From the farm, to the table, this week', text='Olive oil pressed in November, bread baked at four, cheese cut this morning. We ship what is in season and nothing else.')
FEATURES = [('truck', 'Cold-chain delivery', 'Fresh goods travel chilled'), ('leaf', 'Small producers', 'Every maker named on the label'), ('arrow-back-up', 'Freshness promise', 'Not happy, full refund'), ('headset', 'Real people', 'Chat with the kitchen, weekdays')]
STORY = dict(title='We buy from people, not warehouses', text1='Harvest & Hearth started as a market stall with three producers. Today there are forty, and we still visit every one of them each year.', text2='If a harvest is short, the shelf is short. That is the deal, and it is why the food tastes the way it does.')
PROMO = dict(badge='Weekly box', title='The market box', text='Six seasonal items picked by the kitchen every Monday, at a price under the shelf total.', path='gift-boxes', button='See the boxes', list_title='This week in the box')
TESTIMONIALS = [('The olive oil is the best I have had outside Puglia. Peppery, green, alive.', 'Elena R.', 'Bristol'), ('Bread arrived the next morning and was still crackly. I did not think that was possible.', 'Marcus T.', 'Leeds'), ('The gift crate made my mother cry. Good tears.', 'Priya S.', 'Dublin')]
NEWSLETTER = dict(title='What is in season', text='One note a week: what arrived, what is ripe, and a recipe from the kitchen.')
ABOUT = dict(title='A market stall that grew', paragraphs=['We started with a stall, a van and three producers who trusted us with their harvest. The van is gone. The trust is the business.', 'Every product carries the name of the farm or the maker. We visit each one every year, taste the new season, and decide together what goes on the shelf.', 'The kitchen behind the shop cooks the preserves, bakes the bread and packs the boxes. If you have a question, the people who answer are the people who made it.'])
REVIEWS = [
    ('Tastes like the real thing', 'Bright, fresh and clearly made in small batches. Will reorder.', 5),
    ('Good, a little pricey', 'Quality is there, but you pay for it. Worth it for a weekend.', 4),
    ('Arrived cold and fast', 'Packed with ice packs and a note. Everything was perfect.', 5),
    ('Weekly staple now', 'This has replaced the supermarket version in our house.', 5),
    ('Peppery finish', 'Green and grassy, with a proper pepper kick at the end.', 5),
    ('Bread was still warm', 'Well, almost. Same-day delivery from the oven is a marvel.', 5),
    ('Jar was half full', 'Tastes great, but the jar looked short. Check the weight, not the glass.', 3),
    ('Kids ate the crusts', 'That has never happened. Buying every week.', 5),
    ('Strong coffee', 'Dark and chocolatey. Not for people who like it light.', 4),
    ('Cheese needs a warning', 'It is glorious and it stinks out the fridge. Double wrap it.', 5),
    ('Perfect crate', 'Sent as a housewarming gift. They messaged me a photo.', 5),
    ('Too sweet for me', 'Good quality soda but sweeter than I hoped.', 3),
    ('Pasta holds the sauce', 'Bronze cut, rough surface. The difference is real.', 5),
    ('Delivery missed the slot', 'Came a day late. Still cold, still good, but plan a day ahead.', 3),
    ('Honey is set, not runny', 'Set honey with a floral taste. Spread it thick.', 5),
    ('Breakfast is sorted', 'Granola, jam and coffee in one order. Mornings are better.', 5),
    ('Cured ham sliced thin', 'Paper thin and packed flat. Melted on warm bread.', 5),
    ('Bitter chocolate', 'Very dark. I like it, my partner does not.', 4),
    ('Great for a picnic', 'Everything travelled well in the crate and the ice lasted.', 5),
    ('Tea is fragrant', 'Loose leaf, big leaves, three steeps from one spoon.', 5),
    ('Wine surprised me', 'Did not know the producer. Now I do.', 5),
    ('Portion is small', 'Delicious, but two people finished it in one go.', 4),
    ('Olive oil for cooking too', 'I bought the litre for the pan and the small bottle for salads.', 5),
    ('Repeat order', 'Third crate. The team remembers the note about no nuts.', 5),
]
def P(sku, name, cats, price, desc, prompt, **kw):
    d = dict(sku=sku, name=name, categories=cats, price=price, description=desc, prompt=prompt); d.update(kw); return d
PRODUCTS = [
    P('F-OLIVE-OIL', 'Puglia extra virgin olive oil', ['pantry'], 18, 'Cold-pressed from Coratina olives within hours of picking. Peppery, green and best raw on bread and greens.', 'a tall dark glass bottle of extra virgin olive oil with a plain kraft label', axis='pack_size', values=['500 g', '1 kg'], attributes=dict(diet='Vegan|Organic', origin='Italy')),
    P('F-BRONZE-PASTA', 'Bronze-cut rigatoni', ['pantry'], 5.5, 'Slow-dried durum wheat pasta cut through bronze dies, so the sauce clings.', 'a paper bag of dried rigatoni pasta with some pieces spilling out', axis='pack_size', values=['500 g', '1 kg'], attributes=dict(diet='Vegan', origin='Italy')),
    P('F-SPAGHETTI', 'Gragnano spaghetti', ['pantry'], 5, 'Long, slow-dried spaghetti from Gragnano, with the bite to hold a carbonara.', 'a paper bag of dried spaghetti with a bundle of spaghetti beside it', attributes=dict(diet='Vegan', origin='Italy', pack_size='500 g')),
    P('F-APRICOT-JAM', 'Apricot jam', ['pantry'], 7.5, 'Whole apricots cooked in copper with cane sugar and nothing else.', 'a glass jar of apricot jam with a plain kraft label and a gold lid', attributes=dict(diet='Vegan|Vegetarian', origin='France', pack_size='250 g')),
    P('F-FIG-JAM', 'Black fig jam', ['pantry'], 8, 'Late-summer black figs with a squeeze of lemon. Made for cheese.', 'a glass jar of dark fig jam with a plain kraft label', attributes=dict(diet='Vegan|Vegetarian', origin='Greece', pack_size='250 g')),
    P('F-HONEY', 'Wildflower honey', ['pantry'], 12, 'Raw honey from hives on a hillside of thyme and heather. Unfiltered, crystallises with time.', 'a glass jar of golden wildflower honey with a wooden dipper beside it', axis='pack_size', values=['250 g', '500 g'], attributes=dict(diet='Vegetarian', origin='Greece')),
    P('F-TOMATO-PASSATA', 'San Marzano passata', ['pantry'], 4.5, 'Sieved San Marzano tomatoes in a glass bottle, picked ripe and nothing added.', 'a glass bottle of red tomato passata with a plain kraft label', attributes=dict(diet='Vegan|Organic', origin='Italy', pack_size='500 g')),
    P('F-SEA-SALT', 'Flaky sea salt', ['pantry'], 6, 'Pyramid flakes harvested from Atlantic salt pans. Finishing salt, not for the pot.', 'a small wooden box of white flaky sea salt with the lid open', attributes=dict(diet='Vegan', origin='Portugal', pack_size='250 g')),
    P('F-SOURDOUGH', 'Country sourdough', ['bakery'], 6.5, 'A 48-hour sourdough with a dark crust and an open crumb. Wheat, water, salt and time.', 'a round country sourdough loaf with a scored dark crust', attributes=dict(diet='Vegan', origin='Local farms', pack_size='1 kg')),
    P('F-BAGUETTE', 'Baguette tradition', ['bakery'], 3, 'A long-fermented baguette with a thin crust that shatters.', 'a single golden baguette', attributes=dict(diet='Vegan', origin='Local farms', pack_size='250 g')),
    P('F-FOCACCIA', 'Rosemary focaccia', ['bakery'], 5.5, 'Dimpled focaccia with olive oil, rosemary and flaky salt.', 'a square of rosemary focaccia with dimples and flaky salt', attributes=dict(diet='Vegan', origin='Local farms', pack_size='500 g')),
    P('F-CROISSANT', 'Butter croissants', ['bakery'], 9, 'Six croissants laminated with cultured butter. Best warmed for five minutes.', 'six golden butter croissants in a paper tray', attributes=dict(diet='Vegetarian', origin='Local farms', pack_size='6 pack')),
    P('F-RYE-LOAF', 'Seeded rye loaf', ['bakery'], 6, 'Dense rye with sunflower and pumpkin seeds. Keeps for a week.', 'a dark seeded rye loaf sliced at one end', attributes=dict(diet='Vegan', origin='Local farms', pack_size='1 kg')),
    P('F-GF-LOAF', 'Gluten-free seed loaf', ['bakery'], 7, 'A buckwheat and seed loaf with no gluten and no compromise on crust.', 'a rustic gluten free seed loaf on white', attributes=dict(diet='Vegan|Gluten free', origin='Local farms', pack_size='500 g')),
    P('F-CINNAMON-BUN', 'Cardamom buns', ['bakery'], 10, 'Six twisted buns with cardamom sugar and a pearl sugar top.', 'six twisted cardamom buns with pearl sugar in a paper tray', attributes=dict(diet='Vegetarian', origin='Local farms', pack_size='6 pack')),
    P('F-AGED-CHEDDAR', 'Cave-aged cheddar', ['cheese-charcuterie'], 11, 'Clothbound cheddar aged eighteen months in a stone cave. Crumbly, sharp, sweet at the end.', 'a wedge of clothbound aged cheddar cheese', axis='pack_size', values=['250 g', '500 g'], attributes=dict(diet='Vegetarian', origin='Local farms')),
    P('F-MANCHEGO', 'Manchego 12 months', ['cheese-charcuterie'], 12, 'Sheep milk cheese aged a year. Nutty and firm, for slicing with quince.', 'a wedge of manchego cheese with its patterned rind', attributes=dict(diet='Vegetarian', origin='Spain', pack_size='250 g')),
    P('F-BRIE', 'Farmhouse brie', ['cheese-charcuterie'], 9.5, 'A soft, bloomy-rind brie from raw milk. Ripe at the edges, chalky in the middle.', 'a whole round of brie cheese with a bloomy white rind, one slice cut out', attributes=dict(diet='Vegetarian', origin='France', pack_size='500 g')),
    P('F-PECORINO', 'Pecorino romano', ['cheese-charcuterie'], 10, 'Salty sheep milk cheese for grating over pasta.', 'a wedge of pecorino romano cheese with a black rind', attributes=dict(diet='Vegetarian', origin='Italy', pack_size='250 g')),
    P('F-JAMON', 'Iberico ham, sliced', ['cheese-charcuterie'], 16, 'Acorn-fed Iberico ham, hand sliced and vacuum packed.', 'thin slices of iberico ham fanned on white paper', attributes=dict(origin='Spain', pack_size='100 g')),
    P('F-SALAMI', 'Fennel salami', ['cheese-charcuterie'], 8.5, 'A coarse pork salami with wild fennel seed, air dried for eight weeks.', 'a whole fennel salami with a few slices cut', attributes=dict(origin='Italy', pack_size='250 g')),
    P('F-CHORIZO', 'Cured chorizo', ['cheese-charcuterie'], 7.5, 'Smoked paprika chorizo, cured whole. Slice thin or cook in chunks.', 'a horseshoe of cured chorizo sausage', attributes=dict(origin='Spain', pack_size='250 g')),
    P('F-OLIVES', 'Marinated olives', ['cheese-charcuterie', 'pantry'], 6, 'Green and black olives in oil with lemon peel and thyme.', 'a glass jar of mixed marinated olives with lemon peel', attributes=dict(diet='Vegan', origin='Greece', pack_size='250 g')),
    P('F-ESPRESSO', 'Espresso blend', ['coffee-tea'], 14, 'Brazil and Ethiopia, roasted dark enough for milk and bright enough without.', 'a kraft paper bag of coffee beans with beans spilling out', axis='pack_size', values=['250 g', '500 g', '1 kg'], attributes=dict(diet='Vegan', origin='Local farms')),
    P('F-ETHIOPIA', 'Ethiopia single origin', ['coffee-tea'], 16, 'Washed Yirgacheffe with jasmine and citrus. Roasted light for filter.', 'a kraft paper bag of light roast coffee beans', axis='pack_size', values=['250 g', '500 g'], attributes=dict(diet='Vegan|Organic', origin='Local farms')),
    P('F-DECAF', 'Swiss water decaf', ['coffee-tea'], 14, 'A Colombian decaffeinated with water only. Chocolate and red fruit.', 'a kraft paper bag of coffee beans with a small scoop', attributes=dict(diet='Vegan', origin='Local farms', pack_size='250 g')),
    P('F-EARL-GREY', 'Earl Grey loose leaf', ['coffee-tea'], 9, 'Ceylon black tea with cold-pressed bergamot oil.', 'a round tin of loose leaf black tea with the lid off', attributes=dict(diet='Vegan', origin='Local farms', pack_size='100 g')),
    P('F-GREEN-TEA', 'Sencha green tea', ['coffee-tea'], 11, 'First-flush sencha, grassy and sweet. Brew at 70 degrees.', 'a round tin of green loose leaf tea with a wooden scoop', attributes=dict(diet='Vegan|Organic', origin='Local farms', pack_size='100 g')),
    P('F-CHAMOMILE', 'Chamomile flowers', ['coffee-tea'], 7, 'Whole dried chamomile flowers for a calm evening cup.', 'a glass jar of dried chamomile flowers', attributes=dict(diet='Vegan|Organic', origin='Greece', pack_size='100 g')),
    P('F-HOT-CHOC', 'Drinking chocolate flakes', ['coffee-tea'], 10, 'Seventy percent dark chocolate flakes for the pan, not the kettle.', 'a glass jar of dark chocolate flakes', attributes=dict(diet='Vegetarian', origin='France', pack_size='250 g')),
    P('F-APPLE-JUICE', 'Cloudy apple juice', ['drinks'], 4.5, 'Pressed from orchard apples, unfiltered and pasteurised gently.', 'a glass bottle of cloudy apple juice with a plain label', attributes=dict(diet='Vegan|Organic', origin='Local farms', pack_size='1 kg')),
    P('F-LEMONADE', 'Sicilian lemonade', ['drinks'], 3.5, 'Sparkling lemonade with Sicilian lemons and cane sugar, not too sweet.', 'a glass bottle of sparkling lemonade with a slice of lemon beside it', axis='pack_size', values=['500 g', '6 pack'], attributes=dict(diet='Vegan', origin='Italy')),
    P('F-GINGER-BEER', 'Fiery ginger beer', ['drinks'], 3.5, 'Fermented ginger beer with a real kick.', 'a brown glass bottle of ginger beer', axis='pack_size', values=['500 g', '6 pack'], attributes=dict(diet='Vegan', origin='Local farms')),
    P('F-KOMBUCHA', 'Hibiscus kombucha', ['drinks'], 4, 'Live kombucha with hibiscus and lime. Keep it cold.', 'a glass bottle of pink hibiscus kombucha', attributes=dict(diet='Vegan|Organic', origin='Local farms', pack_size='500 g')),
    P('F-RED-WINE', 'Douro red', ['drinks'], 15, 'A field blend from old vines in the Douro. Dark fruit, soft tannin, open an hour early.', 'a bottle of red wine with a plain kraft label', attributes=dict(diet='Vegan', origin='Portugal', pack_size='1 kg')),
    P('F-WHITE-WINE', 'Vinho verde', ['drinks'], 11, 'Light, dry and faintly sparkling. The summer bottle.', 'a bottle of white wine with a plain kraft label', attributes=dict(diet='Vegan', origin='Portugal', pack_size='1 kg')),
    P('F-VERMOUTH', 'Rosso vermouth', ['drinks'], 22, 'A bittersweet vermouth with wormwood and orange peel. Serve on ice with a twist.', 'a bottle of dark red vermouth with a plain label', attributes=dict(diet='Vegan', origin='Italy', pack_size='1 kg')),
    P('F-OIL-VINEGAR-SET', 'Oil and vinegar set', ['gift-boxes'], 32, 'Our Puglia oil with a twelve-year balsamic, boxed together.', 'two glass bottles of olive oil and dark balsamic vinegar standing in an open wooden box', attributes=dict(diet='Vegan', origin='Italy', pack_size='1 kg')),
    P('F-BALSAMIC', 'Balsamic vinegar 12 years', ['pantry', 'gift-boxes'], 19, 'Aged in a series of wooden casks. Thick, sweet, a few drops at a time.', 'a small squat glass bottle of dark balsamic vinegar', attributes=dict(diet='Vegan', origin='Italy', pack_size='250 g')),
    P('F-BREAKFAST-BOX', 'Breakfast crate', ['gift-boxes'], 42, 'Croissants, honey, apricot jam and a bag of espresso in a wooden crate.', 'an open wooden crate with croissants, a jar of honey, a jar of jam and a bag of coffee', grouped=['F-CROISSANT', 'F-HONEY-250-G', 'F-APRICOT-JAM', 'F-ESPRESSO-250-G'], attributes=dict(origin='Local farms')),
    P('F-CHEESE-BOX', 'Cheese board crate', ['gift-boxes'], 48, 'Cheddar, manchego, brie and fig jam, cut and packed cold.', 'an open wooden crate with wedges of cheese and a jar of fig jam on straw', grouped=['F-AGED-CHEDDAR-250-G', 'F-MANCHEGO', 'F-BRIE', 'F-FIG-JAM'], attributes=dict(origin='Local farms')),
    P('F-APERITIVO-BOX', 'Aperitivo crate', ['gift-boxes'], 55, 'Vermouth, olives, fennel salami and a bag of taralli.', 'an open wooden crate with a bottle of vermouth, a jar of olives and a salami on straw', grouped=['F-VERMOUTH', 'F-OLIVES', 'F-SALAMI'], attributes=dict(origin='Italy')),
    P('F-TARALLI', 'Fennel taralli', ['pantry'], 4.5, 'Crunchy ring biscuits with fennel seed and olive oil, for the aperitivo hour.', 'a paper bag of small ring shaped taralli crackers', attributes=dict(diet='Vegan', origin='Italy', pack_size='250 g')),
    P('F-ALMONDS', 'Marcona almonds', ['pantry'], 8, 'Fried in olive oil and salted. The bar snack.', 'a glass jar of roasted marcona almonds', attributes=dict(diet='Vegan', origin='Spain', pack_size='250 g')),
    P('F-DARK-CHOC', 'Dark chocolate bar 72%', ['pantry'], 5, 'Single-estate cacao, stone ground, seventy-two percent.', 'a dark chocolate bar half unwrapped from plain paper', attributes=dict(diet='Vegan|Organic', origin='France', pack_size='100 g')),
    P('F-GRANOLA', 'Maple pecan granola', ['pantry', 'bakery'], 9, 'Oats, pecans and maple, baked in small trays until the clusters hold.', 'a glass jar of granola with pecans', attributes=dict(diet='Vegetarian', origin='Local farms', pack_size='500 g')),
]
POSTS = [
    ('How to taste olive oil', '<p>Pour a spoonful into a small glass, cup it in your hands to warm it, and breathe in. Grass, tomato leaf, artichoke: that is the fruit. Then sip with a little air. The bitterness on the tongue and the pepper in the throat are polyphenols, and they are the point.</p><p>Fresh oil is loud. It quiets over the year, which is why we ship the new harvest in November and tell you to use it, not save it.</p>', 'A small glass of green olive oil on a wooden table with a spoon and a sprig of olive leaves.'),
    ('A cheese board for four', '<p>Three cheeses are enough: one soft, one hard, one blue or aged. Take them out of the fridge an hour before. Add something sweet (fig jam), something sharp (cornichons) and plain bread rather than crackers that shout.</p><p>Cut the wedges so everyone gets rind and centre. Then stop arranging. It is a board, not a painting.</p>', 'A cheese board with three cheeses, fig jam, cornichons and slices of bread, seen from above.'),
    ('Sourdough, day two', '<p>A good loaf is better on the second day. Toast thick slices, rub with a cut garlic clove while hot, then a pour of oil and flaky salt. Or make panzanella: torn stale bread, tomatoes, red onion, vinegar and time.</p><p>Never keep bread in the fridge. A paper bag on the counter, cut side down on the board, is all it needs.</p>', 'Thick slices of toasted sourdough with olive oil and salt on a wooden board.'),
]
MORE = {
    'F-OLIVE-OIL': 'Pressed in November and bottled dark to keep the flavour. Use the small bottle for salads and the litre for the pan.',
    'F-BRONZE-PASTA': 'Dried for two days at a low temperature, which keeps the wheat flavour. Ten minutes in salted water.',
    'F-SPAGHETTI': 'Made from Italian durum wheat and mountain water. Eleven minutes for al dente.',
    'F-APRICOT-JAM': 'Sixty percent fruit, set softly, with pieces of apricot in every spoon. Keep in the fridge once open.',
    'F-FIG-JAM': 'Dark, sticky and not too sweet. A spoon beside a hard cheese or on warm toast.',
    'F-HONEY': 'Never heated above hive temperature, so it sets over the winter. Warm the jar in water to bring it back.',
    'F-TOMATO-PASSATA': 'Bottled the day the tomatoes are picked, with a leaf of basil. Enough for two pans of sauce.',
    'F-SEA-SALT': 'The flakes crush between the fingers over a finished dish. A tub lasts a year in most kitchens.',
    'F-SOURDOUGH': 'Baked before dawn, packed warm, delivered the same day. It keeps for four days in a cloth.',
    'F-BAGUETTE': 'Made with a poolish left overnight, so the crumb is creamy. Best eaten the day it arrives.',
    'F-FOCACCIA': 'A tray of thirty by forty centimetres, cut into six. Warm it for five minutes and add nothing.',
    'F-CROISSANT': 'Twenty-seven layers of butter and dough, proved overnight. They freeze well and bake from frozen.',
    'F-RYE-LOAF': 'A dense loaf that slices thin and toasts well. Good with butter, better with cheese.',
    'F-GF-LOAF': 'Baked in a separate kitchen, so it is safe for coeliacs. Toast it and the crust comes alive.',
    'F-CINNAMON-BUN': 'Freshly ground cardamom in the dough and the sugar. Warm them for three minutes before serving.',
    'F-AGED-CHEDDAR': 'Made from the milk of one herd and turned by hand in the cave. Cut to order, about 250 g.',
    'F-MANCHEGO': 'From the raw milk of Manchega sheep, with a natural rind. Slice thin and serve at room temperature.',
    'F-BRIE': 'About 400 g, sold ripe. Leave it out for an hour before serving and the middle softens.',
    'F-PECORINO': 'Aged ten months, hard and salty. Grate it over pasta or shave it over broad beans.',
    'F-JAMON': 'Cured for thirty-six months in the mountain air. Eighty grams, sliced by hand the day it ships.',
    'F-SALAMI': 'One whole salami of about 300 g. Peel the casing and slice thick.',
    'F-CHORIZO': 'About 250 g, mild smoke, a little heat. Fry it in chunks and use the red oil for eggs.',
    'F-OLIVES': 'A 300 g jar of mixed olives, with stones. Drain and warm them for a minute before serving.',
    'F-ESPRESSO': 'Roasted on Mondays and shipped in the same week. Whole bean or ground for espresso, moka or filter.',
    'F-ETHIOPIA': 'Grown at two thousand metres and washed at the mill. Brew at fifteen to one for filter.',
    'F-DECAF': 'The caffeine is removed with water alone, so the flavour stays. Nobody notices it is decaf.',
    'F-EARL-GREY': 'Big leaves and real bergamot, not flavouring. Three minutes at ninety-five degrees.',
    'F-GREEN-TEA': 'Steamed and rolled leaves from the spring harvest. Sixty seconds for the first cup, longer for the second.',
    'F-CHAMOMILE': 'Whole flowers, not dust, from a farm in the hills. Five minutes covered in a pot.',
    'F-HOT-CHOC': 'Two spoons per cup, heated slowly with milk. Made from a single-estate cacao.',
    'F-APPLE-JUICE': 'Pressed in the autumn from six old varieties. Cloudy because nothing is filtered out.',
    'F-LEMONADE': 'Real lemon juice, cane sugar and water, carbonated in the bottle. Serve very cold.',
    'F-GINGER-BEER': 'Fresh root ginger, fermented for three days. Drink it alone or with a dark rum.',
    'F-KOMBUCHA': 'A live drink with a light fizz and a sour finish. Store it cold and open it slowly.',
    'F-RED-WINE': 'Touriga and friends from vines older than the winemaker. Decant it and drink it with grilled meat.',
    'F-WHITE-WINE': 'Low in alcohol, high in freshness, with a slight prickle. Serve ice cold with fish.',
    'F-VERMOUTH': 'Made on a white wine base with twenty botanicals. Keep it in the fridge once open.',
    'F-OIL-VINEGAR-SET': 'The two bottles our kitchen reaches for most, in a wooden box. A gift that gets used.',
    'F-BALSAMIC': 'Aged in oak, chestnut and cherry casks. Use it drop by drop on cheese, strawberries or a steak.',
    'F-BREAKFAST-BOX': 'Everything for a slow Sunday morning, packed the night before it ships. The crate is a nice thing to keep.',
    'F-CHEESE-BOX': 'Four cheeses and a jam that suits them all, with tasting notes. Serves six as a course.',
    'F-APERITIVO-BOX': 'The hour before dinner, in a box. Serve the vermouth on ice with an orange peel.',
    'F-TARALLI': 'Baked twice, so they stay crunchy for weeks. A 250 g bag.',
    'F-ALMONDS': 'Flat, sweet almonds from Spain, fried and salted lightly. A 200 g bag.',
    'F-DARK-CHOC': 'A 70 g bar with a clean snap and a long finish. Stone ground, so the texture is slightly rough.',
    'F-GRANOLA': 'A 500 g bag with real clusters and not too much sugar. Pecans in every handful.',
}
GALLERY = [('A market stall piled with heirloom tomatoes, peaches and bunches of basil under a striped awning', 'pantry'), ('A baker pulling a tray of sourdough loaves from a wood-fired oven', 'bakery'), ('A tall shot of a cheese cave with wheels of cheese stacked on wooden shelves', 'cheese-charcuterie'), ('A pour-over coffee being brewed on a wooden counter, steam rising', 'coffee-tea'), ('A long outdoor table set for lunch under an olive tree with bread, wine and bowls of pasta', 'gift-boxes')]
BRANDS = [('Coratina', 'OLIVE OIL'), ('Molino Rossi', 'PASTA'), ('Alder Dairy', 'CHEESE'), ('Cinder', 'COFFEE ROASTERS'), ('Hedgerow', 'PRESERVES'), ('Stone Oven', 'BAKERY'), ('Mar Salt', 'SEA SALT'), ('Casa Fina', 'CHARCUTERIE'), ('Bramble', 'SODA'), ('Tarn', 'TEA')]
GALLERY_TITLE = 'From the table'
