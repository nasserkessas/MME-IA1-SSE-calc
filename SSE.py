# Importing Math library for math.exp() function
import math

# Defining data points
t = [0.05, 0.4, 0.6, 1.2, 1.8, 2.1, 3, 4, 6, 8, 10, 12, 18, 24, 30]
C = [14, 50, 293, 401, 374, 320, 230, 158, 77, 50, 32, 23, 15.8, 10.4, 9.5]

# Defining functions with regressed values
def basic_surge_function(x):
    A = 954.069
    p = 1.59635
    b = 1.03585
    return A*((x)**p)*(math.exp(-b*(x)))


def basic_surge_function_with_horizontal_translations(x):
    A = 369.141
    c1 = 0.05
    p = 1.35462
    b = 0.914117
    c2 = 0.978783
    return A*((x-c1)**p)*(math.exp(-b*(x-c2)))


def basic_surge_function_with_horizontal_and_vertical_translations(x):
    A = 0.0000101838
    c1 = 0.05
    p = 1.79156
    b = 1.23153
    c2 = 15.0973
    d = 24.7309
    return A*((x-c1)**p)*(math.exp(-b*(x-c2)))+d


def exponential_surge_function(x):
    A = 7.5135*(10**162)
    p1 = 24.6581
    b = 369.117
    p2 = 0.0654968
    return A*((x)**p1)*(math.exp(-b*(x)**p2))


def exponential_surge_function_with_vertical_translations(x):
    A = 2.94242244*(10**162)
    p1 = 25.9558158
    b = 368.208908
    p2 = 0.0690817123
    d = 15.3940083
    return A*((x)**p1)*(math.exp(-b*(x)**p2))+d


def fractional_surge_function(x):
    A = 3816.94
    p = -1.92151
    b = 2.20671
    return A*((x)**p)*(math.exp(-(b/x)))

# Listing all the functions to calculate SSE for
functions = [basic_surge_function, basic_surge_function_with_horizontal_translations,
             basic_surge_function_with_horizontal_and_vertical_translations, exponential_surge_function, exponential_surge_function_with_vertical_translations, fractional_surge_function]

# Finding length of longest function name (for formatting output)
max_name_length = (len(max(map(lambda f: f.__name__, functions), key=len)))

# Looping through functions
for f in functions:

    # Initialsing SSE variable to 0
    SSE = 0

    # Looping through data points
    for x in t:

        # Calculating SSE (see Appendix 1 for formula)
        SSE += (f(x)-C[t.index(x)])**2
    
    # Outputting function name and SSE
    print(f.__name__.replace("_", " "), ' ' * (max_name_length-len(f.__name__)) + " SSE: " + str(SSE))