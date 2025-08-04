# class Student:
#     def multiplication(self, a = 1, b=1, c=1,d=1):
#         print('Product :',a*b*c*d)
        
# s = Student()

# # s.multiplication(10,20)
# s.multiplication(10,20.5,30)

class Student:
    def multiplication(self, *arr):
        product = 1
        for num in arr:
            product *= num
        print('Product :', product)

s = Student()

# s.multiplication(10,20)
s.multiplication(10,20.5,30,45)