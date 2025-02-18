from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
    print("Signal executed synchronously")

# Example: Printing current thread
import threading
@receiver(post_save, sender=MyModel)
def print_thread(sender, instance, created, **kwargs):
    print(f"Signal is running in thread: {threading.current_thread().name}")
