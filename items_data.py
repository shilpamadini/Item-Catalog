#!/usr/bin/env python
"""Python code to populate itemcatalog.db."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Catalog, CatalogItem

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create user 1
user1 = User(
            username="shilpa koppula",
            email="smkoppula@gmail.com",
            picture="https://lh3.googleusercontent.com/-V3nj_VQZFdY/Wo3fAG43b6E/\
AAAAAAAAAAc/xJtTAeJ5DJM1bwTgE-y-y06jOLrDb664gCEwYCg/w326-h220-p/\
6525116628071837601"
            )
session.add(user1)
session.commit()

# Items for catalog scince fiction

catalog1 = Catalog(user_id=1, catalog_name="Science Fiction")

session.add(catalog1)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="The Lord of the Rings",
                    description="The Lord of the Rings is a book by \
J.R.R. Tolkien, the sequel to his earlier work, \
The Hobbit. It was published in three volumes in 1954 \
and 1955. The story's titular character is the Dark \
Lord Sauron of Mordor.",
                    catalog=catalog1)
session.add(item1)
session.commit()

item2 = CatalogItem(
                    user_id=1,
                    item_name="Frankenstein",
                    description="The Modern Prometheus is a novel written by \
English author Mary Shelley that tells the \
story of Victor Frankenstein, a young scientist who \
creates a grotesque but sapient creature in an unorthodox \
scientific experiment.",
                    catalog=catalog1)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="The Handmaid's Tale",
                    description="The Handmaid's Tale is a dystopian novel by \
Canadian author Margaret Atwood,originally published in \
1985. It is set in a near-future New England, in a \
totalitarian, Christian theonomy that has overthrown \
the United States government.",
                    catalog=catalog1)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="The Last Unicorn",
                    description="The Last Unicorn is a novel by American \
author Peter S. Beagle and published in 1968, by Viking \
Press in the U.S. and The Bodley Head in the U.K. It \
follows the tale of a unicorn, who believes she is the \
last of her kind in the world and undertakes a quest to \
discover what has happened to the others.",
                    catalog=catalog1)
session.add(item4)
session.commit()

item5 = CatalogItem(
                    user_id=1,
                    item_name="1984",
                    description="In George Orwell's 1984, Winston Smith \
wrestles with oppression in Oceania, a place where the \
Party scrutinizes human actions with ever-watchful \
Big Brother. Defying a ban on individuality, Winston \
dares to express his thoughts in a diary and pursues a \
relationship with Julia.",
                    catalog=catalog1)
session.add(item5)
session.commit()

# Items for catalog drama

catalog2 = Catalog(user_id=1, catalog_name="Drama")

session.add(catalog2)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="The Great Gatsby",
                    description="The Great Gatsby is the story of eccentric \
millionaire Jay Gatsby as told by Nick Carraway, a \
Midwesterner who lives on Long Island but works in \
Manhattan. Gatsby's enormous mansion is adjacent to \
Caraway's modest home, and Carraway becomes curious about \
his neighbor after being invited to one of \
his famous parties.",
                    catalog=catalog2)
session.add(item1)
session.commit()

item2 = CatalogItem(
                    user_id=1,
                    item_name="To Kill a Mocking Bird",
                    description="To Kill a Mockingbird is a novel by Harper Lee \
published in 1960. It was immediately successful, winning \
the Pulitzer Prize, and has become a classic of modern \
American literature. The plot and characters are loosely \
based on Lee's observations of her family, her neighbors \
and an event that occurred near her hometown of \
Monroeville,Alabama, in 1936, when she was 10 years old.",
                    catalog=catalog2)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="A tree grows in Brooklyn",
                    description="A Tree Grows in Brooklyn is a 1943 novel \
written by Betty Smith. The story focuses on an \
impoverished but aspirational, second-generation \
Irish-American, adolescent girl and her family in \
Williamsburg, Brooklyn, New York City, during the first \
two decades of the 20th century.",
                    catalog=catalog2)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="Anna Karenina",
                    description="Anna Karenina  is a novel by the Russian \
writer Leo Tolstoy, published in serial installments from \
1873 to 1877 in the periodical The Russian Messenger.",
                    catalog=catalog2)
session.add(item4)
session.commit()

item5 = CatalogItem(
                    user_id=1,
                    item_name="The fault in our starts",
                    description='The Fault in Our Stars is the sixth novel \
by author John Green, published in January 2012. \
The title is inspired by Act 1, Scene 2 of Shakespeare\'s \
play Julius Caesar, in which the nobleman Cassius says to \
Brutus: "The fault, dear Brutus, is not in our stars, / \
But in ourselves, that we are underlings."',
                    catalog=catalog2)
session.add(item5)
session.commit()

# Items for catalog biographies

catalog3 = Catalog(user_id=1, catalog_name="Biographies")

session.add(catalog3)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="I Know why the caged bird sings",
                    description="I Know Why the Caged Bird Sings is a 1969 \
autobiography about the early years of American writer \
and poet Maya Angelou. The first in a seven-volume \
series, it is a coming-of-age story that illustrates \
how strength of character and a love of literature \
can help overcome racism and trauma.",
                    catalog=catalog3)
session.add(item1)
session.commit()

item2 = CatalogItem(
                    user_id=1,
                    item_name="Educated",
                    description="An unforgettable memoir about a young girl \
who, kept out of school, leaves her survivalist family \
and goes on to earn a PhD from Cambridge University .",
                    catalog=catalog3)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="Steve Jobs",
                    description="Steve Jobs is the authorized self-titled \
biography book of Steve Jobs. The book was written at \
the request of Jobs by Walter Isaacson, a former \
executive at CNN and TIME who has written best-selling \
biographies of Benjamin Franklin and Albert Einstein.",
                    catalog=catalog3)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="The Immortal Life of Henrietta Lacks",
                    description="Her name was Henrietta Lacks, but scientists \
know her as HeLa. She was a poor&nbsp;black tobacco \
farmer whose cells are taken without her knowledge in \
1951 became one of the most important tools in \
medicine, vital for developing the polio vaccine, \
cloning, gene mapping, and more.",
                    catalog=catalog3)
session.add(item4)
session.commit()

item5 = CatalogItem(
                    user_id=1,
                    item_name="Hillbilly Elegy",
                    description="A Memoir of a Family and Culture in Crisis \
is a memoir by J.D. Vance about the Appalachian values of \
his upbringing and their relation to the social \
problems of his hometown.",
                    catalog=catalog3)
session.add(item5)
session.commit()

# Items for catalog action and adventure

catalog4 = Catalog(user_id=1, catalog_name="Action and Adventure")

session.add(catalog4)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="The Hunger Games",
                    description="The Hunger Games is a 2008 dystopian \
novel by the American writer Suzanne Collins. \
It is written in the voice of 16-year-old Katniss \
Everdeen, who lives in the future, post-apocalypticnation \
of Panem in North America.",
                    catalog=catalog4)
session.add(item1)
session.commit()


item2 = CatalogItem(
                    user_id=1,
                    item_name="The Da Vinci Code",
                    description="The Da Vinci Code is a 2003 mystery \
thriller novel by Dan Brown. It follows symbologist \
Robert Langdon and cryptologist Sophie Neveu after a \
murder in the Louvre Museum in Paris causes them to \
become involved in a battle between the Priory of Sion \
and Opus Dei over the possibility of Jesus Christ \
having been a companion to Mary Magdalene.",
                    catalog=catalog4)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="The Adventures of Tom Sawyer",
                    description="The Adventures of Tom Sawyer by Mark Twain \
is an 1876 novel about a young boy growing up along the \
Mississippi River. It is set in the 1840s in the \
fictional town of St. Petersburg, inspired by Hannibal, \
Missouri, where Twain lived as a boy",
                    catalog=catalog4)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="The Hobbit",
                    description="The Hobbit,is a children's fantasy novel by \
English author J. R. R. Tolkien. It was published \
on 21 September 1937 to wide critical acclaim, being \
nominated for the Carnegie Medal and awarded a prize from \
the New York Herald Tribune for best juvenile fiction.",
                    catalog=catalog4)
session.add(item4)
session.commit()

# Items for catalog action and romance

catalog5 = Catalog(user_id=1, catalog_name="Romance")

session.add(catalog5)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="White Rose , Black Forest",
                    description="In the shadows of World War II, trust becomes \
the greatest risk of all for two strangers.",
                    catalog=catalog5)
session.add(item1)
session.commit()

item2 = CatalogItem(
                    user_id=1,
                    item_name="Pride and Prejudice",
                    description="Pride and Prejudice is a romantic novel by \
Jane Austen, first published in 1813. The story charts \
the emotional development of the protagonist, \
Elizabeth Bennet, who learns the error of making hasty \
judgments and comes to appreciate the difference between \
the superficial and the essential.",
                    catalog=catalog5)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="Memoirs of a Geisha",
                    description="Memoirs of a Geisha is a historical novel \
by American author Arthur Golden, published in 1997. \
The novel, told in first person perspective, \
tells the story of a fictional geishaworking in \
Kyoto, Japan, before and after World War II.",
                    catalog=catalog5)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="Mr. Perfect",
                    description="Knowing whom to trust and whom to love \
is a matter of survival -- as the dream of Mr. Perfect \
becomes a chilling nightmare.",
                    catalog=catalog5)
session.add(item4)
session.commit()

item5 = CatalogItem(
                    user_id=1,
                    item_name="Norwegian Wood",
                    description="Norwegian Wood is a 1987 novel by Japanese \
author Haruki Murakami.[1] The novel is a nostalgic story \
of loss and burgeoning sexuality.[2] It is told from the \
first-person perspective of Toru Watanabe, who looks \
back on his days as a college student living in Tokyo.",
                    catalog=catalog5)
session.add(item5)
session.commit()

# Items for catalog action and Mystery

catalog6 = Catalog(user_id=1, catalog_name="Mystery")

session.add(catalog6)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="The Woman in White",
                    description="The Woman in White is Wilkie Collins fifth \
published novel, written in 1859. It is considered to be \
among the first mystery novels and is widely regarded as \
one of the finest in this genre.",
                    catalog=catalog6)
session.add(item1)
session.commit()

item2 = CatalogItem(
                    user_id=1,
                    item_name="A Crime in the Neighborhood",
                    description="A Crime in the Neighborhood is a novel by \
Suzanne Berne. It won the Orange Prize for Fiction in \
1999. Told through the eyes of a ten-year-old girl, \
the book chronicles a child's murder in a sleepy suburb \
of Washington, D.C. against the backdrop of the \
unfolding Watergate scandal.",
                    catalog=catalog6)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="The Eye of the beholder",
                    description="Spying on people is routine business for \
private investigators, but a seductive, enigmatic woman \
will turn one P.I.'s life upside down when he becomes \
obsessed with her. Reissue. Movie tie-in.",
                    catalog=catalog6)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="The Quiet American",
                    description="The Quiet American is a 1955 novel by \
English author Graham Greene which depicts French \
colonialism in Vietnam being uprooted by the Americans \
during the 1950s.",
                    catalog=catalog6)
session.add(item4)
session.commit()

item5 = CatalogItem(
                    user_id=1,
                    item_name="Cutter and Bone",
                    description="The Quiet American is a 1955 novel by \
English author Graham Greene which depicts French \
colonialism in Vietnam being uprooted by the Americans \
during the 1950s.",
                    catalog=catalog6)
session.add(item5)
session.commit()

# Items for catalog Poetry

catalog7 = Catalog(user_id=1, catalog_name="Poetry")

session.add(catalog7)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="Milk and Honey",
                    description="The Woman in White is Wilkie Collins fifth \
published novel, written in 1859. It is considered to be \
among the first mystery novels and is widely regarded as \
one of the finest in this genre.",
                    catalog=catalog7)
session.add(item1)
session.commit()

item2 = CatalogItem(
                    user_id=1,
                    item_name="Where the sidewalk ends",
                    description="Where the Sidewalk Ends is a 1974 children's \
poetry collection written and illustrated by Shel \
Silverstein.It was published by Harper and Row Publishers.\
The book's poems address many common childhood \
concerns and also present purely fanciful stories.",
                    catalog=catalog7)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="Paradise Lost",
                    description="Paradise Lost is an epic poem in blank verse \
by the 17th-century English poet John Milton.",
                    catalog=catalog7)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="The Waste Land",
                    description="This all-new Signet Classic contains many \
of T.S. Eliot's most important early poems, leading to \
perhaps his greatest masterpiece, The Waste land, \
which has long been regarded as one of the fundamental \
texts of modernism. By combining poetic elements \
from many diverse sources with bits of popular culture \
and common speech linked in a fragmented narrative, \
Eliot recreated the chaos and disillusionment of Europe \
in the aftermath of WWI.",
                    catalog=catalog7)
session.add(item4)
session.commit()

# Items for catalog Children's Books

catalog8 = Catalog(user_id=1, catalog_name="Children's Books")

session.add(catalog8)
session.commit()

item1 = CatalogItem(
                    user_id=1,
                    item_name="A wrinkle in Time",
                    description="A Wrinkle in Time is a science fantasy novel \
written by American writer Madeleine L'Engle, first \
published in 1962.The book won the Newbery Medal, \
Sequoyah Book Award, and Lewis Carroll Shelf Award, \
and was runner-up for the Hans Christian Andersen Award.",
                    catalog=catalog8)
session.add(item1)
session.commit()

item2 = CatalogItem(
                    user_id=1,
                    item_name="The Magician's Nephew",
                    description="The Magician's Nephew is a high fantasy novel \
for children by C. S. Lewis, published by Bodley Head \
in 1955. It is the sixth published of seven novels \
in The Chronicles of Narnia.",
                    catalog=catalog8)
session.add(item2)
session.commit()

item3 = CatalogItem(
                    user_id=1,
                    item_name="Wolf Story",
                    description="This irresistible book is about a father \
and  his five-year-old son, Michael (intelligent, crafty, \
addicted to stories) and Michael's best friend Stefan \
(stalwart listener, equally addicted to stories).",
                    catalog=catalog8)
session.add(item3)
session.commit()

item4 = CatalogItem(
                    user_id=1,
                    item_name="Loretta Mason Potts",
                    description="Loretta finds a tunnel at the back of her \
closet to a fantasy world where she is encouraged to be \
as bad as she likes and give in to her impulses.Bewitched \
for seven years, Loretta refuses to live with her real \
family and draws her brother, Colin, into the enchantment \
with her.",
                    catalog=catalog8)
session.add(item4)
session.commit()

item5 = CatalogItem(
                    user_id=1,
                    item_name="Stuart Little",
                    description="Stuart Little is a 1945 children's novel \
by E. B. White,[1] his first book for children, and is \
widely recognized as a classic in children's literature. \
Stuart Little was illustrated by the subsequently \
award-winning artist Garth Williams, also his first work \
for children. It is a realistic fantasy about Stuart \
Little who, though born to human parents in New York City,\
looked very much like a rat/mouse in every way ",
                    catalog=catalog8)
session.add(item5)
session.commit()

print("Catalog Items added")
