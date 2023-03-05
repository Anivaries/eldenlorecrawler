import json
from scrapy.spiders import SitemapSpider
import pandas as pd
import re
import csv
data = open(
    r'C:\Users\MaX\Desktop\PyProjects\crawler\tutorial\tutorial\spiders\ove_reci.txt', 'r')
reader = csv.reader(data)
words_to_use = [line.split(' ') for line in data.readlines()]


class ERWeapons(SitemapSpider):
    name = "EldenRing"
    sitemap_urls = ['https://eldenring.wiki.fextralife.com/sitemap.xml']
    sitemap_rules = [('https://eldenring.wiki.fextralife.com/', 'parse_item')]

    def parse(self, response):
        item_links = response.xpath("//a/@href")
        for item in item_links:
            yield from response.follow(item_links, self.parse_item)

    def parse_item(self, response):
        divs = response.xpath('//div')
        for item in divs[1:2]:
            if item is None:
                pass
        yield{
            'name': item.xpath(".//strong/text()").get(),
            'description': item.xpath(".//em/text()").getall()
        }


class ERMissingItems(SitemapSpider):
    name = "EldenRingMissing"
    sitemap_urls = ['https://eldenring.wiki.fextralife.com/sitemap.xml']
    sitemap_rules = [('https://eldenring.wiki.fextralife.com/', 'parse_item')]

    def parse(self, response):
        item_links = response.xpath("//a/@href")
        for item in item_links:
            yield from response.follow(item_links, self.parse_item)

    def parse_item(self, response):
        divs = response.xpath('//div')
        for item in divs:
            if item is None:
                pass
            print(item)
        yield{
            'name': item.xpath(".//strong/text()").get(),
            'description': item.xpath(".//blockquote//p/text()").get()
        }


rx = r"\.(?=\S)"  # space after fullstop

dframe = pd.read_json(
    r"C:\Users\MaX\Desktop\PyProjects\crawler\tutorial\ER.json")
dframe = dframe.mask(dframe.eq('None')).dropna(how='any')
dframe = dframe.reset_index(drop=True)

for item in dframe["description"]:
    # Making space after fullstop because not every sentence after full stop started with space
    item[:] = [''.join(item[:])]
    item[0] = re.sub(rx, ". ", item[0])


with open(r"C:\Users\MaX\Desktop\PyProjects\crawler\tutorial\ERMissing2.json") as f:
    df = pd.read_json(f)
    df = df.mask(df.eq('None')).dropna(inplace=False)
    df = df.reset_index(drop=True)

# x = [dframe, df]
# result = pd.concat(x, ignore_index=True)   merging into dict - don't delete
# pd.DataFrame.to_json(result, r"C:\Users\MaX\Desktop\PyProjects\crawler\tutorial\result.json") - made into json - dont delete

fixed_list_with_symbols = []
data_list = []
words = ""
for a in dframe.description:
    data_list.append(a[0])
for a in data_list:
    words += str(a)
split_it = words.split()
for word in split_it:
    if word.endswith("."):
        word = word.replace(".", "")
    elif word.endswith(","):
        word = word.replace(",", "")
    fixed_list_with_symbols.append(word)


results = [a for a in words_to_use[0]
           for text in dframe.description[131] if a in text]
# print(*(text for a in words_to_use[0] for text in dframe.description[3] if a in text), sep='\n')

with open(r"C:\Users\MaX\Desktop\Reci.txt") as gotove_reci:
    text = gotove_reci.readlines()
    sd = [b.strip() for b in text]  # sd = the most used words
    dftext = pd.read_json(r"tutorial\result.json")
    reci = []
    for rec in sd:
        for a in range(len(dftext.description)):
            if rec in dftext.description[a]:
                recis = [rec], [dftext.name[a], dftext.description[a]]
                reci.append(recis)
count = []
desddictlist = []

creatures = ['Fire Gian', 'Gurranq', "Night's Cavalry", 'Tree Sentinels', 'Bloodhound', 'Gransax', 'Agheel', 'Valiant Gargoyles', 'Dragonlord', 'Beast Clergyman',
             'Serosh', 'Fortissax', 'Demi-Human', 'Lansseax', 'Deathbird', 'Astel', 'Golem', 'Theodorix', 'Alabaster', 'Onyx', 'Ekzykes', 'Magma Wyrm', 'Greyoll']
people = ['Elden Lord', 'Tarnished', 'Prince of Death', 'Finger Maiden', 'Finger Reader', 'Queen Marika', 'Lunar Queen', 'The Gloam-Eyed Queen', 'Demi-Human Queen', 'Radahn', 'Traveling Maiden', 'Fire Monk', 'Cleanrot Knight', 'Crucible Knight', 'Mausoleum Knight', 'Ranni', 'Blackguard', 'Black Flame Monks', 'Marika', 'Rennala', 'Malenia', 'Lord of Blood', 'Godfrey', 'Radagon', 'Miquella', 'Fell Omen', 'Rykard', 'Mohg', 'Godrick', 'Blaidd', 'Maliketh', 'Hoslo', 'Tanith', 'Gideon Ofnir', 'Millicent', 'Loretta', 'Vyke', 'Dung Eater', 'Godwyn', 'Seluvis', 'Azur', 'Lusat', 'Fia', 'Mohgwyn', 'Elemer', 'Bernahl',
          'Nepheli', 'Jerren', 'Alexander', 'Iji', 'Vargram', 'Rogier', 'Morgott', 'Kaiden', 'Niall', 'Sellen', 'Shabriri', 'Marais', 'Loux', 'Frenzied Flame', 'Yura', 'Istvan', 'Goldmask', 'Boc', 'Diallos', 'Hewg', 'Irina', 'Kenneth Haight', 'Boggart', 'Rya', 'Okina', 'Miriel', 'Latenna', 'Roderika', 'Lionel', 'Ensha', 'Tragoth', 'Renna', 'Mad Tongue Alberich', 'Patches', 'Eleonora', 'Inaba', 'Margit', 'Corhyn', 'Gowry', 'Rollo', 'Wilhelm', 'Siluria', 'Ordovis', 'Albus', 'Garris', 'Graven', 'Hugues', 'Kristoff', 'Neidhardt', 'Birac', 'Amon', 'Nial', 'Finlay', 'Miranda', 'Lhutel', 'Tricia', 'Melina', 'Milos', 'Swordstress']
places = ['Erdtree', 'Lands Between', 'Roundtable Hold', 'Raya Lucaria', 'Caria', 'Academy', 'Haligtree', 'Liurnia', 'Volcano Manor', 'Eternal'' City', 'Leyndell', 'Capital', 'Caelid', 'Altus Plateau',
          'Royal Capital', 'Gelmir', 'Sellia', 'Limgrave', 'Stormveil', 'Dragon Communion', 'Weeping Peninsula', 'Ainsel', 'Nokron', 'Siofra', 'Aeonia', 'Dominula', 'Farum Azula', 'Stormhill', 'Greattree', 'Numen', 'Eochaid']
events = ['War against the Giants', 'War of the Ancient Dragons',
          'Liurnian Wars', 'Shattering', 'the Long March']
other = ['Elden Ring', 'Destined Death', 'Death', 'Fingers', 'Two Fingers', 'Three Fingers', 'Golden Order', 'Black Flame', 'Omen', 'Misbegotten',
         'Greater Will', 'Empyrean', 'Godskin', 'Crucible', 'Cleanrot', 'Albinauric', 'Conspectus', 'Nox', 'Prelates', 'Cuckoo', 'Trina', 'Oracle Envoys']
groups = ['Black Knife', 'Night of the Black Knives', 'Redmane', 'Reeds', 'Blackflame', 'Zamor',
          'Crystalians', 'Ravenmount', 'Omenkiller', 'Cadre', 'Crystalian', 'Those Who Live in Death']

gotovo = []
pk = 1
with open('sve.json', 'w') as f:
    for a in sd:
        if a in people:
            loopl = {
                "model": "base.lore",
                "pk": pk,
                "fields":{
                    "name":a,
                    "belongs_to":"People"
                }
            }
            gotovo.append(loopl)
            pk +=1
            loopl = []
        elif a in creatures:
            loopl = {
                "model": "base.lore",
                "pk": pk,
                "fields":{
                    "name":a,
                    "belongs_to":"Creatures"
                }
            }
            gotovo.append(loopl)
            pk +=1
            loopl = []
        elif a in events:
            loopl = {
                "model": "base.lore",
                "pk": pk,
                "fields":{
                    "name":a,
                    "belongs_to":"Events"
                }
            }
            gotovo.append(loopl)
            pk +=1
            loopl = []
        elif a in other:
            loopl = {
                "model": "base.lore",
                "pk": pk,
                "fields":{
                    "name":a,
                    "belongs_to":"Other"
                }
            }
            gotovo.append(loopl)
            pk +=1
            loopl = []
        elif a in places:
            loopl = {
                "model": "base.lore",
                "pk": pk,
                "fields":{
                    "name":a,
                    "belongs_to":"Places"
                }
            }
            gotovo.append(loopl)
            pk +=1
            loopl = []
        elif a in groups:
            if a == "Omenkiller":
                continue
            loopl = {
                "model": "base.lore",
                "pk": pk,
                "fields":{
                    "name":a,
                    "belongs_to":"Groups"
                }
            }
            gotovo.append(loopl)
            pk +=1
            loopl = []
    json.dump(gotovo, f, indent=4)

listaaa = []
with open('probnirad.json', 'w') as f:
    pf = pd.read_json('sve.json')
    for a in sd:
        for rec in reci:
            if a == rec[0][0] and a in rec[1][1]:
                for s in range(len(pf)):
                    if a in pf['fields'][s]['name']:
                        listaaa.append(int(pf['pk'][s]))
                desddict = {
                    "model": "base.lorelist",
                    "fields": {
                        "item_title": rec[1][0],
                        "item_description": rec[1][1],
                        "item_type": listaaa,
                    }
                }
                desddictlist.append(desddict)
                listaaa = []
    json.dump(desddictlist, f, indent=4)

    if a == rec[0][0] and a in rec[1][1] and a in places:
        for s in range(len(pf)):
            if a in pf['fields'][s]['name']:
                listaaa.append(int(pf['pk'][s]))
        desddict = {
            "item_title":rec[1][0],
            "item_description":rec[1][1],
            "item_type":listaaa,
            }
        desddictlist.append(desddict)
        listaaa = []
    if a == rec[0][0] and a in rec[1][1] and a in groups:
        for s in range(len(pf)):
            if a in pf['fields'][s]['name']:
                listaaa.append(int(pf['pk'][s]))
        desddict = {
            "item_title":rec[1][0],
            "item_description":rec[1][1],
            "item_type":listaaa,
            }
        desddictlist.append(desddict)
        listaaa = []
    if a == rec[0][0] and a in rec[1][1] and a in other:
        for s in range(len(pf)):
            if a in pf['fields'][s]['name']:
                listaaa.append(int(pf['pk'][s]))
        desddict = {
            "item_title":rec[1][0],
            "item_description":rec[1][1],
            "item_type":listaaa,
            }
        desddictlist.append(desddict)
        listaaa = []
    if a == rec[0][0] and a in rec[1][1] and a in events:
        for s in range(len(pf)):
            if a in pf['fields'][s]['name']:
                listaaa.append(int(pf['pk'][s]))
        desddict = {
            "item_title":rec[1][0],
            "item_description":rec[1][1],
            "item_type":listaaa,
            }
        desddictlist.append(desddict)
        listaaa = []
    count.append
    json.dump(desddictlist, f, indent=4)
