"""PytSite Google Analytics Plugin Event Handlers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import tpl as _tpl, lang as _lang, router as _router, reg as _reg
from plugins import assetman as _assetman, auth as _auth


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    t_id = _reg.get('google_analytics.tracking_id')
    if not t_id and _auth.get_current_user().has_role('dev'):
        _router.session().add_warning_message(_lang.t('google_analytics@plugin_setup_required_warning'))
    else:
        _assetman.add_inline_js(_tpl.render('google_analytics@counter', {'tracking_id': t_id}))
