#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import urllib, sys
import xkcd

comic = xkcd.get_comic()
comic_link = str(comic['src'])
comic_title = str(comic['title'])

random_comic = xkcd.get_random_comic()
random_comic_link = str(random_comic['src'])
random_comic_title = str(random_comic['title'])

class MainWin:
	def destroy(self,widget,data=None):
		gtk.main_quit()
		
	def __init__(self,link):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.connect("destroy",self.destroy)
		self.window.set_border_width(10)
		self.image = gtk.Image()
		response = urllib.urlopen(link)
		loader=gtk.gdk.PixbufLoader()
		loader.write(response.read())
		loader.close()
		self.image.set_from_pixbuf(loader.get_pixbuf())
		self.window.add(self.image)
		self.image.show()
		self.window.show()
		
	def main(self):
		gtk.main()
	
#if __name__ == '__main__':
#	MainWin(comic_link).main()

print 'The Latest xkcd Comic!\n'
print comic_title + '\n'

print 'Random xkcd Comic!\n'
print random_comic_title + '\n'

print 'Press \'C\' to see the Latest and \'R\' to see the Random.'
choice = raw_input()

if choice == 'R':
	MainWin(random_comic_link).main()
	sys.exit(0)
elif choice == 'C':
	MainWin(comic_link).main()
	sys.exit(0)
else:
	print 'Invalid Choice'
		

# Credit for the MainWin class: unutbu from stackoverflow.
