from django.shortcuts import render, redirect
from django.views import View
from .forms import DefaultForm
import pika


class DefaultView(View):
    def get(self, request):
        default_form = DefaultForm()
        context = {
            "form": default_form,
        }
        return render(request, "sqs/default.html", context)

    def post(self, request):

        #Create a new instance of the Connection object
        #parameters = pika.URLParameters('amqp://pika:pika@rabbit-service:5672/vhost_pika')
        credentials = pika.PlainCredentials('pika', 'pika')
        parameters = pika.ConnectionParameters('rabbitmq-service',
                                            5672,
                                            'pika_vhost',
                                            credentials)

        connection = pika.BlockingConnection(parameters)
        #Create a new channel with the next available channel number or pass in a channel number to use
        channel = connection.channel()
        #Declare queue, create if needed. This method creates or checks a queue. When creating a new queue the client can specify various properties that control the durability of the queue and its contents, and the level of sharing for the queue.
        channel.queue_declare(queue='hello')
        

        default_form = DefaultForm(request.POST)

        if default_form.is_valid():
            default = default_form.save()
            message = '{} {}'.format(default.first_number, default.second_number)
            channel.basic_publish(exchange='', routing_key='hello', body=message)    
            connection.close()    

            return redirect('default')

        