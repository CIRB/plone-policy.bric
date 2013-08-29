from setuptools import setup, find_packages

version = '1.3.dev0'

setup(name='policy.bric',
      version=version,
      description="policy of BRIC site",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='https://github.com/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Products.LinguaPlone',
          'cirb.zopemonitoring',
          'collective.stomach',
          # -*- Extra requirements: -*-
          'plonetheme.bric',
          'collective.ckeditor',
          'Products.PloneFormGen',
          'collective.plonefinder',
          'collective.quickupload',
          'quintagroup.analytics',
          'fourdigits.portlet.twitter',
          'collective.anysurfer',
          'collective.contentstats',
          'webcouturier.dropdownmenu',
          #'cirb.blog',
          #extra feature for blog
          'archetypes.linguakeywordwidget',
          'collective.categories',
          'collective.diggdigg',
          'collective.portlet.oembed',
          'collective.portlet.twittermultistream',
          'collective.portlet.socialnetworks',
          'collective.configviews',
          'collective.portlet.categories',
          'collective.portlet.keywords',
          'collective.languagemovefolders',
          'collective.checktranslated',
          'plone.api',
          'plone.app.theming',
          #'Products.PloneHelpCenter',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
