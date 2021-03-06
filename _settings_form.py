"""PytSite Google Analytics Plugin Settings Form.
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Text(
            uid='setting_tracking_id',
            weight=10,
            label=_lang.t('google_analytics@tracking_id'),
            required=True,
            help=_lang.t('google_analytics@tracking_id_setup_help'),
            rules=_validation.rule.Regex(pattern='UA-\d+-\d+')
        ))

        super()._on_setup_widgets()
