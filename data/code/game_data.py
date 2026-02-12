csv_graphics = {
	'background': 'data/levels/level 1/csv/level_background.csv',
	'blocks': 'data/levels/level 1/csv/level_blocks.csv',
	'borders': 'data/levels/level 1/csv/level_borders.csv',
	'coins': 'data/levels/level 1/csv/level_coins.csv',
	'door': 'data/levels/level 1/csv/level_door.csv',
	'enemies': 'data/levels/level 1/csv/level_enemies.csv',
	'fire': 'data/levels/level 1/csv/level_fire.csv',
	'lava': 'data/levels/level 1/csv/level_lava.csv',
	'player': 'data/levels/level 1/csv/level_player.csv',
	'torch': 'data/levels/level 1/csv/level_torch.csv',
}

png_graphics = {
	'background': 'data/assets/tiles/background 1 tileset.png',
	'bg torch': 'data/assets/tiles/background torch.png',
	'blocks': 'data/assets/tiles/brick tileset.png',
	'brick': 'data/assets/tiles/brick tile.png',
	'coins': 'data/assets/tiles/coin.png',
	'key': 'data/assets/tiles/key.png',
	'door': 'data/assets/tiles/door.png',
	'enemies': 'data/assets/enemy sprites/',  # FOLDER
	'fire': 'data/assets/tiles/fire.png',
	'lava': 'data/assets/tiles/lava.png',
	'torch': 'data/assets/tiles/torch.png',
	'player': 'data/assets/character/knight.png',
	'healthbar': 'data/assets/ui/health_bar.png'
}

spritesheet_animations = {
	# sprite sheets
	'coins': 'data/assets/tiles/coin animation.png',
	'collect': 'data/assets/tiles/collect coin.png',
	'fire': 'data/assets/tiles/fire animation.png',
	'torch': 'data/assets/tiles/torch animation.png',
	'lava': 'data/assets/tiles/lava animation.png',
	'key': 'data/assets/tiles/key animation.png',
	'door': 'data/assets/tiles/door/door.png'
}

folder_animations = {
	# folders
	'skeleton': {
		'attack': 'data/assets/enemies/Skeleton/attack/',
		'death': 'data/assets/enemies/Skeleton/death/',
		'run': 'data/assets/enemies/Skeleton/walk/',
		'take hit': 'data/assets/enemies/Skeleton/take hit/',
		'idle': 'data/assets/enemies/Skeleton/idle/',
	},

	'eye': {
		'attack': 'data/assets/enemies/Flying eye/attack/',
		'death': 'data/assets/enemies/Flying eye/death/',
		'run': 'data/assets/enemies/Flying eye/flight/',
		'idle': 'data/assets/enemies/Flying eye/flight/',
		'take hit': 'data/assets/enemies/Flying eye/take hit/',
	},

	'goblin': {
		'attack': 'data/assets/enemies/Goblin/attack/',
		'death': 'data/assets/enemies/Goblin/death/',
		'run': 'data/assets/enemies/Goblin/run/',
		'take hit': 'data/assets/enemies/Goblin/take hit/',
		'idle': 'data/assets/enemies/Goblin/idle/',
	},

	'mushroom': {
		'attack': 'data/assets/enemies/Mushroom/attack/',
		'death': 'data/assets/enemies/Mushroom/death/',
		'run': 'data/assets/enemies/Mushroom/run/',
		'take hit': 'data/assets/enemies/Mushroom/take hit/',
		'idle': 'data/assets/enemies/Mushroom/idle/',
	},

	'jump': 'data/assets/dust particles/jump/',
	'run': 'data/assets/dust particles/run/',
	'land': 'data/assets/dust particles/land/',
	'torch': 'data/assets/tile assets/tiles/torch animation/',
}

button_images = {
	'start': ['data/assets/ui/buttons/start button.png', 'data/assets/ui/buttons/start button hovered.png'],
	'restart': ['data/assets/ui/buttons/restart button.png', 'data/assets/ui/buttons/restart button hovered.png'],
	'pause': ['data/assets/ui/buttons/pause button.png', 'data/assets/ui/buttons/pause button hovered.png'],
	'quit': ['data/assets/ui/buttons/quit button.png', 'data/assets/ui/buttons/quit button hovered.png'],
	'sound_off': ['data/assets/ui/buttons/mute sound button.png', 'data/assets/ui/buttons/mute sound button hovered.png'],
	'sound_on': ['data/assets/ui/buttons/sound button.png', 'data/assets/ui/buttons/sound button hovered.png'],
	'music_off': ['data/assets/ui/buttons/mute music button.png', 'data/assets/ui/buttons/mute music button hovered.png'],
	'music_on': ['data/assets/ui/buttons/music button.png', 'data/assets/ui/buttons/music button hovered.png'],
	'settings': ['data/assets/ui/buttons/settings button.png', 'data/assets/ui/buttons/settings button hovered.png'],
	'back': ['data/assets/ui/buttons/back button.png', 'data/assets/ui/buttons/back button hovered.png'],
}

audio_paths = {
	'level': {
		'bg': 'data/assets/audio/level bg.wav',
		'complete': 'data/assets/audio/level complete.wav',
		'fail': 'data/assets/audio/game over.wav'
	},
	'player': {
		'attack': 'data/assets/audio/player attack 1.wav',
		'land': 'data/assets/audio/player land.wav',
		'death': 'data/assets/audio/player death.wav',
		'burn': 'data/assets/audio/player burn.flac',
		'hit': 'data/assets/audio/hit.wav',
	},
	'enemy': {
		'hit': 'data/assets/audio/hit.wav',
		'death': 'data/assets/audio/enemy death.wav',
		'attack': {
			'skeleton': 'data/assets/audio/skeleton attack.wav',
			'eye': 'data/assets/audio/enemy bite.wav',
			'mushroom': '',
			'goblin': 'data/assets/audio/skeleton attack.wav',
		},
	},
	'coin': {
		'collect': 'data/assets/audio/coin.mp3',
	},
	'button': 'data/assets/audio/button click.wav',
	'torch': 'data/assets/audio/torch burning.wav'
}
