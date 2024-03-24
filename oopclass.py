class worker():
    
    appellation = 'personnel'
    work_times = '9am - 5pm'
    

    def __init__(self):
        print('Worker class created.')
        self.skills = []
        self.wage = 2000
        self.work_days = 0

mike = worker()
mike.skills.append('knows ruby')
mike.wage = 1700

print(mike.wage)
print(mike.work_times)









#self class
'''
john = worker()
john.skills.append("knows python")
print('john`s skills : ',john.skills)

george = worker()
#george.skills.append('knows c++')
print('Georges skills: ',george.skills)
'''