import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

RED[0]=250

# Paddle properties
paddle_width = 100
paddle_height = 15
paddle_x = (SCREEN_WIDTH // 2) - (paddle_width // 2)
paddle_y = SCREEN_HEIGHT - 50
paddle_speed = 10

# Ball properties
ball_size = 15
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Bricks
brick_rows = 5
brick_cols = 8
brick_width = 80
brick_height = 30
bricks = []
height=5
for row in range(brick_rows):
    brick_row = []
    for col in range(brick_cols):
        brick_x = col * (brick_width + 10) + 35
        brick_y = row * (brick_height + 10) + 35
        brick_row.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))
    bricks.append(brick_row)



# Score
score = 0

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

# Clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the list of all keys currently being pressed
    keys = pygame.key.get_pressed()

    # Move paddle
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed

    # Prevent paddle from moving out of screen
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > SCREEN_WIDTH - paddle_width:
        paddle_x = SCREEN_WIDTH - paddle_width

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x >= SCREEN_WIDTH - ball_size:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # Ball collision with paddle
    if paddle_x < ball_x < paddle_x + paddle_width and paddle_y < ball_y + ball_size < paddle_y + paddle_height:
        ball_speed_y *= -1

    # Ball collision with bricks
    for row in bricks:
        for brick in row:
            if brick.colliderect(pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
                ball_speed_y *= -1
                row.remove(brick)
                score += 1

    # Ball goes out of bounds
    if ball_y > SCREEN_HEIGHT:
        print("Game Over!")
        running = False

    # Fill screen with black background
    screen.fill(BLACK)

    # Draw paddle
    pygame.draw.rect(screen, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])

    # Draw ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_size)

    # Draw bricks
    for row in bricks:
        for brick in row:
            pygame.draw.rect(screen, RED, brick)

    # Display the score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
