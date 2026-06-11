import pandas as pd

movies = [

    ["Avengers","Action","Superhero team saves the world from alien threats",9.2],
    ["John Wick","Action","Retired assassin seeks revenge against criminals",8.7],
    ["Mission Impossible","Action","Secret agent completes dangerous missions",8.5],
    ["Mad Max Fury Road","Action","Survival and action in a post apocalyptic world",9.1],
    ["Extraction","Action","Mercenary rescues kidnapped child",8.3],
    ["The Dark Knight","Action","Batman fights crime in Gotham city",9.8],
    ["Gladiator","Action","Roman warrior seeks justice and revenge",9.0],
    ["Top Gun Maverick","Action","Pilot returns for dangerous air missions",9.3],
    ["The Equalizer","Action","Former operative helps innocent people",8.4],
    ["Die Hard","Action","Police officer fights terrorists in skyscraper",8.6],

    ["Titanic","Romance","Love story aboard a doomed ship",9.1],
    ["The Notebook","Romance","Young couple experiences lifelong romance",8.4],
    ["Me Before You","Romance","Romantic relationship changes two lives",8.2],
    ["A Walk To Remember","Romance","Teenage romance with emotional journey",8.5],
    ["La La Land","Romance","Musicians pursue dreams and love",9.0],
    ["Pride And Prejudice","Romance","Classic romantic drama",8.9],
    ["The Vow","Romance","Couple rebuilds relationship after accident",8.1],
    ["Dear John","Romance","Long distance love story",7.8],
    ["The Lucky One","Romance","Marine searches for woman from photograph",8.3],
    ["Safe Haven","Romance","Romance and mystery in small town",8.2],

    ["Interstellar","Sci-Fi","Space exploration beyond Earth",9.9],
    ["Inception","Sci-Fi","Dream invasion and mind manipulation",9.5],
    ["The Martian","Sci-Fi","Astronaut survives alone on Mars",9.0],
    ["Gravity","Sci-Fi","Astronaut stranded in space",8.4],
    ["Arrival","Sci-Fi","Aliens communicate with humanity",9.1],
    ["Avatar","Sci-Fi","Humans explore alien planet",9.3],
    ["Dune","Sci-Fi","Epic battle on desert planet",9.2],
    ["Edge Of Tomorrow","Sci-Fi","Soldier relives same battle repeatedly",8.8],
    ["Oblivion","Sci-Fi","Future Earth survival mission",8.1],
    ["Passengers","Sci-Fi","Space travelers awaken early",7.9],

    ["The Conjuring","Horror","Paranormal investigators face evil spirit",9.0],
    ["Annabelle","Horror","Haunted doll terrorizes family",7.5],
    ["Insidious","Horror","Family battles supernatural forces",8.4],
    ["The Nun","Horror","Demonic entity haunts church",7.6],
    ["It","Horror","Children fight terrifying clown",8.5],
    ["The Ring","Horror","Cursed videotape causes death",8.3],
    ["Hereditary","Horror","Family experiences dark supernatural events",9.1],
    ["Sinister","Horror","Writer discovers horrifying murders",8.6],
    ["Lights Out","Horror","Creature appears in darkness",7.8],
    ["Smile","Horror","Victims experience disturbing curse",8.2],

    ["The Hangover","Comedy","Friends face hilarious consequences",8.7],
    ["Superbad","Comedy","Teenagers experience chaotic adventures",8.4],
    ["Free Guy","Comedy","Video game character becomes self aware",8.3],
    ["Jumanji","Comedy","Adventure through magical game",8.5],
    ["Central Intelligence","Comedy","Unexpected spy adventure",7.9],
    ["The Mask","Comedy","Man gains magical powers",9.2],
    ["Yes Man","Comedy","Man agrees to every opportunity",8.1],
    ["Bruce Almighty","Comedy","Ordinary man receives divine powers",8.6],
    ["Ride Along","Comedy","Police adventure with future brother in law",7.7],
    ["Night At The Museum","Comedy","Museum exhibits come alive",8.4],

    ["Shutter Island","Thriller","Detective investigates mysterious disappearance",9.3],
    ["Gone Girl","Thriller","Woman vanishes under suspicious circumstances",9.1],
    ["Prisoners","Thriller","Father searches for kidnapped daughter",9.2],
    ["The Girl On The Train","Thriller","Witness uncovers hidden crime",8.2],
    ["Seven","Thriller","Detectives hunt serial killer",9.8],
    ["Zodiac","Thriller","Investigation of notorious killer",9.0],
    ["The Prestige","Thriller","Rival magicians battle for success",9.4],
    ["Memento","Thriller","Man searches for wife's killer",9.1],
    ["Source Code","Thriller","Soldier relives train explosion",8.5],
    ["Nightcrawler","Thriller","Reporter enters dangerous crime world",8.8],

    ["Finding Nemo","Animation","Fish searches for missing son",9.1],
    ["Frozen","Animation","Princess discovers magical powers",8.4],
    ["Toy Story","Animation","Toys come alive when humans leave",9.8],
    ["Coco","Animation","Boy explores land of the dead",9.3],
    ["Up","Animation","Old man embarks on adventure",9.4],
    ["Moana","Animation","Girl journeys across ocean",8.5],
    ["Zootopia","Animation","Rabbit officer solves mystery",9.0],
    ["Inside Out","Animation","Emotions guide young girl",9.2],
    ["Cars","Animation","Race car learns life lessons",8.3],
    ["Encanto","Animation","Family possesses magical abilities",8.7]

]

data = pd.DataFrame(
    movies,
    columns=["movie", "genre", "description", "rating"]
)

data.to_csv(r"Project-5-Smart-Recommendation-System\movies.csv", index=False)

print("Dataset Generated Successfully")