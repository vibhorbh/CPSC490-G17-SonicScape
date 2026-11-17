import arcade

#function that observes if the mouse if over the text
def is_over(text, x, y, pad=10):
    return(abs(x - text.x) <= text.content_width / 2 + pad and
        abs(y - text.y) <= text.content_height / 2 + pad)