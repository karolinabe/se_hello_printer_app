Simple Flask App
================


Monitorowanie w StatusCake:

.. image:: https://app.statuscake.com/button/index.php?Track=icYwk37XE0&Days=1&Design=1
		:target: https://www.statuscake.com

Travis:

.. image:: https://travis-ci.org/karolinabe/se_hello_printer_app.svg?branch=master
    :target: https://travis-ci.org/karolinabe/se_hello_printer_app



Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

Najpierw trzeba znaleźć się na poziomie swojego folderu użytkownika (karolinabe) i folderu se_hello_printer_app. Aby to zrobić:

	pwd   -> sprawdza, w którym miejscu drzewa katalogów jesteś. Jeśli w nieodpowiednim to:
	cd Pulpit
	cd karolinabe
	cd se_hello_printer_app



	cat .git/config    -> ???

- Rozpocząnając pracę z projektem (wykorzystując virtualenv). Hermetyczne środowisko dla pojedyńczej aplikacji w python-ie:

  ::

    source /usr/bin/virtualenvwrapper.sh
    mkvirtualenv wsb-simple-flask-app
    pip install -r requirements.txt
    pip install -r test_requirements.txt

- Uruchamianie applikacji:

  ::

    # jako zwykły program
    python main.py

    # albo:
    PYTHONPATH=. FLASK_APP=hello_world flask run

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ::

    PYTHONPATH=. py.test
    PYTHONPATH=. py.test  --verbose -s

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ::

    source /usr/bin/virtualenvwrapper.sh
    workon wsb-simple-flask-app


- Integracja z TravisCI:

  ::

    ...


Pomocnicze
==========

- Instalacja python virtualenv i virtualenvwrapper:

  ::

    yum install -y python-pip
    pip install -U pip
    pip install virtualenv
    pip install virtualenvwrapper

- Instalacja docker-a:

  ::

    yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

    yum install -y yum-utils

    yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

    yum makecache fast
    yum install docker-ce -y
    systemctl start docker

Materiały
=========

- https://virtualenvwrapper.readthedocs.io/en/latest/


Ponowne uruchamianie na innym komputerze:
==========================================

#tworzenie nowego folderu dla repozytorium i wejście do niego
mkdir ~/nazwa uzytkownika/   #moja nazwa to karolinabe
cd ~/nazwa użytkownika

# konfiguracja gita
git config -l   #sprawdza jaka jest obecna konfiguracja, jeśli nieopowiednia, to konfigurujemy dalej
git config --global user.email "karolinabe@users.noreply.github.com"
git config --global user.name "karolinabe"
# git config --global core.editor "atom"  #ewentualnie, o ile ustawiony jest inny program

git clone link do repozytorium z githuba  #najlepiej go skopiować tak: wchodzimy do repo na github i klikamy "clone or download", tam pojawi się link

#ponownie kopiujemy biblioteki z linków powyżej, czyli:

source /usr/bin/virtualenvwrapper.sh
mkvirtualenv wsb-simple-flask-app
pip install -r requirements.txt
pip install -r test_requirements.txt

#teraz możemy spróbować odpalić program i testy, tak jak napisano wyżej, albo za pomocą poleceń:

make run
make test
make lint


Monitoring
==========

Monitorujemy naszą stronę za pomocą StatusCake
<a href="https://www.statuscake.com" title="Website Uptime Monitoring"><img src="https://app.statuscake.com/button/index.php?Track=icYwk37XE0&Days=1&Design=1" /></a>
