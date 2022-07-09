import logging
logging.basicConfig(filename= "test2.log" , level= logging.INFO , format= '%(levelname)s %(asctime)s %(name)s %(message)s')

class List :

    def __init__(self,l):
        self.l=l

    try :
#list
        def extrect_list(self):
            for i in self.l:
                if type(i) == list:
                    print(i)
            logging.info("we are finding all the list inside the list")
            print("\n")

#dictionary
        def extrect_dict(self):
            for i in self.l:
                if type(i) == dict:
                    return i
            logging.info("we are finding all the dictionary inside the list")
            print("\n")

#tuple
        def extrect_tuple(self):
            for i in self.l:
                if type(i) == tuple:
                    return i
                logging.info("we are finding all the tuple inside the list")
            print("\n")


        def extrect_no(self):
            for i in self.l:
                logging.info("we gpnna find all the numeric values")
                try:
                    if type(i) == list or type(i) == tuple or type(i) == set:
                        for j in i:
                            if type(j) == int:
                                print(j)
                    elif type(i) == dict:
                        for k, v in i.items():
                            if type(k) == int or type(v) == int:
                                print(k)
                                print(v)
                except Exception as e:
                    print(e)
            print("\n")

        def sum_allno(self):
            logging.info("we are gonna do sumetion of all numeric data")
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            l1.append(k)
                            l1.append(v)
            print(l1)
            sum(l1)
            print("\n")

        def odd_out(self):
            logging.info("finding out all odd values from list ")
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l1.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        if type(k) == int or type(v) == int:
                            l1.append(k)
                            l1.append(v)
            for i in range(len(l1)):
                if l1[i] % 2 == 0:
                    pass
                else:
                    print(l1[i])
                    logging.info("we fin the is of odd no %s ", l1[i])

            print("\n")
        def find_inuron(self):
            logging.info("we are gonna find inuron from given list")
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l1.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        l1.append(k)
                        l1.append(v)
            for i in range(len(l1)):
                if l1[i] == 'ineuron':
                    print(l1[i])
                    logging.info("we get %s", l1[i])
            print("\n")

        def no_of_times(self):
            logging.info("we are gonna find occurnes of all ")
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l1.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        l1.append(k)
                        l1.append(v)
            print(l1)
            a = set(l1)
            c = list(a)
            for i in c:
                print(i, ':', l1.count(i))
                logging.info("we get all the no ")
            print("\n")

        def no_dict_key(self):
            for i in range(len(self.l)):
                if type(self.l[i]) == dict:
                    a = self.l[i]
                    b = a.keys()
                    print(b)
                    print(len(b))
                    logging.info("we are finding all keys availebal in list and no keys %s", len(b))
            print("\n")

        def all_str(self):
            logging.info("we are going to find all string type values")
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l1.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        l1.append(k)
                        l1.append(v)
            for i in range(len(l1)):
                if type(l1[i]) == str:
                    print(l1[i])
                    logging.info("we get %s" , l1[i])

            print("\n")
        def multi_ind(self):
            logging.info("we are going to find all type of data sepret and then multiplication done")
            for i in self.l:
                m = 1
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            m = m * j
                    print('Multipilcation of', type(i), 'is', m)
                    logging.info('Multipilcation of %s is %s ',type(i) , m)
                if type(i) == dict:
                    for v,k in i.items():
                        if type(v) == int or type(k) == int:
                            m = m * v
                            m = m * k
                    print('Multipilcation of', type(i), 'is', m)
                    logging.info('Multipilcation of %s is %s ', type(i), m)
            print("\n")

        def makenew(self):
            l1 = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l1.append(j)
                elif type(i) == dict:
                    for k, v in i.items():
                        l1.append(k)
                        l1.append(v)
            print(l1)
            logging.info("we are just make new list %s ",l1)
            print("\n")

        def alpha_num(self):
            d = {}
            for i in self.l:
                if type(i) == dict:
                    d.update(i)

            for i in list(d.keys()):
                n = str(i)
                if n.isalnum() == True:
                    print(n)
            print("\n")




    except Exception as e :
        print(e)


a = List([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,{'k1' : "sudh", 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8} , ['ineuron', 'data science']])
#try to extract all the list entity ?
a.extrect_list()
#try to extract all the dict entity ?
a.extrect_dict()
#try to extract all the tuple entity ?
a.extrect_tuple()
#try to extract all the numerical data it may be a part of dict key and values?
a.extrect_no()
#try to give summation of all the numeric data ?
a.sum_allno()

#try to filter out all the odd values out all numeric data which is a part of a list ?
a.odd_out()
#try to extrect 'ineruon' out of this data ?
a.find_inuron()

#try to find out a number of occurances of all of all the data ?
a.no_of_times()
#try to  find out a number of keys in dict element
a.no_dict_key()
#try to filter out all the string data ?
a.all_str()
#try to find out multiplication of all numeric value in the individual collection inside data set ?
a.multi_ind()
#try to unwrape all the collection inside collection and create a flat list ?
a.makenew()
#alpha num find in given list
a.alpha_num()


class String :
    def __init__(self, str):
        self.str = str

    try:
        def slice(self):
            print(self.str[1:300:3])
            logging.info("we are goning to doing sliceing %s " , self.str[1:300:3])

        def rev(self):
            print(self.str[-1:0:-1])
            logging.info("we are g0ning to doing revers %s ", self.str[-1:0:-1])

        def convert_split(self):
            upper_str = self.str.upper()
            logging.info("we are covert all string in to upper case %s " , self.str.upper())
            print(upper_str.split())
            logging.info("split upper case %s ", upper_str.split())

        def low(self):
            print(self.str.lower())
            logging.info("we are covert all string in to tower case %s ", self.str.lower())

        def cap(self):
            print(self.str.capitalize())
            logging.info("capitalize all the string %s " ,self.str.capitalize() )


    except Exception as e :
        print(e)


s = String("this is My First Python programming class and i am learNING python string and its function")
# Try to extract data from index one to index 300 with a jump of 3
s.slice()
# Try to reverse a string without using reverse function
s.rev()
# Try to split a string after conversion of entire string in uppercase
s.convert_split()
# Try to convert the whole string into lower case
s.low()
# Try to Capitalize the whole string.
s.cap()




