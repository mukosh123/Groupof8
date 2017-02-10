import datetime

class Skills(object):
    def __init__(self):
        self.date_posted = str(datetime.datetime.now().date())
        self.skills = []
        self.studied = []

    def add_skill(self):
        skill_name = str(input('Type the skill title: '))

        self.skills.append(skill_name)
        return self.skills

    def add_studied(self):
        skill_name = str(input('Type the skill title: '))
        self.studied.append(skill_name)

       # return self.studied

    def unstudied(self):
        skills = self.skills
        studied = self.studied
        missing = []
        for skill in studied:
            if skill not in skills:
                missing.append(skill)

        for skill in skills:
            if skill not in studied:
                missing.append(skill)
        return missing





skills = Skills()
skills.add_skill()
skills.find_missing(['GH','B'])





