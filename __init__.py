"""PytSite Google Analytics Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import lang, tpl, router
    from plugins import settings, permissions
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('google_analytics_admin_settings_url',
                         lambda language, args: settings.form_url('google_analytics'))

    # Permissions
    permissions.define_permission('google_analytics.settings.manage',
                                  'google_analytics@manage_google_analytics_settings', 'app')

    # Settings
    settings.define('google_analytics', _settings_form.Form, 'google_analytics@google_analytics',
                    'fa fa-line-chart', 'google_analytics.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
