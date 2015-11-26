import sublime
import sys, os

def plugin_loaded():
	editor_dir = sys.path[0]

	if editor_dir in os.environ['PATH']:
		return

	settings = sublime.load_settings('PortableInstallationHelper.sublime-settings')
	if settings.get('subdir') is None:
		print("="*86)
		print("PortableInstallationHelper: Error loading settings. Please restart Sublime Text after installation")
		print("="*86)
		return

	subdir = settings.get('subdir').replace('/', os.path.sep)
	bindir = os.path.sep.join([editor_dir, subdir]) if len(subdir) else editor_dir

	os.environ['PATH'] = os.pathsep.join([bindir, os.environ['PATH']])
	print("PortableInstallationHelper: PATH altered to " + os.environ['PATH'])

if int(sublime.version()) < 3000:
	plugin_loaded()
