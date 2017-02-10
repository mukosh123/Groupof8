import datetime

class Skills(object):
    def __init__(self):
        self.date_posted = str(datetime.datetime.now().date())
        self.skills = []

    def add_skill(self):
        skill_name = str(input('Type the skill title: '))

        self.skills.append(skill_name)
        return self.skills

    def find_missing(self, studied):
        skills = self.skills
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





