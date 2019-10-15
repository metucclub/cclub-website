from django.db import models
from django.utils.timezone import now
from django.utils import translation

# see https://github.com/praekelt/django-preferences/blob/develop/preferences/
class SingletonManager(models.Manager):
    def get_queryset(self):
        queryset = super(SingletonManager, self).get_queryset()

        if not queryset.exists():
            obj = self.model.objects.create()

        return queryset

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

class Option(models.Model):
    objects = models.Manager()
    singleton = SingletonManager()

    contest_site_banner = models.ImageField()

    def __str__(self):
        return 'Option'

class SponsorImage(models.Model):
    option = models.ForeignKey(Option, related_name='sponsor_images', on_delete=models.CASCADE)
    image = models.ImageField()

class FlatPage(MultilingualModel):
    site = models.CharField(max_length=20, choices=(('main', 'main'), ('contest', 'contest')))
    name = models.CharField(max_length=20)

    title_tr = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)

    redirect_link = models.CharField(max_length=100, default='', blank=True)

    content_tr = models.TextField()
    content_en = models.TextField()

    blank_page = models.BooleanField(default=False)

    enable_carousel = models.BooleanField(default=True)

    add_to_menu = models.BooleanField(default=False)
    item_place = models.CharField(
        max_length=1,
        choices=(('l', 'left'), ('r', 'right'), ('n', 'none')),
        default='r',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{} - {}'.format(self.site, self.title)

class CarouselItem(MultilingualModel):
    title_tr = models.CharField(max_length=100, blank=True)
    title_en = models.CharField(max_length=100, blank=True)

    subtitle_tr = models.CharField(max_length=100, blank=True)
    subtitle_en = models.CharField(max_length=100, blank=True)

    image = models.ImageField()

    def __str__(self):
        return 'no name' if self.title == '' else self.title

class Event(MultilingualModel):
    title_tr = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)

    content_tr = models.TextField()
    content_en = models.TextField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

class Announcement(MultilingualModel):
    title_tr = models.CharField(max_length=40)
    title_en = models.CharField(max_length=40)

    content_tr = models.TextField()
    content_en = models.TextField()

    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']

class UsefulLink(models.Model):
    title_tr = models.CharField(max_length=300)
    title_en = models.CharField(max_length=300)

    icon = models.CharField(max_length=20, blank=True, null=True, default='book')
    url = models.URLField()

    def __str__(self):
        return self.title

class ContestSupportedLanguage(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class ContestRule(MultilingualModel):
    content_tr = models.TextField()
    content_en = models.TextField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.content

class ContestFAQItem(MultilingualModel):
    content_tr = models.TextField()
    content_en = models.TextField()

    answer_tr = models.TextField()
    answer_en = models.TextField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.content
