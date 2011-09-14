#!/bin/sh
rm ../mtgox_widget_package.zip
zip -r ../mtgox_widget_package.zip . --exclude .git/\* README install.sh
plasmapkg -r mtgox-widget
plasmapkg -i ../mtgox_widget_package.zip