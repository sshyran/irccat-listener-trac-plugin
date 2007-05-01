from setuptools import setup

setup(
    name='TracIrcCatListener', version='0.1',
    packages=['irccatlistener'],
    entry_points = {
        'trac.plugins' : [
	    'irccatlistener.irccatlistener = irccatlistener.irccatlistener'
	]
    },
)
				
