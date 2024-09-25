import pygame

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Ploops')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 30
timer = pygame.time.Clock()
steps = 8
instruments = 6
clicks = [[-1 for _ in range(steps)] for _ in range(instruments)]


def draw_grid(clicks):
	left_box = pygame.draw.rect(screen, grey, [0, 0, 200, HEIGHT,], 2)
	bottom_box = pygame.draw.rect(screen, grey, [0, HEIGHT - 200, WIDTH, 200], 2)
	boxes = []
	colors = [grey, white, grey]
	hi_hat_text = label_font.render('HH', True, white)
	screen.blit(hi_hat_text, (30, 30))
	open_hat_text = label_font.render('OH', True, white)
	screen.blit(open_hat_text, (30, 130))
	snare_text = label_font.render('Snare', True, white)
	screen.blit(snare_text, (30, 230))
	kick_text = label_font.render('Kick', True, white)
	screen.blit(kick_text, (30, 330))
	crash_text = label_font.render('Crash', True, white)
	screen.blit(crash_text, (30, 430))
	clap_text = label_font.render('Clap', True, white)
	screen.blit(clap_text, (30, 530))
	for i in range(6):
		pygame.draw.line(screen, grey, (0, (i * 100) + 100), (200, (i * 100) + 100), 2)

	for i in range(steps):
		for j in range(instruments):
			if clicks[j][i] == -1:
				color = grey
			else:
				color = green
			rect = pygame.draw.rect(screen, color,
			 [i * ((WIDTH - 200) // steps) + 202, (j * 100) + 2, ((WIDTH - 200) // steps) - 10, ((HEIGHT - 200)//instruments) - 10], 0, 2)
			rect = pygame.draw.rect(screen, gold,
			 [i * ((WIDTH - 200) // steps) + 200, (j * 100), ((WIDTH - 200) // steps), ((HEIGHT - 200)//instruments)], 2, 2)
			rect = pygame.draw.rect(screen, black,
			 [i * ((WIDTH - 200) // steps) + 200, (j * 100), ((WIDTH - 200) // steps), ((HEIGHT - 200)//instruments)], 2, 2)
			boxes.append((rect, (i, j)))

	return boxes

run = True
while run:
	timer.tick(fps)
	screen.fill(black)
	boxes = draw_grid(clicks)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			for i in range(len(boxes)):
				if boxes[i][0].colliderect(event.pos):
					coords = boxes[i][1]
					clicks[coords[1]][coords[0]] *= -1
	

	pygame.display.flip()
pygame.quit()