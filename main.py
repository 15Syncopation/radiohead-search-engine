'''
This is a simple program for searching and reading about Radiohead.
There is a list for discography, band members, links and resources for the information

Created 17 December 2020
'''

from information.discography import songs
import messages
import webbrowser
import time

# List of commands
commands_list = ['watch', 'read', 'search']


# Problem #1
# Add a dictionary that start with 'watch' string on the first place
# the result should like this 'watch creep'

# PROBLEM SOLVED by Loocid (https://stackoverflow.com/users/2987253/loocid) on Stack Overflow (27/01/2020)
# https://stackoverflow.com/questions/65912708/is-there-an-way-to-appending-a-string-to-each-list-on-first-position

mvl = list(songs.mv_list.values())		# Music videos links
mv = list(songs.mv_list.keys())			# Music videos titles

lowercase_mv = [val.lower() for val in mv]	# Lowercasing all the music videos titles

string_WATCH = 'watch '
command_WATCH = [string_WATCH + i for i in lowercase_mv]


# Main CLI
while True:
	usr = input("> ").lower()

	if usr in command_WATCH:
		mv_index = command_WATCH.index(usr)
		print(f'Opening {usr}')
		time.sleep(2)
		webbrowser.open_new_tab(mvl[mv_index])

	elif usr == 'quit':
		break
