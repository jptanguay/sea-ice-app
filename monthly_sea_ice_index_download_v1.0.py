'''
	monthly_sea_ice_index_download_v1.0.py
	
	get all csv files from https://noaadata.apps.nsidc.org/NOAA/G02135/{ north or south }/monthly/data/
				
		and generate a single csv file "monthly_ice_cover.csv

	Each file contains the same header. The header of the first file is kept, the other headers ase discarded 

	Note: the script is derived from the example code provided on the page:
		https://nsidc.org/data/user-resources/help-center/how-access-and-download-noaansidc-data
		in the section "Download a directory"
		
	Original dataset description: 
		URL: https://nsidc.org/sites/defaul/files/g02135-v003-userguide_1_1.pdf
		Section: 3.1.6 Monthly Sea Ice Extent and Area Data Files, p.15
		
		
	2023-10	Jean-Pierre Tanguay
	
	
'''


import os
import io
import requests
from bs4 import BeautifulSoup


############################

SAVE_TO_DISK = True
TARGET_DIR = "c:/temp" # where the file are to be saved
TARGET_FILENAME = "monthly_sea_ice_index.csv"



DEBUG = False

ARCHIVE_URLS = [
		"http://127.0.0.1:8080/test/ice/north/",
		"http://127.0.0.1:8080/test/ice/south/",
	] if DEBUG else [
		"https://noaadata.apps.nsidc.org/NOAA/G02135/south/monthly/data/",
		"https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/"
	]

	
################################	


# the dataset is quite small, 
#  	so we can use an in memory file to create the csv file before saving the content to disk

with io.StringIO("") as f:

	# if it's the first file, we keep the headers
	first_file = True
	
	for url in ARCHIVE_URLS:
	
		# get the list of data files, then dowload and process each of those files
		r = requests.get(url, verify=False)

		data = BeautifulSoup(r.text, "html.parser")

		for l in data.find_all("a")[1:]:
			print(url + l["href"])
			
			r = requests.get(url + l["href"],  verify=False)

			# remove spaces, split text into lines so we can get rid of the header
			# then rejoin lines with EOLs
			lines = r.text.replace(" ", "").splitlines()
			if (first_file):
				start_idx = 0
				first_file = False
			else:
				start_idx = 1
				
			f.write( "\n".join(lines[start_idx:]) + "\n" )

	monthly_sea_ice_index_data = f.getvalue()	
	#print (monthly_sea_ice_index_data)



# save to disk
if (SAVE_TO_DISK):
	os.chdir(TARGET_DIR);
	with open(TARGET_FILENAME, "w+") as f:
		f.write(monthly_sea_ice_index_data);
	

	
				