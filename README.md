# Crawler for Elden Lord wikipedia

Made a crawler to search for item names and their description which i was going to use in database for my website. After that i created another script to pull
the most common capitalized words that are longer than 2 letters.  
When i got all the words, i arranged them in descending order ( from the most common one ) to filter out some common english words (like 'For', 'Then' etc. which were used as the beginning of a sentence).
The remaining words i manually filtered, to find top ~200 words which are in-game lore related. 
After that i made another script to find connection between Item names or Item description with those common lore words and put them together into dictionary which i exported as json file. Using the json file i populated PostgreSQL database for my website. The website is online on https://eldenlore.herokuapp.com/

