CODE = 'jewelry'; ROOT = 'Jewelry'; STORE_NAME = 'Aurelie'; ATTRIBUTE_SET = 'Jewelry'; WEIGHT = 0.1
ATTRIBUTE_COLUMNS = ['material', 'stone', 'size', 'color']
ATTRIBUTES = [
    dict(code='stone', label='Stone', input='select', scope='global', filterable=1, filterable_in_search=1, visible_on_front=1, comparable=1, sets='Jewelry', group='General', sort_order=50),
]
OPTIONS = {'stone': ['None', 'Diamond', 'Pearl', 'Sapphire', 'Emerald', 'Moonstone', 'Onyx', 'Topaz'], 'material': ['Gold plated', 'Sterling silver', '14k gold', 'Rose gold', 'Stainless steel']}
ROOT_DESCRIPTION = 'Fine and everyday jewelry, made in a small workshop from recycled metals.'
META_DESCRIPTION = 'Aurelie: rings, necklaces, earrings and bracelets in recycled gold and silver, made to order in our workshop.'
PRODUCT_STYLE = 'Macro studio product photograph of a single piece of jewelry on a plain white seamless background, soft diffused light, subtle reflection, no hands, no text, no logos, no watermark, centered with margin around it.'
SCENE_STYLE = 'Luxurious editorial jewelry photograph, dark velvet and marble surfaces, warm low light with soft highlights, shallow depth of field, no text, no lettering, no logos, no watermark.'
SCENES = {
    'hero-main': 'A womans hand resting on dark green velvet wearing a thin gold ring and a pearl bracelet, warm side light.',
    'hero-side': 'A close up of a gold chain necklace with a small pearl pendant on black marble.',
    'editorial': 'A goldsmith at a bench polishing a ring under a lamp, tools laid out, seen from the side.',
    'about': 'A small jewelry workshop with a bench, a magnifier lamp and trays of loose stones.',
}
CATEGORIES = [
    dict(path='rings', name='Rings', description='Bands, stacking rings and stones set by hand.', landing_title='Worn every day', landing_text='Bands and stacking rings in recycled gold and silver, sized to you and made to be worn, not kept.', scene='Three thin gold rings stacked on a dark velvet ring cushion.'),
    dict(path='necklaces', name='Necklaces', description='Chains, pendants and pearls for every neckline.', landing_title='The one you never take off', landing_text='Fine chains, small pendants and a strand of pearls. Layer them or wear one for a year.', scene='A thin gold chain with a small pendant laid on black marble beside a pearl strand.'),
    dict(path='earrings', name='Earrings', description='Hoops, studs and drops, light enough for all day.', landing_title='Light enough to forget', landing_text='Small hoops, tiny studs and a few drops for evenings. All under three grams.', scene='A pair of gold hoop earrings and pearl studs on a dark velvet tray.'),
    dict(path='bracelets', name='Bracelets', description='Chains, cuffs and cords for one wrist or a stack.', landing_title='For the wrist', landing_text='Slim chains, a hammered cuff and silk cords with a single stone.', scene='A gold cuff and a thin chain bracelet on a marble surface with soft shadows.'),
    dict(path='engagement', name='Engagement', description='Solitaires and vintage-style settings, made to order.', landing_title='Made for one person', landing_text='Solitaires, halos and vintage settings, made to order in six weeks with stones you choose.', scene='A solitaire diamond ring in an open dark green ring box on marble.'),
    dict(path='gifts', name='Gifts', description='Sets and small pieces, boxed and ready.', landing_title='Small and boxed', landing_text='Matching sets and small pieces under a hundred, in a linen box with a handwritten card.', scene='A small linen gift box with a gold necklace inside, tied with a silk ribbon on marble.'),
]
HERO = dict(badge='Made to order', title='Small pieces, made slowly', text='Recycled gold and silver, stones we can trace, and a workshop where every piece is finished by hand.')
FEATURES = [('recycle', 'Recycled metals', 'Every piece, every time'), ('ruler', 'Free resizing', 'Within a year of purchase'), ('gift', 'Gift boxed', 'Linen box, handwritten card'), ('shield-check', 'Lifetime repair', 'Bring it back, we fix it')]
STORY = dict(title='A bench, not a factory', text1='Aurelie is three goldsmiths and a bench. Every piece is cast from recycled metal, set and polished by hand, and signed on the inside.', text2='If it breaks, we fix it. If it no longer fits, we resize it. Jewelry should last longer than a season.')
PROMO = dict(badge='New', title='The pearl edit', text='Freshwater pearls on gold chain, in five pieces that work together.', path='necklaces', button='See the edit', list_title='From the pearl edit')
TESTIMONIALS = [('The ring came in a linen box with a note from the goldsmith who made it. It fits perfectly.', 'Elena R.', 'Lyon'), ('Resized my grandmothers ring for free, a year after I bought mine from them.', 'Marcus T.', 'Leeds'), ('Small hoops I have not taken off in six months. Still bright.', 'Priya S.', 'Toronto')]
NEWSLETTER = dict(title='From the bench', text='A note every month: new pieces, workshop days and the occasional sample sale.')
ABOUT = dict(title='Three goldsmiths and a bench', paragraphs=['Aurelie began at a shared bench in a jewelry quarter. Three of us, one polishing motor, and a promise to use only recycled metal.', 'Every piece is cast, set and finished by hand. The stones come from two cutters we know, and every one can be traced.', 'The workshop is open on Fridays. Come and watch your ring being made.'])
REVIEWS = [
    ('Delicate and well made', 'Finer than the photos suggest, in a good way. The finish is flawless.', 5),
    ('Lovely, a little small', 'Beautiful piece. The pendant is smaller than I expected, so check the size.', 4),
    ('Worn every day', 'Six months in, no tarnish, no loose stone.', 5),
    ('Perfect gift', 'The box and the handwritten card made it. She cried.', 5),
    ('Clasp is secure', 'Lobster clasp with a proper spring. Never opened by itself.', 5),
    ('Resized for free', 'Half a size out. Sent back, resized, returned within a week.', 5),
    ('Catches the light', 'The stone sparkles under office lights. Colleagues noticed.', 5),
    ('Chain is fine', 'Beautiful but very fine. I take it off for the gym.', 4),
    ('Stacks well', 'Three thin rings, worn together. That was the plan and it works.', 5),
    ('Earring back is tiny', 'Lovely hoops but the backs are small and easy to drop.', 3),
    ('Solid gold, not plated', 'You can feel the weight. Worth every penny.', 5),
    ('Slight scratch on the band', 'Hairline mark out of the box. Polished it out myself.', 4),
    ('Pearls are matched', 'Same size, same lustre, well knotted between each.', 5),
    ('Fits the wrist', 'Cuff opens just enough. Stays put all day.', 5),
    ('Ring box is lovely', 'The linen box is a keepsake on its own.', 5),
    ('Wanted it bigger', 'Beautiful stone, smaller than the photo led me to expect.', 4),
    ('No green finger', 'A month of daily wear, no mark on the skin.', 5),
    ('Engraving is crisp', 'Two initials and a date, clean and even.', 5),
    ('Bought a second for my sister', 'She saw mine and now we match.', 5),
    ('Post is short', 'Stud sits close to the ear, which I like. Bigger lobes may want longer posts.', 4),
    ('Came with a cloth', 'Polishing cloth and care notes in the box. Thoughtful.', 5),
    ('Priced fairly', 'Compared four shops. This was the best value for the weight.', 5),
    ('Took three weeks', 'Made to order. The wait was stated, and it was worth it.', 4),
    ('Stone is set low', 'Does not catch on jumpers. A ring you can wear every day.', 5),
]
def P(sku, name, cats, price, desc, prompt, **kw):
    d = dict(sku=sku, name=name, categories=cats, price=price, description=desc, prompt=prompt); d.update(kw); return d
RING = ['48', '50', '52', '54', '56', '58']
PRODUCTS = [
    P('J-BAND-THIN', 'Thin band', ['rings'], 120, 'A 1.5 mm round band in recycled gold, the one you stack or wear alone.', 'a thin polished gold band ring', axis='size', values=RING, attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-BAND-HAMMER', 'Hammered band', ['rings'], 95, 'A 3 mm band with a hand-hammered face in sterling silver.', 'a hammered sterling silver band ring', axis='size', values=RING, attributes=dict(material='Sterling silver', stone='None', color='Silver')),
    P('J-SIGNET', 'Oval signet ring', ['rings'], 180, 'A small oval signet in recycled gold, plain for engraving.', 'a small oval gold signet ring', axis='size', values=RING, attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-MOONSTONE-RING', 'Moonstone ring', ['rings'], 140, 'A rainbow moonstone in a low bezel on a thin gold band.', 'a thin gold ring with a round white moonstone in a bezel setting', axis='size', values=RING, attributes=dict(material='14k gold', stone='Moonstone', color='Yellow')),
    P('J-SAPPHIRE-RING', 'Sapphire stacking ring', ['rings'], 220, 'Three tiny blue sapphires set flush in a slim gold band.', 'a slim gold ring with three tiny blue sapphires', axis='size', values=RING, attributes=dict(material='14k gold', stone='Sapphire', color='Yellow')),
    P('J-ONYX-RING', 'Onyx dome ring', ['rings'], 110, 'A black onyx cabochon in a silver dome setting.', 'a sterling silver ring with a black onyx cabochon', axis='size', values=RING, attributes=dict(material='Sterling silver', stone='Onyx', color='Silver')),
    P('J-TWIST-RING', 'Twist ring', ['rings'], 130, 'Two thin bands twisted into one, in rose gold.', 'a twisted rose gold ring', axis='size', values=RING, attributes=dict(material='Rose gold', stone='None', color='Pink')),
    P('J-CHAIN-FINE', 'Fine cable chain', ['necklaces'], 150, 'A 45 cm fine cable chain in recycled gold, the base for every pendant.', 'a fine gold cable chain necklace coiled on white', attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-PEARL-PENDANT', 'Single pearl pendant', ['necklaces', 'gifts'], 130, 'One freshwater pearl on a fine gold chain.', 'a fine gold chain with a single white pearl pendant', attributes=dict(material='Gold plated', stone='Pearl', color='Yellow')),
    P('J-PEARL-STRAND', 'Freshwater pearl strand', ['necklaces'], 260, 'A 42 cm strand of baroque freshwater pearls, knotted by hand.', 'a strand of baroque freshwater pearls with a gold clasp', attributes=dict(material='Gold plated', stone='Pearl', color='White')),
    P('J-DISC-PENDANT', 'Disc pendant', ['necklaces'], 140, 'A hammered 12 mm disc on a fine chain, plain for an initial.', 'a fine gold chain with a small hammered gold disc pendant', attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-BAR-NECK', 'Bar necklace', ['necklaces'], 120, 'A slim horizontal bar in sterling silver on a 45 cm chain.', 'a silver chain necklace with a slim horizontal bar pendant', attributes=dict(material='Sterling silver', stone='None', color='Silver')),
    P('J-EMERALD-PENDANT', 'Emerald drop pendant', ['necklaces'], 340, 'A small pear-cut emerald in a gold bezel on a fine chain.', 'a fine gold chain with a small green emerald drop pendant', attributes=dict(material='14k gold', stone='Emerald', color='Green')),
    P('J-CURB-CHAIN', 'Curb chain', ['necklaces'], 190, 'A 50 cm curb chain in sterling silver with a lobster clasp.', 'a sterling silver curb chain necklace', attributes=dict(material='Sterling silver', stone='None', color='Silver')),
    P('J-LAYER-SET', 'Layering set', ['necklaces', 'gifts'], 250, 'The fine chain, the disc pendant and the pearl pendant, at three lengths.', 'three layered fine gold necklaces with a disc and a pearl pendant', grouped=['J-CHAIN-FINE', 'J-DISC-PENDANT', 'J-PEARL-PENDANT'], attributes=dict(material='14k gold', stone='Pearl', color='Yellow')),
    P('J-HOOP-SMALL', 'Small hoops', ['earrings'], 90, 'A 12 mm hoop in recycled gold with a hinged closure.', 'a pair of small polished {value} hoop earrings', axis='color', values=['Yellow', 'Silver', 'Pink'], picture_per_value=True, attributes=dict(material='14k gold', stone='None')),
    P('J-HOOP-LARGE', 'Large hoops', ['earrings'], 140, 'A 30 mm hollow hoop, light enough for all day.', 'a pair of large thin gold hoop earrings', attributes=dict(material='Gold plated', stone='None', color='Yellow')),
    P('J-PEARL-STUD', 'Pearl studs', ['earrings', 'gifts'], 80, 'Six millimetre freshwater pearls on gold posts.', 'a pair of white pearl stud earrings on gold posts', attributes=dict(material='Gold plated', stone='Pearl', color='White')),
    P('J-DOT-STUD', 'Dot studs', ['earrings'], 60, 'A 3 mm polished dot, the smallest stud we make.', 'a pair of tiny polished gold dot stud earrings', attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-DIAMOND-STUD', 'Diamond studs', ['earrings', 'engagement'], 420, 'Two 0.15 carat diamonds in a four-claw setting.', 'a pair of small diamond stud earrings in gold claw settings', attributes=dict(material='14k gold', stone='Diamond', color='Yellow')),
    P('J-DROP-TOPAZ', 'Topaz drops', ['earrings'], 160, 'Pear-cut blue topaz on short gold hooks.', 'a pair of blue topaz drop earrings on gold hooks', attributes=dict(material='14k gold', stone='Topaz', color='Blue')),
    P('J-THREADER', 'Chain threaders', ['earrings'], 110, 'A 7 cm chain that threads through the ear and hangs free.', 'a pair of thin gold chain threader earrings', attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-CUFF-HAMMER', 'Hammered cuff', ['bracelets'], 170, 'An open cuff with a hammered face in sterling silver.', 'a hammered sterling silver open cuff bracelet', attributes=dict(material='Sterling silver', stone='None', color='Silver')),
    P('J-CHAIN-BRACELET', 'Fine chain bracelet', ['bracelets', 'gifts'], 95, 'A 17 cm fine chain with a 2 cm extender.', 'a fine gold chain bracelet', attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-PEARL-BRACELET', 'Pearl bracelet', ['bracelets'], 140, 'Small freshwater pearls on gold wire, with a toggle clasp.', 'a freshwater pearl bracelet with a gold toggle clasp', attributes=dict(material='Gold plated', stone='Pearl', color='White')),
    P('J-CORD-BRACELET', 'Silk cord bracelet', ['bracelets', 'gifts'], 55, 'A {value} silk cord with a single gold bead, adjustable.', 'a {value} silk cord bracelet with a single gold bead', axis='color', values=['Red', 'Blue Dark', 'Green'], picture_per_value=True, attributes=dict(material='Gold plated', stone='None')),
    P('J-BANGLE', 'Round bangle', ['bracelets'], 210, 'A solid 3 mm round bangle in recycled gold.', 'a thin solid gold round bangle', attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-ID-BRACELET', 'ID bracelet', ['bracelets'], 160, 'A curb chain with a plain plate for engraving, in silver.', 'a sterling silver curb chain ID bracelet with a plain plate', attributes=dict(material='Sterling silver', stone='None', color='Silver')),
    P('J-SOLITAIRE', 'Classic solitaire', ['engagement'], 1900, 'A 0.5 carat round diamond in a six-claw setting on a slim gold band.', 'a classic round diamond solitaire ring in gold', axis='size', values=RING, attributes=dict(material='14k gold', stone='Diamond', color='Yellow')),
    P('J-HALO', 'Halo ring', ['engagement'], 2400, 'A 0.4 carat centre stone with a halo of small diamonds.', 'a diamond halo engagement ring in white gold', axis='size', values=RING, attributes=dict(material='14k gold', stone='Diamond', color='Silver')),
    P('J-SAPPHIRE-SOL', 'Sapphire solitaire', ['engagement'], 1500, 'An oval blue sapphire in a bezel on a rose gold band.', 'an oval blue sapphire ring in a rose gold bezel', axis='size', values=RING, attributes=dict(material='Rose gold', stone='Sapphire', color='Pink')),
    P('J-VINTAGE', 'Vintage cluster', ['engagement'], 2100, 'A daisy cluster of seven small diamonds in a vintage setting.', 'a vintage style diamond daisy cluster ring in gold', axis='size', values=RING, attributes=dict(material='14k gold', stone='Diamond', color='Yellow')),
    P('J-WEDDING-BAND', 'Court wedding band', ['engagement', 'rings'], 380, 'A 2.5 mm court-profile band in recycled gold.', 'a plain polished gold court wedding band', axis='size', values=RING, attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-ETERNITY', 'Half eternity ring', ['engagement'], 980, 'Seven diamonds set half way round a slim band.', 'a slim gold half eternity ring set with small diamonds', axis='size', values=RING, attributes=dict(material='14k gold', stone='Diamond', color='Yellow')),
    P('J-PEARL-SET', 'Pearl gift set', ['gifts'], 190, 'The pearl studs and the pearl pendant, boxed together.', 'pearl stud earrings and a pearl pendant necklace in a linen gift box', grouped=['J-PEARL-STUD', 'J-PEARL-PENDANT'], attributes=dict(material='Gold plated', stone='Pearl', color='White')),
    P('J-STACK-SET', 'Stacking set', ['gifts', 'rings'], 300, 'The thin band, the hammered band and the twist ring in one size.', 'three stacked rings in gold, silver and rose gold on white', grouped=['J-BAND-THIN-52', 'J-BAND-HAMMER-52', 'J-TWIST-RING-52'], attributes=dict(material='14k gold', stone='None', color='Yellow')),
    P('J-RING-BOX', 'Linen ring box', ['gifts'], 18, 'A small linen box with a velvet slot, for the ring you already own.', 'a small natural linen ring box open with a velvet slot', attributes=dict(material='', stone='None', color='Oatmeal')),
    P('J-POLISH-CLOTH', 'Polishing cloth', ['gifts'], 8, 'A two-layer cloth that brings silver and gold back in a minute.', 'a folded grey jewelry polishing cloth', attributes=dict(material='', stone='None', color='Grey')),
    P('J-JEWELRY-DISH', 'Ceramic ring dish', ['gifts'], 22, 'A small hand-thrown dish for the bedside.', 'a small white ceramic ring dish with a gold rim', attributes=dict(material='', stone='None', color='White')),
    P('J-GIFT-CARD', 'Aurelie gift card', ['gifts'], 100, 'A gift card in a linen envelope, for a piece they choose.', 'a cream gift card in a linen envelope with a gold seal', type='virtual', attributes=dict(material='', stone='None', color='')),
]
POSTS = [
    ('How to find your ring size', '<p>Wrap a strip of paper around the base of the finger, mark where it meets, and measure the length in millimetres. That is your size on our chart. Measure in the evening, when fingers are largest, and never in the cold.</p><p>If you are between sizes, go up. We resize for free within a year anyway.</p>', 'A hand measuring a finger with a strip of paper next to a ruler on marble.'),
    ('Why recycled gold', '<p>Gold does not wear out. Every gram we cast was once something else: a chain, a coin, a ring that no longer fit. Refined, it is chemically identical to new gold and needs no mine.</p><p>The price is the same. The story is better.</p>', 'Gold grain and small gold ingots on a dark workbench under a lamp.'),
    ('Caring for pearls', '<p>Pearls are soft. Put them on last, after perfume and hairspray, and take them off first. Wipe them with a soft cloth and let them breathe outside the box now and then.</p><p>Restring a strand every few years if you wear it often. We do it in a week.</p>', 'A strand of pearls on a soft cloth beside a small glass bottle of perfume on marble.'),
]
MORE = {
    'J-BAND-THIN': 'Made from recycled 14 karat gold and polished by hand. Available in sizes from 46 to 62.',
    'J-BAND-HAMMER': 'Each band is hammered by hand, so the pattern is never the same twice. Sterling silver, sizes 48 to 64.',
    'J-SIGNET': 'The oval face is 9 by 7 mm, ready for one or two initials. Engraving is free and takes three days.',
    'J-MOONSTONE-RING': 'The stone shows a blue flash in daylight. Set in 14 karat recycled gold.',
    'J-SAPPHIRE-RING': 'The stones sit flush with the band, so nothing catches. 14 karat recycled gold.',
    'J-ONYX-RING': 'The cabochon is 10 mm across and the dome sits low on the finger. Sterling silver.',
    'J-TWIST-RING': 'Two 1.2 mm bands in 14 karat rose gold, soldered at the twist. Comfortable on its own or in a stack.',
    'J-CHAIN-FINE': 'A 1 mm cable chain with a spring clasp, in 14 karat recycled gold. Strong enough for a small pendant.',
    'J-PEARL-PENDANT': 'A 7 mm round freshwater pearl on a 45 cm chain. Gold filled, so the colour lasts.',
    'J-PEARL-STRAND': 'Each pearl is knotted on silk, so a break loses one pearl, not the strand. The clasp is a gold filled hook.',
    'J-DISC-PENDANT': 'The disc is 14 karat gold on a 45 cm chain. One initial is engraved free.',
    'J-BAR-NECK': 'The bar is 30 mm long and 2 mm wide, polished on the front. Engraving is free.',
    'J-EMERALD-PENDANT': 'The emerald is about 0.3 carat, set in 14 karat gold on a 42 cm chain. Each stone is a little different.',
    'J-CURB-CHAIN': 'A 4 mm curb link, solid sterling silver, with a substantial lobster clasp. Wear it alone.',
    'J-LAYER-SET': 'Three necklaces at 40, 45 and 50 cm so they sit apart. Cheaper than the three bought separately.',
    'J-HOOP-SMALL': 'A 1.5 mm wire with a hinge that clicks shut. 14 karat recycled gold, sold as a pair.',
    'J-HOOP-LARGE': 'A 3 mm hollow tube, so each hoop weighs under two grams. 14 karat gold, sold as a pair.',
    'J-PEARL-STUD': 'Round, white, matched pearls on 14 karat gold posts with butterfly backs. Sold as a pair.',
    'J-DOT-STUD': 'A polished sphere on a post, in 14 karat gold. For a second piercing or a first.',
    'J-DIAMOND-STUD': 'Round brilliant diamonds, G colour, VS clarity, in 14 karat gold. Sold as a pair with a certificate.',
    'J-DROP-TOPAZ': 'Eight millimetre pear cuts on 14 karat gold hooks. They swing when you turn your head.',
    'J-THREADER': 'A fine cable chain with a short bar that passes through the ear. 14 karat gold, sold as a pair.',
    'J-CUFF-HAMMER': 'A 10 mm wide cuff that bends gently to fit. Sterling silver, one size.',
    'J-CHAIN-BRACELET': 'A 1 mm cable chain in 14 karat gold with a spring clasp. Fits wrists from 15 to 19 cm.',
    'J-PEARL-BRACELET': 'Five millimetre pearls on 14 karat gold wire, with a toggle you can close with one hand. 18 cm.',
    'J-CORD-BRACELET': 'A slider knot adjusts it to any wrist. The bead is 14 karat gold.',
    'J-BANGLE': 'Solid 14 karat recycled gold, 65 mm inside. It slides over the hand.',
    'J-ID-BRACELET': 'A 4 mm curb chain with a 30 mm plate, in sterling silver. Engraving is free and takes three days.',
    'J-SOLITAIRE': 'A round brilliant diamond, G colour, VS clarity, with a certificate. Made in 14 or 18 karat gold, in your size.',
    'J-HALO': 'The halo makes the centre stone look larger without adding height. 14 or 18 karat gold, in your size.',
    'J-SAPPHIRE-SOL': 'A 7 by 5 mm oval sapphire in a bezel that protects the stone. 14 karat rose gold, in your size.',
    'J-VINTAGE': 'Seven small diamonds in a milgrain setting, about 0.35 carat in total. 14 karat gold, in your size.',
    'J-WEDDING-BAND': 'Rounded inside and out, so it sits easily on the finger. 14 or 18 karat gold, in your size.',
    'J-ETERNITY': 'Seven round diamonds, about 0.25 carat in total, set in 14 karat gold. It stacks against a solitaire.',
    'J-PEARL-SET': 'The studs and the pendant in one linen box, with a card. Cheaper than the two bought separately.',
    'J-STACK-SET': 'Three rings that were designed to sit together. Cheaper than the three bought separately.',
    'J-RING-BOX': 'Linen outside, velvet inside, 5 cm square. Made for a proposal or a bedside.',
    'J-POLISH-CLOTH': 'One layer cleans and one layer shines. It works for years without washing.',
    'J-JEWELRY-DISH': 'A 9 cm stoneware dish with a matte glaze. A safe place for rings at night.',
    'J-GIFT-CARD': 'A paper card in a linen envelope, posted the same day. Any amount, valid for a year.',
}
