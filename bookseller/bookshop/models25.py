from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    nick_name = models.CharField(max_length=30, blank=True, null=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.nick_name or ''

    
class Tasks(models.Model):
    user=models.ForeignKey(Users,on_delete=models.CASCADE,)
    title=models.CharField(max_length=100,verbose_name="Название задания")
    memo=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name="Время создания")
    datecompleted=models.DateTimeField(null=True,verbose_name="Время выполнения")
    important=models.BooleanField(default=False)

    def __str__(self):
        return self.title or ''

class Basket(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'В Корзине : {self.task.title}'

    @classmethod
    def create_or_update(self, task_id):
        task = Tasks.objects.get(id=task_id)
        baskets = Basket.objects.filter(task=task)
        if not baskets.exists():
            obj = Basket.objects.create(task=task, quantity=1)
            is_created = True
            return obj, is_created
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
            is_created = False
            return basket, is_created

    @classmethod
    def basket_remove(request, basket_id):
        basket = Basket.objects.get(id=basket_id)
        basket.delete()
        return basket




    



    
