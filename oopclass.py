class worker():
    print('Worker class created.')
    appellation = 'personnel'
    work_times = '9am - 5pm'
    

    def __init__(self):
        self.skills = []


john = worker()
john.skills.append("knows python")
print('john`s skills : ',john.skills)

george = worker()
#george.skills.append('knows c++')
print('Georges skills: ',george.skills)