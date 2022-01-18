
import os
import requests
import wget
import ctypes
import time

def get_wallpaper():
	key = os.environ.get('key')
	url = f"https://api.unsplash.com/photos/random/?client_id={key}"
	params = {
		"query":"HD wallpapers",
		"orientation":"landscape"
	}
	res = requests.get(url,params=params).json()
	image_url = res['urls']['full']
	wallpaper = wget.download(image_url,'../Pictures/wallpapers/wall.png')
	return 

def set_wallpaper():
	get_wallpaper()
	wallpaper = "C:/Users/Nitish/Pictures/wallpapers/wall (1).png"
	ctypes.windll.user32.SystemParametersInfoW(20,0,wallpaper,0)


def main():
	try:
		while True:
			set_wallpaper()
			time.sleep(10)
	except KeyboardInterrupt:
		print("Quitting")
	except Exception as e:
		pass


if __name__ == '__main__':
	main()
