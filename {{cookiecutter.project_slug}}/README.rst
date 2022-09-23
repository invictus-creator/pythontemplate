{% set delim = "=" * cookiecutter.app_name|length -%}
{{delim}}
{{cookiecutter.app_name}}
{{delim}}

This is the {{cookiecutter.app_name}} application.

Minimum Requirements
====================

- Python 3.10+


Optional Requirements
=====================

Basic Setup
===========

Run the application:

.. code-block::

        python -m {{cookiecutter.app_name}} --help
