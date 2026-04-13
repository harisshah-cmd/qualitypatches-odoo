from odoo import http
from odoo.http import request


class QPPublicFormController(http.Controller):

    @http.route('/qp/public-form', type='http', auth='public', website=True)
    def qp_public_form(self, **kwargs):
        return request.render('qp_public_form.qp_public_form_page')

    @http.route('/qp/public-form/thank-you', type='http', auth='public', website=True)
    def qp_public_form_thank_you(self, **kwargs):
        return request.render('qp_public_form.qp_public_form_thank_you')

    @http.route('/qp/public-form/submit', type='http', auth='public', website=True, csrf=True, methods=['POST'])
    def qp_public_form_submit(self, **post):
        def to_int(value):
            try:
                return int(value) if value not in (None, '', False) else 0
            except Exception:
                return 0

        values = {
            'x_studio_order_no': post.get('order_no', '').strip(),
            'x_studio_good_pcs_1': to_int(post.get('good_pcs')),
            'x_studio_rejected_pcs': to_int(post.get('rejected_pcs')),
        }

        request.env['x_tracking_qp_orders'].sudo().create(values)

        return request.redirect('/qp/public-form/thank-you')
