# How to create the Trac plugin that talks to IRCCat #

First of all, you need setuptools installed. For information on how to install it, see [the Trac plugin docs](http://trac.edgewall.org/wiki/TracPlugins).

Once you have setuptools installed, download the code onto your machine and run

```
python setup.py bdist_egg
```

You will end up with various directories, one of them being 'dist'. From dist copy the file

```
TracIrcCatListener-0.1-pyX.X.egg
```

to the plugins directory of your Trac folder. Make sure that whatever user is running Trac has access to the plugin.

That's it!