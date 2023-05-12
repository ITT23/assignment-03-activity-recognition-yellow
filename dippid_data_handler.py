# used to handle the dippid data

class Data_Handler():

    def __init__(self):
        self.accelorometer_data = None
        self.button_1_data = None
        self.button_2_data = None
        self.button_3_data = None
        self.activity = 'none'
        self.activity_status = False

    def update_accelorometer_data(self, data):
        self.accelorometer_data = data
    
    def update_button_1_data(self, data):
        self.button_1_data = data

    def update_button_2_data(self, data):
        self.button_2_data = data

    def update_button_3_data(self, data):
        self.button_3_data = data

    def update_activity_label(self, new_activity_label):
        self.activity = new_activity_label

    def get_accelorometer_data(self):
        return self.accelorometer_data
    
    def get_activity(self):
        return self.activity
    
    def is_activity_status(self):
        return self.activity_status
    
    '''
    param status is False or True
    '''
    def set_activity_status(self, status):
        self.activity_status = status

    '''
    Returns the last accelorometer value for the x, y or z axis
    parameter: x, y or z
    '''
    def get_accelorometer_value(self, value_type):
        try:
            if value_type == 'x':
                return self.accelorometer_data['x']
            elif value_type == 'y':
                return self.accelorometer_data['y']
            elif value_type == 'z':
                return self.accelorometer_data['z']
        except:
            print("Wrong paramter input. Input x, y or z.")