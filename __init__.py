"""PytSite Google Analytics Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_wsgi():
    from pytsite import lang, router
    from plugins import settings
    from . import _settings_form, _eh

    # Lang globals
    lang.register_global('google_analytics_admin_settings_url',
                         lambda language, args: settings.form_url('google_analytics'))

    # Settings
    settings.define('google_analytics', _settings_form.Form, 'google_analytics@google_analytics', 'fa fa-line-chart',
                    'dev')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
