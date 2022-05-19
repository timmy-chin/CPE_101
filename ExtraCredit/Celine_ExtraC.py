class student:
    def __init__(self,name,marks):
        self.name = name
        self.mark = marks
    def __lt__(self,other):
        return self.marks < other.marks
    def __gt__(self,other):
        return self.marks > other.marks


    def marks(self):
        mark_list=[]
        for i in range(5):
            mark = self.mark
            mark_list.append(mark)
        return mark_list

    def sort(self, mark_list):
        n_list = []
        start = mark_list[0]
        for val in mark_list:
            if val > start:
                start = val
                n_list.append(val)







