from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser, Profile, Customer, Manager

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def update_profile(sender, instance, created, **kwargs):
    if created==False:
        instance.profile.save()



# @receiver(post_save, sender=CustomUser)
# def create_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def update_customer(sender, instance, created, **kwargs):
#     if created==False:
#         instance.customer.save()

# @receiver(post_save, sender=CustomUser)
# def create_manager(sender, instance, created, **kwargs):
#     if created:
#         Manager.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def update_manager(sender, instance, created, **kwargs):
#     if created==False:
#         instance.manager.save()
