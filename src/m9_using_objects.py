"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Eden.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(500, 500)
    c1 = rg.Circle(rg.Point(50, 50), 50)
    c1.fill_color = "blue"
    c2 = rg.Circle(rg.Point(200, 200), 150)
    c1.attach_to(window)
    c2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow()
    x = 100
    y = 200
    r = 50
    color = "blue"
    t1 = 1
    t2 = 1

    rg.Pen = ("black", t1)
    c = rg.Circle(rg.Point(x, y), r)
    c.fill_color = color

    rg.Pen = ("black", t2)
    a1 = 200
    b1 = 300
    a2 = 100
    b2 = 200
    p1 = rg.Point(a1, b1)
    p2 = rg.Point(a2, b2)
    rec = rg.Rectangle(p1, p2)

    rec.attach_to(window)
    c.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    print(str(t1) + "\n" + color + "\nPoint(" + str(float(x)) + ", " + str(float(y)) + ")" + "\n" + str(x) + "\n" + str(y))
    print(str(t2) + "\nNone\nPoint(" + str(float((a1 + a2) / 2)) + ", " + str(float((b1 + b2)/2)) + ")" + "\n" + str(float((a1 + a2) / 2)) + "\n" + str(float((b1 + b2)/2)))

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.
    window = rg.RoseWindow(500, 500)
    rg.Pen = ("black", 3)
    l1 = rg.Line(rg.Point(100, 100), rg.Point(300, 400))
    l2 = rg.Line(rg.Point(300, 300), rg.Point(50, 50))

    l1.attach_to(window)
    l2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

    m1 = l1.get_midpoint()
    b = l1._get_coordinates_for_drawing()
    print(str(m1) + "\n" + str((b[0] + b[2]) / 2) + "\n" + str((b[1] + b[3]) / 2))
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
