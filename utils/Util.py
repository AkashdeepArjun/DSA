
class Util:

        @staticmethod
        def get_info(data):
        
            if  hasattr(data,'__dict__') and type(data).__module__ !='builtins':
                return data.__dict__
            else:
                return data