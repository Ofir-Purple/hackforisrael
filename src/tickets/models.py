import datetime

from django.conf import settings
from django.db import models

class Ticket(models.Model):
    """
    Ticket for the ticket system. Handles the communication between
    users and admins.
    """
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name='tickets', 
        db_index=True, 
        help_text="The user whose dashboard this ticket is attached")

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    creaetd_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tickets_created', db_index=True)

    text = models.TextField(help_text="Ticket Body")

class TicketComment(models.Model):
    """
    A comment on a ticket.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="ticket_comments")
    text = models.CharField(max_length=500)

    ticket = models.ForeignKey(Ticket, related_name="comments")

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return '%s (%s)' % (self.text, self.author)
