import pygame
import random
from typing import List, Tuple

class SpaceInvaders:
    """Main game class for Space Invaders."""

    # Colors
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    YELLOW: Tuple[int, int, int] = (255, 255, 0)

    def __init__(self, width: int = 800, height: int = 600):
        """Initialize the game with screen dimensions."""
        pygame.init()

        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Invaders (Improved Version)")

        self.font = pygame.font.Font(None, 36)

        # Player
        self.player_width = 50
        self.player_height = 10
        self.player_x = self.WIDTH // 2 - self.player_width // 2
        self.player_y = self.HEIGHT - 50
        self.player_speed = 5

        # Enemies
        self.enemy_radius = 20
        self.enemies: List[dict] = []
        self.num_enemies = 5
        for _ in range(self.num_enemies):
            self.enemies.append({
                "x": random.randint(50, self.WIDTH - 50),
                "y": random.randint(30, 150),
                "speed": 2,
                "dir": 1
            })

        # Bullets
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_speed = 7
        self.bullets: List[List[int]] = []

        # Game state
        self.score = 0
        self.lives = 3
        self.high_score = 0
        self.WINNING_SCORE = 10
        self.running = True
        self.clock = pygame.time.Clock()

    def is_collision(self, enemy_x: float, enemy_y: float, bullet_x: float, bullet_y: float) -> bool:
        """Check for collision between a bullet and an enemy."""
        distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
        return distance < self.enemy_radius

    def handle_events(self) -> None:
        """Handle keyboard and quit events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bullets.append([self.player_x + self.player_width // 2, self.player_y])

    def update_player(self) -> None:
        """Move player left or right based on input."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player_x < self.WIDTH - self.player_width:
            self.player_x += self.player_speed

    def update_enemy(self) -> None:
        """Update positions of all enemies."""
        for enemy in self.enemies:
            enemy["x"] += enemy["speed"] * enemy["dir"]
            if enemy["x"] <= 0 or enemy["x"] >= self.WIDTH - self.enemy_radius:
                enemy["dir"] *= -1
                enemy["y"] += 20

            if enemy["y"] >= self.HEIGHT - 60:
                self.lives -= 1
                self.reset_enemies()
                break

    def update_bullets(self) -> None:
        """Move bullets and check for collisions."""
        for bullet in self.bullets[:]:
            bullet[1] -= self.bullet_speed
            if bullet[1] < 0:
                self.bullets.remove(bullet)
                continue

            for enemy in self.enemies:
                if self.is_collision(enemy["x"], enemy["y"], bullet[0], bullet[1]):
                    self.bullets.remove(bullet)
                    self.score += 1
                    if self.score > self.high_score:
                        self.high_score = self.score
                    enemy["x"] = random.randint(50, self.WIDTH - 50)
                    enemy["y"] = random.randint(30, 150)
                    break

    def reset_enemies(self) -> None:
        """Respawn all enemies after player is hit."""
        for enemy in self.enemies:
            enemy["x"] = random.randint(50, self.WIDTH - 50)
            enemy["y"] = random.randint(30, 150)

    def check_game_over(self) -> bool:
        """Check for win or lose condition."""
        if self.score >= self.WINNING_SCORE:
            self.show_end_screen("🎉 You Win! Press Q to Quit")
            return True
        if self.lives <= 0:
            self.show_end_screen("💀 Game Over! Press Q to Quit")
            return True
        return False

    def show_end_screen(self, message: str) -> None:
        """Display win/lose message and wait for exit."""
        self.screen.fill(self.BLACK)
        text = self.font.render(message, True, self.YELLOW)
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False
                    waiting = False

    def draw(self) -> None:
        """Draw all game elements on screen."""
        self.screen.fill(self.BLACK)

        # Player
        pygame.draw.rect(self.screen, self.BLUE, (self.player_x, self.player_y, self.player_width, self.player_height))

        # Enemies
        for enemy in self.enemies:
            pygame.draw.circle(self.screen, self.RED, (int(enemy["x"]), int(enemy["y"])), self.enemy_radius)

        # Bullets
        for bullet in self.bullets:
            pygame.draw.rect(self.screen, self.GREEN, (bullet[0], bullet[1], self.bullet_width, self.bullet_height))

        # Score & lives
        score_text = self.font.render(f"Score: {self.score} | High Score: {self.high_score}", True, self.WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, self.WHITE)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 40))

        pygame.display.update()

    def run(self) -> None:
        """Main game loop."""
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            if self.check_game_over():
                continue
            self.update_player()
            self.update_enemy()
            self.update_bullets()
            self.draw()
        pygame.quit()


if __name__ == "__main__":
    game = SpaceInvaders()
    game.run()
