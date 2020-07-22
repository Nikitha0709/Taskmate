from todo_app import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='todo_home'),
    path('delete/<task_id>',views.delete_task,name='todo_delete'),
    path('edit/<task_id>',views.edit_task,name='todo_edit'),
     path('done/<task_id>',views.done_task,name='todo_done'),
     path('pending/<task_id>',views.pending_task,name='todo_pending'),
    
     
]
