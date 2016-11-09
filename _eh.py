"""PytSite Google Analytics Pplugin Event Handlers.
"""
from pytsite import settings as _settings, assetman as _assetman, tpl as _tpl

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    t_id = _settings.get('google_analytics.tracking_id')
    if not t_id:
        return

    _assetman.add_inline(_tpl.render('google_analytics@js', {'tracking_id': t_id}))
