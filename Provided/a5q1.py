# Javier Anleu Alegria
# NSID: jaa339; Student number: 11295610
# CMPT 317, Section 04
# CMPT 317: Colored Tiles Problem CSP Implementation


# CMPT 317: CSPs on the Colored Tile problem

# Copyright (c) 2022 Jeff Long
# Department of Computer Science, University of Saskatchewan

# This script reads Colored Tile problems from file, and for each one,
# outputs a CSP formalization (variables, domains, constraints)
#

import sys as sys

if len(sys.argv) < 1:
    print('usage: python', sys.argv[0], 'problem_file')
    sys.exit()

file = open(sys.argv[1], 'r')

# read the examples first
examples = []
file = open(sys.argv[1], 'r')
line = file.readline()

while line:
    #read the puzzle dimension
    dims = int(line)
    puzzle = []
    for i in range(dims):
        line = file.readline().rstrip()
        puzzle.append(line)
    examples.append(puzzle)
    line = file.readline()

file.close()

num = 1
for p in examples:
    print("------")
    print("CSP for problem", num)
    print("Puzzle:")
    for i in p:
        print(i)


    #TODO: analyze p to produce appropriate variables, domains and constraitns
    # print out that info here

    # --------------------------------------------------------------------------
    # Variables
    print("***VARIABLES***")
    # Generate set of tiles
    tiles = []
    # Rows in puzzle
    m = len(p)
    # Columns in puzzle
    n = len(p[0])
    for i in range(m):
        for j in range(n):
            tiles.append((i,j))


    # Print tiles in the puzzle
    print("Variable: Tiles")
    print(tiles, "\n")
    # Print variable of touchpoints
    print("Variable: Touchpoints")

    # --------------------------------------------------------------------------
    # Domains of variables
    print("***DOMAINS OF VARIABLES***")
    # Domain of tiles
    print("Domains of Tiles:")
    print("For each tile on the board, they have a domain {0,1}, where 0 = red "
          "and 1 = green.\n")

    # Domain of touchpoints
    print("Domain of Touchpoints:")
    print("Any set that may contain none or up to a single instance of every "
          "item in the following set:")
    print(tiles,"\n")
    # --------------------------------------------------------------------------
    # Constraints
    print("***CONSTRAINTS***")
    # Tiles can only be touched once
    print("1. Any tile on the board can only be touched once.")
    print("- Variables involved: Touchpoints")
    print("- Tuples allowed:")
    print("  * No tiles are touched.")
    for i in range(len(tiles)):
        if i == 0:
            print("  * Any 1 tile is touched.")
        else:
            print("  * Any {} distinct tiles are touched.".format(i+1))

    # Red tiles can only have odd touches on or adjacent to them
    print("2. If a tile on the board is red (has a value of 0), the count of "
          "touches on or adjacent to the tile must be odd.")
    print("- Variables involved: Tiles, Touchpoints.")
    print("- Tuples allowed:")
    print("If t = some tile and T = subset of touches on the board on or "
          "adjacent to t, then:")

    # Possible counts of touchpoints on or adjacent to red tiles
    odd = [1,3,5]
    for i in range(m):
        for j in range(len(p[i])):
            # Checks if tile is red
            if p[i][j] == "R":
                # Checks to see if tile is on any of the edges
                if i==0 or j==0 or i==m-1 or j==n-1:
                    print("  * {t = "+str((i,j))+", |T| in "+str(odd[:2])+"}")
                else:
                    print("  * {t = "+str((i,j))+", |T| in "+str(odd)+"}")

    # Green tiles can only have even touches (including 0) on or adjacent to
    # them.
    print("3. If a tile on the board is green (has a value of 1), the count of "
          "touches on or adjacent to the tile must be even (including zero).")
    print("- Variables involved: Tiles, Touchpoints.")
    print("- Tuples allowed:")
    print("If t = some tile and T = subset of touches on the board on or "
          "adjacent to t, then:")

    # Possible counts of touchpoints on or adjacent to red tiles
    even = [0,2,4]
    for i in range(m):
        for j in range(len(p[i])):
            # Checks if tile is red
            if p[i][j] == "G":
                # Checks to see if tile is on any of the corners
                if (i==0 and j==0) or (i==0 and j==n-1) or (i==m-1 and j==0) or (i==m-1 and j==n-1):
                    print("  * {t = "+str((i,j))+", |T| in "+str(even[:2])+"}")
                else:
                    print("  * {t = "+str((i,j))+", |T| in "+str(even)+"}")
    print("...")
    print("------")
    num += 1
