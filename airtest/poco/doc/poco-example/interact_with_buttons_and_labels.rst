
Interact with Buttons and Labels
================================

UI objects are just proxies, you can assign it into a variable and reuse without repeated instantiation. The following
example shows the most used methods of UI proxy. It is very easy to access all available attributes of UI in game/app.

Click and long click
--------------------

For operations, the simplest one is click, and can also do long click as long as you wish. The following example shows
the effects of click and long click.

.. code-block:: python

    # coding=utf-8

    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()

    poco('btn_start').click()
    poco('basic').click()
    poco('star_single').long_click()
    poco('star_single').long_click(duration=5)

Get and set attributes
----------------------

The following example shows more functional ways of interacting with UIs, including getting and setting attributes on
UIs.

.. image:: img/interact_with_buttons_and_labels.gif

.. code-block:: python

    # coding=utf-8

    import time
    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()

    poco('btn_start').click()
    poco(text='basic').click()

    star = poco('star_single')
    if star.exists():
        pos = star.get_position()
        input_field = poco('pos_input')
        time.sleep(1)
        input_field.set_text('x={:.02f}, y={:.02f}'.format(*pos))  # very fast
        time.sleep(3)

    title = poco('title').get_text()
    if title == 'Basic test':
        back = poco('btn_back', type='Button')
        back.click()
        back.click()

Existence test
--------------

If retrieve attributes or perform an operation on inexistent UI, exceptions will raise. If you are not sure whether
the UI exists or not, you can call ``.exists()`` to test whether exists. In specific test cases, remember to think of
a bug if the UI does not exist as your wish.

.. code-block:: python

    # coding=utf-8

    from poco.drivers.unity3d import UnityPoco

    poco = UnityPoco()

    btn = poco('btn_start')
    btn.click()
    print(btn.get_text())  # => 'Start'

    intro = poco('introduction')
    print(intro.get_text())  # => 'xxxx'
    print(intro.attr('text'))  # => 'xxxx'
    print(intro.attr('type'))  # => 'Text'
    print(intro.attr('texture'))  # => None. Because there is no texture on Text.
    print(intro.attr('foo-bar'))  # => None. Because "intro" dose not have an attribute named "foo-bar".

    intro.click()  # Perform a click on any UI objects are allowed.

    obj = poco('foo-bar', type='FooBar')
    print(obj.exists())  # => False. This UI does not exist actually

    invisible_obj = poco('result_panel', type='Layer')
    print(invisible_obj.exists())  # => False. This UI is not visible to user.


See also:

* `basic usage`_
* `interact with Buttons and Labels`_
* `drag and swipe operations`_
* `advanced selections`_
* `play with coordinate system and local positioning`_
* `iteration over elements`_
* `handling exceptions`_
* `waiting for events`_
* `play with unittest framework`_
* `optimize speed by freezing UI`_


.. _basic usage: basic.html
.. _interact with Buttons and Labels: interact_with_buttons_and_labels.html
.. _drag and swipe operations: drag_and_swipe_operations.html
.. _advanced selections: advanced_selections.html
.. _play with coordinate system and local positioning: play_with_coordinate_system_and_local_positioning.html
.. _iteration over elements: iteration_over_elements.html
.. _handling exceptions: handling_exceptions.html
.. _waiting for events: waiting_events.html
.. _play with unittest framework: play_with_unittest_framework.html
.. _optimize speed by freezing UI: optimize_speed_by_freezing_UI.html
