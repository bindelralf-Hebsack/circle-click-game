import pygame

from game import CircleGame


WIDTH = 900
HEIGHT = 600
BACKGROUND_COLOR = (20, 20, 20)
CIRCLE_COLOR = (255, 165, 0)
TEXT_COLOR = (255, 255, 255)
MISS_COLOR = (255, 100, 100)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Circle Click Challenge")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 28)
    large_font = pygame.font.SysFont("arial", 48)

    game = CircleGame(WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not game.game_over:
                    game.handle_click(pygame.mouse.get_pos())

        if not game.game_over:
            game.update()

        screen.fill(BACKGROUND_COLOR)

        # Draw circle
        pygame.draw.circle(screen, CIRCLE_COLOR, (int(game.x), int(game.y)), game.radius)

        # Draw score and misses
        score_text = font.render(f"Punkte: {game.score}", True, TEXT_COLOR)
        misses_text = font.render(f"Fehler: {game.misses}/{game.max_misses}", True, MISS_COLOR)
        screen.blit(score_text, (20, 20))
        screen.blit(misses_text, (20, 55))

        if game.game_over:
            title = large_font.render("Game Over", True, (255, 80, 80))
            result = font.render(f"Erreichte Punktzahl: {game.score}", True, TEXT_COLOR)
            screen.blit(title, (WIDTH // 2 - 130, HEIGHT // 2 - 50))
            screen.blit(result, (WIDTH // 2 - 170, HEIGHT // 2 + 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
