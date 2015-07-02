class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        r1 = self.rectangleArea(A,B,C,D)
        r2 = self.rectangleArea(E,F,G,H)
        if r1 == 0:
            return r2
        if r2 == 0:
            return r1
        width = height = 0
        if G <= A: width = 0
        elif E <= A < G <= C: width = G - A
        elif E < A < C < G: width = C - A
        elif A <= E < C <= G: width = C - E
        elif A <= E < G <= C: width = G - E
        else: width = 0
        if H <= B: height = 0
        elif F <= B < H <= D: height = H - B
        elif F < B < D < H: height = D - B
        elif B <= F < D <= H: height = D - F
        elif B <= F < H <= D: height = H - F
        else: height = 0
        return r1 + r2 - width * height
    
    def rectangleArea(self, A, B, C, D):
        return (D - B) * (C - A)
        