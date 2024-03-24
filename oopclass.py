class worker():
    
    appellation = 'personnel'
    work_times = '9am - 5pm'
    

    def __init__(self):
        print('Worker class created.')
        self.skills = []
        self.wage = 2000
        self.work_days = 1
    def work(self):
        self.work_days+= 1
    def promotion(self):
        self.wage +=300


mike = worker()
print('day one')
mike.skills.append('knows ruby')
mike.work
print(mike.wage)
print(mike.work_days)

print('day two')
mike.work()
mike.promotion()
print(mike.wage)
print(mike.work_days)











#self class
'''
john = worker()
john.skills.append("knows python")
print('john`s skills : ',john.skills)

george = worker()
#george.skills.append('knows c++')
print('Georges skills: ',george.skills)
'''