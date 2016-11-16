"""PytSite Google Analytics Plugin Settings Form.
"""
from pytsite import widget as _widget, lang as _lang, settings as _settings, validation as _validation

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _setup_widgets(self):
        self.add_widget(_widget.input.Text(
            uid='setting_tracking_id',
            weight=10,
            label=_lang.t('google_analytics@tracking_id'),
            required=True,
            help=_lang.t('google_analytics@tracking_id_setup_help'),
            rules=_validation.rule.Regex(pattern='UA-\d+-\d+')
        ))

        super()._setup_widgets()
