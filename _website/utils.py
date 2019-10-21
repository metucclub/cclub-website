from django.db import models
from django.utils.timezone import now
from django.utils import translation

# see https://goodcode.io/articles/django-multilanguage/
class MultilingualModel(models.Model):
    default_lang = 'tr'

    class Meta:
        abstract = True

    def __getattribute__(self, name):
        def get(x):
            return super(MultilingualModel, self).__getattribute__(x)

        value = None

        try:
            value = get(name)

            return value
        except AttributeError as e:
            value = None

            try:
                lang = translation.get_language().split('-')[0]

                if not lang:
                    lang = self.default_lang
                if not lang:
                    raise

                value = get(name + '_' + lang)
            except:
                value = None


            # If the translated variant is empty, fallback to default
            if value is None or value == '':
                value = get(name + '_' + self.default_lang)

        return value

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value

        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)

        return super(IntegerRangeField, self).formfield(**defaults)
