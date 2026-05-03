import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class EasyButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (0, 220, 0)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        super().prep_msg(msg)
        
    def draw_button(self):
        super().draw_button()

class MediumButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (255, 160, 28)
        self.rect.left = self.screen_rect.left
        self.prep_msg(msg)

    def prep_msg(self, msg):
        super().prep_msg(msg)
        
    def draw_button(self):
        super().draw_button()

class HardButton(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (255, 28, 28)
        self.rect.right = self.screen_rect.right
        self.prep_msg(msg)

    def prep_msg(self, msg):
        super().prep_msg(msg)
        
    def draw_button(self):
        super().draw_button()