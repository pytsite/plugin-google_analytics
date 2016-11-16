"""PytSite Google Analytics Pplugin Event Handlers.
"""
from pytsite import settings as _settings, assetman as _assetman, tpl as _tpl, auth as _auth, lang as _lang, \
    router as _router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    t_id = _settings.get('google_analytics.tracking_id')
    if not t_id:
        if _auth.get_current_user().has_permission('google_analytics.settings.manage'):
            msg = _lang.t('google_analytics@plugin_setup_required_warning')
            if not _settings.get('google_analytics.app_key') or not _settings.get('google_analytics.app_secret'):
                _router.session().add_warning_message(msg)
            else:
                _router.session().get_warning_message(msg)
    else:
        _assetman.add_inline(_tpl.render('google_analytics@js', {'tracking_id': t_id}))
