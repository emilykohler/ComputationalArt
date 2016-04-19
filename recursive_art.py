""" Computational Art """

import random
import math
from PIL import Image


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)

    >>> build_random_function(0, 0)
    []

    """
    function_list = ['prod', 'avg', 'cos_pi', 'sin_pi', 'exp', 'atan']
    function_list2 = ['x', 'y', 't']
    function_list3 = ['prod', 'avg', 'cos_pi', 'sin_pi', 'exp', 'exp_cos', 'x', 'y', 't']
    new_list = []


    # base cases to stop recursion when necessary/ when the max_depth is reached
    if 0 < min_depth:
        function1 = random.choice(function_list)
    elif 0 < max_depth:
        function1 = random.choice(function_list)
    elif min_depth == 0:
        return new_list
    else:
        function1 = random.choice(function_list2)

    #Recusive steps that add arguments for each function 
    if function1 == ['prod', 'avg']:
        return [function1, (build_random_function(min_depth-1, max_depth-1)]
        return [function1, (build_random_function(min_depth-1, max_depth-1)]
    elif function1 == ['cos_pi', 'sin_pi', 'exp', 'atan']:
        return [function1, (build_random_function(min_depth-1, max_depth-1)]


def evaluate_random_function(f, x, y, t):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75, 1)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02, 1)
        0.02
    """
    # looks for each possible part of the function 
    # and recursively evaluates until a number value is reached
    if f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    elif f[0] == "t":
        return t
    elif f[0] == 'sin_pi':
        argument1 = evaluate_random_function(f[1], x, y, t)
        return math.sin(argument1*math.pi)
    elif f[0] == 'cos_pi':
        argument1 = evaluate_random_function(f[1], x ,y, t)
        return math.cos(argument1*math.pi)
    elif f[0] == 'avg':
        argument1 = evaluate_random_function(f[1], x, y, t)
        argument2 = evaluate_random_function(f[2], x, y, t)
        return (argument1+argument2)/2.0
    elif f[0] == 'prod':
        argument1 = evaluate_random_function(f[1], x, y, t)
        argument2 = evaluate_random_function(f[2], x, y, t)
        return argument1*argument2
    elif f[0] == 'exp':
        argument1 = evaluate_random_function(f[1], x, y, t)
        return math.exp(argument1)
    elif f[0] == 'atan':
        argument1 = evaluate_random_function(f[1], x, y, t)
        return math.atan(argument1)



def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """

    #if input_interval_end >= val >= input_interval_end:

    input_difference = input_interval_end - float(input_interval_start)
    percentage = (float(val) - input_interval_start) / input_difference
    output_difference = output_interval_end - float(output_interval_start)
    answer = (percentage * output_difference) + output_interval_start
    return answer


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(x_size=350, y_size=350, t_size=100):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7, 9)
    green_function = build_random_function(7, 9)
    blue_function = build_random_function(7, 9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for k in range(t_size):
        for i in range(x_size):
            for j in range(y_size):
                x = remap_interval(i, 0, x_size, -1, 1)
                y = remap_interval(j, 0, y_size, -1, 1)
                t = remap_interval(k, 0, t_size, -1, 1)
                pixels[i, j] = (
                        color_map(evaluate_random_function(red_function, x, y, t)),
                        color_map(evaluate_random_function(green_function, x, y, t)),
                        color_map(evaluate_random_function(blue_function, x, y, t))
                        )

        im.save("frame"+str(k)+".png")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    generate_art()


#print(build_random_function(1, 5))
#print(remap_interval(6, 0, 10, 0, 20))
#print(evaluate_random_function(["x"],-0.5, 0.75))
# print(build_random_function(0, 0))
#print(evaluate_random_function(["y"],0.1,0.02))
#print(evaluate_random_function((build_random_function(1, 5)), .5, .3))
