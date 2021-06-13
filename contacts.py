class contacts():
    def __init__(self):
        self.dic = {'Lenner':'83998355365'}
    
    def add_cont(self, name, num):
        if name not in self.dic:
            if len(num) == 11:
                self.dic[name] = num
                return True
            else:
                return False
        
        return False

    def list_conts(self):
        if self.dic:
            names = []
            nums = []

            for key, value in self.dic.items():
                names.append(key)
                nums.append(value)
            
            return names, nums
        return False
    
    def updatecont(self, contact, new_name, new_num):
        del self.dic[contact]
        self.add_cont(new_name, new_num)