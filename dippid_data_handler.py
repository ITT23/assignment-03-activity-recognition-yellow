# used to handle the dippid data

class Data_Handler():

    def __init__(self):
        self.accelorometer_data = None
        self.gyroscope_data = None

    def update_accelorometer_data(self, data):
        self.accelorometer_data = data
        #print(data)

    def update_gyroscope_data(self, data):
        self.gyroscope_data = data

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

    '''
    Returns the last gyroscope value for the x, y or z axis
    parameter: x, y or z
    '''
    def get_gyroscope_value(self, value_type):
        try:
            if value_type == 'x':
                return self.gyroscope_data['x']
            elif value_type == 'y':
                return self.gyroscope_data['y']
            elif value_type == 'z':
                return self.gyroscope_data['z']
        except:
            print("Wrong paramter input. Input x, y or z.")
    