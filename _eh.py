"""PytSite Google Analytics Plugin Event Handlers
"""
from pytsite import tpl as _tpl, lang as _lang, router as _router
from plugins import assetman as _assetman, settings as _settings, auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    t_id = _settings.get('google_analytics.tracking_id')
    if not t_id and _auth.get_current_user().has_permission('google_analytics.settings.manage'):
        _router.session().add_warning_message(_lang.t('google_analytics@plugin_setup_required_warning'))
    else:
        _assetman.add_inline(_tpl.render('google_analytics@counter', {'tracking_id': t_id}))
