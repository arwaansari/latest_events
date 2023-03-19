from odoo import http
from odoo.http import request


class Sales(http.Controller):
    @http.route(['/latest_events'], type="json", auth="public")
    def latest_events(self):
        latest_events = request.env['event.booking'].sudo().\
            search([], order='create_date desc', limit=4)
        # print(latest_events)
        values = {{
                events.name: events.id
            }for events in latest_events}
        # for events in latest_events:
        #     values.update()
        print(values)
        return values

    @http.route(["/latest_events/event_details"], type="http", auth="public",
                website=True, csrf=False)
    def event_details(self, **kwargs):
        event_id = int(kwargs.get('event_id'))
        event = request.env['event.booking'].search([('id', '=', event_id)])
        values = {}
        values.update({

            'event_id': event
        })
        print(event.booking_date)
        print(values)
        return request.render("latest_events.event_details",
                              values)
