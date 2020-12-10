def check_triangle():
    side1 = int(input("Please enter the first side"))
    side2 = int(input("Please enter the first side"))
    side3 = int(input("Please enter the first side"))

    if side1 > (side2 + side3):
        print("You cannot form a triangle with this")
    elif side2 > (side1 + side3):
        print("Nope, wont happen")
    elif side3 > (side2 +side1):
        print("Never")
    else:
        print("This would form a triangle")

# check_triangle()


# def draw(t, length, n):
#     if n == 0:
#         return
#     angle = 50
#     fd(t, length*n)
#     lt(t, angle)
#     draw(t, length, n-1)
#     rt(t, 2*angle)
#     draw(t, length, n-1)
#     lt(t, angle)
#     bk(t, length*n)
    