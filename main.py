'''
This is a simple program for searching and reading about Radiohead.
There is a list for discography, band members, links and resources for the information

Created 17 December 2020
'''

import re
import webbrowser
import time
from information.discography import songs


# Commands: watch, read, search

mv_links = list(songs.mv_list.values())		# Music videos links
mv_titles = list(songs.mv_list.keys())			# Music videos titles

mv_titles_lowercase = [val.lower() for val in mv_titles]	# Lowercasing all the music videos titles


class user_interaction():
	def ui():
		while True:
			user_input = input('> ')
			
			if re.search('^watch', user_input):
				user_interaction.watch(user_input)
				
			elif user_input == 'quit':
				break

	
	def watch(song):
		song.lower()
		
		if re.search('^watch', song) and song[6:] not in mv_titles_lowercase:
			print(f'There is no {song[6:]} music video')
			
		elif re.search('^watch', song):
			print(f'Opening {song[6:]} music video')
			webbrowser.open_new_tab(mv_links[mv_titles_lowercase.index(song[6:])])
