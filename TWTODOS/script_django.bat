@echo off
:: Criar pasta
set "DIR=todos"
if not exist "%DIR%" mkdir "%DIR%"
cd "%DIR%"

:: Criar models.py
(
echo from datetime import date

echo from django.db import models

echo class Todo^(models.Model^):
echo     title = models.CharField^(
echo         verbose_name="Título", max_length=100, null=False, blank=False
echo     ^)
echo     creates_at = models.DateTimeField^(auto_now_add=True, null=False, blank=False^)
echo     deadline = models.DateField^(verbose_name="Data de entrega", null=False, blank=False^)
echo     finished_at = models.DateField^(null=True, blank=True^)

echo     class Meta:
echo         ordering = ^["deadline"^]
    
echo     def mark_has_complete^(self^):
echo         if not self.finished_at:
echo             self.finished_at = date.today^(^)
echo             self.save^(^)
) > models.py

set "DIR=templates/todos"
if not exist "%DIR%" mkdir "%DIR%"
cd "%DIR%"
(
echo ^<!DOCTYPE html^>
echo ^<html lang="pt-br"^>
echo ^<head^>
echo     ^<meta charset="UTF-8"^>
echo     ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>
echo     ^<title^>Página Automatizada!^</title^>
echo ^</head^>
echo ^<body^>
echo     ^<h1^>Criada com Automação de Script^</h1^>
echo     ^<p^>Essa página foi criada com Automação de Script por meio de arquivo ^<strong^>.bat^</strong^>^</p^>
echo ^</body^>
echo ^</html^>
) > pagina_automatizada.html
