# APPLICATION DE COVOITURAGE ENTRE ETUDIANTS: IFRI COMOTORAGE AVEC DJANGO, HTML, CSS, TAILWIND CSS, JAVASCRIPT
# GROUPE PIL1_2425_28 

## CONTEXTE
Chaque année, l'Institut de Formation et de Recherche en Informatique soumet ses étudiants de première année à la réalisation d'un projet de fin d'année. Cette année le projet consiste à réaliser une application web qui met en relation les étudiants de l'IFRI souhaitantpartager leurs trajets quotidiens entre leur domicile et le campus en deux semaines par groupes de cinq ou six étudiants.
La réalisation de ce projet nous aura permis de mettre en pratique et d'étendre nos connaissances des langages HTML, CSS et Javascript et d'apprendre le fonctionnement du framework Django pour le backend.
Afin qu'elle soit testable, le repository contiendra la base de données, la Secret Key Django, ainsi que des informations de connexions. Les instructions de déploiement seront rajoutées un peu plus bas sur le dépôt.

# IFRI COMOTORAGE
![Logo du projet](./logo.jpg)

## Fonctionnalités

- **Inscription et Connexion** : Les utilisateurs peuvent s'inscrire et se connecter avec leurs identifiants pour accéder à la plateforme.
- **Récupération de mot de passe** : Les utilisateurs peuvent récuperer leurs mots de passe en cas d'oubli.
- **Profil Utilisateur** : Chaque utilisateur crée un profil après s'être inscrit et il y renseigne les informations concernant son trajet.
- **Messagerie Instantanée** : Les utilisateurs peuvent échanger entre eux grâce à la messagerie intégrée pour pofiner les détails de leurs déplacement.
- **Liste des Discussions** : Les utilisateurs peuvent accéder à toutes leus discussions.
- **Mise en correspondance de conducteurs et de passagers** : Les utilisateurs sont mis en correspondance grâce à l'algorithme de matching qui permet de lier les offres des conducteurs aux demandes des passager en se basant sur la proximité géographique.

- ## Installation
- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

-  ### Installation
1. Créer un dossier puis y accéder dans l'éditeur de code : 

2. Créer et Activer un environnement virtuel : 
    - Sous Windows :
        ```sh
        python -m venv mon_env
        .\mon_env\Scripts\activate
        ```
    - Sous Linux :
        ```sh
        python3 -m venv mon_env
        source mon_env/bin/activate
        ```
3. Cloner le dépôt :
    ```bash
    (mon_env) git clone https://github.com/Eudes147/PIL1_2425_28.git
    ```
4. Naviguer dans le répertoire du projet :
    ```bash
    (mon_env) cd PIL1_2425_28
    ```
5. Configurer la base de données dans le fichier [settings.py](PIL1_2425_28/ifri_comotorage/settings.py) :
  - Utilisation de MySQL : 
      ```bash
      DATABASES = {
        'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'your_db_host',  # Set to 'localhost' or '127.0.0.1' for local development
          'PORT': '3306',          # Default port for MySQL
          }
    }
        ```
6. AppliqueR les migrations :
    ```bash
    (mon_env) python manage.py makemigrations
    (mon_env) python manage.py migrate
    ```
7. Créer un superutilisateur :
    ```bash
    (mon_env) python manage.py createsuperuser
    ```
8. Démarrer le serveur de développement :
    ```bash
    (mon_env) python manage.py runserver
    ```


## Utilisation

Au lancement du serveur vous arrivez sur la première page d'accueil.

### Inscription et Connexion

Pour vous inscrire, cliquez sur le lien "inscription" dans l'en tête de la page d'accueil. Remplissez le formulaire et soumettez-le. Une fois inscrit, vous êtes redirigé vers la page de profil.

### Profil Utilisateur

Remplissez les différents champs présents pour créer votre profil, puis soumettez le en appuyant sur le bouton "enregister le profil".Vous serez ensuite redirigé vers la page d'accueil secondaire.

### Accueil secondaire
Une fois sur la page d'accueil secondaire : Pour
1. **Accéder aux discussions** : Cliquez sur le lien message au niveau de l'entête de la page d'accueil .
2. **Faites des demandes de covoiturage** : Cliquez sur le bouton " Faire une demande de covoiturage  " pour accéder au formulaire à remplir pour faire votre demande puis publiez la.
3. **Faites des offres de covoiturage** : Cliquez sur le bouton " Faire une offre de covoiturage " pour accéder au formulaire à remplir pour faire votre offre puis publiez la.
Une fois l'offre ou la demande publiée, vous serez en attente des résultats pendant que l'algorithme de matching tourne en arrière plan.Dès que l'algorithme trouvera une correspondance à l'offre ou à la demande, il vous reverra les informations et contact de votre (ou vos)  correspondant(s) afin que vous puissiez le(s) joindre.


### Liste des Discussions

Visualisez toutes vos discussions en cours dans la liste des discussions. Cliquez sur une discussion pour l'ouvrir.

### Récupération de mot de passe 

Cliquez sur le lien <mot de passe oublié ? > sur la page de connexion pour réinitialiser votre mot de passe.



    
