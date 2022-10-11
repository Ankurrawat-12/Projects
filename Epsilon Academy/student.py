class Student:
    def __init__(self, name, fathers_name, mothers_name, age, phone_no, clas_s, i_d, joining_month, fees,
                 jan=None, feb=None, march=None,
                 april=None, may=None, june=None, july=None, aug=None, sept=None, octo=None, nov=None,
                 dec=None, stream=None):
        self.name = name
        self.fathers_name = fathers_name
        self.mothers_name = mothers_name
        self.age = age
        self.stream = stream
        self.phone_no = phone_no
        self.clas_s = clas_s
        self.i_d = i_d
        self.joining_month = joining_month
        self.fees = fees
        self.jan = jan
        self.feb = feb
        self.march = march
        self.april = april
        self.may = may
        self.june = june
        self.july = july
        self.aug = aug
        self.sept = sept
        self.octo = octo
        self.nov = nov
        self.dec = dec

    def make_primary_list(self):
        # primary_data = [self.i_d, self.name, self.fathers_name, self.mothers_name, self.clas_s, self.stream,
        #                 self.phone_no, self.age]
        primary_data = {"ID": self.i_d, "Name": self.name, "Fathers Name": self.fathers_name,
                        "Mothers Name": self.mothers_name, "Class": self.clas_s, "Stream": self.stream,
                        "Phone Number": self.phone_no, "Age": self.age, "Joining Month": self.joining_month,
                        "Fees": self.fees}
        months = {"January": self.jan, "February": self.feb, "March": self.march, "April": self.april, "May": self.may,
                  "June": self.june, "July": self.july, "August": self.aug, "September": self.sept,
                  "October": self.octo, "november": self.nov, "December": self.dec}
        return primary_data

