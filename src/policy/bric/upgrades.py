from Products.CMFCore.utils import getToolByName
PROFILE = 'profile-policy.bric:default'


def upgrade_to_0002(context):
    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile(PROFILE)
