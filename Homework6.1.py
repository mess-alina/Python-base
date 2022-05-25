from time import sleep

class TrafficLight:
    __color = None
    my_list = []
    def running(self):
        i = 0
        while i < 3:
            self.__color = 'red'
            print(self.__color)
            self.my_list.append(self.__color)
            sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            self.my_list.append(self.__color)
            sleep(2)
            self.__color = 'green'
            print(self.__color)
            self.my_list.append(self.__color)
            sleep(7)
            i +=1

    def checking(self):
        self.list2 = ['red', 'yellow', 'green']
        if self.my_list == self.list2*3:
            print("Работа светофора корректна")
        else:
            print("Нарушена работа светофора")

a = TrafficLight()
a.running()
a.checking()
