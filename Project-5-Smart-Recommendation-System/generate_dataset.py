import pandas as pd

movies = [

    ["Avengers","Action","Superhero team saves the world from alien threats",9],
    ["John Wick","Action","Retired assassin seeks revenge against criminals",8],
    ["Mission Impossible","Action","Secret agent completes dangerous missions",8],
    ["Mad Max Fury Road","Action","Survival and action in a post apocalyptic world",9],
    ["Extraction","Action","Mercenary rescues kidnapped child",8],
    ["The Dark Knight","Action","Batman fights crime in Gotham city",10],
    ["Gladiator","Action","Roman warrior seeks justice and revenge",9],
    ["Top Gun Maverick","Action","Pilot returns for dangerous air missions",9],
    ["The Equalizer","Action","Former operative helps innocent people",8],
    ["Die Hard","Action","Police officer fights terrorists in skyscraper",8],

    ["Titanic","Romance","Love story aboard a doomed ship",9],
    ["The Notebook","Romance","Young couple experiences lifelong romance",8],
    ["Me Before You","Romance","Romantic relationship changes two lives",8],
    ["A Walk To Remember","Romance","Teenage romance with emotional journey",8],
    ["La La Land","Romance","Musicians pursue dreams and love",9],
    ["Pride And Prejudice","Romance","Classic romantic drama",9],
    ["The Vow","Romance","Couple rebuilds relationship after accident",8],
    ["Dear John","Romance","Long distance love story",7],
    ["The Lucky One","Romance","Marine searches for woman from photograph",8],
    ["Safe Haven","Romance","Romance and mystery in small town",8],

    ["Interstellar","Sci-Fi","Space exploration beyond Earth",10],
    ["Inception","Sci-Fi","Dream invasion and mind manipulation",9],
    ["The Martian","Sci-Fi","Astronaut survives alone on Mars",9],
    ["Gravity","Sci-Fi","Astronaut stranded in space",8],
    ["Arrival","Sci-Fi","Aliens communicate with humanity",9],
    ["Avatar","Sci-Fi","Humans explore alien planet",9],
    ["Dune","Sci-Fi","Epic battle on desert planet",9],
    ["Edge Of Tomorrow","Sci-Fi","Soldier relives same battle repeatedly",8],
    ["Oblivion","Sci-Fi","Future Earth survival mission",8],
    ["Passengers","Sci-Fi","Space travelers awaken early",7],

    ["The Conjuring","Horror","Paranormal investigators face evil spirit",9],
    ["Annabelle","Horror","Haunted doll terrorizes family",7],
    ["Insidious","Horror","Family battles supernatural forces",8],
    ["The Nun","Horror","Demonic entity haunts church",7],
    ["It","Horror","Children fight terrifying clown",8],
    ["The Ring","Horror","Cursed videotape causes death",8],
    ["Hereditary","Horror","Family experiences dark supernatural events",9],
    ["Sinister","Horror","Writer discovers horrifying murders",8],
    ["Lights Out","Horror","Creature appears in darkness",7],
    ["Smile","Horror","Victims experience disturbing curse",8],

    ["The Hangover","Comedy","Friends face hilarious consequences",8],
    ["Superbad","Comedy","Teenagers experience chaotic adventures",8],
    ["Free Guy","Comedy","Video game character becomes self aware",8],
    ["Jumanji","Comedy","Adventure through magical game",8],
    ["Central Intelligence","Comedy","Unexpected spy adventure",7],
    ["The Mask","Comedy","Man gains magical powers",9],
    ["Yes Man","Comedy","Man agrees to every opportunity",8],
    ["Bruce Almighty","Comedy","Ordinary man receives divine powers",8],
    ["Ride Along","Comedy","Police adventure with future brother in law",7],
    ["Night At The Museum","Comedy","Museum exhibits come alive",8],

    ["Shutter Island","Thriller","Detective investigates mysterious disappearance",9],
    ["Gone Girl","Thriller","Woman vanishes under suspicious circumstances",9],
    ["Prisoners","Thriller","Father searches for kidnapped daughter",9],
    ["The Girl On The Train","Thriller","Witness uncovers hidden crime",8],
    ["Seven","Thriller","Detectives hunt serial killer",10],
    ["Zodiac","Thriller","Investigation of notorious killer",9],
    ["The Prestige","Thriller","Rival magicians battle for success",9],
    ["Memento","Thriller","Man searches for wife's killer",9],
    ["Source Code","Thriller","Soldier relives train explosion",8],
    ["Nightcrawler","Thriller","Reporter enters dangerous crime world",8],

    ["Finding Nemo","Animation","Fish searches for missing son",9],
    ["Frozen","Animation","Princess discovers magical powers",8],
    ["Toy Story","Animation","Toys come alive when humans leave",10],
    ["Coco","Animation","Boy explores land of the dead",9],
    ["Up","Animation","Old man embarks on adventure",9],
    ["Moana","Animation","Girl journeys across ocean",8],
    ["Zootopia","Animation","Rabbit officer solves mystery",9],
    ["Inside Out","Animation","Emotions guide young girl",9],
    ["Cars","Animation","Race car learns life lessons",8],
    ["Encanto","Animation","Family possesses magical abilities",8]
]

data = pd.DataFrame(
    movies,
    columns=["movie","genre","description","rating"]
)

data.to_csv(r"Project-5-Smart-Recommendation-System\movies.csv", index=False)

print("Dataset Generated Successfully")