# Forge
#
# Copyright (C) 2022 Goutham Krishna K V

project(
  'Forge',
  version: '0.0.1-PROTO',
  meson_version: '>= 0.59.0',
  default_options: ['warning_level=2', 'werror=false',],
)

# Internationalization Imports
i18n = import('i18n')
# GNOME Imports
gnome = import('gnome')

subdir('data')
subdir('ui')
subdir('src')

gnome.post_install(
  glib_compile_schemas: true,
  gtk_update_icon_cache: true,
  update_desktop_database: true
)
