
import webbrowser

mv_list = { 'Creep' : 							'https://youtu.be/XFkzRNyygfk',                 
			'No Suprises' : 					'https://youtu.be/u5CVsCnxyXg',
			'Karma Police' : 					'https://youtu.be/1uYWYWPc9HU',
			'Lotus Flower' : 					'https://youtu.be/cfOa1a8hYP8',
			'Daydreaming' : 					'https://youtu.be/TTAU7lLDZYU',
			'High and Dry' : 					'https://youtu.be/7qFfFVSerQo',
			'House of Cards' : 					'https://youtu.be/8nTFjVm9sTQ',
			'Fake Plastic Trees' : 				'https://youtu.be/n5h0qHwNrHk',
			'Burn The Witch' : 					'https://youtu.be/yI2oS2hoL0k',
			'Street Spirit (Fade Out)' : 		'https://youtu.be/LCJblaUkkfc',
			'Jigsaw Falling Into Place' : 		'https://youtu.be/GoLJJRIWCLU',
			'Lift' : 							'https://youtu.be/QBGaO89cBMI',
			'Man Of War' : 						'https://youtu.be/DXP1KdZX4io',
			'There, There' : 					'https://youtu.be/7AQSLozK7aA',
			'I Promise' : 						'https://youtu.be/0sFvFVkeGVg',
			'Pyramid Song' : 					'https://youtu.be/3M_Gg1xAHE4',
			'Just' : 							'https://youtu.be/oIFLtNYI3Ls',
			'I Might Be Wrong' : 				'https://youtu.be/vOa--Dhu11M',
			'Nude' : 							'https://youtu.be/BbWBRnDK_AE',
			'Knives Out' : 						'https://youtu.be/2Lpw3yMCWro',
			'Sit Down Stand Up' : 				'https://youtu.be/CVf_HGoY-1E',
			'Go To Sleep' : 					'https://youtu.be/Fe6X9fLLp0Y',
			'Push Pulk / Spinning Plates' : 	'https://youtu.be/ih2Ftq3hJoI'}

mv = list(mv_list.values())
#webbrowser.open_new_tab(all_mv[2:5])

for i in mv[2:5]:
	print(i)
	webbrowser.open_new_tab(i)
