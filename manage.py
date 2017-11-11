#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lifeboxproject.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Não foi possível importar o Django. Tem certeza de que está instalado e"
                "disponível na sua variável de ambiente PYTHONPATH?"
                "Você não esqueceu de ativar o ambiente virtual?"
                "Vá para o promp, na pasta do projeto e digite:"
                " . venv/bin/activate ou source venv/bin/activate ?"
            )
        raise
    execute_from_command_line(sys.argv)
