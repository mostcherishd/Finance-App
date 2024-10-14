from django.db import models



class MyModel(models.Model):
    plans=(
    ("Basic", "Basic"), 
    ("Platnum", "Platnum"), 
    ("Elite", "Elite"), 
    ("Exclusive", "Exclusive"), 
    )

    username = models.CharField(max_length=100)
    plan = models.CharField(max_length=20, choices=plans)
    wallet_address = models.CharField(max_length=100)
    amount = models.IntegerField(null=True)

    def __str__(self):
        return self.wallet_address