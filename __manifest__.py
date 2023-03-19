{
    'name': 'Latest Events',
    'version': '16.0.1.0.0',
    'sequence': '-1',

    'depends': ['base', 'sale', 'website', 'event_management'],
    'data': [
        'views/snippet.xml',
        'views/latest_event.xml',
        'views/event_details.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'latest_events/static/src/js/latest_event.js',
            'latest_events/static/src/xml/snippet_template.xml'
        ]
}
}
