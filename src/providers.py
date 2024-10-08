# for localized messages
from . import _

providers = {
	"other": {},
	"uk": {
		"name": _("UK"),
		"bouquetname": "FreeView",
		"sections": {
			1: _("Entertainment"),
			100: _("High Definition"),
			201: _("Children"),
			230: _("News"),
			260: _("BBC Interactive"),
			670: _("Adult"),
			700: _("Radio"), }},
	"it": {
		"name": _("Italy"),
		"sections": {
			1: _("Entertainment"),
			700: _("Radio"), }},
	"au": {
		"name": _("Australia"),
		"duplicates": {"lower": 350, "upper": 399}}}
