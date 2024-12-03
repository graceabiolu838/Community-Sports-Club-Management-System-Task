class Person:
    def __init__(self, name, age, contact):
        self.name = "Grace"
        self.age = 17
        self.contact = 07954703510
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
        super.__init__(name, age, contact)
        self.mem_id = "M8962"
        self.sport = "Track"
        self.pfm_score = [10.54, 9.58, 10.49, 10.65, 19.31, 19.49, 50.37]
    def set_mem_details(self, mem_id, sport):
        self.mem_id = mem_id
        self.sport = sport 
    def add_pfm(self, score):
        self.pfm_score.append(score)
    def calc_av(self, pfm_score):
        av = sum(pfm_score)/len(pfm_score)
        return 0 if not pfm_score else av
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
        super.__init__(name, age, contact)
        self.coach_id = "C7014"
        self.spec = "Track"
        self.pay = 120000
        self.mentees = [] #["Shacarri", "Sherika", "Syndey", "Julian", "Noah", "Zharnel", "Erriyon", "Dina", "Keely"]
    def co_details(self, coach_id, spec, pay):
        self.coach_id = coach_id
        self.spec = spec
        self.pay = pay
    def assign(self, Member): #member object made in main program
        self.mentees.append(Member.name)
        return f"Coach: {self.name} is now mentoring {Member.name} in {Member.sport}\n"
    def get_mentees(self):
        x = {}
        for i in range(len(self.mentees)):
            x[self.mentees[i]] = {Member.sport}
        return x
    def inc_pay(self, percent):
        #int(input("Number between 1 and 10- be wise\n"))
        self.pay*=(1+(percent*len(self.mentees))/100)
        return self.pay

class Staff(Person):
    def __init_(self, name, age, contact, staff_id, pos, yrs):
        super.__init__(name, age, contact)
        self.staff_id = "S4836"
        self.pos = "Club Secretary"
        self.yrs = 132
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