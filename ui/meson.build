# Forge: UI
#
# Copyright (C) 2022 Goutham Krishna K V

# - Common "datadir" directory
pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

# UI Blueprints

blueprints = custom_target('blueprints',
  input: files(
    'main_window.blp'
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)

# Compiling UI Blueprints
gnome.compile_resources('Forge.UI',
  'Forge.UI.gresource.xml',
  dependencies: blueprints,
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)
