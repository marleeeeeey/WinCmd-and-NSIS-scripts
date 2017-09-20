# My Windows scripts

Набор скриптов для автоматизации рутинных операций или для выполнения операций имеющий сложный синтаксис в командной строке.

*Файлы , которые начинаются с `_` не должны запускаться вручную.* 

## build_and_autozip

Папка содержит скрипты для автоматической сборки и упаковки проектов в архив. Скрипты могут запускаться из любой дирректории, потому что используются абсолютные пути, прописанные в файле `__path_all.cmd`. Необходимо, чтобы в системе был установлен **архиватор `7z`** в папку по умолчанию, либо в папку, которая находится в `path`.

### Настройки по умолчанию:

`g:\Programming` - папка, в которой содержатся проекты в определенной иерархии.

`g:\_back_up\_bin\` - папка в которой создаются архивы.

### Процедура упаковки:

1. Запустить `RSU-135_zip.cmd`. *Этот макрос вызывает `RSU-135_build_release.cmd`, который строит проекти и копирует бинарники во временную папку. Затем выполняет вызов архиватора `7z`.*
2. По запросу ввода `Please input string:` ввести комментарий, который будет постфиксом имени архива (не обязательно)

### Процедура распаковки:

1. Скопировать файл `exctract_base.cmd` в папку, где содержатся архивы.

2. Отредактировать файл `exctract_base.cmd`, таким образом, чтобы он содержал название архива для распаковки в целевую папку (по умолчанию `Program Files` или `Program Files (x86)`)

   ```
   set ARCHIVE_NAME=your_archive_name.7z
   ```

   ​

## daily_scripts

Папка, в которой содержится несколько скриптов для повседневного использования

`ADATA_G.cmd` - монирование / размонтирование тома `true cript`
`power_off.cmd` - форсированное выключение компьютера
`power_reboot.cmd` - форсированная перезагрузка компьютера
`QKD_vagrant_suspend.cmd` - безопасное завершение виртуальное машины
`QKD_vagrant_up.cmd` - автоматический старт вирутальной машины
`stop_all.cmd` - автоматическое завершение всех процессов и виртуальных машин, безопасное размонтирование томов `true cript`, отмонтирование флешек, вызов очистки `CCleaner`

## nsis

Папка с примером скрипта для создания установщика `nsis`.

## win_huck

`associate_not_extension_files_with_notepad_p_p` - ассоциирование файлов без расширения с `notepad++`