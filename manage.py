#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'me.settings'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django.\n"
            "Are you sure it's installed and available on your PYTHONPATH environment variable?\n"
            "Did you forget to activate a virtual environment?\n"
        ) from exc
    if len(sys.argv) > 1:
        execute_from_command_line(sys.argv)
    else:
        print("No command provided.")


if __name__ == '__main__':
    main()
