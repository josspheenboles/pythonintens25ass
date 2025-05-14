from django.db import models
from django.shortcuts import redirect,get_object_or_404
# Create your models here.
class Catagory2(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)

    #get catagory by id
    @classmethod
    def get_catagory_by_id(cls,id):
        return cls.objects.get(pk=id)
    @classmethod
    def getall(cls):
        return Catagory2.objects.all()
class Book2(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    publish_date=models.DateField()
    update_date=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='books/imgs',blank=True,null=True)
    catagory=models.ForeignKey(to=Catagory2,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

    @classmethod
    def getall(cls):
        return cls.objects.all()
    @classmethod
    def get_by_id(cls,id):
        return cls.objects.get(pk=id)

    @classmethod
    def Add(cls,name,pdate,image,catagoryid):
        catagoryobj = Catagory2.get_catagory_by_id(catagoryid)
        # create object of book model
        Book2.objects.create(name=name,
                             publish_date=pdate,
                             image=image,
                             catagory=catagoryobj)
    @classmethod
    def update(cls,id,name,publish_date,catagory):
        # #update
        Book2.objects.filter(pk=id).update(
            name=name,
            publish_date=publish_date,
            # image=req.FILES['Bimage'],
            catagory=Catagory2.get_catagory_by_id(id)
        )
    @classmethod
    def harddel(cls,id):
        return cls.objects.filter(pk=id).delete()

    @classmethod
    def softdelete(cls,id):
        Book2.objects.filter(pk=id).update(
            status=False
        )

    @staticmethod
    def go_to_Book_List():
        return  redirect('Blist')
