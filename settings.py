class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        self.screen_width = 1400
        self.screen_height = 1000
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        self.fleet_drop_speed = 10

        #Темп ускорения
        self.speed_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Изменения в ходе игры"""
        self.ship_speed = 4
        self.bullet_speed = 7
        self.alien_speed = 2

        #fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale

        self.alien_points = int(self.alien_points *self.score_scale)
