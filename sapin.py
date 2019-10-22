#config: utf-8

import sys

if len(sys.argv) < 2:
    sys.exit("\n\n\t*** Erreur ***\n Veuillez renseigner une taille pour le sapin \n\n\
            \t(1) : petit\n\
            \t(2) : moyen\n\
            \t(3) : grand\n\
            \t(3+): bûcheron tiers\n")

class Tree:

    """
        I'm Groot
    """

    def __init__(self, size = 1, stars = 1, spaces = 3, noel = False):
        self.size = size
        self.base_size = 0
        self.stars = stars
        self.spaces = spaces
        self.noel = noel

    def get_base_size(self):
        stars_base = 1
        lines = 4
        for i in range(0, size):
            for j in range(0, lines - 1):
                stars_base += 2
            stars_base -= 2
            lines += 1
        stars_base += 2
        self.base_size = stars_base
        self.spaces = int(self.base_size / 2)

    def print_leaves(self):
        lines = 4
        spaces_left = self.spaces
        for i in range(0, self.size):
            for k in range(0, lines):
                for l in range(0, spaces_left):
                    print(" ", end = '')
                for m in range(0, self.stars):
                    print("*", end = '')
                spaces_left -= 1
                self.stars += 2
                print("")
            lines += 1
            self.stars -= 4
            spaces_left += 2

    def print_trunc(self):
        spaces_trunc = self.spaces - int((size / 2))
        if self.size % 2 == 0:
            trunc = self.size + 1
        else:
            trunc = self.size
        spaces_right = self.base_size - (spaces_trunc + trunc)
        for i in range(0, size + 2):
            for j in range(0, spaces_trunc):
                if i == 0 and j != spaces_trunc - 1 and j % 2 == 1:
                    print("|", end='')
                elif i == 1 and j != spaces_trunc - 1 and j % 2 == 1:
                    print("o", end = '')
                else:
                    print(" ", end = '')
            for k in range(0, trunc):
                print("|", end = '')
            for j in range(0, spaces_right):
                if i == 0 and j > 0 and j % 2 == 1:
                    print("|", end = '')
                elif i == 1 and j > 0 and j % 2 == 1:
                    print("o", end = '')
                else:
                    print(" ", end = '')
            print("")

size = int(sys.argv[1])
t1 = Tree(size)             # Instanciation du sapin
t1.get_base_size()          # Définition de la base du sapin
t1.print_leaves()           # On affiche les épines
t1.print_trunc()            # On affiche le tronc

