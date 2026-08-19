
class Util:

        @staticmethod
        def get_info(data):
        
            if  hasattr(data,'__dict__') and type(data).__module__ !='builtins':
                return data.__dict__
            else:
                return data



        
def  make_2d_array(row,cols,intial_value):
     return [[intial_value for j in range(cols)] for i in range(row)]
        