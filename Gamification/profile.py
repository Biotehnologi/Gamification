import json
class Profile():
    def __init__(self, username):
        self.username = username

        with open('database/data_users.json') as read_link:
            self.json_content = json.load(read_link)

        with open('database/achivement.json') as read_link:
            self.achivement_content = json.load(read_link)

        self.name = str(self.json_content[self.username]['name'])
        self.id = str(self.json_content[self.username]['id'])
        self.admin = str(self.json_content[self.username]['admin'])

        #print(self.achivement_content[self.json_content[self.name]['id']])
        #print(self.achivement_content)
        #for line_first in self.json_content[self.name]['id']:
            #print(line_first)

    def alert_profile(self):
        print("Profile")
        print("Name: " + str(self.name))
        print("id: " + str(self.id))
        print("admin: " + str(self.admin))
        print("\n Achivements: \n")
        for line in self.achivement_content:
            if self.achivement_content[line]['id'] == self.id and self.achivement_content[line]['admin'] == self.admin:
                print(self.achivement_content[line]['code'])

    def run(self):
        pass

while True:
    login = str(input("Введите логин: \n"))
    if login != "":
        newProfile = Profile(login)
        newProfile.alert_profile()
    else:
        break

input("Wait")
