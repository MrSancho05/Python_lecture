class Student:
    def __init__(self, name):
        self.name = name
        self.__rating = None


    def set_rating(self, rating):
        if 0 <= rating <= 100:
            self.__rating = rating
        else:
            return 'rating xato kiritilgan, rating 0-100 oralig\'ida bo\'lishi shart!'
        
    def get_status(self):
        if self.__rating == None:
            return 'qiymat o\'rnatilmagan!'

        if self.__rating > 60:
            return 'Passed'
        else:
            return 'Failed'

student_1 = Student('Sanjarbek')
    
print(student_1.name)

student_1.set_rating(101)

print(student_1.get_status())