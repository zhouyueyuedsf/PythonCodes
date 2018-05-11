import sqlite3
import pandas as pd
from collections import Counter

# conn = sqlite3.connect('History.db')
# ret = conn.execute("SELECT name from sqlite_master WHERE TYPE=\"table\"")
# print(ret.fetchall())

# [('meta',), ('downloads',), ('downloads_url_chains',), ('visits',), ('visit_source',), 
# ('keyword_search_terms',), ('segments',), ('segment_usage',), ('downloads_slices',),
# ('typed_url_sync_metadata',), ('urls',), ('sqlite_sequence',)]

# c.execute("SELECT * from downloads")
# print(c.fetchall())

 
with sqlite3.connect('History.db') as con:
	df = pd.read_sql_query("SELECT u.url FROM visits v join urls u on v.url = u.id ", con=con)
	# df = pd.read_sql_query("SELECT * FROM visits", con=con)
	print(df.shape)
	print(df.dtypes)
	print(df.head())

urlTimes = []
for url in df["url"]:
	if url[4] == 's':
		urlTimes.append(url[8:][0:url[8:].find('/')])
	elif url[4] == ':':
		urlTimes.append(url[7:][0:url[7:].find('/')])

print(Counter(urlTimes))