import random as rd
import chess as ch
from more_itertools import first


class engine:
    def __init__(self,board,maxDepth,color):
        self.board=board
        self.maxDepth=maxDepth
        self.color=color

    def best_move(self):
        return self.engine(None,1)

    def eval(self):
        evaluation = 0
        for i in range(64):
            evaluation +=self.squareResPoints(i)
        evaluation += self.mate()+0.001*rd.random() +self.opening()
        return evaluation

    def mate(self):
        if(self.board.legal_moves.count() == 0):
            if(self.color==self.board.turn):
                return -999
            else:
                return 999
        else:
            return 0
    
    def opening(self):
        if (self.board.fullmove_number<10):
            if (self.board.turn == self.color):
                return 1/30 * self.board.legal_moves.count()
            else:
                return -1/30 * self.board.legal_moves.count()
        else:
            return 0
    
    

    def squareResPoints(self, square):
        pieceValue = 0
        if(self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        elif (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5
        elif (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3
        elif (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3
        elif (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 9

        if (self.board.color_at(square)!=self.color):
            return -pieceValue
        else:
            return pieceValue

    def engine(self,move,depth):
        if (self.maxDepth == depth or self.board.legal_moves.count() == 0) :
            return self.eval()
        else :
            moves = list(self.board.legal_moves)
            newmove = None
            if(depth % 2 != 0):
                newmove = float("-inf")
            else :
                newmove = float("inf")
            evalu=float(0)
            for i in moves:
                self.board.push(i)

                value = self.engine(newmove,depth+1)
                # print(value)
                if(value > newmove and depth % 2 !=0):
                    if(depth==1):
                        firstmove = i
                        evalu=value
                    newmove=value
                    
                
                if(value < newmove and depth % 2 ==0):
                    newmove = value

                
                if(move != None and value < move and depth % 2 == 0):
                    self.board.pop()
                    break


                elif(move != None and value > move and depth % 2 != 0):
                    self.board.pop()
                    break
                self.board.pop()
            
            if(depth > 1):
                # print(newmove)
                return newmove
            else:
                print(evalu)
                return firstmove