from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    image = models.CharField(max_length=300, default='https://pusheen.com/wp-content/uploads/2020/12/What-Sweet-Quiz-SocialResults_Donut-1-e1608220861325.jpg')
    online = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Message(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sent_messages', on_delete=models.CASCADE, default=3)
    recipient = models.ForeignKey(UserProfile, related_name='received_messages', on_delete=models.CASCADE, default=4)
    message = models.CharField(max_length=1300)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
