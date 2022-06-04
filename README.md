This is the code written when I was watching George Hotz's livestream where he codes twitchess. 
Below are some random notes that I have taken along.

Zero knowledge chess engine

*Establish the search tree
*Use a neural network to prune the search tree

*Minmax concept has game theory

def - value netowrk - function that takes in a board and returns a value.

Need neural representation of the board

8*8 = 64 with the following pieces possible

State:

7 possible pieces
black move and white moves and blank states
Pieces(2+7*2 = 16):
*Universal
**Blank
**Blank (En passant)
*Pieces
**Pawn
**Bishop
**King
**Queen
**Knight
**Rook
**Rook(can castle)

Other potential pieces of state on the board

Extra state:
*To move

8x8x4 + 1 = 257 bits (vector of 0 or 1 )

Every chess position is represented in 257 bits

*Whether the king has moved or not and if it is the part of the board state ?
*Board put the pieces on the board but you cannot have a board full of queens.

Other way is to see if it is the moved king or not a moved king state ?
*Leela chess can be referred maybe ?

Traditional way to write a chess engine
 - Search all the legal moves

*Using python-chess library now. 

We need data of chess games in PGN formats 
Get that from here - https://www.pgnmentor.com/files.html - I will be using Anand's games. 

V = f(state)

V is : 
    All position where white wins = 1
    All position where draw = 0
    All position where black wins = -1