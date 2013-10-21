from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import TicketForm
from .models import Ticket, TicketComment

class TicketView(FormView):
    """"""

    template_name = 'ticket.html'
    form_class = TicketForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        form = self.get_form_class()
        if form is None:
            return redirect('dashboard')

        return super(TicketView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        # Send email

        return super(TicketView, self).form_valid(form)
    # def get_form_class(self):
    #     form_name = get_user_next_form(self.request.user)
    #     if not form_name:
    #         return None

    #     return FORMS[form_name]

    # def form_valid(self, form):
    #     u = self.request.user
    #     data = form.cleaned_data
    #     form_name = get_user_next_form(u)

    #     logger.info("User %s filled %s" % (u, form_name))

    #     Answer.objects.create(user=u, q13e_slug=form_name, data=data)

    #     # Save personal information
    #     if form_name == FORM_NAMES[0]:
    #         dirty = False
    #         if not u.first_name:
    #             u.first_name = data['hebrew_first_name']
    #             dirty = True
    #         if not u.last_name:
    #             u.last_name = data['hebrew_last_name']
    #             dirty = True
    #         if dirty:
    #             u.save()

    #         message = "\n".join(u"{label}: {html}".format(**fld) for fld in
    #                             get_pretty_answer(form, data)['fields'])
    #         mail_managers(u"{}: {hebrew_last_name} {hebrew_first_name}".format(
    #                                        _("New User"), **data), message)

    #     if get_user_next_form(u) is None:
    #         messages.success(self.request,
    #                          _("Registration completed! Thank you very much!"))
    #         mail_managers(_("User registered: %s") % u, ":-)")
    #         return redirect('dashboard')

    #     messages.success(self.request, _("'%s' was saved.") % form.form_title)

    #     return redirect('register')

    # def form_invalid(self, form):
    #     messages.warning(self.request,
    #                      _("Problems detected in form. "
    #                        "Please fix your errors and try again."))
    #     return FormView.form_invalid(self, form)
