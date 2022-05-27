class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        
        
    def change_name(self, name):
        self.name = name
        return (print("New name is", self.name))
        
    
    def add_track(self, new_track):
        self.new_track = new_track
        (self.tracks).append(self.new_track)
        return {
        print(f"New track added! {self.name} now has the following tracks: {self.tracks}")
        }
        
        
    def get_score(self):
          return {
          print(f"{self.name} scored {self.score}")
            }


    def change_age(self, age):
        self.age = age
        return (print("New age is", self.age))
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
