from django.db import models

class Department(models.Model):
      name = models.CharField(max_length=200)
      desc = models.CharField(max_length=200)
      def __str__(self):
          return self.name

class Employee(models.Model):
      name = models.CharField(max_length=200)
      date_of_joining = models.DateTimeField('Date Of Joining')
      dept = models.ForeignKey(Department)
      def __str__(self):
          return self.name

