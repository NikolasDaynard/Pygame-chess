import pygame

class imageRenderer:
    images = {}
    def renderImage(self, screen, image, x, y, w, h):
        try:
            if self.images[image] is None:
                self.images[image] = pygame.image.load(image)
        except KeyError:
            self.images[image] = pygame.image.load(image)

        rect = pygame.Rect(x, y, w, h)
        scaled_image = pygame.transform.scale(self.images[image], (rect.width, rect.height))
        screen.blit(scaled_image, rect.topleft)