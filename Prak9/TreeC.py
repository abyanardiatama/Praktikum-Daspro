# Nama		:
# NIM		:
# Tanggal	:
# Deskripsi	:

from TreeB import *


def display(P):
    lines, _, _, _ = display_aux(P)
    for line in lines:
        print(line)


def display_aux(P):
    if IsOneElmtPB(P):
        line = '%s' % Akar(P)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    elif IsUnerLeft(P):
        lines, n, p, x = display_aux(Left(P))
        s = '%s' % Akar(P)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    elif IsUnerRight(P):
        lines, n, p, x = display_aux(Right(P))
        s = '%s' % Akar(P)
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    else:
        left, n, p, x = display_aux(Left(P))
        right, m, q, y = display_aux(Right(P))
        s = '%s' % Akar(P)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def BSearchX(P, X):
    if(IsTreeEmpty(P)):
        return False
    else:
        if Akar(P) == X:
            return True
        elif Akar(P) < X:
            return BSearchX(Right(P), X)
        else:
            return BSearchX(Left(P), X)


def AddX(P, X):
    if (IsTreeEmpty(P)):
        return MakePB(X, [], [])
    elif(X > Akar(P)):
        return MakePB(Akar(P), Left(P), AddX(Right(P), X))
    else:
        return MakePB(Akar(P), AddX(Left(P), X), Right(P))


def BinSearchTree(L, P):
    if(IsEmpty(L)):
        return P
    else:
        return BinSearchTree(Tail(L), AddX(P, FirstElmt(L)))


def MakeBinSearchTree(L):
    return BinSearchTree(L, [])


def DelBTree(P, X):
    if(IsTreeEmpty(P)):
        return P
    else:
        if(Akar(P) == X):
            if(IsOneElmtPB(P)):
                return []
            elif(IsUnerLeft(P)):
                return Left(P)
            elif(IsUnerRight(P)):
                return Right(P)
            else:
                if(IsExistRight(P)):
                    if(IsUnerRight(P)):
                        return MakePB(Akar(Right(P)), Left(P), Right(Right(P)))
                    else:
                        return MakePB(Terkiri(Right(P)), Left(P), DelBTree(Right(P), Terkiri(Right(P))))
                else:
                    return MakePB(Akar(Left(P)), Right(Left(P)), Right(P))
        else:
            if(X > Akar(P)):
                return MakePB(Akar(P), Left(P), DelBTree(Right(P), X))
            else:
                return MakePB(Akar(P), DelBTree(Left(P), X), Right(P))


P3 = MakeBinSearchTree([7, 10, 8, 6])
