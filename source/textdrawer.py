def draw_textbox(surface, text_lines, pos, font, color=(255,255,255), bg_color=None, line_height=22):
    """Zeichnet mehrere Zeilen Text als Textfeld auf eine Surface."""
    x, y = pos
    for line in text_lines:
        text_surface = font.render(line, True, color, bg_color)
        surface.blit(text_surface, (x, y))
        y += line_height