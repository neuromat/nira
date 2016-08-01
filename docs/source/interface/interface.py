SUIT_CONFIG = {
    'ADMIN_NAME': 'NIRA',
    'MENU_OPEN_FIRST_CHILD': False,
    'HEADER_DATE_FORMAT': 'l, d F Y',
    'MENU': (
        {'app': 'activity', 'icon': 'icon-calendar'},
        {'app': 'dissemination', 'icon': 'icon-facetime-video'},
        {'app': 'person', 'icon': 'icon-user'},
        {'app': 'research', 'icon': 'icon-book'},
        {'app': 'scientific_mission', 'icon': 'icon-plane'},
        {'label': _('Reports'), 'url': '/reports/',
         'icon': 'icon-th', 'permissions': 'custom_auth.view_reports', 'models': (
            {'label': _('Academic works'), 'url': '/reports/academic_works'},
            {'label': _('Articles'), 'url': '/reports/articles'},
            {'label': _('Disseminations'), 'url': '/reports/dissemination'},
            {'label': _('Meetings'), 'url': '/reports/meetings'},
            {'label': _('Scientific missions'), 'url': '/reports/scientific_mission'},
            {'label': _('Seminars'), 'url': '/reports/seminars'},
            {'label': _('Training programs'), 'url': '/reports/training_programs'},
        )},
        {'label': _('Add content'), 'url': '/add_content',
         'icon': 'icon-upload', 'permissions': 'custom_auth.add_content', 'models': (
            {'label': _('Create/Update citation name'), 'url': '/add_content/citation_names'},
            {'label': _('Import papers'), 'url': '/add_content/import_papers'},
        )},
        {'label': _('Documents'), 'url': '/documents',
         'icon': 'icon-list-alt', 'permissions': 'custom_auth.create_documents', 'models': (
            {'label': _('FAPESP - appendix 5'), 'url': '/documents/anexo5'},
            {'label': _('Seminar poster'), 'url': '/documents/seminar_poster'},
        )},
        '-',
        {'app': 'cities_light', 'icon': 'icon-globe', 'label': _('Cities')},
        {'app': 'custom_auth', 'icon': 'icon-lock', 'label': _('Users')},
        {'app': 'auth', 'icon': 'icon-lock', 'label': _('Groups')},
    ),
}