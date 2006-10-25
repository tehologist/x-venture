<?xml version="1.0" encoding="UTF-8"?>
<leo_file>
<leo_header file_format="2" tnodes="0" max_tnode_index="0" clone_windows="0"/>
<globals body_outline_ratio="0.5">
	<global_window_position top="10" left="10" height="986" width="1280"/>
	<global_log_window_position top="0" left="0" height="0" width="0"/>
</globals>
<preferences/>
<find_panel_settings/>
<vnodes>
<v t="234.20061005225913"><vh>Buttons and settings</vh>
<v t="234.20061019231137"><vh>Buttons</vh>
<v t="234.20061005210354"><vh>@button epydoc</vh></v>
<v t="234.20061005222732"><vh>@button unittest</vh></v>
</v>
<v t="234.20061019231137.1"><vh>Configuration Files</vh>
<v t="234.20061019181445"><vh>@thin .\\Config\\epydoc_config.ini</vh></v>
</v>
</v>
<v t="234.20061005225913.1" a="E"><vh>Libs</vh>
<v t="234.20061005223719"><vh>@thin .\\Lib\\__init__.py</vh></v>
<v t="234.20061018204229"
expanded="234.20061019180722,"><vh>@thin .\\Lib\\env.py</vh></v>
<v t="234.20061019180722.3"><vh>@thin .\\Lib\simpleClient.py</vh></v>
<v t="234.20061024175708.3"><vh>@thin .\\Lib\loginApp.py</vh></v>
<v t="234.20061024202810" a="E"
expanded="234.20061024202810.1,"><vh>@thin .\\Lib\appDaemon.py</vh></v>
<v t="234.20061024203053" a="E"
expanded="234.20061024203053.1,"><vh>@thin .\\Lib\\daemon.py</vh></v>
<v t="234.20061005194826" a="E"
expanded="234.20061005231611,234.20061005195839,"><vh>@thin .\\Lib\\mudParser.py</vh></v>
<v t="234.20061024181033"><vh>@thin .\\Lib\\application.py</vh></v>
</v>
<v t="234.20061005225913.2"><vh>Tests</vh>
<v t="234.20061005221733"><vh>@thin .\\Tests\\mudParseTest.py</vh></v>
</v>
<v t="234.20061013003017"><vh>Documents</vh>
<v t="234.20061013003017.1"><vh>@thin .\\docs\Changelog.txt</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="234.20061005210354">@ os.chdir will have to be changed to location of xvent/working.
@c

import os
os.chdir("c:\\xvent\\working")
os.system("cmd /c epydoc.py --config .\config\epydoc_config.ini &gt; ./Logs/epylog.txt 2&gt;&amp;1")
#os.system("cmd /c epydoc.py -o .\docs\libs\html ./Lib &gt;&gt; ./Logs/epylog.txt 2&gt;&amp;1")
#os.system("cmd /c epydoc.py -o .\docs\libs\pdf --pdf ./Lib  &gt;&gt; ./Logs/epylog.txt 2&gt;&amp;1")
c.frame.log.selectTab('Epydoc')
bleh = open(".\\Logs\\epylog.txt")
g.es(bleh.read(),tabName='Epydoc')
bleh.close()
os.startfile('.\\docs\\libs\\html\\index.html')</t>
<t tx="234.20061005222732">import os
os.chdir("c:\\xvent\\working")
os.system("cmd /c python ./Tests/mudParseTest.py &gt; .\Logs\unittest.txt 2&gt;&amp;1")
c.frame.log.selectTab('Unit Test')
bleh = open(".\\Logs\\unittest.txt")
g.es(bleh.read(),tabName='Unit Test')
bleh.close()</t>
<t tx="234.20061005225913"></t>
<t tx="234.20061005225913.1"></t>
<t tx="234.20061005225913.2"></t>
<t tx="234.20061013003017"></t>
<t tx="234.20061019231137"></t>
<t tx="234.20061019231137.1"></t>
</tnodes>
</leo_file>
