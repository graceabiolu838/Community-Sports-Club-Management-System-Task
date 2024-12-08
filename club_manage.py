class Person:
    def __init__(self, name, age, contact):
        self.name = name 
        self.age = age 
        self.contact = contact
    def set_details(self, name, age, contact):
        self.name = name
        self.age = age
        self.contact = contact
    def get_details(self):
        return f"Name: {self.name}\n\
         Age: {self.age}\n\
         Contact: {self.contact}\n"

class Member(Person):
    def __init__(self, name, age, contact, mem_id, sport, pfm_score):
        super().__init__(name, age, contact)
        self.mem_id = mem_id 
        self.sport = sport 
        self.pfm_score = pfm_score 
    def set_mem_details(self, mem_id, sport):
        self.mem_id = mem_id
        self.sport = sport 
    def add_pfm(self, score):
        self.pfm_score.append(score)
    def calc_av(self, pfm_score):
        try:
            av = sum(pfm_score)/len(pfm_score)
            return av
        except ZeroDivisionError: return 0
    def mem_summ(self):
        return f"Name: {self.name}\n\
            Age: {self.age}\n\
            Contact: {self.contact}\n\
            Membership ID: {self.mem_id}\n\
            Sport: {self.sport}\n\
            Performaance Score: {self.pfm_score}\n\
            Average Performance Score: {str(self.calc_av(self.pfm_score))}\n"
    
class Coach(Person):
    def __init__(self, name, age, contact, coach_id, spec, pay, mentees):
        super().__init__(name, age, contact)
        self.coach_id = coach_id
        self.spec = spec
        self.pay = pay
        self.mentees = mentees #["Shacarri", "Sherika", "Syndey", "Julian", "Noah", "Zharnel", "Erriyon", "Dina", "Keely"]
    def co_details(self, coach_id, spec, pay):
        self.coach_id = coach_id
        self.spec = spec
        self.pay = pay
    def assign(self, Member): #member object made in main program
        self.mentees.append(Member.name)
        return f"Coach: {self.name} is now mentoring {Member.name} in {Member.sport}\n"
    def get_mentees(self):
        x = {}
        quit
        while not quit:
            name = input("Enter mentee name\n")
            sport = input("Enter mentee sport\n")
            x[name] = sport
            quit = input("Is that all?\n")
            if quit.lower()=="yes": break
            else: continue 

        return f"{x}"
    def inc_pay(self, percent):
        #int(input("Number between 1 and 10- be wise\n"))
        self.pay*=(1+(percent*len(self.mentees))/100)
        return self.pay
    def coach_sum(self):
        return f"Name: {self.name}\n\
            Age: {self.age}\n\
            Contact: {self.contact}\n\
            Coach ID: {self.coach_id}\n\
            Speciality: {self.spec}\n\
            Salary: {self.pay}\n\
            Mentees: {self.mentees}\n"

class Staff(Person):
    def __init_(self, name, age, contact, staff_id, pos, yrs):
        super().__init__(name, age, contact)
        self.staff_id = staff_id
        self.pos = pos 
        self.yrs = yrs
    def set_det(self, staff_id, pos, yrs):
        self.staff_id = staff_id
        self.pos = pos
        self.yrs = yrs
    def inc_yrs(self):
        self.yrs+=1
    def assist_mem(self, Member): #member object made in main program
        return f"Staff {self.name} assisted {Member.name} in resolving an issue\n"
    def staff_summ(self):
        return f"Name: {self.name}\n\
            Age: {self.age}\n\
            Contact: {self.contact}\n\
            Staff ID: {self.staff_id}\n\
            Position: {self.pos}\n\
            Years of Service: {self.yrs}\n"
  
grace = Member("Grace", 17, 37826496291, "M8962", "Track", [10.54, 9.58, 10.49, 10.65, 19.31, 19.49, 50.37])
flo = Coach("Grace", 17, 37826496291, "C7014", "Track", 120000, [])
worker = Staff("Grace", 17, 37826496291, "S4836", "Club Secretary", 132)

flo.assign(grace)
flo.inc_pay(15)
grace.add_pfm(10)
grace.calc_av(grace.pfm_score)
worker.assist_mem(grace)
worker.inc_yrs()

grace.mem_summ()
flo.coach_sum()
worker.staff_summ()




