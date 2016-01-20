# Copyright 2014 Richar Nunez - rnezferreira9@gmail.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
import gtk
import pygtk
pygtk.require('2.0')
import logging

from gettext import gettext as _
from ConfigParser import SafeConfigParser

class Base():

    def __init__(self):

        # label with the text, make the string translatable
        ven = gtk.Window()
        win = gtk.VBox()
        eb = gtk.EventBox()     
        eb.add(win)
        eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('White'))
        title = gtk.Image()
        achehety = gtk.Image()
        texto = gtk.Entry()
        traducido=gtk.TextView()
        traducido.set_editable(False)
        traducido.set_wrap_mode(gtk.WRAP_WORD)
        dic = gtk.TextView()
        textbuffer = dic.get_buffer()
        dic.set_wrap_mode(gtk.WRAP_WORD)
        dic.set_editable(False)
        
        hbox3=gtk.HButtonBox()  
        hbox3.set_layout(gtk.BUTTONBOX_CENTER)
        
        parser = SafeConfigParser()
        parser.read('config.ini')   
        bo1=gtk.Button(parser.get('dic','A'))
        bo1.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#FCB947'))
        bo2=gtk.Button(parser.get('dic','E'))
        bo3=gtk.Button(parser.get('dic','I'))
        bo3.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#FCB947'))
        bo4=gtk.Button(parser.get('dic','O'))
        bo5=gtk.Button(parser.get('dic','U'))
        bo5.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#FCB947'))
        bo6=gtk.Button(parser.get('dic','Y'))   
        bo7=gtk.Button(parser.get('dic','G'))
        bo7.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color('#FCB947'))

        pixbuf = gtk.gdk.pixbuf_new_from_file('images/logo.jpg')
        scaled_pixbuf = pixbuf.scale_simple(400,100,gtk.gdk.INTERP_BILINEAR)
        title.set_from_pixbuf(scaled_pixbuf)
        pixbuf = gtk.gdk.pixbuf_new_from_file('images/achegety.jpg')
        scaled_pixbuf = pixbuf.scale_simple(600,200,gtk.gdk.INTERP_BILINEAR)
        achehety.set_from_pixbuf(scaled_pixbuf)
        #connect

        bo1.connect('clicked', self.__agregar__, texto, 'A')
        bo2.connect('clicked', self.__agregar__, texto, 'E')
        bo3.connect('clicked', self.__agregar__, texto, 'I')
        bo4.connect('clicked', self.__agregar__, texto, 'O')
        bo5.connect('clicked', self.__agregar__, texto, 'U')
        bo6.connect('clicked', self.__agregar__, texto, 'Y')
        bo7.connect('clicked', self.__agregar__, texto, 'G')
        #Cargando archivo .txt
        infile = open("lang/guarani/dic.txt", "r")
        if infile:
            string = infile.read()      
            infile.close()
            textbuffer.set_text(string)
    
     
        
        hbox2 = gtk.HBox()

        # Conexion de botones
        texto.connect("activate", self.traducir_cb, traducido)
        texto.connect("backspace", self.__backspace_cb, traducido)

        # creando scrolled
        scrolled_window = gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)
        scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        
        scrolled_window.add_with_viewport(dic)
        #Disenho de ventana
        ven.add(eb)
        win.add(title)
        win.add(hbox3)
        hbox3.add(bo1)
        hbox3.add(bo2)
        hbox3.add(bo3)
        hbox3.add(bo4)
        hbox3.add(bo5)
        hbox3.add(bo6)
        hbox3.add(bo7)
        win.add(texto)
        win.add(traducido)
        win.add(hbox2)
        win.add(achehety)
        win.add(scrolled_window)
     
        ven.show_all()

    def __agregar__(self, bo1, texto=None, Data=None):
        parser = SafeConfigParser()
        parser.read('config.ini')       
        texto.set_text(texto.get_text()+parser.get('dic',Data))
        
    def traducir_cb(self, texto, traducido=None):
        entry = texto.get_text()+' = '
        cargar = traducido.get_buffer()
        infile = "lang/guarani/dic.txt"
        with open(infile, 'r') as f:
            for line in f:
                if line.lstrip().startswith(entry.capitalize()):
                    line = line.rstrip()
                    cargar.set_text(line) 
                    break
            
                if entry != line:
                    cargar.set_text('No se ha encontrado coincidencia')
                
    def __backspace_cb(self, texto, traducido=None):
        cargar = traducido.get_buffer()        
        cargar.set_text('')

    def main(self):
       gtk.main()

base = Base()
base.main()
