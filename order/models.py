from django.db import models
from django.utils.translation import ugettext_lazy as _
from member.models import Investigator
from django.core.urlresolvers import reverse
from model_utils.managers import InheritanceManager
from django.core.mail import EmailMultiAlternatives
from django.core.mail import BadHeaderError
from django.http import HttpResponse

# Create your models here.

# Defining types of order
EVENT = 'e'
HARDWARE_SOFTWARE = 'h'
SERVICE = 's'
TICKET = 't'
DAILY_STIPEND = 'd'
REIMBURSEMENT = 'r'
ORDER_TYPE = (
    (EVENT, _('Scientific event')),
    (HARDWARE_SOFTWARE, _('Equipment / Supplies / Miscellaneous')),
    (SERVICE, _('Service')),
    (TICKET, _('Ticket')),
    (DAILY_STIPEND, _('Daily stipend')),
    (REIMBURSEMENT, _('Reimbursement')),
)

# Defining status of order
OPEN = 'o'
PENDING = 'p'
CANCELED = 'c'
APPROVED = 'a'
DENIED = 'd'
ORDER_STATUS = (
    (OPEN, _('Open')),
    (PENDING, _('Pending')),
    (CANCELED, _('Canceled')),
    (APPROVED, _('Approved')),
    (DENIED, _('Denied'))
)


class Order(models.Model):
    """

    '__unicode__'		Returns the requester.
    'class Meta'		Ordering of data by date modification.
    """
    requester = models.ForeignKey(Investigator, verbose_name=_('Investigator'))
    justification = models.TextField(_('Justification'), max_length=500)
    order_date = models.DateTimeField(_('Order date'), auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(_('Modified'), auto_now=True, blank=True)
    type_of_order = models.CharField(_('Type of order'), max_length=1, choices=ORDER_TYPE, blank=True)
    status = models.CharField(max_length=1, default=OPEN, choices=ORDER_STATUS, blank=True)
    protocol = models.IntegerField(_('Protocol'), blank=True, null=True)
    objects = InheritanceManager()

    def __unicode__(self):
        return u'%s' % self.requester

    # Description of the model / Sort by title
    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
        ordering = ('-date_modified', )

    def id_order(self):
        orders = Order.objects.filter(id=self.id).select_subclasses()
        order = orders[0]
        return '<a href="%s">%s</a>' % (reverse('admin:%s_%s_change' % (order._meta.app_label, order._meta.module_name),
                                                args=(order.id,)), order.id)
    id_order.allow_tags = True
    id_order.short_description = _('Order number')
    id_order.admin_order_field = '-id'

    # Getting the ID and showing as order number
    def order_number(self):
        return self.id
    order_number.short_description = _('Order number')
    order_number.admin_order_field = '-id'

    def save(self, *args, **kw):
        if self.pk is not None:
            check_order = Order.objects.get(pk=self.pk)
            requester_email = check_order.requester.user.email
            order_type = check_order.type_of_order

            # Check the type of request. It will be used in the email that will be sent.
            if order_type == 'e':
                order_type = 'event'
            elif order_type == 'h':
                order_type = 'hardwaresoftware'
            elif order_type == 's':
                order_type = 'service'
            elif order_type == 't':
                order_type = 'ticket'
            elif order_type == 'd':
                order_type = 'dailystipend'
            else:
                order_type = 'reimbursement'

            if check_order.status != self.status:
                subject = 'NIRA - O status do seu pedido foi alterado'
                from_email = 'neuromatematica@gmail.com'
                to = requester_email
                text_content = 'O status do seu pedido foi alterado. Acesse http://nira.numec.prp.usp.br e confira.'
                html_content = '<p></p><p>O status do seu pedido foi alterado. ' \
                               '<a href="http://localhost:8000/admin/order/%s/%s">Clique aqui</a> ' \
                               'para ver o pedido</p>' % (order_type, check_order.id)
                if subject and from_email and to:
                    try:
                        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                        msg.attach_alternative(html_content, "text/html")
                        msg.send()
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')

        super(Order, self).save(*args, **kw)


class Event(Order):
    """
    An instance of this class is a solicitation for inscription in an event.

    """
    name = models.CharField(_('Name'), max_length=200)
    url = models.URLField(_('URL'), max_length=50, blank=True, null=True)
    value = models.CharField(_('Value'), max_length=15, blank=True, null=True)
    start_date = models.DateField(_('Start date'))
    end_date = models.DateField(_('End date'))
    invitation = models.FileField(_('Invitation'))

    class Meta:
        verbose_name = _('Scientific event')
        verbose_name_plural = _('Scientific events')

    # Sets the type of order
    def save(self, *args, **kwargs):
        self.type_of_order = EVENT
        super(Event, self).save(*args, **kwargs)


class HardwareSoftware(Order):
    """
    An instance of this class is a solicitation for a new permanent material or consumption item.

    """
    type = models.TextField(_('Description'), max_length=500)
    quantity = models.IntegerField(_('Quantity'))
    url = models.URLField(_('URL'), max_length=50, blank=True, null=True,
                          help_text='Put here as an example a link from any store selling the product you want.')
    origin = models.CharField(_('Origin'), max_length=1, blank=True, null=True)
    category = models.CharField(_('Category'), max_length=1, blank=True, null=True)

    class Meta:
        verbose_name = _('Equipment / Supplies / Miscellaneous')
        verbose_name_plural = _('Equipment / Supplies / Miscellaneous')

    # Sets the type of order
    def save(self, *args, **kwargs):
        self.type_of_order = HARDWARE_SOFTWARE
        super(HardwareSoftware, self).save(*args, **kwargs)


class Service(Order):
    """
    An instance of this class is a solicitation for a third party service.

    """
    type = models.TextField(_('Description'), max_length=500)
    origin = models.CharField(_('Origin'), max_length=1, blank=True, null=True)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    # Sets the type of order
    def save(self, *args, **kwargs):
        self.type_of_order = SERVICE
        super(Service, self).save(*args, **kwargs)


class Ticket(Order):
    """
    An instance of this class is a solicitation for a new passage.

    """
    origin = models.CharField(_('Origin'), max_length=200)
    destination = models.CharField(_('Destination'), max_length=200)
    outbound_date = models.DateField(_('Outbound Date'))
    outbound_date_preference = models.CharField(_('Outbound Preferred time'), max_length=10, blank=True, null=True)
    inbound_date = models.DateField(_('Inbound Date'), blank=True, null=True)
    inbound_date_preference = models.CharField(_('Inbound Preferred time'), max_length=10, blank=True, null=True)
    type = models.NullBooleanField(_('Type of Trip'))
    type_transportation = models.NullBooleanField(_('Type of transportation'))
    note = models.CharField(_('Note'), max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = _('Ticket')
        verbose_name_plural = _('Tickets')

    # Sets the type of order
    def save(self, *args, **kwargs):
        self.type_of_order = TICKET
        super(Ticket, self).save(*args, **kwargs)


class DailyStipend(Order):
    """
    An instance of this class is a solicitation for daily stipend.

    """
    origin = models.CharField(_('Origin'), max_length=200)
    destination = models.CharField(_('Destination'), max_length=200)
    departure = models.DateTimeField(_('Departure'))
    arrival = models.DateTimeField(_('Arrival'))

    class Meta:
        verbose_name = _('Daily stipend')
        verbose_name_plural = _('Daily stipends')

    # Sets the type of order
    def save(self, *args, **kwargs):
        self.type_of_order = DAILY_STIPEND
        super(DailyStipend, self).save(*args, **kwargs)


class Reimbursement(Order):
    """
    An instance of this class is a reimbursement request.

    """
    why = models.TextField(_('Description'), max_length=500)

    class Meta:
        verbose_name = _('Reimbursement')
        verbose_name_plural = _('Reimbursements')

    # Sets the type of order
    def save(self, *args, **kwargs):
        self.type_of_order = REIMBURSEMENT
        super(Reimbursement, self).save(*args, **kwargs)