all_prompt_prefix = {
    'pony': "score_9, score_8_up, score_7_up, BREAK",
    'sdxl': "masterpiece"
}

neg_prompt_prefix = {
    'pony': "score_4, score_5, score_6, BREAK, headband, text, logo, watermark, bad hands, bad feet",
    'sdxl': "headband, poorly rendered face, low quality, worst quality, 3d, cgi, rendered, text, logo, watermark, bad hands, bad feet"
}

all_style = {
    'anime': "source_anime, anime, 2d",
    '2.5d': "2.5D, semi-realistic, cinematic",
    'real': "photograph, realistic"
}

all_hair_color = {
    "blond": {
        "platinum blond",
        "ash blond",
        "golden blond",
        "bleach blond",
        "beige blond",
        "dirty blond",
        "ice blond"
        },
    "brown": {
        "light brown",
        "ash brown",
        "golden brown",
        "chestnut brown",
        "espresso brown",
        "mocha brown"
        },
    "red": {
        "light auburn",
        "dark auburn",
        "copper red",
        "ginger",
        "titian red",
        "mahogany",
        "cascading ginger",
        "crimson",
        "bright red",
        "burgundy",
        "ruby red"
        },
    "black": {
        "jet black",
        "soft black",
        "blue-black",
        "natural black",
        "raven",
        "velvet black"
        },
    "white": {
        "white",
        "silver gray",
        "salt and pepper",
        "steel gray",
        "white gray",
        "platinum silver"
        },
    "dyed": {
        "pastel pink",
        "pastel blue",
        "lilac",
        "peach",
        "mint green",
        "teal",
        "neon yellow",
        "electric blue",
        "vibrant purple"
        "coral",
        "silver metallic",
        "bronze metallic",
        "ombre",
        "rainbow",
        "pastel pink",
        "lavender",
        "sky blue",
        "seafoam green"
        }
}

all_bust_size = {
    "small": [
        "flat chest",
        "tiny breasts",
        "small breasts",
        "perky breasts",
        "petite breasts"
    ],
    "medium": [
        "modest breasts",
        "moderate breasts",
        "medium breasts",
        "natural breasts",
        "round breasts",
        "bouncy breasts"
    ],
    "large": [
        "busty",
        "swollen breasts",
        "large breasts",
        "huge breasts",
        "massive breasts",
        "((gigantic breasts))",
        "pillowy breasts"
    ]
}

all_act = {
    "solo": [
        "posing",
        "yoga, downward facing dog",
        "yoga, human crane",
        "cooking",
        "spider pose, table pose, stretching, flexible",
        "standing, spreading vagina",
        "lounging, spreading vagina",
        "female masturbation",
        "female masturbation, anal",
        "dildo, vaginal insertion",
        "dildo, anal insertion",
        "dildo, large insertion",
        "squatting on dildo, vaginal insertion",
        "squatting on dildo, anal insertion",
        "vibrator",
        "pillow humping",
        "table humping",
        "female masturbation, crotch rub",
        "self-sucking, licking vagina",
        "self-sucking, licking cock"
    ],

    "vanilla": [
        "missionary sex, vaginal sex",
        "cowgirl sex, vaginal sex",
        "reverse cowgirl sex, vaginal sex",
        "doggystyle sex, on all fours, vaginal sex",
        "lotus sex, vaginal sex",
        "standing sex, vaginal sex",
        "missionary sex, anal sex",
        "cowgirl sex, anal sex",
        "reverse cowgirl sex, anal sex",
        "doggystyle sex, on all fours, anal sex",
        "lotus sex, anal sex",
        "standing sex, anal sex",
        "missionary sex, pov, vaginal sex",
        "cowgirl sex, pov, vaginal sex",
        "reverse cowgirl sex, pov, vaginal sex",
        "missionary sex, pov, anal sex",
        "cowgirl sex, pov, anal sex",
        "reverse cowgirl sex, pov, anal sex",
        "mutual masturbation",
        "thigh sex"
    ],

    "bdsm": [
        "missionary sex, (choking), vaginal sex",
        "missionary sex, (choking), anal sex",
        "cowgirl sex, vaginal sex, bondage",
        "reverse cowgirl sex, vaginal sex, bondage",
        "doggystyle sex, on all fours, vaginal sex, bondage",
        "lotus sex, vaginal sex, bondage",
        "standing sex, vaginal sex, bondage",
        "missionary sex, anal sex, bondage",
        "cowgirl sex, anal sex, bondage",
        "reverse cowgirl sex, anal sex, bondage",
        "doggystyle sex, on all fours, anal sex, bondage",
        "lotus sex, anal sex, bondage",
        "standing sex, anal sex, bondage",
        "missionary sex, pov, bondage",
        "cowgirl sex, pov, bondage",
        "reverse cowgirl sex, pov, bondage",
        "fucking machine",
        "vaginal sex, bdsm, bound arms",
        "anal sex, bdsm, bound arms",
        "vaginal sex, bdsm, bound breasts",
        "anal sex, bdsm, bound breasts",
        "vaginal sex, bdsm, bound legs",
        "anal sex, bdsm, bound legs",
        "vaginal sex, bdsm, bound legs, bound arms",
        "anal sex, bdsm, bound legs, bound arms",
        "vaginal sex, bdsm, hogtie",
        "anal sex, bdsm, hogtie",
    ],

    "oral": [
        "blowjob, gentle",
        "blowjob, licking",
        "blowjob, biting",
        "blowjob, biting, blood",
        "blowjob, deepthroat",
        "blowjob, throat fucking",
        "blowjob, skullfuck, irrumatio",
        "blowjob, female masturbation",
        "blowjob, gagging",
        "facesitting",
        "facesitting, pissing",
        "facesitting, domination",
        "rimming",
        "ball licking"
    ],

    "touching": [
        "handjob",
        "handjob, caressing testicles",
        "handjob, nursing handjob",
        "handjob, cuddling handjob",
        "handjob, reach-around",
        "handjob, two-handed handjob",
        "handjob, female masturbation",
        "titjob",
        "titjob, licking",
        "armpit sex",
        "fingering, anal",
        "fingering, vaginal",
        "fingering, anal, pov",
        "fingering, vaginal, pov"
    ],

    "feet": [
        "(footjob), side view, (five toes)",
        "(footjob), visible vagina, (five toes)",
        "(footjob), stepping on, (five toes)",
        "(footjob), domination, (five toes)",
        "(footjob), domination, (five toes), ball crushing",
        "(footjob), pov, (five toes)",
        "(footjob), pov, visible vagina, (five toes)",
        "(footjob), pov, stepping on, (five toes)",
        "(footjob), pov, domination, (five toes)",
        "(footjob), pov, domination, (five toes), ball crushing",
        "missionary sex, vaginal sex, legs up, feet",
        "missionary sex, anal sex, legs up, feet",
        "(footjob), foot worship",
        "foot worship, toe sucking",
        "(footjob), pov, foot worship",
        "foot worship, pov, toe sucking"
    ],

    "lesbian": [
        "fingering, lesbian",
        "vaginal fingering",
        "anal fingering",
        "(strap-on), missionary sex, vaginal sex",
        "(strap-on), cowgirl sex, vaginal sex",
        "(strap-on), doggystyle sex, vaginal sex",
        "(strap-on), standing sex, vaginal sex",
        "(strap-on), missionary sex, anal sex",
        "(strap-on), cowgirl sex, anal sex",
        "(strap-on), doggystyle sex, anal sex",
        "(strap-on), standing sex, anal sex",
        "(strap-on), missionary sex, bondage",
        "(strap-on), cowgirl sex, bondage",
        "(strap-on), doggystyle sex, bondage",
        "(strap-on), standing sex, bondage",
        "(strap-on), blowjob"
    ],

    "extreme": [
        "cervical penetration",
        "vaginal insertion, dildo, belly bulge",
        "anal insertion, dildo, belly bulge",
        "enema",
        "urethral insertion, sounding",
        "(fisting), vaginal fisting",
        "(fisting), anal fisting",
        "(fisting), self fisting, vaginal fisting",
        "(fisting), self, fisting, anal fisting",
        "tentacle monster, tentacle sex",
        "vines, tentacle sex",
        "asphyxiation, strangling",
        "defloration, blood",
        "anal beads",
        "double penetration",
        "double penetration, bondage",
        "macrophilia, giantess, stepping on",
        "netorare, cuckolding, vaginal sex",
        "netorare, cuckolding, anal sex",
        "netorare, cuckolding, vaginal sex, bondage",
        "netorare, cuckolding, anal sex, bondage"
    ]
}

all_hair_style = {
    "short": [
        "buzz cut",
        "short hair, bob cut",
        "short hair, pixie cut",
        "short hair, layered pixie cut",
        "short hair, undercut pixie cut",
        "short hair, blunt cut",
        "short hair, a-line bob",
        "short hair, pageboy cut",
        "short hair, undone crop",
        "short hair, bowl cut"
    ],
    "long": [
        "long hair, straight and sleek cut",
        "long hair, layered cut",
        "long hair, feathered hair",
        "long hair, curtain bangs with long hair",
        "long hair, mermaid hair"
    ],
    "curly": [
        "curly hair, natural curls",
        "curly hair, ringlets",
        "curly hair, curly bob",
        "curly hair, short afro",
        "curly hair, afro",
        "curly hair, waterfall curls"
    ],
    "braided": [
        "braided hair, french braid",
        "braided hair, dutch braid",
        "braided hair, fishtail braid",
        "braided hair, crown braid",
        "braided hair, box braid",
        "braided hair, halo braid"
    ],
    "updo": [
        "updo hair, classic bun",
        "updo hair, messy bun",
        "updo hair, chignon",
        "updo hair, french twist",
        "updo hair, top knot",
        "updo hair, gibson tuck",
        "updo hair, geisha updo",
        "updo hair, space buns",
        "half-up half-down hair, half-up bun",
        "half-up half-down hair, twisted half-up",
        "half-up half-down hair, braided crown half-up"
    ],
    "bangs": [
        "blunt bangs",
        "side-swept bangs",
        "wispy bangs",
        "curly bangs"
    ],
    "ponytail": [
        "high ponytail",
        "low ponytail",
        "bubble ponytail",
        "side ponytail",
        "pigtails",
        "voluminous ponytail",
        "sleek ponytail",
        "curly ponytail",
        "braided ponytail",
        "twisted ponytail",
        "knotted ponytail",
        "double ponytail"
    ]
}

all_addin = {
    "shape": [
        "slender, lanky",
        "athletic, fit",
        "petite, short",
        "petite, loli",
        "petite, waif",
        "hourglass figure, slender",
        "tall, lanky",
        "round face, adorable, cute",
        "amazonian, muscular",
        "plump, chubby",
        "plump, voluptuous"

    ],
    "skin": [
        "pale skin, ((freckles))",
        "olive skin",
        "dark skin",
        "tanned",
        "Asian",
        "Black",
        "European",
    ],
    "style": [
        "glasses, nerdy",
        "glasses, secretary, formal",
        "glasses, bookish, shy",
        "goth, makeup, plump",
        "emo, makeup, slender",
        "punk, piercings, fit",
        "tsundere, standoffish",
        "yandere, frantic, desperate",
        "gamer girl, distracted, slouching, looking down",
        "gamer girl, distracted, dismissive",
        "sporty, fit",
        "elegant, aloof, jewelry",
        "rebel, streetwear, casual, uncaring",
        "schoolgirl, studious",
        "schoolgirl, studious, glasses",
        "bollywood, henna, sequins, colorful",
        "futuristic, ultramodern, geometric",
        "victorian, intricate, elegant"
    ],
    "anthro": [
        "catgirl, cat ears, tail, (paws), claws",
        "doggirl, dog ears, tail, fangs, (paws), claws",
        "catgirl, cat ears, tail, (paws), claws, (fangs)",
        "doggirl, dog ears, tail, fangs, (paws), claws, (fangs)",
        "catgirl, cat ears, tail, (paws), claws, collar",
        "doggirl, dog ears, tail, fangs, (paws), claws, collar",
        "foxgirl, fox ears, tail",
        "deergirl, deer ears, spotted skin, hooves",
        "mousegirl, mouse ears, tail, paws, claws",
        "froggirl, slimy skin, webbed toes, webbed hands, green skin",
        "lizardgirl, scales, tail",
        "((spidergirl, arachne)), spider legs, (webbing)",
        "bunnygirl, bunny ears, (paws), fluffy tail"
    ],
    "furry": [
        "((furry), source_furry), catgirl, cat ears, tail, (paws), claws",
        "((furry), source_furry), doggirl, dog ears, tail, fangs, (paws), claws",
        "((furry), source_furry), catgirl, cat ears, tail, (paws), claws, (fangs)",
        "((furry), source_furry), doggirl, dog ears, tail, fangs, (paws), claws, (fangs)",
        "((furry), source_furry), catgirl, cat ears, tail, (paws), claws, collar",
        "((furry), source_furry), doggirl, dog ears, tail, fangs, (paws), claws, collar",
        "((furry), source_furry), foxgirl, fox ears, tail",
        "((furry), source_furry), deergirl, deer ears, spotted skin, hooves",
        "((furry), source_furry), mousegirl, mouse ears, tail, paws, claws",
        "((furry), source_furry), bunnygirl, bunny ears, (paws), fluffy tail"
    ],
    "fantasy": [
        "fairy, fairy wings, big eyes, adorable",
        "goblin, green skin, petite",
        "goblin, green skin, pointed ears",
        "elf, pointed ears",
        "gnome, short",
        "halfling, short",
        "dwarf, muscular, short",
        "orc, green skin, muscular, fangs",
        "succubus, horns, purple skin",
        "slimegirl, transparent skin",
        "imp, horns, red skin",
        "demon, horns, fiery",
        "golem, stone skin, moss",
        "minotaur, horns, muscular",
        "warforged, mechanical",
        "harpy, wings, feathers",
        "genasi, elemental",
        "vampire, red eyes, pale skin, fangs",
        "vampire, victorian, red eyes, pale skin, fangs",
        "werewolf, body hair",
        "witch, magic",
        "wizard, incantation",
        "very long tongue"
    ],
    "scifi": [
        "doll, cute, doll joints",
        "((alien)), (huge eyes)",
        "((alien)), huge eyes, blue skin",
        "((alien)), huge eyes, green skin",
        "((alien)), huge eyes, webbed feet, webbed hands",
        "cybernetic, android",
        "sexbot, android"
    ],
    "misc": [ 
        "swollen breasts, (pregnant)",
        "(puffy labia)",
        "pain, whip marks, bruises",
        "ball gag",
        "((tattoos), body art)",
        "sweaty, gleaning skin",
        "((big eyes)), adorable",
        "(hairy), pubic hair",
        "(hairy), armpit hair, pubic hair",
        "identical twins, incest, twincest",
        "squirting",
        "nipple clamps",
        "nipple vibrators",
        "clit vibrator",
        "nipple vibrators, clit vibrator"
    ]
}

all_loc = {
    "fantasy": [
        "fantasy, enchanted forest glade",
        "fantasy, midnight castle spire",
        "fantasy, glowing dragon lair",
        "fantasy, arcane mage tower",
        "fantasy, shimmering crystal cave",
        "fantasy, shispering willow grove",
        "fantasy, shadowed mountain pass",
        "fantasy, ancient runestone shrine",
        "fantasy, sparkling fairy pond",
        "fantasy, haunted misty swamp",
        "fantasy, eternal ice fortress",
        "fantasy, golden phoenix flight",
        "fantasy, forgotten kings tomb",
        "fantasy, roaring waterfall cavern",
        "fantasy, starry ocean horizon",
        "fantasy, hidden elven village",
        "fantasy, crimson battle plains",
        "fantasy, frozen time portal",
        "fantasy, glowing amber artifact",
        "fantasy, warlocks cursed keep",
        "fantasy, silent snowy forest",
        "fantasy, eternal sunlit valley",
        "fantasy, burning ember field",
        "fantasy, moonlit crystal arch",
        "fantasy, howling wind cliffs",
        "fantasy, magical healers sanctuary",
        "fantasy, stormy sea temple",
        "fantasy, starlit dragon nest",
        "fantasy, overgrown fairy-lit nook",
        "fantasy, obsidian tower ruins",
        "fantasy, dreamers tranquil grove",
        "fantasy, ethereal flame circle",
        "fantasy, wandering nomad caravan",
        "fantasy, endless enchanted desert",
        "fantasy, verdant jungle ruins",
        "fantasy, mystical library vault",
        "fantasy, winding fantasy staircase",
        "fantasy, sun-drenched floating island",
        "fantasy, hidden celestial city",
        "fantasy, gargoyle-guarded cathedral",
        "fantasy, wraith-infested battlefield",
        "fantasy, eldritch portal rift",
        "fantasy, sparkling aurora skies",
        "midnight-blue celestial chamber"
    ],
    "scifi": [
        "science-fiction, neon-lit cyber alley",
        "science-fiction, crystal asteroid field",
        "science-fiction, pulsing energy reactor",
        "science-fiction, bio-dome research facility",
        "science-fiction, gravity-defying sky city",
        "science-fiction, starship command bridge",
        "science-fiction, alien desert colony",
        "science-fiction, intergalactic trade hub",
        "science-fiction, abandoned moon outpost",
        "science-fiction, terraforming operations zone",
        "science-fiction, mech repair bay",
        "science-fiction, echoing metallic corridor",
        "science-fiction, cryogenic stasis chamber",
        "science-fiction, xenobiology research lab",
        "science-fiction, sentient ai sanctuary",
        "science-fiction, drone manufacturing hive",
        "science-fiction, subterranean alien ruins",
        "science-fiction, warp drive chamber",
        "science-fiction, suspended asteroid colony",
        "science-fiction, lunar mining base",
        "science-fiction, galactic emperors throneroom",
        "science-fiction, artificial star core",
        "science-fiction, deep-space scavenger ship",
        "science-fiction, nebula-fringed outpost",
        "science-fiction, molecular fabricator lab",
        "science-fiction, voidrunners asteroid hangar",
        "science-fiction, holographic leisure dome",
        "science-fiction, alien jungle hive",
        "science-fiction, nanotech innovation hub",
        "science-fiction, crystaline starport",
        "science-fiction, industrial shuttle dock",
        "science-fiction, rogue planetary prison",
        "science-fiction, futuristic drone city",
        "science-fiction, replicator assembly station",
        "starlit galaxy-themed dome",
        "evil lair",
        "steampunk airship",
    ],
    "contemporary": [
        "bustling urban plaza",
        "cozy coffee shop",
        "crowded subway station",
        "quiet suburban street",
        "trendy rooftop bar",
        "neon cityscape",
        "downtown art gallery",
        "beachfront luxury hotel",
        "vibrant farmers market",
        "secluded mountain cabin",
        "high-rise corporate office",
        "peaceful riverside park",
        "sleek modern museum",
        "nighttime jazz club",
        "deserted airport terminal",
        "quaint bookshop corner",
        "elegant theater district",
        "upscale shopping mall",
        "quiet library nook",
        "tree-lined university quad",
        "sunlit garden patio",
        "crowded food festival",
        "vibrant street mural",
        "coastal boardwalk promenade",
        "chic urban loft",
        "serene countryside cottage",
        "downtown fitness studio",
        "stylish city boutique",
        "rain-soaked alleyway",
        "trendy coworking space",
        "industrial warehouse loft",
        "hidden speakeasy bar",
        "modern art installation",
        "scenic lakeside trail",
        "neon-lit diner counter",
        "bustling tech campus",
        "contemporary open-air market",
        "local sports stadium",
        "oceanfront seafood restaurant",
        "small-town community center",
        "sun-dappled outdoor café",
        "urban graffiti alley",
        "quiet rooftop garden",
        "sleek urban transit hub",
        "upscale wine bistro",
        "sprawling urban park",
        "quaint city townhouse",
        "gleaming modern skyscraper",
        "tranquil yoga studio",
        "high-energy music festival",
        "hidden reading nook",
        "firelit cabin den",
        "secret garden hideaway",
        "candlelit attic room",
        "blanket-covered window seat",
        "moonlit rooftop retreat",
        "overgrown garden gazebo",
        "whispering forest clearing",
        "warm quilted armchair",
        "secluded treehouse perch",
        "tranquil lakeside dock",
        "tucked-away library alcove",
        "ivy-covered stone patio",
        "dimly-lit basement studio",
        "plush velvet sofa",
        "serene bedroom corner",
        "snow-dusted woodland hut",
        "padded bay window",
        "cozy kitchen corner",
        "hidden sunlit meadow",
        "rustic farmhouse loft",
        "shaded hammock retreat",
        "sheltered mountain overlook",
        "quiet riverside cottage",
        "overstuffed reading chair",
        "enclosed courtyard sanctuary",
        "frosty window fireplace",
        "secluded sandy cove",
        "warm log sauna",
        "private terrace garden",
        "shaded orchard hammock",
        "breezy ocean balcony",
        "rustic stone fireplace",
        "quiet journal hideaway",
        "morning-lit kitchen nook",
        "cozy art studio",
        "midnight stargazing perch",
        "canopy-covered forest path",
        "velvet-draped lounge alcove",
        "hidden blanket fort",
        "quaint countryside verandah",
        "sunset cabin porch",
        "dim-lit writing loft",
        "wood-paneled study corner",
        "candle-lit spiral stairwell",
        "tapestry-covered daybed alcove",
        "serene wildflower field",
        "candlelit attic sanctuary",
        "velvet-draped canopy bed",
        "rustic log cabin retreat",
        "skylit minimalist haven",
        "tranquil ocean-view suite",
        "warm quilted alcove",
        "tapestry-lined bohemian den",
        "frosty mountain-view loft",
        "sun-dappled morning haven",
        "dim-lit vintage parlor",
        "geometric modernist retreat",
        "sterile laboratory",
        "eerie pirate ship"
    ]
}

all_top = [
    "blouse",
    "frilled shirt",
    "sleeveless shirt",
    "bustier",
    "crop top",
    "camisole",
    "cardigan",
    "cardigan vest",
    "coat",
    "duffel coat",
    "fur coat",
    "fur-trimmed coat",
    "long coat",
    "overcoat",
    "peacoat",
    "raincoat",
    "yellow raincoat",
    "trench coat",
    "winter coat",
    "dress",
    "hoodie",
    "jacket",
    "blazer",
    "cropped jacket",
    "letterman jacket",
    "safari jacket",
    "suit jacket",
    "nightgown",
    "poncho",
    "robe",
    "thobe",
    "shirt",
    "collared shirt",
    "dress shirt",
    "off-shoulder shirt",
    "sleeveless shirt",
    "striped shirt",
    "t-shirt",
    "sweater",
    "turtleneck sweater",
    "sleeveless turtleneck",
    "sweater dress",
    "ribbed sweater",
    "aran sweater",
    "tailcoat",
    "tank top",
    "stringer",
    "tube top",
    "vest",
    "sweater vest",
    "waistcoat"
]

all_bottom = [
    "bloomers",
    "kilt",
    "pants",
    "bell-bottoms",
    "capri pants",
    "detached pants",
    "jeans",
    "cutoff jeans",
    "lowleg pants",
    "pants rolled up",
    "yoga pants",
    "shorts",
    "bike shorts",
    "denim shorts",
    "gym shorts",
    "shorts under skirt",
    "skirt",
    "bubble skirt",
    "high-waist skirt",
    "high-low skirt",
    "long skirt",
    "overall skirt",
    "overskirt",
    "plaid skirt",
    "pleated skirt",
    "tutu"
]

all_fit = {
    "medical scrubs",
    "lab coat",
    "surgical gown",
    "nurses dress",
    "lined apron",
    "firefighter gear",
    "paramedic uniform",
    "lifeguard uniform",
    "school uniform",
    "academic robes",
    "sports uniform",
    "business suit",
    "concierge staff uniform",
    "pilot uniform",
    "delivery driver uniform",
    "referee uniform",
    "martial arts uniform",
    "mechanic coveralls",
    "construction worker",
    "park ranger uniform",
    "beekeeping suit",
    "clergy",
    "nun habits",
    "monk habits",
    "postal worker uniform",
    "cosplay"
}

all_expression = {
    "positive": [
        "happy, eager grin",
        "happy, gentle smile",
        "happy, joyful laugh",
        "happy, contented look",
        "happy, excited expression",
        "happy, confident smile",
        "happy, playful wink",
        "happy, relieved smile",
        "happy, affectionate gaze",
        "happy, hopeful look"
    ],
    "neutral": [
        "neutral expression, disinterested",
        "neutral expression, thoughtful frown",
        "neutral expression, smug expression",
        "neutral expression, listless",
        "neutral expression, blank stare",
        "neutral expression, empty eyes",
        "neutral expression, suspicious glance",
        "neutral expression, inquisitive look",
        "neutral expression, skeptical, one eyebrow lifted",
        "neutral expression, ambivalent, wandering eyes",
        "neutral expression, distracted look, unfocused eyes",
        "surprise, delighted, bright eyes"
    ],
    "negative": [
        "upset, angry scowl",
        "upset, irritated glare",
        "upset, fearful expression",
        "upset, sad look",
        "upset, confused frown",
        "upset, disgusted grimace",
        "upset, exasperated look",
        "upset, pained expression",
        "upset, anxious expression, tense, darting eyes",
        "upset, ashamed look, lowered head",
        "upset, insane smile",
        "surprise, wide-eyed",
        "surprise, shock, mouth agape",
        "surprise, amazement, raised eyebrows",
        "surprise, startled look",
        "surprise, terrified",
        "fleeting smile",
        "nervous smirk",
        "pitying look",
        "guilty look",
        "dismissive look"
    ],
    "sexy": [
        "sarcastic smile",
        "flirty gaze",
        "pleading look, pout",
        "resigned expression, exhale",
        "cautious look",
        "sadistic smile",
        "sadistic grin",
        "angry smile",
        "tearful",
        "determined glare",
        "triumphant smirk",
        "ahegao",
        "orgasm face",
        "seductive, sultry gaze, blushing",
        "seductive, biting lip, blushing",
        "seductive, coy smile",
        "seductive, smoldering look",
        "seductive, lingering glance, looking at viewer",
        "seductive, mischievous smirk",
        "seductive, flirtatious wink",
        "seductive, teasing expression",
        "seductive, pouting lips",
        "seductive, shy glance, downturned eyes, smile",
        "seductive, dreamy expression, blushing",
        "seductive, provocative laugh",
        "seductive, mysterious smile"
    ],
    "misc": [
        "licking",
        "sticking tongue out",
        "(sleeping), eyes closed",
        "eyes crossed"
    ]
}