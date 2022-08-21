### TEST ENV ###
import duality
import time
from logistics.plugins.coloring import paint_text

myset = {
    'credit' : 'Fy', 
    'display_headline' : 'Fr', 
    'display_message' : 'Fr', 
    'output_message' : 'Fr',
    'enter_message' : 'Fr', 
    'tmp_name_list' : 'Fr',
    'tmp_func' : 'Fy',
    'warning' : 'Fr',
    'exit_message' : 'Fy'
    }

app = duality.DualityApp()

class University:

    @app.entry(option_name = 'create', option_description = 'creates the university.')
    def __init__(
        self,
        name = app.store('name', 'str', 'NAME'),
        headquarters = app.store('headquarters', 'str', 'HEADQUARTERS'),
        students = app.store('students', 'int', 'STUDENTS')
        ):
        self.name = name
        self.headquarters = headquarters
        self.students = students
        
    @app.entry(option_name = 'promote', option_description = 'creates a promotion of the university.', print_val = True)
    def show(self):
        return f'{self.name} with headquartes in {self.headquarters} and {self.students} students.'
         
if __name__ == '__main__':
    paint_text(text = '\n>>> Executed on: ' + str(duality.__version__) + ' <<<', color = 'Fy', print_trigger = True)
    time.sleep(3)
    app.script(type = 'dynamic', break_key = 'close', color_mode = 'custom', custom_color_mode = myset)
