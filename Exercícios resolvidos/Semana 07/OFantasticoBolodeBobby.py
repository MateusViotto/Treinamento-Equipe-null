import math

class Point:
    def __init__(self, x, y) -> None:
        self.x: float = x
        self.y: float = y

def eqGeralReta(p1: Point, p2: Point) -> tuple[float,float,float]:
    m = (p1.y - p2.y)/(p1.x - p2.x)

    a = p1.x
    b = p1.y
    c = p2.x
    d = p2.y

    A = 1
    B = ((b-d)/(c-a))
    C = (d*a-b*a-b*c+b*a)/(c-a)

    return (A,B,C)

    '''
        (a,b) e (c,d)

        m = (d-b)/(c-a)

        y-b = ((d-b)/(c-a))*(x-a) 

        y-b = (d-b)*(x-a)/(c-a)

        y = (dx-da-bx+ba)/(c-a) + b

        y = [(dx-da-bx+ba) + b(c-a)]/(c-a)

        y = (dx-da-bx+ba+bc-ba)/(c-a)

        y = [d/(c-a)]*x - [b/(c-a)]*x + (-da+ba+bc-ba)/(c-a)

        y = ((d-b)/(c-a))*x + (-da+ba+bc-ba)/(c-a)

        y + ((b-d)/(c-a))*x + (da-ba-bc+ba)/(c-a) = 0
    '''

def distPontoReta(p: Point, reta: tuple[float,float,float]):

    x = p.x
    y = p.y
    A = reta[0]
    B = reta[1]
    C = reta[2]

    return abs(A*x + B*y + C) / math.sqrt(A**2 + B**2)
