class git_test:
    def __init__(self,project_name):
        self.project_name = project_name
    
    @property
    def get_project_name(self):
        print("The Project name is {0}".format(self.project_name))

git_obj = git_test("Git Project Test")
git_obj.get_project_name
