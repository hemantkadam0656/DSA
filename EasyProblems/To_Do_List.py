class To_Do_List:
    def __init__(self, lst):
        self.lst = lst

    def List_Of_works(self):        
        return lst

    def Complete_task(self):
        print('Completed task is :-', lst[0])
        lst.remove(lst[0])
        


if __name__ == '__main__':
    lst=['Bay some fruits', 'complete your study', 'go to gym', 'go to sleep']
    obj = To_Do_List(lst)
    print(obj.List_Of_works())
    print(obj.Complete_task())
    print(obj.List_Of_works())
