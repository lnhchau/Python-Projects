# Create a Youtube playlist by Pygame
import pygame
import webbrowser

BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

class Video:
	def __init__(self, title, link):
		self.title = title
		self.link = link
		self.seen = False

	def open(self):
		webbrowser.open(self.link)
		print("Open: " + self.title)
		self.seen = True

class Playlist:
	def __init__(self, name, description, rating, videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class TextButton:
	def __init__(self, text, position):
		self.text = text
		self.position = position
	
	def is_mouse_on_text(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if mouse_x>self.position[0] and mouse_x<(self.position[0]+self.text_box[2]) and mouse_y>self.position[1] and mouse_y<(self.position[1]+self.text_box[3]):
			return True
		else: 
			return False
	
	def draw(self):
		font = pygame.font.SysFont('sans', 20)
		text_render = font.render(self.text, True, BLACK)
		
		self.text_box = text_render.get_rect()

		if self.is_mouse_on_text():
			text_render = font.render(self.text, True, BLUE)
			pygame.draw.line(screen, BLUE, (self.position[0],(self.position[1]+self.text_box[3]+2)), ((self.position[0]+self.text_box[2]),(self.position[1]+self.text_box[3]+2)))
		else: 
			text_render = font.render(self.text, True, BLACK)

		screen.blit(text_render, self.position)

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	return Video(title, link)

def read_videos_from_txt(file):
	videos_txt = []
	total = int(file.readline())
	for i in range(total):
		video_txt = read_video_from_txt(file)
		videos_txt.append(video_txt)
	return videos_txt

def read_playlist_from_txt(file):
	name = file.readline()
	description = file.readline()
	rating = file.readline()
	videos = read_videos_from_txt(file)
	return Playlist(name, description, rating, videos)

def read_playlists_from_txt():
	playlists = []
	with open("Playlist_GUI.txt", "r", encoding = "utf-8") as file:
		total = int(file.readline())
		for i in range(total):
			playlist = read_playlist_from_txt(file)
			playlists.append(playlist)
	return playlists

pygame.init()
screen = pygame.display.set_mode((1000,400))
pygame.display.set_caption('Youtube Playlist')
clock = pygame.time.Clock()

playlists = read_playlists_from_txt()
videos_btn_list = []
playlist_choice = None
playlists_btn_list = [] 
margin = 50
total_playlists = len(playlists)
for i in range(total_playlists):
	playlist_btn = TextButton(playlists[i].name.rstrip(), (50,50+i*margin))
	playlists_btn_list.append(playlist_btn)

running = True
while running:
	clock.tick(60)
	screen.fill(WHITE)

	for playlist_button in playlists_btn_list:
		playlist_button.draw()
	for video_button in videos_btn_list:
		video_button.draw()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1: 
				for i in range(len(playlists_btn_list)):
					if playlists_btn_list[i].is_mouse_on_text():
						playlist_choice = i
						videos_btn_list = []
						for j in range(len(playlists[i].videos)):
							video_btn = TextButton(str(j+1) + ". " + playlists[i].videos[j].title.rstrip(), (250,(50+j*margin)))
							videos_btn_list.append(video_btn)

				if playlist_choice != None:
					for i in range(len(videos_btn_list)): 
						if videos_btn_list[i].is_mouse_on_text():
							playlists[playlist_choice].videos[i].open() 
						else: continue
		if event.type == pygame.QUIT:
			running = False
	pygame.display.flip()

pygame.quit()
