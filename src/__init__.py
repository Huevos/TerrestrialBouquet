import gettext

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS


PluginLanguageDomain = "terrestrialbouquet"
PluginLanguagePath = "SystemPlugins/TerrestrialBouquet/locale"


def pluginlanguagedomain():
	return PluginLanguageDomain


def localeInit():
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	if translated := gettext.dgettext(PluginLanguageDomain, txt):
		return translated
	else:
		print("[" + PluginLanguageDomain + "] fallback to default translation for " + txt)
		return gettext.gettext(txt)


localeInit()
language.addCallback(localeInit)
