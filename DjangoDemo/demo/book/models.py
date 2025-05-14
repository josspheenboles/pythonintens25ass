from django.db import models

# Create your models here.
class Catagory2(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)

    #get catagory by id
    @classmethod
    def get_catagory_by_id(cls,id):
        return cls.objects.get(pk=id)
class Book2(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    publish_date=models.DateField()
    update_date=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='books/imgs',blank=True,null=True)
    catagory=models.ForeignKey(to=Catagory2,on_delete=models.CASCADE)

    @classmethod
    def Add(cls,name,pdate,image,catagoryid):
        catagoryobj = Catagory2.get_catagory_by_id(catagoryid)
        # create object of book model
        Book2.objects.create(name=name,
                             publish_date=pdate,
                             image=image,
                             catagory=catagoryobj)
