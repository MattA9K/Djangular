from django.core.management.base import BaseCommand, CommandError
from dynamic_lazarus_page.models import NgIncludedJs, NgIncludedHtml


#  READ JS & HTML FILES AS A STRING LIKE SO:
#     f = open('static/app/toolbar/toolbar.controller.js', 'r')
#     f = open('static/app/toolbar/toolbar.module.js', 'r')






class Command(BaseCommand):
    help = 'prints the toolbar module and controller.'

    # def add_arguments(self, parser):
    #     parser.add_argument('mvc_id', nargs="+", type=int)

    def handle(self, *args, **options):

        ctrl = open('static/app/toolbar/toolbar.controller.js', 'r')
        module = open('static/app/toolbar/toolbar.module.js', 'r')

        jsLayout = open('Djangular/management/default_templates/mainHtmlLayout.js', 'r')
        htmlMain = open('Djangular/management/default_templates/layoutMain.html', 'r')
        htmlNav = open('Djangular/management/default_templates/layoutNavigation.html', 'r')
        htmlToolbar = open('Djangular/management/default_templates/layoutToolbar.html', 'r')

        str_ctrl = ctrl.read()
        str_module = module.read()

        str_jsLayout = jsLayout.read()
        str_htmlMain = htmlMain.read()
        str_htmlNav = htmlNav.read()
        str_htmlToolbar = htmlToolbar.read()

        self.stdout.write(self.style.SUCCESS(''))
        # toolbarController
        try:
            sqlCtrl = NgIncludedJs(name='toolbarController')
            sqlCtrl.contents = str_ctrl
            sqlCtrl.save()
            self.stdout.write(self.style.SUCCESS( 'ADDED... toolbarController' ))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... toolbarController'))

        # toolbarModule
        try:
            modCtrl = NgIncludedJs(name='toolbarModule')
            modCtrl.contents = str_module
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... toolbarModule'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... toolbarModule'))

        # jsLayout
        try:
            modCtrl = NgIncludedJs(name='mainHtmlLayout')
            modCtrl.contents = str_jsLayout
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... mainHtmlLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... mainHtmlLayout'))

        # htmlMainLayout
        try:
            modCtrl = NgIncludedHtml(name='htmlMainLayout')
            modCtrl.contents = str_htmlMain
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... htmlMainLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... htmlMainLayout'))

        # htmlNavLayout
        try:
            modCtrl = NgIncludedHtml(name='htmlNavLayout')
            modCtrl.contents = str_htmlNav
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... htmlNavLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... htmlNavLayout'))

        # htmlToolbarLayout
        try:
            modCtrl = NgIncludedHtml(name='htmlToolbarLayout')
            modCtrl.contents = str_htmlToolbar
            modCtrl.save()
            self.stdout.write(self.style.SUCCESS('ADDED... htmlToolbarLayout'))
        except:
            self.stdout.write(self.style.WARNING('SKIPPING... htmlToolbarLayout'))