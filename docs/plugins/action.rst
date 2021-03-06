Action
======

Features
--------

This plugin provides a way to attach Flask actions from the datasource.

Configuration
-------------

There is no configuration option. You only need to enable the plugin by adding this line into the IoC configuration file.

.. code-block:: yaml

    element.plugins.action:

Usage
-----

Actions collection
~~~~~~~~~~~~~~~~~~

In order to attach a set of action, you need to create a node of type ``action.collection`` and defines an ``actions`` array.

An action is composed by:

  - name: the route name pointing to the controller, the name can also be used in a template to generate the path.
  - path: the relative path pointing to the controller. The final url will be the concatenation of the ``api.collection`` node's path with the path value from the action definition.
  - methods: the accepted http method
  - default: the default value sent to the controller, the controller must be a service registered into the IOC. The ``_controller`` key represents the controller which handled the request object.

The node should look like:

.. code-block:: yaml

    # api.yml
    title: API
    type: action.collection
    actions:
        element_api_list_index:
            path: /element/node.<_format>
            methods: ['GET']
            defaults:
                _controller: element.api.view.node.list:execute
                path: /


The action is a simple service like, where the ``execute`` method will be call as configured in the previous file

.. code-block:: python

    import json

    class CrudView(object):
        def execute(self, context, *args, **kwargs):
            # flask is the flask module
            flask = context.settings['flask']

            response = flask.make_response(json.dumps({"mydata": "myvalue"}))
            response.headers['Content-Type'] = 'application/json'

            return response

Once the action is created, you can register it in the IOC like this:

.. code-block:: yaml

    services:
        element.api.view.node:
            class: element.plugins.api.views.NodeView


.. note::

    For now, actions are registered once when the application is booted.

Redirect Action
~~~~~~~~~~~~~~~

The plugin also provides a redirect handler, to redirect a node to another one, just create a node like this:

.. code-block:: yaml

    type: action.redirect
    redirect: en

