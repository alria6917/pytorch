import pygame
import random

# 游戏区域大小
WIDTH = 800
HEIGHT = 600

# 蛇身和食物大小
BLOCK_SIZE = 20

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (128, 128, 128)

# 初始化Pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇')

# 创建时钟对象，用于控制游戏帧率
clock = pygame.time.Clock()

# 显示得分
def show_score(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Score: " + str(score), True, WHITE)
    window.blit(text, (10, 10))

# 显示提示信息
def show_message(message):
    font = pygame.font.SysFont(None, 48)
    text = font.render(message, True, RED)
    window.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()

# 游戏结束
def game_over():
    show_message("Game Over!! Press C to Restart or E to Exit")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return True
                elif event.key == pygame.K_e:
                    return False

# 绘制网格
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(window, GREY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(window, GREY, (0, y), (WIDTH, y))

# 主游戏逻辑
def main():
    # 蛇的初始位置
    snake_x = WIDTH / 2
    snake_y = HEIGHT / 2

    # 蛇的初始移动方向
    snake_dx = 0
    snake_dy = 0

    # 初始化蛇的身体，初始长度为1
    snake_body = []
    body_length = 1

    # 初始化得分
    score = 0

    # 生成食物的位置
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    # 游戏循循环
    game_over_flag = False
    while not game_over_flag:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_dx = -BLOCK_SIZE
                    snake_dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake_dx = BLOCK_SIZE
                    snake_dy = 0
                elif event.key == pygame.K_UP:
                    snake_dy = -BLOCK_SIZE
                    snake_dx = 0
                elif event.key == pygame.K_DOWN:
                    snake_dy = BLOCK_SIZE
                    snake_dx = 0


        # 移动蛇的头部
        snake_x += snake_dx
        snake_y += snake_dy

        # 判断是否吃到食物
        if snake_x == food_x and snake_y == food_y:
            # 食物被吃掉后，重新生成食物的位置
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            body_length += 1
            # 增加得分
            score += 10

        # 更新蛇的身体
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)

        # 控制蛇的长度，删除多余的身体部分
        if len(snake_body) > body_length:
            del snake_body[0]

        # 检测蛇是否碰到自己的身体
        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_over_flag = True

        # 检测蛇是否碰到边界
        if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
            game_over_flag = True

        # 绘制游戏界面
        window.fill(BLACK)
        draw_grid()  # 绘制网格
        pygame.draw.rect(window, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        for segment in snake_body:
            pygame.draw.rect(window, WHITE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        # 显示得分
        show_score(score)

        # 刷新显示
        pygame.display.update()

        # 控制游戏帧率
        clock.tick(10)
    if game_over():
        main()
    else:
        pygame.quit()
        quit()

main()