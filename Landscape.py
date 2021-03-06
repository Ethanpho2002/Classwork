import arcade

WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.SKY_BLUE)

arcade.start_render()
# Begin drawing

# Grass
arcade.draw_lrtb_rectangle_filled(0, WIDTH, 100, arcade.color.DARK_GREEN)

# Tree One
arcade.draw_triangle_filled(160, 240, 175, 250, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(190, 210, 100, 175, arcade.color.DARK_BROWN)

# Sun
arcade.draw_circle_filled(590, 540, 430, 380, arcade.color.YELLOW)

# Tree Two
arcade.draw_triangle_filled(440, 520, 125, 200, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(470, 490, 100, 175, arcade.color.DARK_BROWN)

# Tree Three
arcade.draw_triangle_filled(485, 565, 125, 200, arcade.color.BROWN)
arcade.draw_lrtb_rectangle_filled(515, 535, 100, 175, arcade.color.DARK_BROWN) 

# End drawing
arcade.finish_render()
arcade.run()
