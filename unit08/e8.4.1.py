HANGMAN_PHOTOS = dict()

HANGMAN_PHOTOS[0] = """    x-------x"""
HANGMAN_PHOTOS[1] =  """
    x-------x
    |
    |
    |
    |
    |"""

HANGMAN_PHOTOS[2] = """
    x-------x
    |       |
    |       0
    |
    |
    |"""

HANGMAN_PHOTOS[3] = """
    x-------x
    |       |
    |       0
    |       |
    |
    | """

HANGMAN_PHOTOS[4] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |  """

HANGMAN_PHOTOS[5] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |   """

HANGMAN_PHOTOS[6] = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    | """

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

num = 6
print_hangman(num)
