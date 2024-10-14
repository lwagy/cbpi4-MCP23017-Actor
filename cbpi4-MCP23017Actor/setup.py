from setuptools import setup

setup(name='cbpi4-MCP23017Actor',
      version='0.1.2',
      description='CraftBeerPi Plugin',
      author='Lawrence Wagy',
      author_email='lnwagy@gmail.com',
      url='https://github.com/lwagy/cbpi4-MCP23017-Actor',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4_MCP23017Actor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4_MCP23017Actor'],
     )
