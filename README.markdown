
2010/12/16 Update
-----------------

I've been in touch with the original author of this plugin, and his latest version (0.12) supports English now. 

I recommend you [use his svn repository](http://svn.sourceforge.jp/svnroot/shibuya-trac/plugins/ganttcalendarplugin/trunk) rather than this out-dated version :

```bash
> svn co http://svn.sourceforge.jp/svnroot/shibuya-trac/plugins/ganttcalendarplugin/trunk ganttcalendarplugin
```

The version here will remain available for those that want to install the 0.11 version, but will no longer be maintained, and the sourceforge repository above will be the home of this plugin moving forward.

More information is available at the [Trac-Hacks plugin page](http://trac-hacks.org/wiki/GanttCalendarPlugin).

About
-----

The GanttCalendar plugin adds ticket Gantt chart and calendar functionality to Trac. It is licensed under the [new BSD license](http://www.opensource.org/licenses/bsd-license.php) .

It's basically an English translation of the Japanese plugin developed by the [Shibuya Trac](http://sourceforge.jp/projects/shibuya-trac/) project - I've cleaned up a few things but the bulk of the work is theirs.

Requirements
------------

This plugin is only compatible with Trac version 0.11 and above - 0.10 users will need to upgrade. The install instructions provided will only work if you have 'ez_setup' installed - see the [TracPlugins wiki](http://trac.edgewall.org/wiki/TracPlugins) if you have any problems.

Installation
------------

Use git to checkout the plugin from our repository :

```bash
> git clone git://recursive-design.com/gantt-calendar.git
```

Then use 'easy_install' to install it :

```bash
> python setup.py bdist_egg
> sudo easy_install dist/TracGanttCalendarPlugin-0.1-py2.4.egg
```

If you don't have 'ez_setup' installed, see the [TracPlugins wiki](http://trac.edgewall.org/wiki/TracPlugins) for installation instructions

Configuration
-------------

To configure the plugin, you first need to add it to the _components_ section in _trac.ini_ :

```python
[components]
ganttcalendar.ticketcalendar.ticketcalendarplugin = enabled
ganttcalendar.ticketgantt.ticketganttchartplugin  = enabled
```

Next, you need to configure Trac to display a couple of extra fields in the ticket page :

```python
[ticket-custom]
complete         = select
complete.label   = % Complete
complete.options = 0|5|10|15|20|25|30|35|40|45|50|55|60|65|70|75|80|85|90|95|100
complete.order   = 3
due_assign       = text
due_assign.label = Start (YYYY/MM/DD)
due_assign.order = 1
due_close        = text
due_close.label  = End (YYYY/MM/DD)
due_close.order  = 2
```

The _Start_ & _End_ date fields should be inputted in the format _YYYY/MM/DD_. You can make these fields a little more user-friendly using the [datefield plugin](http://trac-hacks.org/wiki/DateFieldPlugin) .

Screenshots
-----------

![Trac Gantt_Chart](http://recursive-design.com/images/projects/gantt-calendar/Trac_Gantt_Chart.png)

![Trac Calendar](http://recursive-design.com/images/projects/gantt-calendar/Trac_Calendar.png)

![Ticket Creation](http://recursive-design.com/images/projects/gantt-calendar/Ticket_Creation.png)

Bug Reports
-----------

If you come across any problems, please [create a ticket](https://github.com/recurser/trac-gantt-calendar/issues) and we'll try to get it fixed as soon as possible.
