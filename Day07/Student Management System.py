class student:
    def __init__(self, name , marks ):
        self.name = name 
        self.marks = marks 
    def grade(self):
        if self.marks >= 90:
            return 'a'
        elif self.marks >= 80:
            return 'b'  
        elif self.marks >= 70:
            return 'c'  
        elif self.marks >= 60:
            return 'd'
        else:
            return 'f'