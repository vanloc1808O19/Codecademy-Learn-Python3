# source: http://codepad.org/trz2mPzR

# import turtle graphics package
import turtle
import turtle as tt

# create a turtle object named pen
pen = tt.Turtle()


# define a method to draw curves
def draw_curve():
    for i in range(0, 200, 1):
        # define step by step curve motion
        pen.right(1)
        pen.forward(1)


def draw_heart():
    # set the color to pink
    pen.fillcolor('red')

    # start filling the color
    pen.begin_fill()

    # draw the left line
    pen.left(140)  # 150 degrees
    pen.forward(117)

    # draw the left curve
    draw_curve()
    pen.left(120)  # 120 degrees

    # draw the right curve
    draw_curve()

    # draw the right line
    pen.forward(116)

    # end filling
    pen.end_fill()


def write_text():
    # move turtle to air
    pen.up()

    # move turtle to a given position
    pen.setpos(-90, 90)

    # move the turtle to the ground
    pen.down()

    # set the text color
    pen.color('lightgreen')

    # write the specified text in specified font style and size
    pen.write("Happy Women's Day", font=("Arial", 15, "bold"))


paused = False


def pause():
    global paused
    paused = True
    pausing()  # start watching for global paused to be changed


def pausing():
    if paused:
        tt.ontimer(pausing, 250)  # check again after delay
    # else quit checking


if __name__ == "__main__":
    draw_heart()
    write_text()
    tt.ontimer(pen.hideturtle(), 10000)
    pause()
