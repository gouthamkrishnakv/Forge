pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'forge')

# GNOME Module Import
gnome = import('gnome')

# Compile Forge Resources
gnome.compile_resources('Forge',
  'forge.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

# Import Python
python = import('python')

# Set Configuration Data
conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

# Add config file
configure_file(
  input: 'Forge.in',
  output: 'Forge',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)


sources = files(
  '__init__.py',
  'main.py',
  'main_window.py',
)

subdir('mail')

install_data(sources, install_dir: moduledir)
