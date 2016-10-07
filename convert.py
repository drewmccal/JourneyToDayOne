import random
import json
import glob
import time

#uuid generator
def euuid():
	hexlist = 'ABCDEF0123456789'
	return ''.join(random.choice(hexlist) for _ in range(32))

#convert from epoch format date
def utc_date(epochdate):
	d = epochdate/1000
	return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(d))

#initialize data object to hold converted entries
converted_journal = {}
converted_journal['metadata']={"version":"1.0"}
converted_journal['entries']=[]
for entry_file in glob.glob('*.json'):

   #load each journey json entry file
	with open(entry_file) as entry_f:
		entry = json.load(entry_f)
	#initialize variables to be used to create corresponding dayone entry
	uuid = euuid()
	e_text = entry["text"]
	edate = entry["date_journal"]
	creation_date = utc_date(edate)
	tags = entry["tags"]
	locality = "New York"
	country = "United States"
	#object to hold data from current Journey entry
	new_entry = {}
	new_entry['uuid'] = uuid
	new_entry['text'] = e_text
	new_entry['tags'] = tags
	new_entry['location']={}
	new_entry['location']['localityName'] = locality
	new_entry['location']['country']= country
	new_entry['creationDate'] = creation_date

	#append converted entry data object to dayone entry
	converted_journal['entries'].append(new_entry)

#write converted journal to file
with open('journal.json','w+') as f:
	json.dump(converted_journal,f)