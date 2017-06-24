# Pencil
Simple Tkinter drawing app.

Intended to be used as a quick and dirty visualization app for
C software. Just pipe the out of the C program to it.

Recognized commands:
* `rectangle from_x from_y to_x to_y`
  Draw a rectangle.
* `line from_x from_y to_x to_y`
  Draw a line.
* `point x y`
  Draw a point as a very small rectangle.
* `changesize new_width new_height`
  Change the canvas size.
* `changebg new_color`
  Change the background color.
* `changecolor new_drawing_color`
  Change color used to draw primitives.
* `txt center_x center_y the_words...`
  Draws a sentence.
* `clear`
  Delete all primitives in the canvas.
* `update`
  Refresh the canvas.
* `quit`
  Quits.
