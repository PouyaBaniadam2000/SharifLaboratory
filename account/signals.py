from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from threading import Timer

from account.models import OTP


@receiver(post_save, sender=OTP)
def schedule_deletion(instance, created, **kwargs):
    if created:
        deletion_time = instance.created_at + timezone.timedelta(seconds=100)
        t = Timer((deletion_time - timezone.now()).total_seconds(), instance.delete)
        t.start()
        instance.delete_at = deletion_time
        instance.save(update_fields=['delete_at'])
