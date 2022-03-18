'''
Created on 12/1/2020
@author:   Dylan Tran
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 12 - Date class
'''

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
from cs115 import *

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
 as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
     whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
        '''Test all the instances that they are different to recieve the next date'''
        date=Date(self.month,self.day,self.year)
        '''New Year Decemeber 31 to January 1'''
        if self.month==12 and self.day==31:
            self.month=1
            self.day=1
            self.year=self.year+1
            '''Leap Year'''
        elif self.month==2 and self.day==28 and date.isLeapYear() == True:
            self.day=self.day+1
            '''If the day is greater than the days in month go to next month '''
        elif self.day>=DAYS_IN_MONTH[self.month]:
            self.month=self.month+1
            self.day=1
        else:
            '''Regular tomorrow'''
            self.day+=1

    def yesterday(self):
        date=Date(self.month,self.day,self.year)
        '''if its 1/1/2020 go to 12/31/2019 '''
        if self.month==1 and self.day==1:
            self.month=12
            self.day=31
            self.year=self.year-1
        elif self.month==3 and self.day==1 and date.isLeapYear()==True:
            self.day=29
            self.month-=1
        elif self.month==3 and self.day==1 and date.isLeapYear()==False:
            self.day=28
            self.month=2
        elif self.day==1:
            self.month=self.month-1
            self.day=DAYS_IN_MONTH[self.month]
        else:
            self.day-=1
        
    def addNDays(self, N):
        '''print all dates in range N and the ogrinal date'''
        for element in range(N):
            print(self)
            self.tomorrow()
        print(self)

    def subNDays(self, N):
        '''print all dates in range N and the ogrinal date'''
        for element in range(N):
            print(self)
            self.yesterday()
        print(self)

    def isBefore(self, d2):
        '''If date is before another one. Exact opposite to isAfter'''
        if self.year<d2.year:
            return True
        elif self.month<d2.month and self.year==d2.year:
            return True
        elif self.day<d2.day and self.month==d2.month and self.year==d2.year:
            return True
        else:
            return False

    def isAfter(self, d2):
        '''Compare the years together and months and days. One step at a time'''
        if self.year>d2.year:
            return True
            '''Compare if month (ex 12) is greater than another(3) in the same year '''
        elif self.month>d2.month and self.year==d2.year:
            return True
            '''Compare when day is greater than another in the same month and year '''
        elif self.day>d2.day and self.month==d2.month and self.year==d2.year:
            return True
        else:
            return False

    def diff(self, d2):
        date1=self.copy()
        date2=d2.copy()
        differ=0
        if date1.isBefore(date2):
            while date1.isBefore(date2):
                differ -=1
                date1.tomorrow()
            return differ
        else:
            while date1.isAfter(date2):
                differ +=1
                date1.yesterday()
            return differ


    def dow(self):
        '''Compare dates with previous and future dates. Get the number that differeniates them and divide by 7. if number is 0 it is monday'''
        dow=self.diff(Date(10, 28, 1929))
        Order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if abs(dow) % 7==0:
            return Order[0]
        elif abs(dow) % 7==1:
            return Order[1]
        elif abs(dow) % 7==2:
            return Order[2]
        elif abs(dow) % 7==3:
            return Order[3]
        elif abs(dow) % 7==4:
            return Order[4]
        elif abs(dow) % 7==5:
            return Order[5]
        elif abs(dow) % 7==6:
            return Order[6]
        
