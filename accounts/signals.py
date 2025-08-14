from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_save, sender=User)
def set_superuser_role(sender, instance, created, **kwargs):
    """
    Automatically set role='admin' for superusers.
    """
    if created and instance.is_superuser:
        if instance.role != 'admin':
            instance.role = 'admin'
            instance.save(update_fields=['role'])
