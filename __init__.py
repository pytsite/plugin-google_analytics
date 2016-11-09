"""PytSite Google Analytics Plugin.
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, tpl, permissions, settings, events
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='google_analytics')
    tpl.register_package(__name__, alias='google_analytics')

    # Permissions
    permissions.define_permission('google_analytics.settings.manage',
                                  'google_analytics@manage_google_analytics_settings', 'app')

    # Settings
    settings.define('google_analytics', _settings_form.Form, 'google_analytics@google_analytics',
                    'fa fa-line-chart', 'google_analytics.settings.manage')

    # Event handlers
    events.listen('pytsite.router.dispatch', _eh.router_dispatch)


_init()
