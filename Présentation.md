# Présentation du langage python

- Python est portable, non seulement sur les différentes variantes d’Unix, mais aussi sur les OS propriétaires : Mac OS, BeOS, NeXTStep, MS-DOS et les différentes variantes de Windows. 
- Python est gratuit, mais on peut l’utiliser sans restriction dans des projets commerciaux. 
- Python convient aussi bien à des scripts d’une dizaine de lignes qu’à des projets complexes de plusieurs dizaines de milliers de lignes. 
- La syntaxe de Python est très simple et, combinée à des types de données évolués (listes, dictionnaires...), conduit à des programmes à la fois très compacts et très lisibles. À fonctionnalités égales, un programme Python (abondamment commenté et présenté selon les canons standards) est souvent de 3 à 5 fois plus court qu’un programme C ou C++ (ou même Java) équivalent, ce qui représente en général un temps de développement de 5 à 10 fois plus court et une facilité de maintenance largement accrue. 
- Python gère ses ressources (mémoire, descripteurs de fichiers...) sans intervention du programmeur
- Il n’y a pas de pointeurs explicites en Python. 
- Python est (optionnellement) multi-threadé. 
- Python est orienté-objet. 
- Python intègre, comme Java ou les versions récentes de C++, un système d’exceptions, qui permettent de simplifier considérablement la gestion des erreurs. 
- Python est dynamique (l’interpréteur peut évaluer des chaînes de caractères représentant des expressions ou des instructions Python), orthogonal (un petit nombre de concepts suffit à engendrer des constructions très riches), réflectif (il supporte la métaprogrammation, par exemple la capacité pour un objet de se rajouter ou de s’enlever des attributs ou des méthodes, ou même de changer de classe en cours d’exécution) et introspectif (un grand nombre d’outils de développement, comme le debugger ou le profiler, sont implantés en Python lui-même). 
- Python est dynamiquement typé. Tout objet manipulable par le programmeur possède un type bien défini à l’exécution, qui n’a pas besoin d’être déclaré à l’avance. 
- Python possède actuellement deux implémentations. L’une, interprétée, dans laquelle les programmes Python sont compilés en instructions portables, puis exécutés par une machine virtuelle (comme pour Java, avec une différence importante : Java étant statiquement typé, il est beaucoup plus facile d’accélérer l’exécution d’un programme Java que d’un programme Python). L’autre génère directement du bytecode Java. • Python est extensible : comme Tcl ou Guile, on peut facilement l’interfacer avec des bibliothèques C existantes. On peut aussi s’en servir comme d’un langage d’extension pour des systèmes logiciels complexes. • La bibliothèque standard de Python, et les paquetages contribués, donnent accès à une grande variété de services : chaînes de caractères et expressions régulières, services UNIX standards (fichiers, pipes, signaux, sockets, threads...), protocoles Internet (Web, News, FTP, CGI, HTML...), persistance et bases de données, interfaces graphiques.
- Python est un langage qui continue à évoluer, soutenu par une communauté d’utilisateurs enthousiastes et responsables, dont la plupart sont des supporters du logiciel libre. Parallèlement à l’interpréteur principal, écrit en C et maintenu par le créateur du langage, un deuxième interpréteur, écrit en Java, est en cours de développement.
- Enfin, Python est un langage de choix pour traiter le XML.

# Question général sur un langage de programmation

## Qu’est-ce qu’un langage interprété et un langage compilé ?

### langage interprété 
Dans ces langages, le code source (celui que vous écrivez) est interprété, par un logiciel qu'on appelle **interpréteur**. Celui-ci va utiliser le code source et les données d'entrée pour calculer les données de sortie :

<img src="http://data.france-ioi.org/Course/general_interpreted_vs_compiled/schema_interpreted_FR.png">

Principe d'un langage interprété
L'interprétation du code source est un processus « pas à pas » : l'interpréteur va **exécuter les lignes du code une par une**, en décidant à chaque étape ce qu'il va faire ensuite.

### langage compilé
Dans ces langages, le code source (celui que vous écrivez) est tout d'abord compilé, par un logiciel qu'on appelle **compilateur**, en un code binaire qu'un humain ne peut pas lire mais qui est très facile à lire pour un ordinateur. C'est alors **directement le système d'exploitation** qui va utiliser le **code binaire** et les données d'entrée pour calculer les données de sortie :

<img src="http://data.france-ioi.org/Course/general_interpreted_vs_compiled/schema_compiled_FR.png">

### remarque

> Dans un langage interprété, le même code source pourra marcher directement sur tout ordinateur. Avec un langage compilé, il faudra (en général) tout recompiler à chaque fois ce qui pose parfois des soucis.

> Dans un langage compilé, le programme est directement exécuté sur l'ordinateur, donc il sera en général plus rapide que le même programme dans un langage interprété.

## Qu’appelle-t-on portabilité d’un programme informatique ?

C'est la possibilité de faire exécuter des programmes sur des systèmes différents sans modification des applications ni des données

## Citez les avantages et inconvénients des deux types de langage

x | Langage Interprété | Langage Compilé
--- | --- | ---
Avantage | Les langages interprétés vous donnent une plus grande flexibilité par rapport aux langages compilés.<br> Les langages interprétés fonctionnent sur toutes les plateformes.<br>Le code est plus léger,plus simple à écrire.<br> Globalement, il est plus simple d’utiliser ces langages | Les langages compilés sont plus rapides que les langages interprétés.<br>Ils sont doncpréférés pour développer les systèmes d’exploitation, les logiciels puissants et les jeux vidéos.
Inconvénient | Le gros désavantage des langages interprétés, c’est leur vitesse. Ils sont significativement plus lents que les langages compilés.<br>Ce qui pose problème pour créer des logiciels rapides, des jeux vidéos ou des systèmes d’exploitation. | Ils demandent beaucoup plus de lignes de code.<br>Ils sont plus dure à apprendre.<br>Vous devez gérer des concepts complexes comme la mémoire.<br>Votre code compilé dépends de la plateforme.

## Complétez par des croix le tableau suivant traduisant le type correspondant

Langage | compilé | interprété
C (programmation système) | ✅ | ❌
C++ (programmation système objet) | ✅ | ❌
Cobol (gestion) | ✅ | ❌
Fortran (calcul) | ✅ | ❌
Java (programmation orientée web) | ✅ | ✅
Matlab (calcul mathématique) | ❌ |
LISP (intelligence artificielle) | ✅ | ✅
PHP (développement de sites web dynamiques) | ❌ | ✅
Perl (traitement de chaînes de caractères) | ❌ | ✅
Python | ❌ | ✅
