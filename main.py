class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name 
        self.age = int(age)
        self.track = tracks
        self.score = float(score)

    def change_name(self,change_name):
        self.change_name = change_name
    def change_age(self,change_age):
        self.change_age = change_age
    def add_track(self,add_track):
        self.add_track = add_track
    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())
