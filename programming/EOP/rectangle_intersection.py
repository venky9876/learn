# Write a program which tests if two rectangles have a nonempty intersection. If the intersection is nonempty, return the rectangle formed by the intersection.

# NOT COMPLETE

from collections import namedtuple


def intersection_rectangle(R1,R2):

    



    return int_rect

if __name__ == "__main__":

    Rectangle = namedtuple('Rectangle', ('x', 'y', 'width', 'height'))

    R1 = Rectangle(0,0,1,1)
    R2 = Rectangle(1,1,2,2)

    int_rect = intersection_rectangle(R1,R2)

    print ("Intersection of %s and %s is %s"%(R1,R2,int_rect))

